
{
    'name':'Jeisys Product List', #프로그램 이름
    'author':'kyumin Hwang',
    'summary' : 'Product List',
    'data' : [
        'security/ir.model.access.csv',

        'wizard/Create_class.xml',
        'wizard/Create_line.xml',
        'wizard/Create_model.xml',
        'wizard/Create_genration.xml',

        'views/product_example_view.xml',
        'views/product_main_view.xml',
        
        'views/product_model_view.xml',
        'views/product_line_view.xml',
        'views/product_class_view.xml',
        'views/product_generation_view.xml',

        'views/product_main_menu.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'jeisys_product_list/static/src/js/my_kanban_script.js',
        ],
    },
    'license': 'LGPL-3',
    "installable": True,
    "auto_install": False,
    "application": True,
}