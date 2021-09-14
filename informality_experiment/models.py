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
    initial='')

def makefield_string(label, choices):
    return models.StringField(
        label=label,
        choices=choices,
        widget=widgets.RadioSelect
    )

def makefield_integer():
    return models.IntegerField(initial=0)

def makefield_urnz_question1():
    return models.StringField(
        label='1. A continuación, por favor de una descripción detallada del por qué la Urna (Z) fue su elección.',
        widget=widgets.TextArea
)

def makefield_urnz_question2():
    return models.StringField(
        label='2. ¿En caso de existir unos pagos más altos en la Urna (Y) mantendría su decisión actual?.',
        widget=widgets.TextArea
)

def makefield_urnz_question3():
    return models.StringField(
        label='3. Por favor de una descripción detallada de cómo esta elección puede relacionarse con alguna actividad del día a día.',
        widget=widgets.TextArea
)

def make_field(label):
    return models.StringField(
        choices=[
            ['Fuertemente en desacuerdo', ""],
            ['En desacuerdo', ""],
            ['Ligeramente en desacuerdo', ""],
            ['Ni de acuerdo, ni en desacuerdo', ""],
            ['De acuerdo', ""],
            ['Fuertemente de acuerdo', ""],
        ],
        label=label,
        widget=widgets.RadioSelect,
    )

def make_field2(label):
    return models.IntegerField(
        choices=[-2,-1,0,1,2],
        label=label,
    )

# ******************************************************************************************************************** #
# ***                                                           CHOICES
# ******************************************************************************************************************** #

#################### STAGE 1 #######################
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

#################### STAGE 2 #######################
choices_gen_instructions4 = [
    [1,'$1,000'], 
    [2,'$3,000'],
    [3,'$5,000']
]

choices_gen_instructions5 = [
    [1,'$2,000'], 
    [2,'$6,000'],
    [3,'$9,000']
]

