# Copyright Maharaj

from odoo import models, fields


class Company(models.Model):
    _inherit = 'res.company'

    sms_url = fields.Char(
        string='SMS Url', help="Example: https://panel.asanak.com/webservice/v1rest/sendsms?username=YourUsername&password=YourPassword&source=YourSourceNumber&destination=#SHOMAREMOBILE#&message=#PAYAM#")