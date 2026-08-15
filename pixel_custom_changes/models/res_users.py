# -*- coding: utf-8 -*-

from odoo import models, fields, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    partner_access_ids = fields.Many2many('res.partner',
                                                compute="_compute_partner_access_ids")

    def _compute_partner_access_ids(self):
        for user in self:
            partner_ids = {2}
            if user.partner_id:
                partner_ids.add(user.partner_id.id)
                
            if hasattr(user, 'employee_id') and user.employee_id:
                employees = self.env['hr.employee'].search([])
                # Optimize by using Odoo's recordset mapping instead of a for loop
                partner_ids.update(employees.user_id.partner_id.ids)
                        
            user.partner_access_ids = [(6, 0, list(partner_ids))]
