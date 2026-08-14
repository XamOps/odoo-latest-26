# -*- coding: utf-8 -*-

from odoo import models, fields, _


class ResPartner(models.Model):
    _inherit = 'hr.leave'

    is_hr_manager = fields.Boolean(compute="_compute_is_hr_manager")

    def _compute_is_hr_manager(self):
        for leave in self:
            if self.env.user.employee_id.id == leave.employee_id.parent_id.id or self.env.user.has_group("base.group_system"):
                leave.is_hr_manager = True
            else:
                leave.is_hr_manager = False


    def _get_employee_domain(self):
        return [('id', '=', self.env.user.employee_id.id)]
