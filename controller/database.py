# -*- coding: utf-8 -*-

import openerp
from openerp import http
from openerp.http import request
from openerp.addons.web.controllers.main import Database

class Database_restrict(Database):

    @http.route('/web/database/manager', type='http', auth="none")
    def manager(self, **kw):

        if(not http.is_private_newtork('','',request.httprequest.host)):
            openerp.addons.web.controllers.main.abort_and_redirect('/notallowed-by-dbfilter_cogitoweb')
            return

        return super(Database_restrict, self).manager(**kw)

    @http.route('/web/database/backup', type='http', auth="none")
    def backup(self, backup_db, backup_pwd, token, backup_format='zip'):

        if(not http.is_private_newtork('','',request.httprequest.host)):
            raise Exception("AccessDenied by dbfilter_cogitoweb")

        return super(Database_restrict, self).backup(backup_db, backup_pwd, token, backup_format)


    @http.route('/web/database/restore', type='http', auth="none")
    def restore(self, db_file, restore_pwd, new_db, mode):

        if(not http.is_private_newtork('','',request.httprequest.host)):
            raise Exception("AccessDenied by dbfilter_cogitoweb")

        return super(Database_restrict, self).restore(db_file, restore_pwd, new_db, mode)

    @http.route('/web/database/create', type='json', auth="none")
    def create(self, fields):

        if(not http.is_private_newtork('','',request.httprequest.host)):
            raise Exception("AccessDenied by dbfilter_cogitoweb")

        return super(Database_restrict, self).create(fields)

    @http.route('/web/database/duplicate', type='json', auth="none")
    def duplicate(self, fields):

        if(not http.is_private_newtork('','',request.httprequest.host)):
            raise Exception("AccessDenied by dbfilter_cogitoweb")

        return super(Database_restrict, self).duplicate(fields)

    @http.route('/web/database/drop', type='json', auth="none")
    def drop(self, fields):

        if(not http.is_private_newtork('','',request.httprequest.host)):
            raise Exception("AccessDenied by dbfilter_cogitoweb")

        return super(Database_restrict, self).drop(fields)

    @http.route('/web/database/change_password', type='json', auth="none")
    def change_password(self, fields):

        if(not http.is_private_newtork('','',request.httprequest.host)):
            raise Exception("AccessDenied by dbfilter_cogitoweb")

        return super(Database_restrict, self).change_password(fields)

