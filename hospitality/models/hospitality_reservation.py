from odoo import models, fields, api

class Reservation(models.Model):
    _name = 'hospitality.reservation'
    _discription = 'Reservation'

    booking_name = fields.Char(required=True)
    # booking_id = fields.Char(required=True, copy=False)
    check_in = fields.Date(copy=False)
    check_out = fields.Date(copy=False)
    no_of_person = fields.Integer()
    meal = fields.Selection(
        selection=[('veg', 'Veg'),
                   ('non_veg', 'Non-veg')]
    )
    net_amount = fields.Float()
    amount_paid = fields.Float()
    balance = fields.Float(compute="_compute_balance")
    company = fields.Selection(
        selection=[('direct', 'Direct'),
                   ('goibibo', 'Goibibo'),
                   ('makemytrip', 'Makemytrip'),
                   ('yatra', 'Yatra')]
    )
    # info_id = fields.Many2one('hospitality.guest', required=True)
    extra_services_ids = fields.Many2many("room.service", string="Extra services")
    reservation_hotel_id = fields.Many2one("hospitality.hotel")
    guest_id = fields.Many2one("hospitality.guest")
    # reservation_type_id = fields.Many2one('hospitality.guest',related='reservation_hotel_id.reservation_type_id', store=True)

    @api.depends('net_amount', 'amount_paid')
    def _compute_balance(self):
        for record in self:
            record.balance = record.net_amount - record.amount_paid