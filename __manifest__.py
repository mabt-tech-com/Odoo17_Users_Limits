# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
{
    'name': "Users Limits",
    'version': '17.0.0.2',
    'author': "Bytelegion",
    'website': "http://www.bytelegions.com",
    'depends': ['base'],
    'license': "AGPL-3",
    'category': "Tools",
    'summary': "This Module sets user creation limits.",
    'description': """
        Users Limits module allows admins to set a maximum user limit, preventing further user creation when the limit is reached. Portal and public users are excluded from this limit.
    """,
    'data': ['views/res_users_view.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.gif'],
    'readme': 'README.rst',  # This line ensures Odoo will fetch the module info from the README.rst file
}
