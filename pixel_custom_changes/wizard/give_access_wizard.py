from odoo import api, fields, models


class GiveAccessWizard(models.TransientModel):
    _name = 'give.access.wizard'
    _description = 'Give Access Wizard'

    access_users_ids = fields.Many2many("res.users", string="Access Users")
    partner_ids = fields.Many2many("res.partner", string="Partners")

    def action_give_access(self):
        self.partner_ids.access_user_ids = [(4, user.id, False) for user in self.access_users_ids]