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
from num2words import num2words

class SampleDevelopmentReport(models.AbstractModel):
    _name = 'report.customer_invoice_generic.module_report'

    @api.model
    def render_html(self,docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('customer_invoice_generic.module_report')
        records = self.env['account.invoice'].browse(docids)

        enteries = []
        for x in records.invoice_line_ids:
          if x.product_id.product_tmpl_id not in enteries:
               enteries.append(x.product_id.product_tmpl_id)

        varients = []
        def getdata(current_record,attrb):
            del varients[:]
            for x in records.invoice_line_ids:
                if x.product_id.product_tmpl_id == current_record:
                    varients.append(x)
                
            if attrb == "style":
                style = ""
                for x in records.invoice_line_ids:
                    if x.product_id.product_tmpl_id == current_record:
                        style = x.product_id.style_no
                return style

            if attrb == "desc":
                desc = ""
                for x in records.invoice_line_ids:
                    if x.product_id.product_tmpl_id == current_record:
                        desc = x.product_id.product_tmpl_id.composition
                return desc

            if attrb == "qty":
                quantity = 0
                for x in records.invoice_line_ids:
                    if x.product_id.product_tmpl_id == current_record:
                        quantity = quantity + x.quantity
                return quantity

            if attrb == "uom":
                uom = ""
                for x in records.invoice_line_ids:
                    if x.product_id.product_tmpl_id == current_record:
                        uom = x.uom_id.name
                return uom

            if attrb == "rate":
                rate = ""
                for x in records.invoice_line_ids:
                    if x.product_id.product_tmpl_id == current_record:
                        rate = x.price_unit
                return rate
            
            if attrb == "amount":
                amount = 0
                for x in varients:
                    amount = amount + x.price_subtotal
                return amount

        total_sizes = []
        def getsizes(prod):
            del total_sizes[:]
            for x in records.invoice_line_ids:
                if x.product_id.product_tmpl_id == prod:
                    for y in x.product_id.attribute_value_ids:
                        if y.attribute_id.name == 'size':
                            if y.name not in total_sizes:
                                total_sizes.append(y.name)

        def getcolor(current_record):
            color = ' '
            for x in records.invoice_line_ids:
                if x.product_id.product_tmpl_id == current_record:
                    for y in x.product_id.attribute_value_ids:
                        if y.attribute_id.name == 'color':
                            return y.name

        def getqty(prod,size):
            active_ids = []
            qty = 0
            for x in records.invoice_line_ids:
                if x.product_id.product_tmpl_id == prod:
                    if x.product_id not in active_ids:
                        active_ids.append(x)

            for x in active_ids:
                for y in x.product_id.attribute_value_ids:
                    if y.attribute_id.name == 'size':
                        if y.name == size:
                            qty = qty + x.quantity

            return qty

        docargs = {
            'doc_ids': docids,
            'doc_model': 'account.invoice',
            'docs': records,
            'data': data,
            'entries': enteries,
            'getdata': getdata,
            'getsizes': getsizes,
            'total_sizes': total_sizes,
            'getcolor': getcolor,
            'getqty': getqty
            }

        return report_obj.render('customer_invoice_generic.module_report', docargs)

        ##################### pip install num2words ################################


class Num2Words(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def number_to_words(self):
        word = num2words((self.amount_untaxed))
        word = word.title() + " " + "Only"
        return word




