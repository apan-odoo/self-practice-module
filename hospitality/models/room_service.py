from odoo import fields, models

class RoomService(models.Model):
    _name = "room.service"
    _description = "Room services"
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Integer()

    _sql_constraints = [
        ('check_service', 'unique(name)', 'This service already exists')
    ]