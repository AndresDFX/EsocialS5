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

def make_radiohorizontal_button(label, choices):
    return models.IntegerField(
        choices=choices,
        label=label,
        widget=widgets.RadioSelectHorizontal,
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

choices_payment = [
    [1,'Etapa 1'], 
    [2,'Etapa 2']
]

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
    num_rounds = 20

    #STAGE 1
    coin_value = 20 # default: 20
    rate_error = 2 # default: 2
    min_length_textarea = 50 # default: 50
    max_length_textarea = 200 # default: 200
    num_seconds_stage_1 = 30 # default: 60
    urn_z_token_min_random = 2
    urn_z_token_max_random = 8
    urn_y_token_min_random = 0
    urn_y_token_max_random = 10

    images_per_phase = 25
    images_max_phase1 = images_per_phase
    images_max_phase2 = images_max_phase1*2
    images_max_phase3 = images_max_phase1*3
    images_max_phase4 = images_max_phase1*4 
    images_names_questions = [
        '1_1_1_4',
        '1_1_2_5',
        '1_1_3_6',
        '1_1_4_2',
        '1_1_5_4',
        '1_2_1_2',
        '1_2_2_6',
        '1_2_3_3',
        '1_2_4_3',
        '1_2_5_1',
        '1_3_1_4',
        '1_3_2_3',
        '1_3_3_5',
        '1_3_4_2',
        '1_3_5_3',
        '1_4_1_1',
        '1_4_2_2',
        '1_4_3_2',
        '1_4_4_4',
        '1_4_5_5',
        '1_5_1_4',
        '1_5_2_4',
        '1_5_3_2',
        '1_5_4_2',
        '1_5_5_1',
        '2_6_1_2',
        '2_6_2_4',
        '2_6_3_2',
        '2_6_4_5',
        '2_6_5_2',
        '2_7_1_3',
        '2_7_2_1',
        '2_7_3_2',
        '2_7_4_5',
        '2_7_5_3',
        '2_8_1_4',
        '2_8_2_3',
        '2_8_3_4',
        '2_8_4_2',
        '2_8_5_1',
        '2_9_1_4',
        '2_9_2_4',
        '2_9_3_6',
        '2_9_4_5',
        '2_9_5_1',
        '2_10_1_2',
        '2_10_2_3',
        '2_10_3_3',
        '2_10_4_4',
        '2_10_5_3',
        '3_11_1_2',
        '3_11_2_3',
        '3_11_3_3',
        '3_11_4_4',
        '3_11_5_2',
        '3_12_1_3',
        '3_12_2_2',
        '3_12_3_2',
        '3_12_4_3',
        '3_12_5_2',
        '3_13_1_3',
        '3_13_2_2',
        '3_13_3_2',
        '3_13_4_4',
        '3_13_5_1',
        '3_14_1_2',
        '3_14_2_2',
        '3_14_3_2',
        '3_14_4_4',
        '3_14_5_2',
        '3_15_1_3',
        '3_15_2_2',
        '3_15_3_3',
        '3_15_4_2',
        '3_15_5_4',
        '4_16_1_2',
        '4_16_2_2',
        '4_16_3_4',
        '4_16_4_5',
        '4_16_5_3',
        '4_17_1_2',
        '4_17_2_2',
        '4_17_3_4',
        '4_17_4_3',
        '4_17_5_2',
        '4_18_1_3',
        '4_18_2_1',
        '4_18_3_3',
        '4_18_4_5',
        '4_18_5_2',
        '4_19_1_4',
        '4_19_2_3',
        '4_19_3_3',
        '4_19_4_1',
        '4_19_5_2',
        '4_20_1_3',
        '4_20_2_2',
        '4_20_3_6',
        '4_20_4_2',
        '4_20_5_5'
    ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    round_counter = makefield_integer()
    payment_total = makefield_integer()
    choice_payment = make_radiohorizontal_button(
        "Seleccione el pago que desea: ",
        choices_payment
    )
# ******************************************************************************************************************** #
# *** STAGE 1
# ******************************************************************************************************************** #
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
    edad = models.IntegerField(label='¿Cuántos años cumplidos tiene?')
    ciudad = models.StringField(label='¿En qué ciudad vive actualmente?')

    rol_hogar = models.StringField(
        label='¿Cuál es su rol en su hogar? (Por favor, escoja una opción)',
        choices=['Padre / Madre', 'Espos@', 'Hij@', 'Otro']
    )

    estado_civil = models.StringField(
        label='¿Cuál es su estado civil? (Por favor, escoja una opción)',
        choices=['Soltero', 'Casado', 'Unión libre', 'Divorciado', 'Viudo', 'Prefiero no decir']
    )

    hijos = models.IntegerField(label='¿Cuántos hijos tiene usted?')

    etnia = models.StringField(
        label='De acuerdo con su cultura o rasgos físicos, usted es o se reconoce como:(Por favor, escoja una opción)',
        choices=['Afrocolombiano', 'Indigena', 'Mestizo', 'Mulato', 'Blanco', 'Raizal del archipielago', 'Palenquero', 'Otro', 'Prefiero no decir']
    )

    religion = models.StringField(
        label='¿En cuál de los siguientes grupos se identifica usted?(Por favor, escoja una opción)',
        choices=['Católico', 'Cristiano', 'Testigo de Jehová', 'Ateo', 'Agnóstico', 'Judío', 'Musulmán', 'Hinduista', 'Otro', 'Prefiero no decir' ]
    )

    estudios = models.StringField(
        label='¿Cuál es el máximo nivel de estudios alcanzado a la fecha? (Por favor, escoja una opción)',
        choices=[
            'Primaria incompleta',
            'Primaria completa',
            'Básica secundaria (9º grado completo)',
            'Media secundaria (11º grado completo)',
            'Técnico incompleto',
            'Técnico completo',
            'Tecnológico incompleto',
            'Tecnológico completo',
            'Pregrado incompleto',
            'Pregrado completo',
            'Postgrado incompleto',
            'Posgrado completo'
        ]
    )

    actividad_actual = models.StringField(
        label='Actualmente, ¿cuál es su actividad principal? (Por favor, escoja una opción)',
        choices=['Estudiar', 'Trabajar', 'Oficios del hogar', 'Buscar trabajo' ,'Otra actividad']
    )

    esta_laborando = models.BooleanField(
        label='¿Se encuentra usted laborando actualmente? (Por favor, escoja una opción)',
        choices=[
            [True, "Sí"],
            [False, "No"],
        ]
    )

    ingreso_mensual = models.StringField(
        label='¿Cuál es su nivel aproximado de ingresos mensuales (incluya mesadas, subsidios y remesas)?',
        choices=[
            'De 1 a $200.000',
            'De $200.001 a $400.000',
            'De $400.001 a $700.000',
            'De $700.001 a $1.000.000',
            'De $1.000.001 a $2.000.000',
            'De $2.000.001 a $5.000.000',
            'Más de 5.000.001',
            'Prefiero no decir'
        ]
    )

    gasto_mensual = models.StringField(
        label='¿Cuál es su nivel aproximado de gastos mensuales?',
        choices=[
            'De 1 a $200.000',
            'De $200.001 a $400.000',
            'De $400.001 a $700.000',
            'De $700.001 a $1.000.000',
            'De $1.000.001 a $2.000.000',
            'De $2.000.001 a $5.000.000',
            'Más de 5.000.001',
            'Prefiero no decir'
        ]
    )

    alimentos = models.IntegerField(label="Alimentos")
    aseo = models.IntegerField(label="Productos de aseo")
    electronicos = models.IntegerField(label="Artículos electrónicos")
    transporte = models.IntegerField(label="Transporte")
    servicios = models.IntegerField(label="Pago de servicios")
    diversion  = models.IntegerField(label="Diversión y ocio")
    ahorro = models.IntegerField(label="Ahorro")
    deudas = models.IntegerField(label="Pago de deudas")

    #Escala Likert
    offer_1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7,8,9,10], label= "")

    Estabilidad = models.IntegerField(choices=[1,2,3,4,5], label='Mantenerse invariable o inalterable en el mismo lugar, estado o situación.')
    Independencia = models.IntegerField(choices=[1,2,3,4,5], label='Autonomía de tomar las decisiones propias.')
    Descanso = models.IntegerField(choices=[1,2,3,4,5], label='Reposar fuerzas a través de un estado inactivo')
    Lucro = models.IntegerField(choices=[1,2,3,4,5], label='Ganancia o provecho de algún actividad u objeto.')
    Protección = models.IntegerField(choices=[1,2,3,4,5], label='Seguridad o respaldo frente a un acontecimiento.')

    encuesta_tabla1_pregunta1 = make_field('Por lo general, cuando consigo lo que quiero es porque me he esforzado por lograrlo.')
    encuesta_tabla1_pregunta2 = make_field('Cuando hago planes estoy casi seguro (a) que conseguiré que lleguen a buen término.')
    encuesta_tabla1_pregunta3 = make_field('Prefiero los juegos que entrañan algo de suerte que los que sólo requieren habilidad.')
    encuesta_tabla1_pregunta4 = make_field('Si me lo propongo, puedo aprender casi cualquier cosa.')
    encuesta_tabla1_pregunta5 = make_field('Mis mayores logros se deben más que nada a mi trabajo arduo y a mi capacidad.')
    encuesta_tabla1_pregunta6 = make_field('Por lo general no establezco metas porque se me dificulta mucho hacer lo necesario para alcanzarlas.')
    encuesta_tabla1_pregunta7 = make_field('La competencia desalienta la excelencia.')
    encuesta_tabla1_pregunta8 = make_field('Las personas a menudo salen adelante por pura suerte.')
    encuesta_tabla1_pregunta9 = make_field('En cualquier tipo de examen o competencia me gusta comparar mis calificaciones con las de los demás.')
    encuesta_tabla1_pregunta10 = make_field('Pienso que no tiene sentido empeñarme en trabajar en algo que es demasiado difícil para mí.')

    encuesta_tabla2_pregunta1 = make_field('Podré alcanzar la mayoría de los objetivos que me he propuesto.')
    encuesta_tabla2_pregunta2 = make_field('Cuando me enfrento a tareas difíciles, estoy seguro de que las cumpliré.')
    encuesta_tabla2_pregunta3 = make_field('En general, creo que puedo obtener resultados que son importantes para mí.')
    encuesta_tabla2_pregunta4 = make_field('Creo que puedo tener éxito en cualquier esfuerzo que me proponga.')
    encuesta_tabla2_pregunta5 = make_field('Seré capaz de superar con éxito muchos desafíos.')
    encuesta_tabla2_pregunta6 = make_field('Confío en que puedo realizar eficazmente muchas tareas diferentes.')
    encuesta_tabla2_pregunta7 = make_field('Comparado con otras personas, puedo hacer la mayoría de las tareas muy bien.')
    encuesta_tabla2_pregunta8 = make_field('Incluso cuando las cosas son difíciles, puedo realizarlas bastante bien.')
    encuesta_tabla2_pregunta9 = make_field('Podré alcanzar la mayoría de los objetivos que me he propuesto.')

    encuesta_tabla3_pregunta1 = make_field2 ('Llegar tarde a una cita')
    encuesta_tabla3_pregunta2 = make_field2 ('Comprar a vendedores ambulantes')
    encuesta_tabla3_pregunta3 = make_field2 ('Tirar basura en la calle')
    encuesta_tabla3_pregunta4 = make_field2 ('Trabajar y recibir un pago sin que haya firmado un contrato formal (pintar una casa, realizar un reporte, etc.)')
    encuesta_tabla3_pregunta5 = make_field2 ('Silbar o decirle un piropo a un (a) desconocido (a) en la calle')
    encuesta_tabla3_pregunta6 = make_field2 ('Darle trabajo a alguien y pagarle sin pedirle que firme un contrato formal (pintar una casa, realizar un reporte, etc.)')
    encuesta_tabla3_pregunta7 = make_field2 ('Consumir cerveza, aguardiente, ron u otras bebidas alcohólicas en un andén o parque')
    encuesta_tabla3_pregunta8 = make_field2 ('No cotizar al sistema de pensiones')
    encuesta_tabla3_pregunta9 = make_field2 ('No aportar al sistema de salud')
    encuesta_tabla3_pregunta10 = make_field2 ('No ceder un asiento preferente a una embarazada o un(a) anciano(a) se sube al bus')
    encuesta_tabla3_pregunta11 = make_field2 ('Colarse en las filas')
    encuesta_tabla3_pregunta12 = make_field2 ('No tener cuenta bancaria')
    encuesta_tabla3_pregunta13 = make_field2 ('Pedir dinero prestado a prestamistas informales (ejemplo: gota a gota)')
    encuesta_tabla3_pregunta14 = make_field2 ('No recoger los desechos de las mascotas')
    encuesta_tabla3_pregunta15 = make_field2 ('Usar transportes alternativos como piratas o mototaxis')
    encuesta_tabla3_pregunta16 = make_field2 ('Vender cosas o hacer negocios de manera informal')
    encuesta_tabla3_pregunta17 = make_field2 ('Usar plataformas de transporte como Uber, Didi, etc.')
    encuesta_tabla3_pregunta18 = make_field2 ('No votar')
    encuesta_tabla3_pregunta19 = make_field2 ('Ir a eventos políticos para conseguir empleo/beneficios personales')
    encuesta_tabla3_pregunta20 = make_field2 ('Comprar réplicas de productos originales (lociones, bolsos, zapatos, camisas)')
    encuesta_tabla3_pregunta21 = make_field2 ('Comprar productos sin factura')
    encuesta_tabla3_pregunta22 = make_field2 ('Subarrendar una habitación')
    encuesta_tabla3_pregunta23 = make_field2 ('Vivir en una habitación subarrendada')
    encuesta_tabla3_pregunta26 = make_field2 ('Circular en bicicleta por el andén (no usar la cicloruta)')