# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Paolo Cazzitti
#    Copyright 2016 Cogito Srl
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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

import openerp
from openerp import http
import re

def db_filter(dbs, httprequest=None):

    httprequest = httprequest or http.request.httprequest
    h = httprequest.environ.get('HTTP_HOST', '').split(':')[0]
    d, _, r = h.partition('.')
    if d == "www" and r:
        d = r.partition('.')[0]
    
    out_dbs = []
    
    if d == 'odoo':
        out_dbs = ['cogitoweb'] 
    elif d.isdigit():
        out_dbs = dbs
    else:
        r = openerp.tools.config['dbfilter'].replace('%h', h).replace('%d', d)
        out_dbs = [i for i in dbs if re.match(r, i)]
        
    return out_dbs

http.db_filter = db_filter