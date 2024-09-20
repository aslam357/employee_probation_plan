{
    'name': "Employee Probation Plan",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Amzsys",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','hr', 'hr_recruitment','mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/employee_probation.xml',
        'views/email_templates.xml',
                'views/employee_probation.xml',
                'views/kanban_view.xml',
                'views/menu_items.xml',
                'views/grouping_employeestatus.xml',
                'wizard/review_wizard.xml',
                'wizard/set_plan_wizard.xml',
    ],
'css': [
    'static/src/css/styles.css',
],

}

