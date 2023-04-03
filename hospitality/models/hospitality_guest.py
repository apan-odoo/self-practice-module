from odoo import models, fields

class Guest(models.Model):
    _name = 'hospitality.guest'
    _description = 'Guest'

    name = fields.Char(required=True)
    guest_id_type = fields.Selection(
        selection=[('aadhar_card', 'Aadhar card'),
                   ('pan_card', 'Pan card'),
                   ('driving_license', 'Driving license')]
    )
    guest_id_no = fields.Char()
    gender = fields.Selection(
        selection=[('male', 'Male'),
                   ('female', 'Female'),
                   ('other', 'Other')]
    )
    
    vehicle = fields.Boolean(default=False)
    vehicle_type = fields.Selection(
        selection=[('hatchback', 'Hatchback'),
                   ('suv', 'SUV'),
                   ('muv', 'MUV'),
                   ('sedan', 'Sedan')]
    )
    vehicle_no = fields.Char()
    # reservation_ids = fields.One2many("hospitality.reservation", "info_id")
    guest_reservation_ids = fields.One2many("hospitality.reservation","guest_id")