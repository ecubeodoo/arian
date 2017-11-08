# -*- coding: utf-8 -*-
{
    'name': "Berik Proforma Invoice",

    'summary': "Berik Proforma Invoice",

    'description': "Berik Proforma Invoice",

    'author': "Muhammmad Awais",
    'website': "http://www.bcube.com",

    # any module necessary for this one to work correctly
    'depends': ['base', 'report', 'sale'],
    # always loaded
    'data': [
        'template.xml',
        'views/module_report.xml',
    ],
    'css': ['static/src/css/report.css'],
}
