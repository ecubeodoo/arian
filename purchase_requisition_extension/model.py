# -*- coding: utf-8 -*- 
from odoo import models, fields, api

class PurchaseRequisitionExtension(models.Model):
	_name = 'purchase.requisition.extension'
	_rec_name = 'seq'

	mo_no = fields.Char("Manufacturing Order #")
	pr_no = fields.Char("Purchase Requisition #")
	pr_date = fields.Datetime("Purchase Requisition Date", required=False, readonly=False, select=True, default=lambda self: fields.datetime.now())
	app_doc_no = fields.Char("Approval Document #")
	app_doc_date = fields.Datetime("Approval Document Date", required=False, readonly=False, select=True, default=lambda self: fields.datetime.now())
	seq = fields.Char("PR No",readonly=True)
	state = fields.Selection([
		('draft', 'Draft'),
		('wait', 'Waiting for Approval'),
		('send_approval', 'Send for Approval'),
		('approve', 'Approved'),
		],default='draft')

	purchase_requisition_tree_link=fields.One2many('purchase.requisition.extension.tree','purchase_requisition_tree')

	@api.multi
	def cancel(self):
		self.state = "draft"

	@api.multi
	def wait(self):
		self.state = "wait"

	@api.multi
	def approve(self):
		self.state = "approve"

	@api.multi
	def send(self):
		self.state = "send_approval"

	@api.multi
	def create_purchase_order(self):

		vn_list = []
		v_list = []
		head = self.env['purchase.order'].search([])
		line = self.env['purchase.order.line'].search([])
		for x in self.purchase_requisition_tree_link:
			if x.vendor not in vn_list:
				vn_list.append(x.vendor)
		for y in vn_list:
			create_purchase = head.create({
					'partner_id':y.id,
					'date_order':self.pr_date,
					'date_planned':self.pr_date,
					})
			for x in self.purchase_requisition_tree_link:
				if y == x.vendor:
					create_line = line.create({
						'product_id':x.t_p.id,
						'name': x.t_p.name,
						'date_planned':self.pr_date,
						'product_qty':x.qty_pr,
						'price_unit':x.rate,
						'product_uom':x.uom.id,
						'uom':x.uom.id,
						'order_id':create_purchase.id,
						})
					x.qty_or=0
					x.qty_rm=0
					x.qty_or = x.qty_or + x.qty_pr
					x.qty_rm = x.qty_order - x.qty_or

	@api.model 
	def create(self, vals):
		vals['seq'] = self.env['ir.sequence'].next_by_code('pr.seq')
		new_record = super(PurchaseRequisitionExtension, self).create(vals) 
		return new_record

class PurchaseRequisitionExtensionTree(models.Model):
	
	_name = 'purchase.requisition.extension.tree'

	material_id = fields.Char("Material ID")
	material_name = fields.Many2one('product.template',string="Material Name")
	color=fields.Many2one('product.attribute.value',"Color")
	size=fields.Many2one('product.attribute.value',"Size")
	uom = fields.Many2one('product.uom', string="UOM", readonly=True)
	required_quantity = fields.Integer("Required Quantity")
	available_quantity = fields.Integer("Available Quantity")
	balance_quantity = fields.Integer("Balance Quantity")
	vendor = fields.Many2one('res.partner',"Vendor")
	remarks = fields.Char("Remarks")
	rate = fields.Integer("Rate")
	p_terms = fields.Selection([('cash','Cash'),('credit','Credit')],default='cash',string="Payment Terms")
	records = fields.Many2many('res.partner')
	purchase_requisition_tree = fields.Many2one('purchase.requisition.extension')
	qty_order = fields.Integer("Quantity to Order")
	cmnt = fields.Char("Comments")
	qty_pr = fields.Integer("Qty in purchase")
	qty_rm = fields.Integer("Qty Remain")
	qty_or = fields.Integer("Qty Ordered")
	t_p = fields.Many2one('product.product'," ")


	@api.onchange('material_name','required_quantity','color','size','qty_pr')
	def on_change_material_name(self):
		value = 0
		self.available_quantity=0
		self.balance_quantity =0
		self.qty_or =0
		self.qty_rm	=0					
		if self.material_name.name:
			similar_id = self.env['product.template'].search([('name','=',self.material_name.name)])
			self.material_id = similar_id.internal_ref
			self.uom = similar_id.uom
			all_vendors = []
			for x in similar_id.seller_ids:
				for y in x.name:
					 all_vendors.append(y.id)
			self.records = all_vendors
			myids = []
			for item in self.env['stock.quant'].search([]):
				if item.product_id.product_tmpl_id.id == self.material_name.id:
					for attr in  item.product_id.attribute_value_ids:
						if attr.id == self.color.id:
							myids.append(item)
			for rec in myids:
				for x in rec.product_id.attribute_value_ids:
					if x.id == self.size.id:
						self.available_quantity = rec.qty
						self.t_p = rec.product_id.id

		self.qty_or = self.qty_or + self.qty_pr
		self.qty_rm = self.qty_order - self.qty_or
		self.balance_quantity = self.available_quantity - self.required_quantity

