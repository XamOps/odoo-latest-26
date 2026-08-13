from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    is_current_user_employee = fields.Boolean(
        compute="_compute_access_flags",
    )

    is_hr_manager = fields.Boolean(
        compute="_compute_access_flags",
    )

    @api.depends_context("uid")
    def _compute_access_flags(self):
        current_employee = self.env.user.employee_id
        is_manager = self.env.user.has_group("base.group_system")

        for employee in self:
            employee.is_current_user_employee = employee == current_employee
            employee.is_hr_manager = is_manager
