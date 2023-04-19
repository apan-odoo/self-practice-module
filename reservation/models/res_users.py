from odoo import models, fields

class ResUsers(models.Model):
    _inherit = "res.users"

    reservation_ids = fields.One2many("res.users", "agent")
    