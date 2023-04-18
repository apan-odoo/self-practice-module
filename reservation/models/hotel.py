from odoo import models, fields, api


class Hotel(models.Model):
    _name = "hotel"
    _description = "Reservation Hotel"
    _order = "sequence, name"

    name = fields.Char(required=True)
    address = fields.Char()
    contact = fields.Char()
    review = fields.Selection(
        selection=[('no','no review'),
                   ('bad', 'Bad'),
                   ('good', 'Good'),
                   ('average', 'Average'),
                   ('exe', 'Excellent')]
    )
    sequence = fields.Integer('Sequence', default=1)
    reservation_ids = fields.One2many('reservation.main', 'hotel_id')
    # room_ids = fields.One2many('room.type', 'hotel_id')
    reservation_count = fields.Integer(compute="_compute_count")

    @api.depends('reservation_ids')
    def _compute_count(self):
        for record in self:
            record.reservation_count = len(record.reservation_ids)

    

    _sql_constraints = [
        ('check_type', 'unique(name)', 'The tag name must be unique.')
    ]
