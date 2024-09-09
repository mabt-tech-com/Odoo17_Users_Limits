# -*- coding: utf-8 -*-
from odoo import tools, api, models, _, fields
from odoo.exceptions import UserError
from odoo.tools import config


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, vals):
        users = self.env['res.users'].search([])
        user = self.env['res.users'].sudo().search([('login', '=', 'admin')])
        user_limits = user.set_users_limit + 2
        if user_limits <= len(users):
            raise UserError("Maximum number of users created. Please contact to your system administrator!")
        res = super(ResUsers, self).create(vals)
        return res

    set_users_limit = fields.Integer(string='Set User Limit', tracking=True)
