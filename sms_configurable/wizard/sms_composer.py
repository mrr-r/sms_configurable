# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models


class SendSMS(models.TransientModel):
    _inherit = 'sms.composer'
    _description = 'Send SMS Wizard'

    def action_send_sms_mass_now(self):
        sms_api = self.env['sms.api']
        active_ids = self.env.context.get('active_ids')
        model = self.env[self.res_model]
        records = model.browse(active_ids)
        numbers = []
        msg = self.body
        for record in records.filtered(lambda r: r.mobile):
            numbers.append(record.mobile)
        sms_api.with_context(self.env.context)._send_sms(numbers, msg)
