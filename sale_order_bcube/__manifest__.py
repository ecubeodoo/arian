{
	'name': 'Arain Sales order', 
	'description': 'Manage your sales Orders', 
	'author': 'Muhammad Kamran & Muhammad Awais', 
	'depends': ['sale'], 
	'application': True,
	'data': [
	'views/template.xml',
 	'security/inwardpass_security.xml',
 	'security/ir.model.access.csv',
 	],
}