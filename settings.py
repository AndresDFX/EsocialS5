from os import environ

SESSION_CONFIGS = [
    dict(
        name='informality_experiment',
        display_name='Informality experiment [Juan R.]',
        num_demo_participants=1,
        app_sequence=['informality_experiment'],
    ),
        dict(
        name='real_effort_numbers_t_t',
        display_name="Gift-exchange Game T-T",
        num_demo_participants=6,
        app_sequence=['real_effort_numbers_t_t']
    ),
    dict(
        name='real_effort_numbers_t_nt',
        display_name="Gift-exchange Game T-NT",
        num_demo_participants=6,
        app_sequence=['real_effort_numbers_t_nt']
    ),
    dict(
        name='real_effort_numbers_nt_t',
        display_name="Gift-exchange Game NT-T",
        num_demo_participants=6,
        app_sequence=['real_effort_numbers_nt_t']
    ),
    dict(
        name='real_effort_numbers_nt_nt',
        display_name="Gift-exchange Game NT-NT",
        num_demo_participants=6,
        app_sequence=['real_effort_numbers_nt_nt']
    ),  
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4122948265296'
