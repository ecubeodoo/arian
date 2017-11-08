# -*- coding: utf-8 -*- 
from odoo import models, fields, api

class ArianVendor(models.Model): 
    _inherit = 'res.partner'

    vendor_ref_no = fields.Char(string="Vendor Reference #") 
    ntn = fields.Char(string="NTN No") 
