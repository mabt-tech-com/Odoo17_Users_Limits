# -*- coding: utf-8 -*-
from odoo import api, models, fields
from odoo.exceptions import UserError
import logging
from lxml import etree  # Import etree for XML parsing

_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.users'

    set_users_limit = fields.Integer(string='Set User Limit', tracking=True)

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(ResUsers, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        
        # Add logging for debugging
        _logger.info("User login: %s", self.env.user.login)
        
        if self.env.user.login != 'admin':
            doc = etree.XML(res['arch'])
            for node in doc.xpath("//field[@name='set_users_limit']"):
                node.set('invisible', '1')  # Set field invisible if user is not 'admin'
            res['arch'] = etree.tostring(doc, encoding='unicode')
        
        return res
