{
    "name": "OWL Practice",  # 프로그램 이름
    "author": "kyumin Hwang",
    "summary": "OWL Practice",
    "sequnece": "-1",
    "description": "OWL Practice",
    "cataegory": "OWL",
    "dependes": ['base'],
    "data": ["security/ir.model.access.csv", "views/todo_list.xml"],
    "license": "LGPL-3",
    "assets": {
        "web.assets_backend": [
            'owl_practice/static/src/components/*/*.js',
            'owl_practice/static/src/components/*/*.xml',
            'owl_practice/static/src/components/*/*.scss',
        ],
    },
    "installable": True,
    "auto_install": False,
    "application": True,
}
