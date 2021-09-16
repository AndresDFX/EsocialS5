from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import *
import random, math


# ******************************************************************************************************************** #
# *** STAGE 1
# ******************************************************************************************************************** #
class Consent(Page):
    form_model = 'player'
    form_fields = ['accepts_terms']

    def is_displayed(self):
        if(self.round_number == 1 and self.player.round_counter == 0):
            return self.round_number == self.round_number

#=======================================================================================================================
class GenInstructions(Page):
    
    def is_displayed(self):
        if(self.round_number == 1 and self.player.round_counter == 0):
            return self.round_number == self.round_number

#=======================================================================================================================
class Stage1Instructions(Page):

    def is_displayed(self):
        if(self.round_number == 1 and self.player.round_counter == 0):
            return self.round_number == self.round_number
    
#=======================================================================================================================
class Stage1Questions(Page):
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
        # ToDo: Copy forms fields  6-11-16 rounds in player round 1
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

    def js_vars(self):
        return dict(
            #Tamaño de textarea
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
            print("round_counter", player.round_counter)
            print("phase 1")
            
        #Phase 2
        if (round_counter > Constants.images_max_phase1 and round_counter <= Constants.images_max_phase2):
            player.answer_correct_phase2 += correct_answer
            player.last_answer_correct_phase = player.answer_correct_phase2
            print("round_counter", player.round_counter)
            print("phase 2")
        
        #Phase 3
        elif (round_counter >Constants.images_max_phase2 and round_counter <= Constants.images_max_phase3):
            player.answer_correct_phase3 += correct_answer
            player.last_answer_correct_phase = player.answer_correct_phase3
            print("round_counter", player.round_counter)
            print("phase 3")
        
        #Phase 4
        elif (round_counter > Constants.images_max_phase3 and round_counter <= Constants.images_max_phase4):
            player.answer_correct_phase4 += correct_answer
            player.last_answer_correct_phase = player.answer_correct_phase4
            print("round_counter", player.round_counter)
            print("phase 4")
        
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
        player = self.player.in_round(1)
        if (player.round_counter == Constants.images_max_phase4):
            return self.round_number == self.round_number


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
class Stage2Start(Page):

    def is_displayed(self):
        if (self.round_number == Constants.num_rounds):
            return self.round_number == self.round_number

#=======================================================================================================================
class Stage2Questions(Page):

    form_model = 'player'
    form_fields = [
        'question_1_stage2_instructions',
        'question_2_stage2_instructions'
    ]

    def is_displayed(self):
        if (self.round_number == Constants.num_rounds):
            return self.round_number == self.round_number

    def error_message(self, values):
        solutions = dict(
            question_1_stage2_instructions='1',
            question_2_stage2_instructions='3'
        )

        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Respuesta incorrecta, por favor lea de nuevo las instrucciones'

        return error_messages

#=======================================================================================================================
class Stage2DoubleMoney(Page):
    form_model = 'player'
    form_fields = ['amount_inversion']

    def is_displayed(self):
        if (self.round_number == Constants.num_rounds):
            return self.round_number == self.round_number

#=======================================================================================================================
class Stage2HeadTails(Page):
    form_model = 'player'

    def is_displayed(self):
        if (self.round_number == Constants.num_rounds):
            return self.round_number == self.round_number
    
    def live_method(self, data):
        self.flip_value = float(data)

    def vars_for_template(self):
        amount_inversion = math.trunc(c(self.player.amount_inversion))
        return {
            'amount_inversion' : amount_inversion
        }

#=======================================================================================================================
class Stage2ResultCoin(Page):

    def is_displayed(self):
        if (self.round_number == Constants.num_rounds):
            return self.round_number == self.round_number

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

        player.in_round(1).payment_stage_2 = payment_stage_2

        return {
            'amount_inversion' : amount_inversion,
            'cara_sello_name' : cara_sello_name,
            'payment_stage_2' : payment_stage_2
        }
    
#=======================================================================================================================
class ResultAllStages(Page):

    def is_displayed(self):
        if (self.round_number == Constants.num_rounds):
            return self.round_number == self.round_number 

    def vars_for_template(self):
        player = self.player.in_round(1)
        payment_phase_1 = player.payment_phase_1
        payment_phase_2 = player.payment_phase_2
        payment_phase_3 = player.payment_phase_3
        payment_phase_4 = player.payment_phase_4
        payment_stage_1 = player.payment_stage_1
        payment_stage_2 = player.payment_stage_2

        return{
            'payment_phase_1': payment_phase_1,
            'payment_phase_2': payment_phase_2,
            'payment_phase_3': payment_phase_3,
            'payment_phase_4': payment_phase_4,
            'payment_stage_1': payment_stage_1,
            'payment_stage_2': payment_stage_2
        } 
        
#=======================================================================================================================
class SocioDemSurvey(Page):
    form_model = 'player'
    form_fields = ['genero', 'edad', 'ciudad', 'estrato', 'estado_civil', 'numero_hijos', 'identifica_cultura',
    'identifica_religion','nivel_estudios', 'tendencia_politica', 'disposicion_riesgos', 'conseguir_esfuerzo',
    'planes_termino', 'juego_suerte', 'propongo_aprender', 'mayores_logros', 'establecer_metas', 'competencia_excelencia',
    'salir_adelante', 'comparar_calificaciones', 'empeno_trabajo', 'alcanzar_objetivos', 'cumplir_tareas', 'obtener_resultados',
    'exito_esfuerzo','superar_desafios', 'confianza_tareas', 'tareas_excelencia', 'tareas_dificiles', 'alcanzar_objetivos',
    'tarde_cita', 'comprar_vendedores_ambulantes', 'trabajar_sin_contrato', 'emplear_sin_contrato', 'no_cotizar_pension', 'no_cotizar_salud',
    'no_cuenta_bancaria', 'pedir_prestado', 'transporte_alternativo', 'vender_informal', 'no_votar', 'comprar_sin_factura',
    'tarde_cita_otros', 'comprar_vendedores_ambulantes_otros', 'trabajar_sin_contrato_otros', 'emplear_sin_contrato_otros', 'no_cotizar_pension_otros', 'no_cotizar_salud_otros',
    'no_cuenta_bancaria_otros', 'pedir_prestado_otros', 'transporte_alternativo_otros', 'vender_informal_otros', 'no_votar_otros', 'comprar_sin_factura_otros',
    'tarde_cita_apropiado', 'comprar_vendedores_ambulantes_apropiado', 'trabajar_sin_contrato_apropiado', 'emplear_sin_contrato_apropiado', 'no_cotizar_pension_apropiado', 'no_cotizar_salud_apropiado',
    'no_cuenta_bancaria_apropiado', 'pedir_prestado_apropiado', 'transporte_alternativo_apropiado', 'vender_informal_apropiado', 'no_votar_apropiado', 'comprar_sin_factura_apropiado'
    ]


# ******************************************************************************************************************** #
# *** MANAGEMENT PAGES
# ******************************************************************************************************************** #
stage_1_sequence = [Consent, GenInstructions, Stage1Instructions, Stage1Questions, Stage1Start, Stage1UrnZPreview, Stage1Urn, Stage1Round, Stage1ResultPhase, Stage1AllResult]
#stage_1_sequence = [Stage1Start, Stage1UrnZPreview, Stage1Urn, Stage1Round, Stage1ResultPhase, Stage1AllResult]
stage_2_sequence = [Stage2Start, Stage2Questions, Stage2DoubleMoney, Stage2HeadTails, Stage2ResultCoin]
stage_final = [ResultAllStages]
page_sequence = stage_1_sequence + stage_2_sequence + stage_final
