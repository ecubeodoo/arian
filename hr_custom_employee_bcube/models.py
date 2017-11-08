from odoo import models, fields, api
from datetime import datetime as dt
from dateutil import relativedelta as rd

# Hr_Employee
class Hr_Employee(models.Model):
    _inherit = 'hr.employee'

    laptop_des = fields.Char('Laptop/Desktop')
    name_as_pass = fields.Char('Name(As in Passport)')
    iqama_num = fields.Char('Iqama Number')
    employee_code = fields.Char()
    arabic_name = fields.Char()
    office = fields.Many2one('office.office')
    work_fax = fields.Char('Work Fax')
    serial_num = fields.Char('Serial No.')
    performence_manager = fields.Many2one('hr.employee','Performance Manager')
    grade = fields.Char()
    head = fields.Many2one('hr.employee','Head of Function')
    line_man = fields.Many2one('hr.employee','Line Manager')
    is_head = fields.Boolean('Is Head  of Function')
    is_line_man = fields.Boolean('Is Line Manager')
    religion =fields.Char()
    gosi_no =fields.Many2one('employee.grops','GOSI NO')
    spouse_no =fields.Char('Spouse Phone No.')
    address_ksa =fields.Char('Address in KSA')
    joining_date = fields.Date('Joining Date',required=True)
    leaving_date = fields.Date()
    serv_year = fields.Char('Total Service Year')
    vendor_no = fields.Char("Vendor No")
    vehiclee = fields.Many2many('vehicles.vehicles',string='Vehicle')
    project = fields.Many2one('project.project')
    mol_no = fields.Char("MOL No")
    iban = fields.Char("IBAN")
    bank_code = fields.Char("Bank Code")
    emp_status = fields.Selection([(
    	'Active','Active'),
    	('Inactive','Inactive'),],'Employee Status',required=True)
    dependent_id = fields.One2many('hr.dependent', 'dependent_relation', string="Dependent")
    qualifiction_id = fields.One2many('hr.qualification', 'qualification_relation_name', string="Qualifications")
    certification_id = fields.One2many('hr.certification', 'certification_relation', string="Certification")
    insurance_id = fields.One2many('hr.insurance', 'insurance_relation', string="Insurance")
    trainings_id = fields.One2many('hr.trainings', 'trainings_relation', string="Trainings")
    documents_id = fields.One2many('hr.documents', 'documents_relation', string="Documents")

    @api.onchange('joining_date','leaving_date')
    def onchange_dates(self):
    	if self.joining_date:
			if self.leaving_date:
				start_date_1  = dt.strptime(self.joining_date, "%Y-%m-%d")
				end_date_1   = dt.strptime(self.leaving_date, "%Y-%m-%d")
				r = rd.relativedelta(end_date_1, start_date_1)
				if r.years > 0 :
					years = r.years
					months = r.months
					self.serv_year = "%s Years %s Months" %(years,months)
				else:
					years = r.years
					months = r.months
					self.serv_year = "%s Months" % months