# ******************************************************************************************************************** #
# ***                                                       CLASS APPLICATION
# ******************************************************************************************************************** #
class Constants(BaseConstants):
    name_in_url = 'informality_experiment'
    players_per_group = None
    num_rounds = 2
    num_round = 1

    #STAGE 1
    urn_z_token_min_random = 2
    urn_z_token_max_random = 8
    urn_y_token_min_random = 0
    urn_y_token_max_random = 10
    sub_rounds_stage_1 = 20
    sub_round_for_round_stage_1 = 5
    rate_error = 2
    num_seconds_stage_1 = 15
    images_names_questions = [
        "1_1_1_4",
        "1_1_2_5",
        "1_1_3_6",
        "1_1_4_2",
        "1_1_5_4",
        "3_15",
        "4_20",
        "5_25",
        "6_5",
        "7_10",
        "8_15",
        "9_20",
        "10_25",
        "11_5",
        "12_10",
        "13_15",
        "14_20",
        "15_25",
        "16_5",
        "17_10",
        "18_15",
        "19_20",
        "20_25"
    ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    round_counter = models.IntegerField(initial=1)
    payment_total = makefield_integer()
# ******************************************************************************************************************** #
# *** STAGE 1
# ******************************************************************************************************************** #
    last_phase = makefield_integer()
    last_decision_phase = makefield_urn_decision()
    last_token_value_phase = makefield_integer()
    last_answer_correct_phase = makefield_integer()
    payment_phase_1 = makefield_integer()
    payment_phase_2 = makefield_integer()
    payment_phase_3 = makefield_integer()
    payment_phase_4 = makefield_integer()
    payment_stage_1 = makefield_integer()
    decision_phase_1 = makefield_urn_decision()
    decision_phase_2 = makefield_urn_decision()
    decision_phase_3 = makefield_urn_decision()
    decision_phase_4 = makefield_urn_decision()
    answer_correct_phase1 = makefield_integer()
    answer_correct_phase2 = makefield_integer()
    answer_correct_phase3 = makefield_integer()
    answer_correct_phase4 = makefield_integer()
    answer_correct_stage1 = makefield_integer()

    ############################### Consent #########################
    accepts_terms = models.BooleanField()

    ############################ Instructions #######################
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

    num_entered = models.IntegerField(
        label="Por favor indique el número de inconsistencias que logró identificar dentro del texto:",
        initial=0, 
    )

    ############################ PHASE 1 ############################
    question_1_phase1_urnz = makefield_urnz_question1()
    question_2_phase1_urnz = makefield_urnz_question2()
    question_3_phase1_urnz = makefield_urnz_question3()
    
    ############################ PHASE 2 ############################
    question_1_phase2_urnz = makefield_urnz_question1()
    question_2_phase2_urnz = makefield_urnz_question2()
    question_3_phase2_urnz = makefield_urnz_question3()

    ############################ PHASE 3 ############################
    question_1_phase3_urnz = makefield_urnz_question1()
    question_2_phase3_urnz = makefield_urnz_question2()
    question_3_phase3_urnz = makefield_urnz_question3() 

    ############################ PHASE 4 ############################
    question_1_phase4_urnz = makefield_urnz_question1() 
    question_2_phase4_urnz = makefield_urnz_question2()
    question_3_phase4_urnz = makefield_urnz_question3()
    

# ******************************************************************************************************************** #
# *** STAGE 2
# ******************************************************************************************************************** #
    payment_stage_2 = makefield_integer()
    answer_correct_stage2 = makefield_integer()
    count_flips = makefield_integer()
    flip_value = models.FloatField(initial=0.0)

    ############################ Instructions #######################
    question_1_stage2_instructions = makefield_string(
        '1. Imagina que has decidido invertir $4,000 y que la ficha lanzada ha caído sello ¿Cuánto dinero ganarás?',
        choices_gen_instructions4
    )

    question_2_stage2_instructions = makefield_string(
        '2. En caso de que inviertas $4000 y la ficha lanzada caiga en cara ¿Cuánto dinero ganarás?',
        choices_gen_instructions5
    )

    amount_inversion = models.IntegerField(
        label="Por favor, indica el monto que invertirás en el activo de riesgo (sin puntos o comas)", 
        min=0, 
        max=5000
    )

# ******************************************************************************************************************** #
# *** Encuesta sociodemográfica
# ******************************************************************************************************************** #
    genero = models.StringField(
        label="¿Cuál es su género?",
        choices=[["Masculino", "Masculino"], #[StoredValue, "Label"]
                ["Femenino", "Femenino"]],
        widget=widgets.RadioSelect,
    )
    edad = models.IntegerField(label="¿Cuántos años cumplidos tiene usted?")
    ciudad = models.StringField(label="¿En qué ciudad vive actualmente?")
    estrato = models.IntegerField(
        label="¿Cuál es el estrato de la vivienda en la cual habita actualmente?",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
            [6, "6"]],
        widget=widgets.RadioSelect)
    estado_civil =  models.StringField(
        label="¿Cuál es su estado civil? Escoja una opción",
        choices = [
            ["Soltero", "Soltero"],
            ["Casado ", "Casado "],
            ["Unión libre", "Unión libre"],
            ["Divorciado", "Divorciado"],
            ["Viudo", "Viudo"],
            ["Prefiero no decir", "Prefiero no decir"],
        ],
        widget=widgets.RadioSelect
    )
    numero_hijos = models.IntegerField(label="¿Cuántos hijos tiene usted?")
    identifica_cultura = models.StringField(
        label="De acuerdo con su cultura o rasgos físicos, usted es o se reconoce como:",
        choices = [
            ["Afro-colombiano", "Afro-colombiano"],
            ["Indígena ", "Indígena "],
            ["Mestizo", "Mestizo"],
            ["Mulato", "Mulato"],
            ["Blanco", "Blanco"],
            ["Raizal del archipielago", "Raizal del archipielago"],
            ["Palenquero", "Palenquero"],
            ["Otro", "Otro"],
            ["Prefiero no decir", "Prefiero no decir"],
        ],
        widget=widgets.RadioSelect
    )
    identifica_religion = models.StringField(
        label="¿En cuál de los siguientes grupos se identifica usted? Escoja una opción",
        choices = [
            ["Católico", "Católico"],
            ["Cristiano ", "Cristiano "],
            ["Testigo de Jehová", "Testigo de Jehová"],
            ["Ateo", "Ateo"],
            ["Judío", "Judío"],
            ["Musulmán", "Musulmán"],
            ["Hinduista", "Hinduista"],
            ["Otro", "Otro"],
            ["Prefiero no decir", "Prefiero no decir"],
        ],
        widget=widgets.RadioSelect
    )
    nivel_estudios = models.StringField(
        label="¿Cuál es el máximo nivel de estudios alcanzado a la fecha? Escoja una opción",
        choices = [
            ["Primaria incompleta", "Primaria incompleta"],
            ["Primaria completa ", "Primaria completa "],
            ["Básica secundaria (9o grado completo)", "Básica secundaria (9o grado completo)"],
            ["Media secundaria (11o grado completo)", "Media secundaria (11o grado completo)"],
            ["Técnico incompleto", "Técnico incompleto"],
            ["Técnico completo", "Técnico completo"],
            ["Tecnológico incompleto", "Tecnológico incompleto"],
            ["Tecnológico completo", "Tecnológico completo"],
            ["Pregrado incompleto", "Pregrado incompleto"],
            ["Pregrado completo", "Pregrado completo"],
            ["Postgrado incompleto", "Postgrado incompleto"],
            ["Posgrado completo", "Posgrado completo"],
        ],
        widget=widgets.RadioSelect
    )
    tendencia_politica = models.IntegerField(
        label="Hoy en día cuando se habla de tendencias políticas, mucha gente habla de aquellos que simpatizan más con la izquierda o con la derecha. Según el sentido que tengan para usted los términos 'izquierda' y 'derecha' cuando piensa sobre su punto de vista político, ¿dónde se encontraría usted en esta escala?",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
            [6, "6"],
            [7, "7"],
            [8, "8"],
            [9, "9"],
            [10, "10"],
        ],
        widget=widgets.RadioSelect,
    )
    disposicion_riesgos = models.IntegerField(
        label="Por favor, califique en un escala de 1 a 10 su disposición a asumir riesgos en general, siendo 1 para nada dispuesto y 10 completamente dispuesto",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
            [6, "6"],
            [7, "7"],
            [8, "8"],
            [9, "9"],
            [10, "10"],
        ],
        widget=widgets.RadioSelect,
    )
     # ******************************************************************************************************************** #
