# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class HrVersion(models.Model):
    _inherit = 'hr.version'

    date_version = fields.Date(
        groups="hr.group_hr_user,pixel_custom_changes.group_hr_only_user")
