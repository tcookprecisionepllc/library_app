{
    'name': 'Library Management',
    'description': 'Manage library book calogue and lending.',
    'author': 'Daniel Reis',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
    ],
}