# Dependent
class Dependent(models.Model):
	_name = 'hr.dependent'
	_rec_name = 'name'

	name = fields.Char('Name(As in Passport)')
	employee = fields.Many2one('hr.employee')
	arabic_name = fields.Char()
	dob = fields.Date('Date of Birth', required=True)
	date_issue = fields.Date('Date of Issue')
	date_expiry = fields.Date('Date of Expiry')
	nationality = fields.Selection([
		('US', 'United States'),
	    ('AF', 'Afghanistan'),
	    ('AL', 'Albania'),
	    ('DZ', 'Algeria'),
	    ('AS', 'American Samoa'),
	    ('AD', 'Andorra'),
	    ('AO', 'Angola'),
	    ('AI', 'Anguilla'),
	    ('AQ', 'Antarctica'),
	    ('AG', 'Antigua And Barbuda'),
	    ('AR', 'Argentina'),
	    ('AM', 'Armenia'),
	    ('AW', 'Aruba'),
	    ('AU', 'Australia'),
	    ('AT', 'Austria'),
	    ('AZ', 'Azerbaijan'),
	    ('BS', 'Bahamas'),
	    ('BH', 'Bahrain'),
	    ('BD', 'Bangladesh'),
	    ('BB', 'Barbados'),
	    ('BY', 'Belarus'),
	    ('BE', 'Belgium'),
	    ('BZ', 'Belize'),
	    ('BJ', 'Benin'),
	    ('BM', 'Bermuda'),
	    ('BT', 'Bhutan'),
	    ('BO', 'Bolivia'),
	    ('BA', 'Bosnia And Herzegowina'),
	    ('BW', 'Botswana'),
	    ('BV', 'Bouvet Island'),
	    ('BR', 'Brazil'),
	    ('BN', 'Brunei Darussalam'),
	    ('BG', 'Bulgaria'),
	    ('BF', 'Burkina Faso'),
	    ('BI', 'Burundi'),
	    ('KH', 'Cambodia'),
	    ('CM', 'Cameroon'),
	    ('CA', 'Canada'),
	    ('CV', 'Cape Verde'),
	    ('KY', 'Cayman Islands'),
	    ('CF', 'Central African Rep'),
	    ('TD', 'Chad'),
	    ('CL', 'Chile'),
	    ('CN', 'China'),
	    ('CX', 'Christmas Island'),
	    ('CC', 'Cocos Islands'),
	    ('CO', 'Colombia'),
	    ('KM', 'Comoros'),
	    ('CG', 'Congo'),
	    ('CK', 'Cook Islands'),
	    ('CR', 'Costa Rica'),
	    ('CI', 'Cote D`ivoire'),
	    ('HR', 'Croatia'),
	    ('CU', 'Cuba'),
	    ('CY', 'Cyprus'),
	    ('CZ', 'Czech Republic'),
	    ('DK', 'Denmark'),
	    ('DJ', 'Djibouti'),
	    ('DM', 'Dominica'),
	    ('DO', 'Dominican Republic'),
	    ('TP', 'East Timor'),
	    ('EC', 'Ecuador'),
	    ('EG', 'Egypt'),
	    ('SV', 'El Salvador'),
	    ('GQ', 'Equatorial Guinea'),
	    ('ER', 'Eritrea'),
	    ('EE', 'Estonia'),
	    ('ET', 'Ethiopia'),
	    ('FK', 'Falkland Islands (Malvinas)'),
	    ('FO', 'Faroe Islands'),
	    ('FJ', 'Fiji'),
	    ('FI', 'Finland'),
	    ('FR', 'France'),
	    ('GF', 'French Guiana'),
	    ('PF', 'French Polynesia'),
	    ('TF', 'French S. Territories'),
	    ('GA', 'Gabon'),
	    ('GM', 'Gambia'),
	    ('GE', 'Georgia'),
	    ('DE', 'Germany'),
	    ('GH', 'Ghana'),
	    ('GI', 'Gibraltar'),
	    ('GR', 'Greece'),
	    ('GL', 'Greenland'),
	    ('GD', 'Grenada'),
	    ('GP', 'Guadeloupe'),
	    ('GU', 'Guam'),
	    ('GT', 'Guatemala'),
	    ('GN', 'Guinea'),
	    ('GW', 'Guinea-bissau'),
	    ('GY', 'Guyana'),
	    ('HT', 'Haiti'),
	    ('HN', 'Honduras'),
	    ('HK', 'Hong Kong'),
	    ('HU', 'Hungary'),
	    ('IS', 'Iceland'),
	    ('IN', 'India'),
	    ('ID', 'Indonesia'),
	    ('IR', 'Iran'),
	    ('IQ', 'Iraq'),
	    ('IE', 'Ireland'),
	    ('IL', 'Israel'),
	    ('IT', 'Italy'),
	    ('JM', 'Jamaica'),
	    ('JP', 'Japan'),
	    ('JO', 'Jordan'),
	    ('KZ', 'Kazakhstan'),
	    ('KE', 'Kenya'),
	    ('KI', 'Kiribati'),
	    ('KP', 'Korea (North)'),
	    ('KR', 'Korea (South)'),
	    ('KW', 'Kuwait'),
	    ('KG', 'Kyrgyzstan'),
	    ('LA', 'Laos'),
	    ('LV', 'Latvia'),
	    ('LB', 'Lebanon'),
	    ('LS', 'Lesotho'),
	    ('LR', 'Liberia'),
	    ('LY', 'Libya'),
	    ('LI', 'Liechtenstein'),
	    ('LT', 'Lithuania'),
	    ('LU', 'Luxembourg'),
	    ('MO', 'Macau'),
	    ('MK', 'Macedonia'),
	    ('MG', 'Madagascar'),
	    ('MW', 'Malawi'),
	    ('MY', 'Malaysia'),
	    ('MV', 'Maldives'),
	    ('ML', 'Mali'),
	    ('MT', 'Malta'),
	    ('MH', 'Marshall Islands'),
	    ('MQ', 'Martinique'),
	    ('MR', 'Mauritania'),
	    ('MU', 'Mauritius'),
	    ('YT', 'Mayotte'),
	    ('MX', 'Mexico'),
	    ('FM', 'Micronesia'),
	    ('MD', 'Moldova'),
	    ('MC', 'Monaco'),
	    ('MN', 'Mongolia'),
	    ('MS', 'Montserrat'),
	    ('MA', 'Morocco'),
	    ('MZ', 'Mozambique'),
	    ('MM', 'Myanmar'),
	    ('NA', 'Namibia'),
	    ('NR', 'Nauru'),
	    ('NP', 'Nepal'),
	    ('NL', 'Netherlands'),
	    ('AN', 'Netherlands Antilles'),
	    ('NC', 'New Caledonia'),
	    ('NZ', 'New Zealand'),
	    ('NI', 'Nicaragua'),
	    ('NE', 'Niger'),
	    ('NG', 'Nigeria'),
	    ('NU', 'Niue'),
	    ('NF', 'Norfolk Island'),
	    ('MP', 'Northern Mariana Islands'),
	    ('NO', 'Norway'),
	    ('OM', 'Oman'),
	    ('PK', 'Pakistan'),
	    ('PW', 'Palau'),
	    ('PA', 'Panama'),
	    ('PG', 'Papua New Guinea'),
	    ('PY', 'Paraguay'),
	    ('PE', 'Peru'),
	    ('PH', 'Philippines'),
	    ('PN', 'Pitcairn'),
	    ('PL', 'Poland'),
	    ('PT', 'Portugal'),
	    ('PR', 'Puerto Rico'),
	    ('QA', 'Qatar'),
	    ('RE', 'Reunion'),
	    ('RO', 'Romania'),
	    ('RU', 'Russian Federation'),
	    ('RW', 'Rwanda'),
	    ('KN', 'Saint Kitts And Nevis'),
	    ('LC', 'Saint Lucia'),
	    ('VC', 'St Vincent/Grenadines'),
	    ('WS', 'Samoa'),
	    ('SM', 'San Marino'),
	    ('ST', 'Sao Tome'),
	    ('SA', 'Saudi Arabia'),
	    ('SN', 'Senegal'),
	    ('SC', 'Seychelles'),
	    ('SL', 'Sierra Leone'),
	    ('SG', 'Singapore'),
	    ('SK', 'Slovakia'),
	    ('SI', 'Slovenia'),
	    ('SB', 'Solomon Islands'),
	    ('SO', 'Somalia'),
	    ('ZA', 'South Africa'),
	    ('ES', 'Spain'),
	    ('LK', 'Sri Lanka'),
	    ('SH', 'St. Helena'),
	    ('PM', 'St.Pierre'),
	    ('SD', 'Sudan'),
	    ('SR', 'Suriname'),
	    ('SZ', 'Swaziland'),
	    ('SE', 'Sweden'),
	    ('CH', 'Switzerland'),
	    ('SY', 'Syrian Arab Republic'),
	    ('TW', 'Taiwan'),
	    ('TJ', 'Tajikistan'),
	    ('TZ', 'Tanzania'),
	    ('TH', 'Thailand'),
	    ('TG', 'Togo'),
	    ('TK', 'Tokelau'),
	    ('TO', 'Tonga'),
	    ('TT', 'Trinidad And Tobago'),
	    ('TN', 'Tunisia'),
	    ('TR', 'Turkey'),
	    ('TM', 'Turkmenistan'),
	    ('TV', 'Tuvalu'),
	    ('UG', 'Uganda'),
	    ('UA', 'Ukraine'),
	    ('AE', 'United Arab Emirates'),
	    ('UK', 'United Kingdom'),
	    ('UY', 'Uruguay'),
	    ('UZ', 'Uzbekistan'),
	    ('VU', 'Vanuatu'),
	    ('VA', 'Vatican City State'),
	    ('VE', 'Venezuela'),
	    ('VN', 'Viet Nam'),
	    ('VG', 'Virgin Islands (British)'),
	    ('VI', 'Virgin Islands (U.S.)'),
	    ('EH', 'Western Sahara'),
	    ('YE', 'Yemen'),
	    ('YU', 'Yugoslavia'),
	    ('ZR', 'Zaire'),
	    ('ZM', 'Zambia'),
	    ('ZW', 'Zimbabwe')])
	relation = fields.Many2one('relation.relation')
	religion = fields.Many2one('religion.religion')
	iqama_num = fields.Char('Iqama Number')
	serial_num = fields.Char('Serial Number')
	issue_place = fields.Many2one('issued_place.issued_place')

	dependent_relation = fields.Many2one('hr.employee')

