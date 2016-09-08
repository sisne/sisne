# -*- coding: utf-8 -*-

{
    'name' : 'Evozard 606',
    'version' : '1.1',
    'summary': '',
    'sequence': 30,
    'description': """
    
    
    """,
    'author': 'Evozard',
    'category': 'Account',
    'website': 'http://evozard.com/',
    'depends' : ['purchase','account'],
    'data': [
        'views/account_invoice_view.xml',
        'views/partner_view.xml',
        'views/service_tax_view.xml',
        'wizard/report_wizard.xml',
        'demo/purchase_good_category.xml'
    ],
    # 'demo': [
    #         'demo/purchase_good_category.xml',
    #         ],
    'installable': True,
    'auto_install': False,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
