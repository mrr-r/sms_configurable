# Copyright Maharaj

import logging
import threading

from odoo import api, fields, models, tools, _

_logger = logging.getLogger(__name__)


class SmsSms(models.Model):
    _inherit = 'sms.sms'

    def _postprocess_iap_sent_sms(self, iap_results, failure_reason=None, unlink_failed=False, unlink_sent=True):
        pass
