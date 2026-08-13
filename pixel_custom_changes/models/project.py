# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Project(models.Model):
    _inherit = 'project.project'

    # group_ids = fields.Many2many("res.groups", compute="_compute_group_ids", store=True)
    group_domain_ids = fields.Many2many("res.groups", relation='project_project_res_groups',
        column1='project_id', column2='group_id', compute='_compute_group_domain_ids')
    group_ids = fields.Many2many("res.groups", string="Department")

    def _compute_group_domain_ids(self):
        for record in self:
            record.group_domain_ids = [
                self.env.ref('pixel_custom_changes.group_department_devops').id,
                self.env.ref('pixel_custom_changes.group_department_marketing').id,
                self.env.ref('pixel_custom_changes.group_department_finance').id,
                self.env.ref('pixel_custom_changes.group_department_business').id]

    # @api.depends('message_partner_ids', 'message_partner_ids.user_ids', 'message_partner_ids.user_ids.group_ids')
    # def _compute_group_ids(self):
    #     devops = self.env.ref('pixel_custom_changes.group_department_devops', raise_if_not_found=False)
    #     marketing = self.env.ref('pixel_custom_changes.group_department_marketing', raise_if_not_found=False)
    #     finance = self.env.ref('pixel_custom_changes.group_department_finance', raise_if_not_found=False)
    #     business = self.env.ref('pixel_custom_changes.group_department_business', raise_if_not_found=False)
    #
    #     target_groups = self.env['res.groups']
    #     if devops: target_groups |= devops
    #     if marketing: target_groups |= marketing
    #     if finance: target_groups |= finance
    #     if business: target_groups |= business
    #
    #     for rec in self:
    #         users = rec.message_partner_ids.mapped('user_ids')
    #         user_groups = users.mapped('group_ids')
    #         assigned_groups = user_groups & target_groups
    #
    #         # Remove any groups that are automatically applied (implied) by other groups
    #         implied_groups = user_groups.mapped('implied_ids')
    #         final_groups = assigned_groups - implied_groups
    #
    #         rec.group_ids = [(6, 0, final_groups.ids)]
