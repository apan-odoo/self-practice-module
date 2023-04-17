from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class ReservationMain(models.Model):
    _name = "reservation.main"
    _description = "Reservation"

    name = fields.Char(required=True)
    address = fields.Char()
    phone = fields.Char()
    email = fields.Char()
    check_in = fields.Date(default=fields.Datetime.now())
    duration = fields.Integer(default=2)
    check_out = fields.Date(copy=False, compute="_compute_checkout", inverse='_inverse_checkout', readonly=False)
    no_of_person = fields.Integer()
    meal = fields.Selection(
        selection=[('veg', 'Veg'),
                   ('non_veg', 'Non-veg')]
    )
    net_amount = fields.Float()
    amount_paid = fields.Float()
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
    balance = fields.Float(compute="_compute_balance")
    state = fields.Selection(
        selection=[('new', 'New'),
                   ('checked_in', 'Checked In'),
                   ('checked_out', 'Checked Out'),
                   ('canceled', 'Canceled')]
    )
    active = fields.Boolean(default=True)
    room_type_id = fields.Many2one('room.type', string="Room Type")
    hotel_id = fields.Many2one('hotel', string="Hotel")
    extra_services_ids = fields.Many2many('services')
    agent = fields.Many2one('res.users', default=lambda self: self.env.user)

    @api.depends('net_amount', 'amount_paid')
    def _compute_balance(self):
        for record in self:
            record.balance = record.net_amount - record.amount_paid

    @api.depends('check_in', 'duration')
    def _compute_checkout(self):
        for record in self:
            record.check_out = record.check_in + relativedelta(days=record.duration)

    def _inverse_checkout(self):
        for record in self:
            record.duration = (record.check_out - record.check_in).days