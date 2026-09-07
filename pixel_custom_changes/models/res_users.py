# -*- coding: utf-8 -*-

from odoo import models, fields, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    partner_access_ids = fields.Many2many('res.partner',
                                                compute="_compute_partner_access_ids")

    def _compute_partner_access_ids(self):
        self = self.sudo()
        for user in self:
            partner_ids = {1, 2, 3, 4}
            if user.partner_id:
                partner_ids.add(user.partner_id.id)
                
            if hasattr(user, 'employee_id') and user.employee_id:
                employees = self.env['hr.employee'].sudo().search([])
                users = self.env['res.users'].sudo().search([('active', 'in', [True, False])])
                partners = users.sudo().partner_id.ids + employees.sudo().user_id.sudo().partner_id.ids + employees.sudo().message_partner_ids.ids + users.sudo().company_ids.sudo().partner_id.ids
                # partners = users.sudo().partner_id.ids + employees.sudo().user_id.sudo().partner_id.ids + users.sudo().company_ids.sudo().partner_id.ids
                partner_ids.update(partners)
                        
            user.partner_access_ids = [(6, 0, list(partner_ids))]