# Qualification
class Qualification(models.Model):
	_name = 'hr.qualification'
	_rec_name = 'uni_name'

	uni_name = fields.Many2one('office.office',string='University Name', required=True)
	prg_status = fields.Char('Program Status')
	comp_date = fields.Date('Completion Date')
	contact_name = fields.Char('Contact Name')
	contact_phn = fields.Char('Contact Phone No')
	contact_email = fields.Char('Contact Email')

	qualification_relation_name = fields.Many2one('hr.employee',string='Qualification Relation Name')

# Certification
class Certification(models.Model):
	_name = 'hr.certification'
	_rec_name = 'car_name'

	car_name = fields.Char('Certification Name', required=True)
	issue_org = fields.Char('Issuing Organization', required=True)
	issue_date = fields.Date('Date of Issue')
	exp_date = fields.Date('Date of Expiry')
	regis_no = fields.Char('Registration No.')
	contact_name = fields.Char()
	contact_phn = fields.Char('Contact Phone No')
	contact_email = fields.Char()

	certification_relation = fields.Many2one('hr.employee',string='Certification Relation')

# EmployeeCard
class EmployeeCard(models.Model):
	_name = 'employee.card'
	_rec_name = 'employee'

	employee = fields.Many2one('hr.employee', required=True)
	employee_code = fields.Char(string='Employee Code')
	department = fields.Many2one('hr.department')
	job_title = fields.Many2one('hr.job',string='Job Title')
	office = fields.Char()
	card_type = fields.Selection([(
    	'Acces Card','Access Card'),
    	('Business Card','Business Card'),
    	('Id Card','Id Card')], required=True,string='Card Type')
	card_no = fields.Char(string='Card No.')
	requested_date = fields.Char(string='Requesed Date')
	reason = fields.Char()
	status = fields.Char()
	access_type = fields.Char(string='Access Type')
	period_stay = fields.Date(string='Period of Stay')

	@api.onchange('employee') 
	def onchange_date_id(self):
		if self.employee:
			self.employee_code = self.employee.employee_code
			self.job_title = self.employee.job_id
			self.department = self.employee.department_id
			self.office = self.employee.office.name

