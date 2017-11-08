# -*- coding: utf-8 -*- 
from odoo import models, fields, api

class DemandNote(models.Model):

	_name = 'demand.note'
	_rec_name = 'dm_no'

	dm_no  = fields.Char("Demand Note # " ,readonly=True)
	dm_date = fields.Date("Demand Note Date")
	req_dep = fields.Char("Requisitioning Department")
	purpose  = fields.Char("Purpose")
	mo_no = fields.Char("Manufacturing Order #")
	user = fields.Char("User")
	demand_note_tree_link=fields.One2many('demand.note.tree','demand_note_tree')

	@api.model 
	def create(self, vals):
		vals['dm_no'] = self.env['ir.sequence'].next_by_code('dem.seq')
		new_record = super(DemandNote, self).create(vals) 
		return new_record


class DemandNoteTree(models.Model):
	
	_name = 'demand.note.tree'

	serial_no = fields.Char("Serial #")
	material_id = fields.Char("Material ID")
	item_desc = fields.Many2one('product.template', string="Item Description")
	uom = fields.Many2one('product.uom', string="UOM", readonly=True)
	requisite_quantity = fields.Char("Requisite Quantity")
	# issued_quantity = fields.Char(" Issued Quantity")
	remarks = fields.Char("Remarks")
	color=fields.Many2one('product.attribute.value',"Color")
	size=fields.Many2one('product.attribute.value',"Size")
	demand_note_tree = fields.Many2one('demand.note')


	@api.onchange('item_desc')
	def on_change_item_desc(self):
		if self.item_desc.name:
			similar_id = self.env['product.template'].search([('name','=',self.item_desc.name)])
			self.material_id = similar_id.internal_ref
			self.uom = similar_id.uom
			
		
		

			