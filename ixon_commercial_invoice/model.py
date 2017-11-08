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
    _name = 'report.ixon_commercial_invoice.module_report'

    @api.model
    def render_html(self,docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('ixon_commercial_invoice.module_report')
        records = self.env['account.invoice'].browse(docids)

        def get_color(attr):
            prod = attr
            varient = self.env['product.product'].search([('id','=',prod)])
            for x in varient.attribute_value_ids:
                if x.attribute_id.name == "color":
                    return x.name

        def get_size(attr):
            prod = attr
            varient = self.env['product.product'].search([('id','=',prod)])
            for x in varient.attribute_value_ids:
                if x.attribute_id.name == "size":
                    return x.name

        docargs = {
            'doc_ids': docids,
            'doc_model': 'account.invoice',
            'docs': records,
            'data': data,
            'get_color': get_color,
            'get_size': get_size
            }

        return report_obj.render('ixon_commercial_invoice.module_report', docargs)

##################### to install num2words ################################
##################### pip install num2words ################################


class Num2Words(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def convert_amount(self):
        word = num2words(self.amount_untaxed)
        word = word.title() + " " + "Only"
        return word
