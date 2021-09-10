from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


doc = """
Your app description
"""

# ******************************************************************************************************************** #
# ***                                                           UTILITY
# ******************************************************************************************************************** #

def make_radio_button(label, choices, fieldtype):
    return models.fieldtype(
        choices=choices,
        label=label,
        widget=widgets.RadioSelect,
    )

def makefield_urn_decision():
    return models.StringField(
        choices=choices_urn
    )

def makefield_string(label, choices):
    return models.StringField(
        label=label,
        choices=choices,
        widget=widgets.RadioSelect
    )

def makefield_integer():
    return models.IntegerField(initial=0)

# ******************************************************************************************************************** #
# ***                                                           CHOICES
# ******************************************************************************************************************** #

#################### STAGE 1 #######################
choices_urn = [
    ['Y', 'Urna Y'], 
    ['Z', 'Urna Z']
]

choices_gen_instructions1 = [
    [1,'2 puntos'], 
    [2,'0 puntos'],
    [3,'8 puntos'],
    [4,'Ninguna de las anteriores']
]

choices_gen_instructions2 = [
    [1,'8 puntos'], 
    [2,'10 puntos'],
    [3,'6 puntos'],
    [4,'Ninguna de las anteriores']
]

choices_gen_instructions3 = [
    [1,'$1400 (7 puntos x 10 respuestas x $20)'], 
    [2,'$0 (7 puntos x 10 respuestas x $0) 8 '],
    [3,'$2000 (10 puntos x 10 respuestas x $20)'],
    [4,'Ninguna de las anteriores' ]
]



# ******************************************************************************************************************** #
# ***                                                       CLASS APPLICATION
# ******************************************************************************************************************** #
class Constants(BaseConstants):
    name_in_url = 'informality_experiment'
    players_per_group = None
    num_rounds = 100

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

    
#ToDo: agregar funcion para que las variables de pagos del player vayan actualizando la variable de pagos propia de otree
class Player(BasePlayer):

    payment_total = makefield_integer()
# ******************************************************************************************************************** #
# *** STAGE 1
# ******************************************************************************************************************** #
    payment_phase_1 = makefield_integer()
    payment_phase_2 = makefield_integer()
    payment_phase_3 = makefield_integer()
    payment_phase_4 = makefield_integer()
    payment_stage_1 = makefield_integer()
    decision_phase_1 = makefield_urn_decision()
    decision_phase_2 = makefield_urn_decision()
    decision_phase_3 = makefield_urn_decision()
    decision_phase_4 = makefield_urn_decision()
    token_value_phase_1 = makefield_integer()
    token_value_phase_2 = makefield_integer()
    token_value_phase_3 = makefield_integer()
    token_value_phase_4 = makefield_integer()
    answer_correct_stage1 = makefield_integer()

    ############################ Consent ############################
    accepts_terms = models.BooleanField()

    ############################ Instructions ############################
    question_1_stage1_instructions = makefield_string(
        '1. ¿Cuál es el valor mínimo de las fichas de la Urna Z?',
        choices_gen_instructions1
    )

    question_2_stage1_instructions = makefield_string(
        '2.	¿Cuál es el valor mínimo de las fichas de la de la Urna Y?',
        choices_gen_instructions1
    )

    question_3_stage1_instructions = makefield_string(
        '3.	¿Cuál es el valor máximo de las fichas de la Urna Y?',
        choices_gen_instructions2
    )

    question_4_stage1_instructions = makefield_string(
        '4.	Si para las rondas 6-10 escoges la urna Z y sale al azar una ficha de 7 puntos, ¿cuántos pesos ganarás por 10 respuestas correctas?',
        choices_gen_instructions3
    )

# ******************************************************************************************************************** #
# *** STAGE 2
# ******************************************************************************************************************** #
    payment_stage_2 = makefield_integer()
    answer_correct_stage2 = makefield_integer()



