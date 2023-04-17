from odoo import models, fields


class Hotel(models.Model):
    _name = "hotel"
    _description = "Reservation Hotel"
    # _order = "sequence, name"

    name = fields.Char(required=True)
    # sequence = fields.Integer('Sequence', default=1)

    # _sql_constraints = [
    #     ('check_type', 'unique(name)', 'The tag name must be unique.')
    # ]
