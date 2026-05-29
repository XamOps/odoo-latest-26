# -*- coding: utf-8 -*-

from odoo import models, fields, api


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
    access_user_ids = fields.Many2many('res.users')
    status = fields.Selection([
        ('green', 'GreenField'),
        ('brown', 'BrownField'),
        ('prospect', 'Prospect'),
        ('chase', 'Chase'),
        ('client', 'Client'),
        ('whiteField', 'WhiteField')
    ])

    @api.model
    def create(self, vals):
        res = super(ResPartner, self).create(vals)
        for rec in res:
            if rec.company_type == 'person' and not rec.parent_id:
                rec.parent_id = self.env.ref('pixel_custom_changes.account_res_partner').id
        return res
