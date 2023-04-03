from odoo import models, fields

class Hotel(models.Model):
    _name = 'hospitality.hotel'
    _description = 'Hotel'

    name = fields.Char(required=True)
    # address = fields.Char()
    city = fields.Char()
    state = fields.Char()
    zip_code = fields.Char()
    phone = fields.Char()
    email = fields.Char()
    website = fields.Char()
    staff_ids = fields.One2many("hotel.staff", "staff_hotel_id")
    room_ids = fields.One2many("hospitality.room", "room_hotel_id")
    reservation_ids = fields.One2many("hospitality.reservation", "reservation_hotel_id")