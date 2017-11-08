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
from num2words import num2words


class SampleDevelopmentReport(models.AbstractModel):
    _name = 'report.rst_commercial_invoice.module_report'

    @api.model
    def render_html(self,docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('rst_commercial_invoice.module_report')
        records = self.env['account.invoice'].browse(docids)
        
        def get_value(cart_id,attr):
            prod = cart_id

            if attr == 'color':
                varient = self.env['product.product'].search([('id','=',prod)])
                for x in varient.attribute_value_ids:
                    if x.attribute_id.name == 'color':
                        return x.name

        def get_qty(cart_id,attr,qty):
            prod = cart_id

            if attr == 'xs':
                quantity = 0
                varient = self.env['product.product'].search([('id','=',prod)])
                for x in varient.attribute_value_ids:
                    if x.attribute_id.name == 'size':
                        if x.name == 'xs':
                            quantity = qty

                return quantity

            if attr == 's':
                quantity = 0
                varient = self.env['product.product'].search([('id','=',prod)])
                for x in varient.attribute_value_ids:
                    if x.attribute_id.name == 'size':
                        if x.name == 's':
                            quantity = qty

                return quantity

            if attr == 'm':
                quantity = 0
                varient = self.env['product.product'].search([('id','=',prod)])
                for x in varient.attribute_value_ids:
                    if x.attribute_id.name == 'size':
                        if x.name == 'm':
                            quantity = qty

                return quantity

            if attr == 'l':
                quantity = 0
                varient = self.env['product.product'].search([('id','=',prod)])
                for x in varient.attribute_value_ids:
                    if x.attribute_id.name == 'size':
                        if x.name == 'l':
                            quantity = qty

                return quantity
            
            if attr == 'xl':
                quantity = 0
                varient = self.env['product.product'].search([('id','=',prod)])
                for x in varient.attribute_value_ids:
                    if x.attribute_id.name == 'size':
                        if x.name == 'xl':
                            quantity = qty

                return quantity    


            if attr == 'xxl':
                quantity = 0
                varient = self.env['product.product'].search([('id','=',prod)])
                for x in varient.attribute_value_ids:
                    if x.attribute_id.name == 'size':
                        if x.name == 'xxl':
                            quantity = qty

                return quantity
                
            if attr == '3xl':
                quantity = 0
                varient = self.env['product.product'].search([('id','=',prod)])
                for x in varient.attribute_value_ids:
                    if x.attribute_id.name == 'size':
                        if x.name == '3xl':
                            quantity = qty

                return quantity
                

            if attr == '4xl':
                quantity = 0
                varient = self.env['product.product'].search([('id','=',prod)])
                for x in varient.attribute_value_ids:
                    if x.attribute_id.name == 'size':
                        if x.name == '4xl':
                            quantity = qty

                return quantity 

            if attr == '5xl':
                quantity = 0
                varient = self.env['product.product'].search([('id','=',prod)])
                for x in varient.attribute_value_ids:
                    if x.attribute_id.name == 'size':
                        if x.name == '5xl':
                            quantity = qty

                return quantity

        size_list = []
        def getsizes(tree):
            del size_list[:]
            for x in tree:
                for y in x.product_id.attribute_value_ids:
                    if y.attribute_id.name == "size":
                        if y.name not in size_list:
                            size_list.append(y.name)

        def colsizes():
            return len(size_list)

        def get_name(line):
            for x in line.product_id.attribute_value_ids:
                if x.attribute_id.name == "size":
                    return x.name
                


        docargs = {
            'doc_ids': docids,
            'doc_model': 'account.invoice',
            'docs': records,
            'data': data,
            'get_qty':get_qty,
            'get_value':get_value,
            'getsizes': getsizes,
            'size_list': size_list,
            'colsizes': colsizes,
            'get_name': get_name
            }

        return report_obj.render('rst_commercial_invoice.module_report', docargs)

class Num2Words(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def convert_amount(self):
        word = num2words(self.amount_total - self.air_freight)
        word = word.title() + " " + "Only"
        return word