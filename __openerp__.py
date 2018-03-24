# -*- coding: utf-8 -*-
{
    'name': "account_invoice_att",

    'summary': """
        Define one or more attachments on company level to send with every invoice
        eg. for general conditions""",

    'description': """
        Define one or more attachments on company level to send with every invoice
        eg. for general conditions""",

    'author': "Lubon bvba",
    'website': "http://www.lubon.be",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail', 'mass_mailing'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/res_company.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}