# Employee Amedment
class Employee_Amedment(models.Model):
	_name = 'contract.amedment'
	_rec_name = 'employee'

	employee = fields.Many2one('hr.employee', required=True)
	employee_code = fields.Char()
	contract = fields.Many2one('hr.contract', required=True)
	effective_date = fields.Date()
	office = fields.Many2one('office.office')
	department = fields.Many2one('hr.department')
	grade = fields.Char()
	job = fields.Many2one('hr.job')
	to_office = fields.Many2one('office.office')
	to_department = fields.Many2one('hr.department')
	to_grade = fields.Char()
	to_job = fields.Many2one('hr.job')

	@api.onchange('employee') 
	def onchange_employee(self):
		if self.employee:
			self.office = self.env['office.office'].search([('name','=',self.employee.office.name)])
			self.grade = self.employee.grade
			self.employee_code = self.employee.employee_code
			self.contract = self.env['hr.contract'].search([('name','=',self.employee.name)])
			self.department = self.env['hr.department'].search([('name','=',self.employee.department_id.name)])
			self.grade = self.employee.grade
			self.job = self.env['hr.job'].search([('name','=',self.employee.job_id.name)])

	@api.model
	def validate_changes(self):
		self.employee.department_id = self.to_department
		self.employee.office = self.to_office
		self.employee.grade = self.to_grade
		self.employee.job_id = self.to_job

