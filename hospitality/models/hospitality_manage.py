from odoo import models, fields

class Manage(models.Model):
    _name = "hospitality.manage"
    _description = "Manage"

    name = fields.Char()