{
    'name': "N-Development extension",
    'version': '1.0',
    'depends': ['base', 'mail', 'sale', 'sale_management', 'sale_stock'],
    'summary': """ Test task for  N-Development
                """,
    'author': "My company",
    'category': 'Category',
    'description': """
    Module with extension to sale order line
    """,
    # data files always loaded at installation
    'data': [
        'view/sale_order_inh.xml',
        'view/res_partner_inh.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
