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
        return self.round_number == 1

#=======================================================================================================================

class GenInstructions(Page):
    
    def is_displayed(self):
        return self.round_number == 1

#=======================================================================================================================

class Stage1Instructions(Page):

    def is_displayed(self):
        return self.round_number == 1
    
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
        return self.round_number == 1

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
        if (self.round_number == 1 or self.round_number == 6 or 
            self.round_number == 11 or self.round_number == 16):
            return self.round_number == self.round_number

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
        if (self.round_number == 1 or self.round_number == 6 or 
            self.round_number == 11 or self.round_number == 16):
            player = self.player.in_round(1)
            if player.last_decision_phase  == 'Z':
                return self.round_number == self.round_number

    def get_form_fields(self):
        if self.player.round_number == 1:
            return ['question_1_phase1_urnz', 'question_2_phase1_urnz', 'question_3_phase1_urnz']
        elif self.player.round_number == 6:
            return ['question_1_phase2_urnz', 'question_2_phase2_urnz', 'question_3_phase2_urnz']

    def js_vars(self):
        return dict(
            #Tamaño de textarea
            min_length=1,
            max_length=2
        )
    
#=======================================================================================================================
class Stage1Urn(Page):
    
    def is_displayed(self):
        if (self.round_number == 1 or self.round_number == 6 or 
            self.round_number == 11 or self.round_number == 16):
                return self.round_number == self.round_number

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
            'urn_decision_label': urn_decision_label
        }

#=======================================================================================================================
class Stage1Round(Page):

    form_model = 'player'
    form_fields = ['num_entered']
    timer_text = 'Tiempo restante para completar la Ronda: '
    timeout_seconds = Constants.num_seconds_stage_1

 
    def is_displayed(self):
        if self.round_number > Constants.sub_rounds_stage_1:
            return False
        elif self.round_number <= Constants.num_rounds/2:
            return True
    
    def js_vars(self):
        round_index = self.round_number - 1 
        rate_error = Constants.rate_error
        path_image = Constants.images_names_questions[round_index]
        num_errors = path_image.split(sep='_')[1]
        
        return dict(
            rate_error=rate_error,
            path_image=path_image,
            num_errors=num_errors
        )
    
    def live_method(self, data):
        player = self.in_round(1)
        
        #Phase 1
        if self.round_number >= 1 and self.round_number <= 5:
            player.answer_correct_phase1 += int(data)
            player.last_answer_correct_phase = player.answer_correct_phase1
            
        #Phase 2
        elif self.round_number >= 6 and self.round_number <= 10:
            player.answer_correct_phase2 += int(data)
            player.last_answer_correct_phase = player.answer_correct_phase2

#=======================================================================================================================
class Stage1ResultPhase(Page):

    form_model = 'player'

    def is_displayed(self):
        if (self.round_number == 5 or self.round_number == 10 or 
            self.round_number == 15 or self.round_number == 20):
                return True

    def vars_for_template(self):
        player = self.player.in_round(1)
        token_value_phase = player.last_token_value_phase
        answer_correct_phase = player.last_answer_correct_phase 
        payment_phase =  token_value_phase * answer_correct_phase
        player.payment_total += payment_phase
        payment_total = player.payment_total
        phase_label = 0
        
        #Phase 1
        if self.round_number == 5:
            player.payment_phase_1 = payment_phase
            phase_label = 1

        #Phase 2
        if self.round_number == 10:
            player.payment_phase_2 = payment_phase
            phase_label = 2
     
        return {
            'token_value_phase': token_value_phase,
            'answer_correct_phase': answer_correct_phase,
            'payment_phase': payment_phase,
            'phase_label': phase_label, 
            'payment_total': payment_total
        }

# ******************************************************************************************************************** #
# *** MANAGEMENT PAGES
# ******************************************************************************************************************** #
#stage_1_sequence = [Consent, GenInstructions, Stage1Instructions, Stage1Questions, Stage1Start, Stage1UrnZPreview, Stage1Urn]
#stage_1_sequence = [Stage1Start, Stage1UrnZPreview, Stage1Urn]
stage_1_sequence = [Stage1Start, Stage1UrnZPreview, Stage1Urn, Stage1Round, Stage1ResultPhase]
page_sequence = stage_1_sequence
