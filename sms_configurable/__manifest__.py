# Copyright Maharaj


{
    'name': 'SMS Configurable Gateway',
    'version': '16.0.0.0.1',
    'license': 'AGPL-3',
    'category': 'Comunication',
    'sequence': 1,
    'complexity': 'easy',
    'author': 'Maharaj',
    'depends': [
        'base',
        'mail',
        'sms'
    ],
    'data': [
        'views/company_view.xml',
        'views/partner_view.xml',
        'wizard/sms_composer_views.xml',
    ],
    'installable': True,
}
