import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-bank-statement-import",
    description="Meta package for oca-bank-statement-import Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_bank_statement_clear_partner>=15.0dev,<15.1dev',
        'odoo-addon-account_bank_statement_import_move_line>=15.0dev,<15.1dev',
        'odoo-addon-account_statement_import>=15.0dev,<15.1dev',
        'odoo-addon-account_statement_import_base>=15.0dev,<15.1dev',
        'odoo-addon-account_statement_import_camt54>=15.0dev,<15.1dev',
        'odoo-addon-account_statement_import_camt>=15.0dev,<15.1dev',
        'odoo-addon-account_statement_import_file_reconciliation_widget>=15.0dev,<15.1dev',
        'odoo-addon-account_statement_import_move_line>=15.0dev,<15.1dev',
        'odoo-addon-account_statement_import_ofx>=15.0dev,<15.1dev',
        'odoo-addon-account_statement_import_online>=15.0dev,<15.1dev',
        'odoo-addon-account_statement_import_online_gocardless>=15.0dev,<15.1dev',
        'odoo-addon-account_statement_import_online_paypal>=15.0dev,<15.1dev',
        'odoo-addon-account_statement_import_online_ponto>=15.0dev,<15.1dev',
        'odoo-addon-account_statement_import_paypal>=15.0dev,<15.1dev',
        'odoo-addon-account_statement_import_txt_xlsx>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
