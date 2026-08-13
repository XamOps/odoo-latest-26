# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def get_recurring_plan(self):
        plan  = self.env.ref('crm.crm_recurring_plan_monthly')
        if plan:
            return plan.id
        return False

    recurring_plan = fields.Many2one('crm.recurring.plan', default=get_recurring_plan)
