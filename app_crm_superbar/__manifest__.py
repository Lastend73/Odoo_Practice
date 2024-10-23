# -*- coding: utf-8 -*-


{
    'name': "App CRM browse by partner and User_id",
    'version': '16.0.0.1',
    'author': 'BinhTT',
    'category': 'Base',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Browse sale order by partner and sale channel. Use for parent children tree list kanban navigator. 
    ztree widget.Hierarchy Tree.Parent Children relation tree..
    """,
    'description': """
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'crm', 'sale'
    ],
    'data': [
        'views/crm_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'js': [
    ],
    'post_load': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}