class GRN(models.Model):
	_inherit='stock.picking'

	grn_date = fields.Datetime("GRN Date", required=False, 
		readonly=False, select=True, default=lambda self: fields.datetime.now())
	Req_dep = fields.Char("Requisitioning Department")
	sgp_no = fields.Char("Supplier Gate Pass #")
	veh_no = fields.Char("Vehicle Reg #")
	driver_name = fields.Char("Driver Name")

class GRNTree(models.Model):
	_inherit='stock.pack.operation'

	prod_id = fields.Char("Product Id")
	uom = fields.Char("UOM")
	remain_qty = fields.Float("Remaining Qty")
	reject = fields.Float("Rejected")
	lot_no = fields.Char("Lot #")
	remarks = fields.Char("Remarks/Description.")
	rcv_qty = fields.Integer("Received")

	@api.onchange('rcv_qty','reject')
	def on_change_qty_done(self):
		self.qty_done = self.rcv_qty - self.reject	
		self.remain_qty = self.product_qty - self.qty_done
		self.prod_id = self.product_id.internal_ref
		self.uom = self.product_id.uom.name

class BackOrderOwn(models.TransientModel):
	_inherit='stock.backorder.confirmation'

	@api.multi
	def process(self):
		new_record = super(BackOrderOwn, self).process()

		operations_to_delete = self.pick_id.pack_operation_ids.filtered(lambda o: o.qty_done <= 0)
		for pack in self.pick_id.pack_operation_ids - operations_to_delete:
			print "XXXXXXXXXXXXXXXXXXX TO-DO " + str(pack.product_qty)
			print "XXXXXXXXXXXXXXXXXXX Recived" + str(pack.rcv_qty)
			pack.product_qty = pack.product_qty-pack.rcv_qty
			print "XXXXXXXXXXXXXXXXXXXAfter Todo" + str(pack.product_qty)
		return new_record

	@api.multi
	def _create_backorder(self, backorder_moves=[]):

		backorders = self.env['stock.picking']
		for picking in self:
			backorder_moves = backorder_moves or picking.move_lines
			if self._context.get('do_only_split'):
				not_done_bo_moves = backorder_moves.filtered(lambda move: move.id not in self._context.get('split', []))
			else:
				not_done_bo_moves = backorder_moves.filtered(lambda move: move.state not in ('done', 'cancel'))
			if not not_done_bo_moves:
				continue
			backorder_picking = picking.copy({
				'name': '/',
				'move_lines': [],
				'pack_operation_ids': [],
				'backorder_id': picking.id,
				'backorder':True,
			})
			picking.message_post(body=_("Back order <em>%s</em> <b>created</b>.") % (backorder_picking.name))
			not_done_bo_moves.write({'picking_id': backorder_picking.id})
			if not picking.date_done:
				picking.write({'date_done': time.strftime(DEFAULT_SERVER_DATETIME_FORMAT)})
			backorder_picking.action_confirm()
			backorder_picking.action_assign()
			backorders |= backorder_picking

 		purchase_order = self.env['purchase.order'].search([('name','=',self.origin)])
 		sale_order = self.env['sale.order'].search([('name','=',self.origin)])
 		if purchase_order:
 			purchase_order.state = "partial"
 		if sale_order:
 			sale_order.state= "partial"

		return backorders