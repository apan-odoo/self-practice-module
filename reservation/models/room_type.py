from odoo import fields, models, api

class RoomType(models.Model):
    _name = "room.type"
    _description = "Reservation Room Type"
    _order = "name"


    name = fields.Char(required=True)
    # sequence = fields.Integer('Sequence', default=1)


    _sql_constraints = [
        ('check_type', 'unique(name)', 'The tag name must be unique.')
    ]