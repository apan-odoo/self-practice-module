{
    'name': "Reservation",
    'version': '1.0',
    'author': "apan",
    'category': 'Reservation',
    'description': """

    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/room_type_view.xml',
        'views/reservation_view.xml',
        'views/hotel_view.xml',
        'views/extra_service_view.xml',
        'views/menu.xml',
        'views/res_users_view.xml'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [

    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}