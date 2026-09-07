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

    # Inherited fields
    version_id = fields.Many2one(
        groups="hr.group_hr_user,pixel_custom_changes.group_hr_only_user")
    current_date_version = fields.Date(
        groups="hr.group_hr_user,pixel_custom_changes.group_hr_only_user")
    version_ids = fields.One2many(
        groups="hr.group_hr_user,pixel_custom_changes.group_hr_only_user")
    versions_count = fields.Integer(
        groups="hr.group_hr_user,pixel_custom_changes.group_hr_only_user")
    version_revision = fields.Char(
        groups="hr.group_hr_user,pixel_custom_changes.group_hr_only_user")
    current_leave_id = fields.Many2one(
        groups="hr.group_hr_user,pixel_custom_changes.group_hr_only_user")
    exceptional_location_id = fields.Many2one(
        groups="hr.group_hr_user,pixel_custom_changes.group_hr_only_user")
    birthday = fields.Date(
        groups="hr.group_hr_user,pixel_custom_changes.group_hr_only_user")
    has_work_entries = fields.Boolean(
        groups="hr.group_hr_user,pixel_custom_changes.group_hr_only_user")
    structure_id = fields.Many2one(
        groups="hr.group_hr_user,pixel_custom_changes.group_hr_only_user")

    @api.depends_context("uid")
    def _compute_access_flags(self):
        current_employee = self.env.user.employee_id
        is_manager = self.env.user.has_group("hr.group_hr_user") or self.env.user.has_group("base.group_system")

        for employee in self:
            employee.is_current_user_employee = employee == current_employee
            employee.is_hr_manager = is_manager

    @api.model
    def get_view(self, view_id=None, view_type="form", **options):
        res = super().get_view(view_id=view_id, view_type=view_type, **options)
        if view_type == "form":
            # is_officer = self.env.user.has_group("hr.group_hr_user") or self.env.user.has_group("base.group_system")
            is_officer = self.env.user.has_group("hr.group_hr_user")
            if not is_officer and "arch" in res:
                doc = etree.XML(res["arch"])
                doc.set("edit", "0")
                res["arch"] = etree.tostring(doc, encoding="unicode")
        return res

