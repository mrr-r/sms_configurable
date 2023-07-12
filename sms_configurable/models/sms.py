# Copyright Maharaj

import requests

from odoo import _, api, models
from odoo.addons.iap.tools import iap_tools


class SmsApi(models.AbstractModel):
	_inherit = 'sms.api'

	@api.model
	def _send_sms(self, numbers, message):
		Yabande = self.env['res.partner'].search([])
		for Yaft in Yabande:
			if Yaft.sms_out:
				company = self.env.user.company_id
				url = company.sms_url

		try:

			for number in numbers:
				number_search = number
				rurl = url.replace('#SHOMAREMOBILE#', number).replace(
					'#PAYAM#', message)
				contentType = {
					'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
				requests.post(rurl,
								  headers=contentType, timeout=(5, 60))

		except requests.ConnectTimeout:
			print("Connection timed out")
		except requests.ReadTimeout:
			print("Response Time Out")
		except Exception as ex:
			print("Internal error: " + str(ex))

	@api.model
	def _send_sms_batch(self, messages):
		numbers = []
		msg = messages[0].get('content')
		for message in messages:
			numbers.append(message.get('number'))
		self._send_sms(numbers, msg)
