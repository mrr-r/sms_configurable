# Copyright Maharaj

from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    sms_out = fields.Boolean(
        string='SMS Send',
        help="Dismark this field if partner don't want to recieve SMS", translation=True)
