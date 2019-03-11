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

def is_private_newtork(d1,d2,host = ''):

    if(host):
        d1,d2 = (host + '.x').split('.')[:2]

    #http._logger.info("call is_private_newtork %s %s", d1, d2)

    return (d1 == 'localhost' or d1 == '127' or d1 == '10' or (d1 == '172' and int(d2) > 15 and int(d2) < 32) or (d1 == '192' and d2 == '168'))

def db_filter(dbs, httprequest=None):

    mainhost = openerp.tools.config.get("main_host");
    maindb = openerp.tools.config.get("main_db");
    port_limit = openerp.tools.config.get("port_limit");

    httprequest = httprequest or http.request.httprequest
    h = httprequest.environ.get('HTTP_HOST', '').split(':')[0]
    
    # if port_limit is specified
    # limit access to only 1 db (maindb)
    p = '80'
    if len(httprequest.environ.get('HTTP_HOST', '').split(':')) > 1:
        p = httprequest.environ.get('HTTP_HOST', '').split(':')[1]
    
    if str(p) == str(port_limit) and maindb:
        return [maindb]
        
    d, _, r = h.partition('.')
    if d == "www" and r:
        d = r.partition('.')[0]

    out_dbs = []
    r1 = r.split('.')[0];

    ## allow access to maindb if hostname is mainhost or
    ## hostname is mainhost-devel
    if mainhost and maindb and (d == mainhost or d == ('%s-devel' % mainhost)):
        out_dbs = [maindb]
    ## allow access on any db if id PN
    elif d.isdigit() and r1.isdigit() and is_private_newtork(d,r1):
        # is private network
        out_dbs = dbs
    ## standard dbfilter
    else:
        r = openerp.tools.config['dbfilter'].replace('%h', h).replace('%d', d)
        out_dbs = [i for i in dbs if re.match(r, i)]

    return out_dbs

# replase db_filter
http.db_filter = db_filter
# expose private network function
http.is_private_newtork = is_private_newtork