# *** Pregunta 24: Primer conjunto de afirmaciones (10 preguntas)
# ******************************************************************************************************************** #
    conseguir_esfuerzo =  models.StringField(
        label="Por lo general, cuando consigo lo que quiero es porque me he esforzado por lograrlo.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    planes_termino =  models.StringField(
        label="Cuando hago planes estoy casi seguro (a) que conseguiré que lleguen a buen término.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    juego_suerte =  models.StringField(
        label="Prefiero los juegos que entrañan algo de suerte que los que sólo requieren habilidad.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    propongo_aprender =  models.StringField(
        label="Si me lo propongo, puedo aprender casi cualquier cosa.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    mayores_logros =  models.StringField(
        label="Mis mayores logros se deben más que nada a mi trabajo arduo y a mi capacidad",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    establecer_metas =  models.StringField(
        label="Por lo general no establezco metas porque se me dificulta mucho hacer lo necesario para alcanzarlas.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    competencia_excelencia =  models.StringField(
        label="La competencia desalienta la excelencia",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    salir_adelante =  models.StringField(
        label="Las personas a menudo salen adelante por pura suerte.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    comparar_calificaciones =  models.StringField(
        label="En cualquier tipo de examen o competencia me gusta comparar mis calificaciones con las de los demás.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    empeno_trabajo = models.StringField(
        label="Pienso que no tiene sentido empeñarme en trabajar en algo que es demasiado difícil para mí.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    # ******************************************************************************************************************** #
# *** Pregunta 25: Segundo conjunto de afirmaciones (10 preguntas)
# ******************************************************************************************************************** #
    alcanzar_objetivos = models.StringField(
        label="Podré alcanzar la mayoría de los objetivos que me he propuesto.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    cumplir_tareas = models.StringField(
        label="Cuando me enfrento a tareas difíciles, estoy seguro de que las cumpliré.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    obtener_resultados = models.StringField(
        label="En general, creo que puedo obtener resultados que son importantes para mí.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    exito_esfuerzo = models.StringField(
        label="Creo que puedo tener éxito en cualquier esfuerzo que me proponga.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    superar_desafios = models.StringField(
        label="Seré capaz de superar con éxito muchos desafíos.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    confianza_tareas = models.StringField(
        label="Confío en que puedo realizar eficazmente muchas tareas diferentes.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    tareas_excelencia = models.StringField(
        label="Comparado con otras personas, puedo hacer la mayoría de las tareas muy bien.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
    tareas_dificiles = models.StringField(
        label="Incluso cuando las cosas son difíciles, puedo realizarlas bastante bien.",
        choices = [
            ["Fuertemente en desacuerdo", "Fuertemente en desacuerdo"],
            ["En desacuerdo", "En desacuerdo"],
            ["Ligeramente en desacuerdo", "Ligeramente en desacuerdo"],
            ["Ni de acuerdo, ni en desacuerdo", "Ni de acuerdo, ni en desacuerdo"],
            ["De acuerdo", "De acuerdo"],
            ["Fuertemente de acuerdo", "Fuertemente de acuerdo"],
        ],
        widget=widgets.RadioSelect,
    )
# ******************************************************************************************************************** #
# *** Pregunta 26: Segundo conjunto de afirmaciones (10 preguntas)
# ******************************************************************************************************************** #
    tarde_cita = models.IntegerField(
        label="Llegar tarde a una cita",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    comprar_vendedores_ambulantes = models.IntegerField(
        label="Comprar a vendedores ambulantes",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    trabajar_sin_contrato = models.IntegerField(
        label="Trabajar y recibir un pago sin que haya firmado un contrato formal (pintar una casa, realizar un reporte, etc.)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    emplear_sin_contrato = models.IntegerField(
        label="Darle trabajo a alguien y pagarle sin pedirle que firme un contrato formal (pintar una casa, realizar un reporte, etc.)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cotizar_pension = models.IntegerField(
        label="No cotizar al sistema de pensiones",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cotizar_salud = models.IntegerField(
        label="No aportar al sistema de salud",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cuenta_bancaria = models.IntegerField(
        label="No tener cuenta bancaria",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    pedir_prestado = models.IntegerField(
        label="Pedir dinero prestado a prestamistas informales (ejemplo: gota a gota)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    transporte_alternativo = models.IntegerField(
        label="Usar transportes alternativos como piratas o mototaxis",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    vender_informal = models.IntegerField(
        label="Vender cosas o hacer negocios de manera informal",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_votar = models.IntegerField(
        label="No votar",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    comprar_sin_factura = models.IntegerField(
        label="Comprar productos sin factura",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
# ******************************************************************************************************************** #
# *** Pregunta 27: Segundo conjunto de afirmaciones (10 preguntas)
# ******************************************************************************************************************** #
    tarde_cita_otros = models.IntegerField(
        label="Llegar tarde a una cita",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    comprar_vendedores_ambulantes_otros = models.IntegerField(
        label="Comprar a vendedores ambulantes",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    trabajar_sin_contrato_otros = models.IntegerField(
        label="Trabajar y recibir un pago sin que haya firmado un contrato formal (pintar una casa, realizar un reporte, etc.)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    emplear_sin_contrato_otros = models.IntegerField(
        label="Darle trabajo a alguien y pagarle sin pedirle que firme un contrato formal (pintar una casa, realizar un reporte, etc.)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cotizar_pension_otros = models.IntegerField(
        label="No cotizar al sistema de pensiones",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cotizar_salud_otros = models.IntegerField(
        label="No aportar al sistema de salud",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cuenta_bancaria_otros = models.IntegerField(
        label="No tener cuenta bancaria",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    pedir_prestado_otros = models.IntegerField(
        label="Pedir dinero prestado a prestamistas informales (ejemplo: gota a gota)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    transporte_alternativo_otros = models.IntegerField(
        label="Usar transportes alternativos como piratas o mototaxis",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    vender_informal_otros = models.IntegerField(
        label="Vender cosas o hacer negocios de manera informal",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_votar_otros = models.IntegerField(
        label="No votar",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    comprar_sin_factura_otros = models.IntegerField(
        label="Comprar productos sin factura",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect   
    )
# ******************************************************************************************************************** #
# *** Pregunta 28: Apropiado (10 preguntas)
# ******************************************************************************************************************** #
    tarde_cita_apropiado = models.IntegerField(
        label="Llegar tarde a una cita",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    comprar_vendedores_ambulantes_apropiado = models.IntegerField(
        label="Comprar a vendedores ambulantes",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    trabajar_sin_contrato_apropiado = models.IntegerField(
        label="Trabajar y recibir un pago sin que haya firmado un contrato formal (pintar una casa, realizar un reporte, etc.)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    emplear_sin_contrato_apropiado = models.IntegerField(
        label="Darle trabajo a alguien y pagarle sin pedirle que firme un contrato formal (pintar una casa, realizar un reporte, etc.)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cotizar_pension_apropiado = models.IntegerField(
        label="No cotizar al sistema de pensiones",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cotizar_salud_apropiado = models.IntegerField(
        label="No aportar al sistema de salud",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_cuenta_bancaria_apropiado = models.IntegerField(
        label="No tener cuenta bancaria",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    pedir_prestado_apropiado = models.IntegerField(
        label="Pedir dinero prestado a prestamistas informales (ejemplo: gota a gota)",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    transporte_alternativo_apropiado = models.IntegerField(
        label="Usar transportes alternativos como piratas o mototaxis",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    vender_informal_apropiado = models.IntegerField(
        label="Vender cosas o hacer negocios de manera informal",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    no_votar_apropiado = models.IntegerField(
        label="No votar",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect
    )
    comprar_sin_factura_apropiado = models.IntegerField(
        label="Comprar productos sin factura",
        choices = [
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
        ],
        widget=widgets.RadioSelect  
    )