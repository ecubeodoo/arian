#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 OpenERP SA (<http://openerp.com>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api
from datetime import date


class SampleDevelopmentReport(models.AbstractModel):
    _name = 'report.ixs_proforma_invoice.module_report'

    @api.model
    def render_html(self,docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('ixs_proforma_invoice.module_report')
        records = self.env['sale.order'].browse(docids)
        
        def get_colour(attr):
            prod = attr
            col = ' '
            ser = self.env['product.product'].search([('id','=',prod)])
            if ser:
                for x in ser.attribute_value_ids:
                    if x.attribute_id.name == "color":
                        col = x.name
            return col
        
        def get():
            total=0.0
            for x in records.order_line:
                total = x.product_uom_qty + total
                print total
            return total

        def get_size(prod):
            ser = self.env['product.product'].search([('id','=',prod.id)])
            if ser:
                for x in ser.attribute_value_ids:
                    if x.attribute_id.name == "size":
                        col = x.name
            return col

        docargs = {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'docs': records,
            'data': data,
            'get_colour':get_colour,
            'get':get,
            'get_size': get_size
            }

        return report_obj.render('ixs_proforma_invoice.module_report', docargs)
