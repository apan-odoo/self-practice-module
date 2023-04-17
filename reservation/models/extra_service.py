from odoo import fields, models

class ExtraService(models.Model):
    _name = "extra.service"
    _description = "Extra Services"
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Integer()

    _sql_constraints = [
        ('check_tag', 'unique(name)', 'The tag name must be unique.')
    ]