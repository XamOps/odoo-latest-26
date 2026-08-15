# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import requests
import base64
import json


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
    email_1 = fields.Char(string='Email')
    email_2 = fields.Char(string='Email')
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

    def action_give_action(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Give Access',
            'res_model': 'give.access.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_partner_ids': self.ids}
        }

    def fetch_easylead_data(self):
        config = self.env['ir.config_parameter'].sudo()
        url = config.get_param('pixel_custom_changes.easylead_url')
        api_key = config.get_param('pixel_custom_changes.easylead_api_key')
        if not url or not api_key:
            raise UserError(_("Please provide easylead url and api key."))
        header = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Enapi-Key': api_key}
        for rec in self:
            params = {
                'data': {
                    'email': rec.email or rec.email_1 or rec.email_2,
                    'url': rec.linkedin_url,
                    # "callbackUrl": "https://fe38-45-250-44-201.ngrok-free.app/fetch_easylead_data"
                    "callbackUrl": " https://webhook.site/de992029-1d1a-4eb1-8c8e-ec8c17c39d7c"
                }
            }   
            try:
                response = requests.get(url, json=params, headers=header)
                result = json.loads(response.content)
                if result.get('status') == '1':
                    print(result)
                else:
                    raise ValidationError(_(result.get('message')))
            except Exception as e:
                raise ValidationError(e)

    def fetch_apollo_data(self):
        config = self.env['ir.config_parameter'].sudo()
        url = config.get_param('pixel_custom_changes.apollo_url')
        api_key = config.get_param('pixel_custom_changes.apollo_api_key')
        if not url or not api_key:
            raise UserError(_("Please provide apollo url and api key."))
        header = {'Content-Type': 'application/json', 'Accept': 'application/json', 'x-api-key': api_key}
        for rec in self:
            params = {
                'email': rec.email or rec.email_1 or rec.email_2,
                'linkedin_url': rec.linkedin_url,
            }
            try:
                response = requests.get(url, json=params, headers=header)
                result = json.loads(response.content)
                if response.status_code == 200:
                    if result.get("person").get('city'):
                        rec.city = result.get("person").get('city')
                    if result.get("person").get('state'):
                        rec.state_id = self.env['res.country.state'].search(['name', '=', (result.get("person").get('state'))], limit=1).id
                    if result.get("person").get('country'):
                        rec.country_id = self.env['res.country'].search(['name', '=', (result.get("person").get('country'))], limit=1).id
                    if result.get("person").get('email'):
                        rec.email = result.get("person").get('email')
                    if result.get("person").get('linkedin_url'):
                        rec.linkedin_url = result.get("person").get('linkedin_url')
                    if result.get("person").get('name'):
                        rec.name = result.get("person").get('name')
                    if result.get("person").get('organization').get('name') and rec.parent_id:
                        rec.parent_id.name = result.get("person").get('organization').get('name')

                    print(result)
                else:
                    raise ValidationError(_(result.get('message')))
            except Exception as e:
                raise ValidationError(e)