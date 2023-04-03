from odoo import models, fields

class Room(models.Model):
    _name = 'hospitality.room'
    _description = 'Room'

    room_no = fields.Integer()
    room_type = fields.Selection(
        selection=[('single', 'Single'),
                   ('double', 'Double'),
                   ('triple', 'Triple'),
                   ('quad', 'Quad'),
                   ('suite', 'Suite'),
                   ('president_suite', 'President Suite')]
    )
    room_charges = fields.Float()
    room_hotel_id = fields.Many2one("hospitality.hotel")
    