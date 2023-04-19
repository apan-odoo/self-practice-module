from odoo import models, fields, api
# from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError

class ReservationMain(models.Model):
    _name = "reservation.main"
    _description = "Reservation"

    name = fields.Char(required=True)
    address = fields.Char()
    phone = fields.Char()
    email = fields.Char()
    check_in = fields.Date(copy=False)
    duration = fields.Integer(compute="_compute_duration", string="Duration (days)", readonly=False)
    check_out = fields.Date(copy=False)
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
    guestid_no = fields.Char()
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
    state = fields.Selection(default='new',
        selection=[('new', 'New'),
                   ('checked_in', 'Checked In'),
                   ('checked_out', 'Checked Out'),
                   ('canceled', 'Canceled')]
    )
    active = fields.Boolean(default=True)
    room_type_id = fields.Many2one('room.type', string="Room Type")
    hotel_id = fields.Many2one('hotel', string="Hotel")
    extra_services_ids = fields.Many2many('extra.service')
    agent = fields.Many2one('res.users', default=lambda self: self.env.user)
    hotel_address = fields.Char(related="hotel_id.add")
    hotel_review = fields.Selection(related="hotel_id.review")

    @api.depends('net_amount', 'amount_paid')
    def _compute_balance(self):
        for record in self:
            record.balance = record.net_amount - record.amount_paid

    # @api.depends('check_in', 'duration')
    # def _compute_checkout(self):
    #     for record in self:
    #         record.check_out = record.check_in + relativedelta(days=record.duration)

    # def _inverse_checkout(self):
    #     for record in self:
    #         record.duration = (record.check_out - record.check_in).days

    @api.depends('check_in', 'check_out')
    def _compute_duration(self):
        for record in self:
            if record.check_out and record.check_in:
                record.duration = (record.check_out - record.check_in).days
    
    @api.constrains('check_in')
    def _checkin_state(self):
        if self.check_in:
            self.state = 'checked_in'

    def check_out_action(self):
        for record in self:
            if record.state == 'canceled':
                raise UserError('Canceled reservation cannot be check out')
            else:
                record.state = 'checked_out'

    def cancel_action(self):
        for record in self:
            if record.state == 'checked_out':
                raise UserError('Checked out reservation cannot be canceled')
            else:
                record.state = 'canceled'

    @api.ondelete(at_uninstall=False)
    def _on_delete_action(self):
        for record in self:
            if record.state in ['checked_in', 'checked_out']:
                raise UserError("Only new and canceled reservation can be deleted.")