# Employee Iqama
class Iqama(models.Model):
	_name = 'employee.iqama'
	_rec_name = 'employee'

	type_iqama = fields.Char('Type')
	employee = fields.Many2one('hr.employee', required=True)
	employee_code = fields.Char()
	office = fields.Char()
	department = fields.Char()
	job = fields.Char('Job Position')
	name = fields.Char('Name(As in Passport)')
	arabic_name = fields.Char()
	nationality = fields.Char()
	relegion = fields.Char('Religion')
	dob = fields.Date('Date of Birth')
	profession = fields.Char()
	iqama_no = fields.Char()
	serial_no = fields.Char()
	iqama_position = fields.Char()
	place_issue = fields.Char('Place of Issue')
	issue_date = fields.Date()
	expiry_date = fields.Date()
	date_hijri = fields.Char('Date of Expiry(Hijri)')
	arrival_date = fields.Date('Arrival Date in Suadi')
	in_saudi = fields.Boolean('In Saudi?')

	@api.onchange('employee') 
	def onchange_employee(self):
		if self.employee:
			self.employee_code = self.employee.employee_code
			self.job = self.employee.job_id.name
			self.name = self.employee.name_as_pass
			self.arabic_name = self.employee.arabic_name
			self.department = self.employee.department_id.name
			self.office = self.employee.office.name
			self.dob = self.employee.birthday
			self.relegion = self.employee.religion
			self.profession = self.employee.documents_id.profession
			self.serial_no = self.employee.serial_num
			self.name = self.employee.name_as_pass
			self.iqama_no = self.employee.iqama_num
			self.arabic_name = self.employee.arabic_name
			self.nationality = self.employee.country_id.name
			self.profession = self.employee.department_id.name

# Employee Clearance
class EmployeeClearance(models.Model):
	_name = 'employee.clearance'
	_rec_name = 'employee'

	employee = fields.Many2one('hr.employee')
	employee_code = fields.Char()
	department = fields.Char()
	office = fields.Char()
	email = fields.Char()
	contact_phone = fields.Char()
	seniority_date = fields.Date()
	res_date = fields.Date('Resignation/Term Date')
	last_country_day = fields.Date()
	last_day_work = fields.Date('Last Day of Work')
	letter_to_client = fields.Char()

	it_department = fields.One2many('it.department', 'department_relation')

	@api.onchange('employee') 
	def onchange_employee(self):
		if self.employee:
			self.employee_code = self.employee.employee_code
			self.department = self.employee.department_id.name
			self.office = self.employee.office.name
			self.email = self.employee.work_email
			self.contact_phone = self.employee.work_phone

# Employee Gosi 
class Gosi(models.Model):
	_name = 'employee.grops'
	_rec_name = 'employee'

	employee = fields.Many2one('hr.employee', required=True)
	employee_code = fields.Char()
	department = fields.Char()
	office = fields.Char()
	passport_no = fields.Char()
	nationality = fields.Char()
	iqama_no = fields.Char()
	type_d = fields.Char('Type')
	issue_date = fields.Date()
	dob = fields.Date('Date of Birth')
	dob_hijri = fields.Date('Date of Birth(Hijri)')
	gosi_no = fields.Char('GOSI No', required=True)

	grops_id = fields.One2many('employee.payslip', 'grops_relation')

	@api.onchange('employee') 
	def onchange_employee(self):
		if self.employee:
			self.employee_code = self.employee.employee_code
			self.department = self.employee.department_id.name
			self.office = self.employee.office.name
			self.passport_no = self.employee.passport_id
			self.nationality = self.employee.country_id
			self.iqama_no = self.employee.iqama_num

