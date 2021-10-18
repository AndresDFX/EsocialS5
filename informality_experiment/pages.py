from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import *
import random, math

# ******************************************************************************************************************** #
# *** UTILS
# ******************************************************************************************************************** #

def get_data(player, list_atrr):
    values = []
    for attr in list_atrr:
        values.append(getattr(player, attr))
    return values

def set_data(player, list_atrr, values):
    for i,atrr in enumerate(list_atrr):
        setattr(player, atrr, values[i])

#TODO: Not work if method get_forms_fields is present in Class Page.
def get_and_set_data(self_player, player, list_atrr):
    values = get_data(self_player, list_atrr)
    set_data(player, list_atrr, values)


# ******************************************************************************************************************** #
# *** STAGE 1
# ******************************************************************************************************************** #
class Consent(Page):
    form_model = 'player'
    form_fields = ['accepts_terms', 'num_temporal']
    

    def is_displayed(self):
        if(self.round_number == 1 and self.player.round_counter == 0):
            return self.round_number == self.round_number

#=======================================================================================================================
class Stage1Instructions(Page):
    form_model = 'player'
    form_fields = [
        'question_1_stage1_instructions',
        'question_2_stage1_instructions',
        'question_3_stage1_instructions',
        'question_4_stage1_instructions'
    ]
    
    def is_displayed(self):
        if(self.round_number == 1 and self.player.round_counter == 0):
            return self.round_number == self.round_number

    def error_message(self, values):
        solutions = dict(
            question_1_stage1_instructions='1',
            question_2_stage1_instructions='2',
            question_3_stage1_instructions='2',
            question_4_stage1_instructions='1'
        )

        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Respuesta incorrecta, por favor lea de nuevo las instrucciones'

        return error_messages
    
#=======================================================================================================================
class Stage1Start(Page):

    def is_displayed(self):
        player = self.player.in_round(1)
        if (player.round_counter % Constants.images_per_phase == 0 
            or self.round_number == 1):
            return self.round_number == self.round_number
        else:
            return False


    def live_method(self, data):
        
        player = self.in_round(1)
        player.last_decision_phase = data
    
        if self.round_number == 1:
            player.decision_phase_1 = data 
        elif self.round_number == 6:
            player.decision_phase_2 = data
        elif self.round_number == 11:
            player.decision_phase_3 = data
        elif self.round_number == 16:
            player.decision_phase_4 = data

        
#=======================================================================================================================
class Stage1UrnZPreview(Page):

    form_model = 'player'

    def is_displayed(self):
        player = self.player.in_round(1)
        if (player.round_counter % Constants.images_per_phase == 0 
            or self.round_number == 1):
            if player.last_decision_phase  == 'Z':
                return self.round_number == self.round_number
        else:
            return False

    def get_form_fields(self):
        if self.round_number == 1:
            return ['question_1_phase1_urnz', 'question_2_phase1_urnz', 'question_3_phase1_urnz']
        elif self.round_number == 6:
            return ['question_1_phase2_urnz', 'question_2_phase2_urnz', 'question_3_phase2_urnz']
        elif self.round_number == 11:
            return ['question_1_phase3_urnz', 'question_2_phase3_urnz', 'question_3_phase3_urnz']
        elif self.round_number == 16:
            return ['question_1_phase4_urnz', 'question_2_phase4_urnz', 'question_3_phase4_urnz']

    def before_next_page(self):
        player = self.player.in_round(1)
        list_atrr = self.form_fields
        get_and_set_data(self.player, player, list_atrr)

    def js_vars(self):
        return dict(
            #Tamaño de TextArea
            min_length=Constants.min_length_textarea,
            max_length=Constants.max_length_textarea
        )
    
#=======================================================================================================================
class Stage1Urn(Page):

    def is_displayed(self):
        player = self.player.in_round(1)
        if (player.round_counter % Constants.images_per_phase == 0 
            or self.round_number == 1):
            return self.round_number == self.round_number
        else:
            return False

    def vars_for_template(self):
        
        player = self.player.in_round(1)

        if player.last_decision_phase == 'Y':
            num_random = random.randint(Constants.urn_y_token_min_random, Constants.urn_y_token_max_random)
        else:
            num_random = random.randint(Constants.urn_z_token_min_random, Constants.urn_z_token_max_random)

        urn_decision_label = player.last_decision_phase
        player.last_token_value_phase = num_random #Numero de ficha aleatoria en cada fase

        return{
            'num_random': num_random,
            'urn_decision_label': urn_decision_label,
            'round_counter':player.round_counter
        }

