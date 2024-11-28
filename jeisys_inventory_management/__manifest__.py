
{
    'name':'Jeisys Inventory ManageMent', #프로그램 이름
    'author':'kyumin Hwang',
    'summary' : 'Jeisys producet Management',
    'data' : [
        'security/ir.model.access.csv',

        'views/inventory_management_view.xml',
        'views/inventory_management_menus.xml',
    ],
    'license': 'LGPL-3',
    "installable": True,
    "auto_install": False,
    "application": True,
}