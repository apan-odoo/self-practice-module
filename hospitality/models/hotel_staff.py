from odoo import models, fields

class HotelStaff(models.Model):
    _name = "hotel.staff"
    _description = "Hotel staff Information"

    
    staff_no = fields.Integer()
    department = fields.Selection(
        selection=[('management', 'Management'),
                   ('kitchen', 'Kitchen'),
                   ('security', 'Security'),
                   ('sales_and_purchase', 'Sales and Purchase'),
                   ('hr_deparment', 'Human Resource')]
    )
    department_id = fields.Integer()
    staff_hotel_id = fields.Many2one("hospitality.hotel")
    