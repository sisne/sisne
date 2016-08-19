# -*- coding: utf-8 -*-

from openerp import models, fields, api

class AccountFiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'
    _description = 'Fiscal Position'

    @api.v8     # noqa
    def map_tax(self, taxes):
        result = self.env['account.tax'].browse()
        for tax in taxes:
            tax_count = 0
            for t in self.tax_ids:
                if t.tax_src_id == tax:
                    tax_count += 1
                    if t.tax_dest_id:
                        result |= t.tax_dest_id
            if not tax_count:
                result |= tax
        return result