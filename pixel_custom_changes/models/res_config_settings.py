# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    easylead_url = fields.Char(config_parameter='pixel_custom_changes.easylead_url', readonly=False)
    easylead_api_key = fields.Char(config_parameter='pixel_custom_changes.easylead_api_key', readonly=False)

    apollo_url = fields.Char(config_parameter='pixel_custom_changes.apollo_url', readonly=False)
    apollo_api_key = fields.Char(config_parameter='pixel_custom_changes.apollo_api_key', readonly=False)
