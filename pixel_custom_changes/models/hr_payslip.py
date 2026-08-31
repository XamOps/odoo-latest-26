from odoo import models


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    def action_print_custom_payslip(self):
        return self.env.ref(
            "pixel_custom_changes.action_report_custom_payslip"
        ).report_action(self)