#=======================================================================================================================
class Stage1Round(Page):

    form_model = 'player'
    form_fields = ['num_entered']
    timer_text = 'Tiempo restante para completar la Ronda: '
    timeout_seconds = Constants.num_seconds_stage_1

    
    def before_next_page(self):
        player = self.player.in_round(1)
        if (player.round_counter % Constants.images_per_phase  != 0):
            player.round_counter = math.ceil(player.round_counter/5)*5
  
    def is_displayed(self):
        player = self.player.in_round(1)
        if (player.round_counter <= Constants.images_max_phase4):
                return self.round_number == self.round_number
        else:
            False

    def js_vars(self):
        player = self.player.in_round(1)

        if (player.round_counter % Constants.images_per_phase != 0):
            player.round_counter = math.ceil(player.round_counter/5)*5
        
        round_counter = player.round_counter
        rate_error = Constants.rate_error
        path_image = Constants.images_names_questions[round_counter]
        num_errors = path_image.split(sep='_')[3]
        
        return dict(
            rate_error=rate_error,
            path_image=path_image,
            num_errors=num_errors,
            round_counter=round_counter
        )

    def live_method(self, data):
        player = self.in_round(1)
        player.round_counter = player.round_counter + 1
        round_counter = player.round_counter
        correct_answer = int(data)
        path_image = Constants.images_names_questions[round_counter]
        values_image = path_image.split(sep='_')
        num_errors = values_image[3]
        round_label = values_image[1]

        #Phase 1
        if (round_counter >=0 and round_counter <= Constants.images_max_phase1):
            player.answer_correct_phase1 += correct_answer
            player.last_answer_correct_phase = player.answer_correct_phase1
            
        #Phase 2
        if (round_counter > Constants.images_max_phase1 and round_counter <= Constants.images_max_phase2):
            player.answer_correct_phase2 += correct_answer
            player.last_answer_correct_phase = player.answer_correct_phase2

        #Phase 3
        elif (round_counter >Constants.images_max_phase2 and round_counter <= Constants.images_max_phase3):
            player.answer_correct_phase3 += correct_answer
            player.last_answer_correct_phase = player.answer_correct_phase3
        
        #Phase 4
        elif (round_counter > Constants.images_max_phase3 and round_counter <= Constants.images_max_phase4):
            player.answer_correct_phase4 += correct_answer
            player.last_answer_correct_phase = player.answer_correct_phase4
        
        response = dict(
            path_image=path_image,
            num_errors=num_errors,
            round_counter=round_counter,
            round_label=round_label
        )
        return {
            player.id_in_group: response
        }


#=======================================================================================================================
class Stage1ResultPhase(Page):

    form_model = 'player'

    def is_displayed(self):
        player = self.player.in_round(1)
        if (player.round_counter % Constants.images_per_phase == 0):
            return self.round_number == self.round_number
            
    def vars_for_template(self):
        player = self.player.in_round(1)
        token_value_phase = player.last_token_value_phase
        answer_correct_phase = player.last_answer_correct_phase 
        payment_phase =  Constants.coin_value * token_value_phase * answer_correct_phase 
        phase_label = player.round_counter // Constants.images_per_phase 

        #Phase 1
        if phase_label == 1:
            player.payment_phase_1 = payment_phase

        #Phase 2
        if phase_label == 2:
            player.payment_phase_2 = payment_phase
        
        #Phase 3
        if phase_label == 3:
            player.payment_phase_3 = payment_phase
        
        #Phase 4
        if phase_label == 4:
            player.payment_phase_4 = payment_phase

        return {
            'round_counter':player.round_counter,
            'token_value_phase': token_value_phase,
            'answer_correct_phase': answer_correct_phase,
            'payment_phase': payment_phase,
            'phase_label': phase_label,
            'payment_phase': payment_phase
        }

