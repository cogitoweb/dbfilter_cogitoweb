# -*- coding: utf-8 -*-
import odoo
from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import Database

import logging
_logger = logging.getLogger(__name__)


class Database_restrict(Database):

    ### database manager
    @http.route('/web/database/manager', type='http', auth="none")
    def manager(self, **kw):

        if(not http.is_private_newtork('', '', request.httprequest.host)):
            odoo.addons.web.controllers.main.abort_and_redirect('/not-allowed-by-dbfilter_cogitoweb')
            return

        return super(Database_restrict, self).manager(**kw)



    ### database create
    @http.route('/web/database/create', type='http', auth="none", methods=['POST'], csrf=False)
    def create(self, master_pwd, name, lang, password, **post):

        if(not http.is_private_newtork('', '', request.httprequest.host)):
            raise Exception("AccessDenied by dbfilter_cogitoweb")

        return super(Database_restrict, self).create(master_pwd, name, lang, password, **post)



    ### database duplicate
    @http.route('/web/database/duplicate', type='http', auth="none", methods=['POST'], csrf=False)
    def duplicate(self, master_pwd, name, new_name):

        if(not http.is_private_newtork('', '', request.httprequest.host)):
            raise Exception("AccessDenied by dbfilter_cogitoweb")

        return super(Database_restrict, self).duplicate(master_pwd, name, new_name)



    ### database backup
    @http.route('/web/database/backup', type='http', auth="none", methods=['POST'], csrf=False)
    def backup(self, master_pwd, name, backup_format = 'zip'):

        if(not http.is_private_newtork('', '', request.httprequest.host)):
            raise Exception("AccessDenied by dbfilter_cogitoweb")

        return super(Database_restrict, self).backup(master_pwd, name, backup_format)



    ### database restore
    @http.route('/web/database/restore', type='http', auth="none", methods=['POST'], csrf=False)
    def restore(self, master_pwd, backup_file, name, copy=False):

        if(not http.is_private_newtork('', '', request.httprequest.host)):
            raise Exception("AccessDenied by dbfilter_cogitoweb")

        return super(Database_restrict, self).restore(master_pwd, backup_file, name, copy)



    ### database drop
    @http.route('/web/database/drop', type='http', auth="none", methods=['POST'], csrf=False)
    def drop(self, master_pwd, name):

        if(not http.is_private_newtork('', '', request.httprequest.host)):
            raise Exception("AccessDenied by dbfilter_cogitoweb")

        return super(Database_restrict, self).drop(master_pwd, name)



    ### database password
    @http.route('/web/database/change_password', type='http', auth="none", methods=['POST'], csrf=False)
    def change_password(self, master_pwd, master_pwd_new):

        if(not http.is_private_newtork('', '', request.httprequest.host)):
            raise Exception("AccessDenied by dbfilter_cogitoweb")

        return super(Database_restrict, self).change_password(master_pwd, master_pwd_new)
