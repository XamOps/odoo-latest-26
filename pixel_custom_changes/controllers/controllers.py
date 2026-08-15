# -*- coding: utf-8 -*-

from odoo import http, SUPERUSER_ID
from odoo.http import request, Response
from datetime import datetime, timedelta
import json


class CamsAttendance(http.Controller):
    @http.route('/fetch_easylead_data', method=["POST", "GET"], csrf=False, auth='public', type='http')
    def fetch_easylead_data(self, **params):
        machine_id = params.get('stgid')
        param_direction = params.get('direction')
        db_name = params.get('db')