# Employee Leaving
class EOSLeaving(models.Model):
	_name = 'eos.leaving'
	_rec_name = 'employee'

	employee = fields.Many2one('hr.employee', required=True)
	employee_code = fields.Char()
	department = fields.Char()
	office = fields.Char()
	reason = fields.Char(required=True)
	requested_date = fields.Date()
	notice_date = fields.Date('Notice Start Date')
	end_date = fields.Date('Notice End Date')
	interview_date = fields.Date('Exit Interview Date')
	contact_person = fields.Char('GOSI No')
	description = fields.Text()
	employee_clearence_ref = fields.Many2one('employee.clearance', string = "Employee Clearence Ref", readonly = True)

	@api.multi
	def create_emp_clearence(self):
		clearence_recs            = self.env['employee.clearance'].search([])
		if self.employee_clearence_ref.id == 0:
			new = clearence_recs.create ({'employee':self.employee.id})
			self.employee_clearence_ref = new
			self.employee_clearence_ref.employee_code = self.employee_code
			self.employee_clearence_ref.department = self.department
			self.employee_clearence_ref.office = self.office
			self.employee_clearence_ref.email = self.employee.work_email
			self.employee_clearence_ref.contact_phone = self.employee.work_phone

		else:
			self.employee_clearence_ref.employee = self.employee.id
			self.employee_clearence_ref.employee_code = self.employee_code
			self.employee_clearence_ref.department = self.department
			self.employee_clearence_ref.office = self.office
			self.employee_clearence_ref.email = self.employee.work_email
			self.employee_clearence_ref.contact_phone = self.employee.work_phone

	@api.onchange('employee') 
	def onchange_employee(self):
		if self.employee:
			self.employee_code = self.employee.employee_code
			self.department = self.employee.department_id.name
			self.office = self.employee.office.name

# EOS
class EOS(models.Model):
	_name = 'employee.eos'
	_rec_name = 'employee'

	employee = fields.Many2one('hr.employee', required=True)
	department = fields.Char()
	job = fields.Char()
	contract = fields.Char()
	joining_date = fields.Date('Joining Date')
	leaving_date = fields.Date()
	employee_code = fields.Char()
	currency = fields.Char()
	year = fields.Char()
	date = fields.Date()
	type_d = fields.Char('Type')
	payslip = fields.Char()
	remaining_leave = fields.Float()
	no_year = fields.Char('No of Years')
	no_month = fields.Char('No of Months')
	no_days	= fields.Char('No of Days')
	total_award = fields.Float()
	leave_balance = fields.Float()
	salary	= fields.Float('Salary of Current Month')
	others = fields.Float()
	total_amount = fields.Float()

	@api.onchange('employee') 
	def onchange_employee(self):
		if self.employee:
			self.department = self.employee.department_id.name
			self.job = self.employee.job_id.name
			self.employee_code = self.employee.employee_code

# Contract
class Contract(models.Model):
    _inherit = 'hr.contract'

    employee_code = fields.Char()
    allow_mbl = fields.Boolean('Allow Mobile Allowance')
    sign_bonous = fields.Boolean('Sign on Bounus')
    loan_allow = fields.Boolean('Allow Loan Allowance')
    air_allow = fields.Boolean('Air Allowance')
    adults = fields.Integer('Adult(s)')
    children = fields.Integer()
    infants = fields.Integer()
    vac_des = fields.Many2one('vac_des.vac_des', string='Vacation Destination')
    package = fields.Float()
    gosi = fields.Boolean('GOSI')
    vehicle_attendance = fields.Integer('Vehicle Attendance')
    system_attendance = fields.Integer('System Attendance')
    line_manager_attendance = fields.Integer('Line Manager Attendance')
    incentive = fields.Float()
    expense_claim = fields.Float('Expense Claim')
    hr_visa_ticket = fields.Float('HR Visa/Ticket')
    other_allowances = fields.Float('Other Allowances')
    advance_salary = fields.Float('Advance AGT Salary')
    hr_expense = fields.Float('Hr Expense')
    cash_sales = fields.Float('Cash Sales')
    traffic_fine = fields.Float('Traffic Fine')
    bk_balance = fields.Float('Bank Balance')
    other_deductions = fields.Float('Other Deductions')

