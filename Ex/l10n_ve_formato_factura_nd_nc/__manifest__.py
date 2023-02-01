# -*- coding: utf-8 -*-
{
    'name': "Formatos de Factura, NC, ND de forma Libre 5 continente",

    'summary': """Formatos de Factura, NC, ND de forma Libre para 5 Continente""",

    'description': """
       Formatos de Factura, NC, ND de forma Libre para 5 continente.
       Formato de Nota de entrega ,todos los formato se muestran en base al cambio.
    """,
    'version': '15.0',
    'author': 'INM & LDR Soluciones Tecnológicas y Empresariales C.A',
    'category': 'Tools',
    'website': 'http://soluciones-tecno.com/',

    # any module necessary for this one to work correctly
    'depends': ['base','account','l10n_ve_igtf_formato_libre','ext_extension_nota_debit'],

    # always loaded
    'data': [
        'formatos/factura_libre.xml',
        'formatos/nota_entrega.xml' ,
       # 'formatos/account_move.xml' ,

     
    ],
    'application': True,
    'active':False,
    'auto_install': False,
}
