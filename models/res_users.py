# -*- coding: utf-8 -*-
from odoo import tools, api, models, _, fields
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, vals):
        users = self.env['res.users'].search([])
        user = self.env['res.users'].sudo().search([('login', '=', 'admin')])

        _logger.info("Number of existing users: %s", len(users))
        _logger.info("Admin user limit: %s", user.set_users_limit)

        user_limits = user.set_users_limit + 2

        if user_limits <= len(users):
            raise UserError(_("Maximum number of users created. Please contact your system administrator!"))

        res = super(ResUsers, self).create(vals)
        return res

    set_users_limit = fields.Integer(string='Set User Limit', tracking=True)
