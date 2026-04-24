# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    designation = fields.Char()
    department = fields.Char()
    linkedin_url = fields.Char(string='LinkedIn URL')
    facebook_url = fields.Char(string='Facebook URL')
    twitter_url = fields.Char(string='Twitter URL')
    description = fields.Char()
    mobile_no_1 = fields.Char()
    mobile_no_2 = fields.Char()
    mobile_no_3 = fields.Char()
