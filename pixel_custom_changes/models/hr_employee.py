from lxml import etree
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
        is_manager = self.env.user.has_group("pixel_custom_changes.group_hr_manager") or self.env.user.has_group("base.group_system")

        for employee in self:
            employee.is_current_user_employee = employee == current_employee
            employee.is_hr_manager = is_manager

    @api.model
    def get_view(self, view_id=None, view_type="form", **options):
        res = super().get_view(view_id=view_id, view_type=view_type, **options)
        if view_type == "form":
            # is_officer = self.env.user.has_group("hr.group_hr_user") or self.env.user.has_group("base.group_system")
            is_officer = self.env.user.has_group("pixel_custom_changes.group_hr_manager")
            if not is_officer and "arch" in res:
                doc = etree.XML(res["arch"])
                doc.set("edit", "0")
                res["arch"] = etree.tostring(doc, encoding="unicode")
        return res

