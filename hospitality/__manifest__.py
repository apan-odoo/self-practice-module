{
    'name': "Hospitality",
    'version': '1.0',
    'author': "apan",
    'category': 'Management',
    'description': """

    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        # 'views/hospitality_manage.xml',
        'views/hospitality_hotels_view.xml',
        'views/hotel_staff_view.xml',
        'views/hospitality_guests_view.xml',
        'views/hospitality_reservations_view.xml',
        'views/hospitality_rooms_view.xml',
        'views/hospitality_menu_view.xml',   
    ],
    # data files containing optionally loaded demonstration data
    'demo': [

    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}