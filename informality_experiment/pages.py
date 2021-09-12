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

    def vars_of_template(self):
        return{
            'round_number': self.round_number
        }

#=======================================================================================================================

class GenInstructions(Page):
    
    def is_displayed(self):
        return self.round_number == 1

    def vars_of_template(self):
        return{
            'round_number': self.round_number
        }
#=======================================================================================================================

class Stage1Instructions(Page):

    def is_displayed(self):
        return self.round_number == 1
    
    def vars_of_template(self):
        return{
            'round_number': self.round_number
        }

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
    
    def vars_of_template(self):
        return{
            'round_number': self.round_number
        }

#=======================================================================================================================
class Stage1Start(Page):

    def is_displayed(self):
        if (self.round_number == 1 or self.round_number == 6 or 
            self.round_number == 11 or self.round_number == 16):
            return True

    def live_method(self, data):
        if self.round_number == 1:
            self.decision_phase_1 = data
            self.last_decision_phase = data
        elif self.round_number == 6:
            self.decision_phase_2 = data
            self.last_decision_phase = data
        elif self.round_number == 11:
            self.decision_phase_3 = data
            self.last_decision_phase = data
        elif self.round_number == 16:
            self.decision_phase_4 = data
            self.last_decision_phase = data

    def vars_of_template(self):
        return{
            'round_number': self.round_number,
            'last_decision_phase': self.last_decision_phase
        }

#=======================================================================================================================
class Stage1UrnZPreview(Page):

    form_model = 'player'

    def is_displayed(self):
        if self.player.last_decision_phase == 'Z':
            return self.round_number == self.round_number

    def get_form_fields(self):
        if self.player.round_number == 1:
            return ['question_1_phase1_urnz', 'question_2_phase1_urnz', 'question_3_phase1_urnz']
        elif self.player.round_number == 5:
            return ['question_1_phase2_urnz', 'question_2_phase2_urnz', 'question_3_phase2_urnz']

    def js_vars(self):
        return dict(
            #Tamaño de textarea
            min_length=1,
            max_length=2
        )
    
    def vars_of_template(self):
        return{
            'round_number': self.round_number
        }

#=======================================================================================================================
class Stage1Urn(Page):

    def is_displayed(self):
        return self.round_number == self.round_number

    def vars_for_template(self):

        if self.player.last_decision_phase == 'Y':
            num_random = random.randint(Constants.urn_y_token_min_random, Constants.urn_y_token_max_random)
        else:
            num_random = random.randint(Constants.urn_z_token_min_random, Constants.urn_y_token_max_random)

        urn_decision_label = self.player.last_decision_phase
        self.player.last_token_value_phase = num_random #Numero de ficha aleatoria en cada fase

        return{
            'round_number': self.round_number,
            'num_random': num_random,
            'urn_decision_label': urn_decision_label
        }

#=======================================================================================================================
class Stage1Round(Page):

    form_model = 'player'
    form_fields = ['field_answer']
    
    def js_vars(self):
        round_index = self.round_number - 1 
        path_image = Constants.images_path[round_index]
        num_errors = path_image.split(sep='_')[1]
        return dict(
            path_image=path_image,
            num_errors=num_errors
        )

# ******************************************************************************************************************** #
# *** MANAGEMENT PAGES
# ******************************************************************************************************************** #
#stage_1_sequence = [Consent, GenInstructions, Stage1Instructions, Stage1Questions, Stage1Start, Stage1UrnZPreview, Stage1Urn]
#stage_1_sequence = [Stage1Start, Stage1UrnZPreview, Stage1Urn]
stage_1_sequence = [Stage1Round]
page_sequence = stage_1_sequence
