# -*- coding: utf-8 -*-
from openerp import http

# class AccountDgii(http.Controller):
#     @http.route('/account_dgii/account_dgii/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_dgii/account_dgii/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_dgii.listing', {
#             'root': '/account_dgii/account_dgii',
#             'objects': http.request.env['account_dgii.account_dgii'].search([]),
#         })

#     @http.route('/account_dgii/account_dgii/objects/<model("account_dgii.account_dgii"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_dgii.object', {
#             'object': obj
#         })