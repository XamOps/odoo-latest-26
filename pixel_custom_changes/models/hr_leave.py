# -*- coding: utf-8 -*-

from odoo import models, fields, _
from odoo.exceptions import UserError


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

    def action_approve(self, check_state=True):
        current_employee = self.env.user.employee_id
        leave_to_approve = self.env['hr.leave']
        leave_to_validate = self.env['hr.leave']
        for leave in self:
            if ((check_state and leave.can_validate or not check_state and
                 leave.validation_type != "both") and
                    self.env.user.has_group("hr_holidays.group_hr_holidays_manager")):
                leave_to_validate += leave
                if leave.state != 'validate1' and self.employee_id.leave_manager_id.id != self.env.user.id:
                    raise UserError(self.env._(
                        'You cannot approve this leave, Manager need approve first.'))
            elif (check_state and leave.can_approve or not check_state and
                  leave.validation_type == 'both'):
                leave_to_approve += leave
            else:
                raise UserError(self.env._('You cannot approve this leave.'))
        leave_to_approve.write(
            {'state': 'validate1', 'first_approver_id': current_employee.id})
        leave_to_validate._action_validate(check_state)
        if not self.env.context.get('leave_fast_create'):
            self.activity_update()
        return True
