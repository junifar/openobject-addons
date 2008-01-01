##############################################################################
#
# Copyright (c) 2007 TINY SPRL. (http://tiny.be) All Rights Reserved.
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

import netsvc
from osv import fields, osv


class res_partner_contact(osv.osv):
    _name = "res.partner.contact"
    _description = "res.partner.contact"
    _columns = {
        'name': fields.char('First Name', size=30,required=True),
        'surname': fields.char('Last Name', size=30),
        'mobile':fields.char('Mobile',size=30),
        'title':fields.char('Title',size=10,help='Courtesy'),
        'website':fields.char('Website',size=120),
        'lang_id':fields.many2one('res.lang','Language'),
        'address_ids':fields.one2many('res.partner.address','partner_id1','Adresses'),#sholu be correct ,see view tag in partner.ods
        'country_id':fields.many2one('res.country','Country'),#should be correct.....see view tag
        'birthdate':fields.date('Birthdate'),
        'active' : fields.boolean('Active'),
        'contact_ids':fields.many2one('res.partner.contact','Contacts')
    }
    _defaults = {
        'active' : lambda *a: True,
    }
res_partner_contact()

class res_partner_address(osv.osv):
    _description ='Partner Contact'
    _name = 'res.partner.address'
    _inherit='res.partner.address'
    _columns = {
        'partner_id1': fields.many2one('res.partner.contact', 'Partner', ondelete='cascade', select=True),
        }
res_partner_address()

