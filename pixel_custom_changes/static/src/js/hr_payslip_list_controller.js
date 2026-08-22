import { patch } from "@web/core/utils/patch";
import { user } from "@web/core/user";
import { PayslipListController } from "@hr_payroll/views/payslip_list/hr_payslip_list_controller";

patch(PayslipListController.prototype, {
    async setup() {
        super.setup();
        this.is_canCreatePayRun = await (user.hasGroup("pixel_custom_changes.group_hr_payroll_only_manager") || user.hasGroup("hr_payroll.group_hr_payroll_manager"));
    }
})