# Insurance
class Insurance(models.Model):
	_name = 'hr.insurance'
	_rec_name = 'member_name'

	card_code = fields.Char(required=True)
	member_name = fields.Char(required=True)
	dob = fields.Date('Date of Birth', required=True)
	clas_n = fields.Char('Class')
	gender = fields.Selection([
		('male','Male'),
		('femail','Femail'),
		])
	relation = fields.Many2one('relation.relation')
	sponsor_id = fields.Char()
	job = fields.Char()
	premium = fields.Float()
	start_date = fields.Date()
	expiry_date = fields.Date()

	insurance_relation = fields.Many2one('hr.employee')

# Trainings
class Trainings(models.Model):
	_name = 'hr.trainings'
	_rec_name = 'training_sum'

	training_sum = fields.Char('Training Summary')
	start_date = fields.Date('Start Date')
	end_date = fields.Date('End Date')
	type_training = fields.Char('Type of Training')
	training_company = fields.Char('Training Company')
	training_place = fields.Char('Training Place')
	status = fields.Char()
	
	trainings_relation = fields.Many2one('hr.employee',string='Training Relation')

# Documents
class Documents(models.Model):
	_name = 'hr.documents'
	_rec_name = 'number'

	type_d = fields.Many2one('documents.typed','Type', required=True)
	issue_date = fields.Date('Issue Date')
	expiry_date = fields.Date('Expiry Date')
	number = fields.Char(required=True)
	profession = fields.Char()
	date_hijri = fields.Char('Date of Expiry(Hijri)')
	place_issue = fields.Char('Place of Issue')
	notes = fields.Char()
	
	documents_relation = fields.Many2one('hr.employee')

# IT Department
class ItDepartment(models.Model):
	_name = 'it.department'
	_rec_name = 'item'


	item = fields.Char()
	status = fields.Char()
	handled_by = fields.Char()
	remarks = fields.Char()

	department_relation = fields.Many2one('employee.clearance')

# Employee Payslip
class Payslip(models.Model):
	_name = 'employee.payslip'

	payslip = fields.Char()
	date = fields.Date()
	gosi_ammount =fields.Char('GOSI Amount')

	grops_relation = fields.Many2one('employee.grops')

#######################################
#==>Helping Classes
#######################################

# office
class office(models.Model):
	_name = 'office.office'
	_rec_name = 'name'
	name = fields.Char()

# uni_name
class uni_name(models.Model):
	_name = 'uni_name.uni_name'
	_rec_name = 'name'
	name = fields.Char()

# vac_des
class vac_des(models.Model):
	_name = 'vac_des.vac_des'
	_rec_name = 'name'
	name = fields.Char()

# relation
class relation(models.Model):
	_name = 'relation.relation'
	_rec_name = 'name'
	name = fields.Char()

# religion
class religion(models.Model):
	_name = 'religion.religion'
	_rec_name = 'name'
	name = fields.Char()

# issue_place
class issue_place(models.Model):
	_name = 'issued_place.issued_place'
	_rec_name = 'name'
	name = fields.Char()

# documentstype
class xxdocumentstype(models.Model):
	_name = 'documents.typed'
	_rec_name = 'type_c'
	type_c = fields.Char('Type')

# project
class Project(models.Model):
	_name = 'projects.projects'
	_rec_name = 'name'
	name = fields.Char()

# Vehicle
class Vehicle(models.Model):
	_name = 'vehicles.vehicles'
	_rec_name = 'vehicle_model'
	vehicle_model = fields.Char("Vehicle Model")
	vehicle_no = fields.Char("Vehicle No")