#=======================================================================================================================
class Stage1AllResult(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player = self.player.in_round(1)
        payment_phase_1 = player.payment_phase_1
        payment_phase_2 = player.payment_phase_2
        payment_phase_3 = player.payment_phase_3
        payment_phase_4 = player.payment_phase_4
        payment_stage_1 = payment_phase_1 + payment_phase_2 + payment_phase_3 + payment_phase_4
        player.payment_stage_1 = payment_stage_1

        return{
            'payment_phase_1': payment_phase_1,
            'payment_phase_2': payment_phase_2,
            'payment_phase_3': payment_phase_3,
            'payment_phase_4': payment_phase_4,
            'payment_stage_1': payment_stage_1
        } 
        
# ******************************************************************************************************************** #
# *** STAGE 2
# ******************************************************************************************************************** #
class Stage2PlayCoin(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

#=======================================================================================================================

class Stage2DoubleMoney(Page):
    form_model = 'player'
    form_fields = ['amount_inversion']

    def before_next_page(self):
        player = self.player.in_round(1)
        list_atrr = self.form_fields
        get_and_set_data(self.player, player, list_atrr)

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

#=======================================================================================================================
class Stage2DoubleMoney(Page):
    form_model = 'player'
    form_fields = ['amount_inversion']

    def before_next_page(self):
        player = self.player.in_round(1)
        list_atrr = self.form_fields
        get_and_set_data(self.player, player, list_atrr)

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

#=======================================================================================================================
class Stage2HeadTails(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    def live_method(self, data):
        player = self.in_round(1)
        player.flip_value = float(data)
        self.flip_value = float(data)

    def vars_for_template(self):
        amount_inversion = math.trunc(c(self.player.amount_inversion))
        return {
            'amount_inversion' : amount_inversion
        }

#=======================================================================================================================
class Stage2ResultCoin(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player = self.player.in_round(1)
        flip_value = self.player.flip_value 
        amount_inversion = math.trunc(c(self.player.amount_inversion))
        cara_sello_name = ""
        payment_stage_2 = 0

        if(flip_value <= 0.5):
            cara_sello_name = "rojo"
            payment_stage_2 = 5000-amount_inversion + math.trunc(amount_inversion*2)
        else:
            cara_sello_name = "azul"
            payment_stage_2 = 5000-amount_inversion

        player.payment_stage_2 = payment_stage_2

        return {
            'amount_inversion' : amount_inversion,
            'cara_sello_name' : cara_sello_name,
            'payment_stage_2' : payment_stage_2
        }
    
#=======================================================================================================================
class SocioDemSurvey(Page):
    form_model = 'player'
    form_fields = [
        'edad',
        'ciudad',
        'rol_hogar',
        'estado_civil',
        'hijos',
        'etnia',
        'religion',
        'estudios',
        'actividad_actual',
        'esta_laborando' ,
        'ingreso_mensual' ,
        'gasto_mensual' ,
        'offer_1',
        'Estabilidad',
        'Independencia',
        'Descanso',
        'Lucro',
        'Protección',
        'encuesta_tabla3_pregunta1',
        'encuesta_tabla3_pregunta2',
        'encuesta_tabla3_pregunta3',
        'encuesta_tabla3_pregunta4',
        'encuesta_tabla3_pregunta5',
        'encuesta_tabla3_pregunta6',
        'encuesta_tabla3_pregunta7',
        'encuesta_tabla3_pregunta8',
        'encuesta_tabla3_pregunta9',
        'encuesta_tabla3_pregunta10',
        'encuesta_tabla3_pregunta11',
        'encuesta_tabla3_pregunta12',
        'encuesta_tabla3_pregunta13',
        'encuesta_tabla3_pregunta14',
        'encuesta_tabla3_pregunta15',
        'encuesta_tabla3_pregunta16',
        'encuesta_tabla3_pregunta17',
        'encuesta_tabla3_pregunta18',
        'encuesta_tabla3_pregunta19',
        'encuesta_tabla3_pregunta20',
        'encuesta_tabla3_pregunta21',
        'encuesta_tabla3_pregunta22',
        'encuesta_tabla3_pregunta23',
        'encuesta_tabla3_pregunta24',
        'encuesta_tabla3_pregunta25',
        'encuesta_tabla3_pregunta26',
        ]

    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    def before_next_page(self):
        player = self.player.in_round(1)
        list_atrr = self.form_fields
        get_and_set_data(self.player, player, list_atrr)
    
    def error_message(self, values):
        error_messages = dict()
        list_iter = [values['Estabilidad'], values['Independencia'], values['Descanso'], \
                    values['Lucro'], values['Protección'] ]
        list_new = set(list_iter)

        if len(list_new) != len(list_iter):
            error_messages['Protección'] = 'Debe seleccionar un valor unico a cada item'
        return error_messages

#=======================================================================================================================
class ResultAllStages(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    def before_next_page(self):
        player = self.player.in_round(1)
        list_atrr = self.form_fields
        get_and_set_data(self.player, player, list_atrr)

    def vars_for_template(self):
        player = self.player.in_round(1)
        payment_phase_1 = player.payment_phase_1
        payment_phase_2 = player.payment_phase_2
        payment_phase_3 = player.payment_phase_3
        payment_phase_4 = player.payment_phase_4
        payment_stage_1 = player.payment_stage_1
        payment_stage_2 = player.payment_stage_2
        payment_total = payment_stage_1 + payment_stage_2 + Constants.fixed_payment
        player.payment_total = payment_total

        return{
            'payment_phase_1': payment_phase_1,
            'payment_phase_2': payment_phase_2,
            'payment_phase_3': payment_phase_3,
            'payment_phase_4': payment_phase_4,
            'payment_stage_1': payment_stage_1,
            'payment_stage_2': payment_stage_2,
            'payment_total': payment_total
        } 
    
#=======================================================================================================================
class Greeting(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

# ******************************************************************************************************************** #
# *** MANAGEMENT PAGES
# ******************************************************************************************************************** #
stage_1_sequence = [Consent, Stage1Instructions, Stage1Start, Stage1UrnZPreview, Stage1Urn, Stage1Round, Stage1ResultPhase, Stage1AllResult]
stage_2_sequence = [Stage2PlayCoin, Stage2DoubleMoney, Stage2HeadTails, Stage2ResultCoin]
final_pages = [SocioDemSurvey, ResultAllStages, Greeting]

page_sequence = stage_1_sequence + stage_2_sequence + final_pages

