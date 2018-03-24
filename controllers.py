# -*- coding: utf-8 -*-
from openerp import http

# class AccountInvoiceAtt(http.Controller):
#     @http.route('/account_invoice_att/account_invoice_att/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_invoice_att/account_invoice_att/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_invoice_att.listing', {
#             'root': '/account_invoice_att/account_invoice_att',
#             'objects': http.request.env['account_invoice_att.account_invoice_att'].search([]),
#         })

#     @http.route('/account_invoice_att/account_invoice_att/objects/<model("account_invoice_att.account_invoice_att"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_invoice_att.object', {
#             'object': obj
#         })