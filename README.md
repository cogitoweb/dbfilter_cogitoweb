# dbfilter_cogitoweb

* host name based dbfiler
* disable manage databases in public networks
* fix css for login and reset pwd

Odoo dbfilter requires host dbfilter enabled on odoo config. In a buildout config append on section [config] 

    dbfilter = ^%d$

dbfilter optionally remaps host name to dbdname for all hosts except mainhost (remapped to maindatabase).
To enable the feature add these entries in your buildout [odoo] section

    options.main_host = mymainhost
    options.main_db = mymaindb

dbfilter does prevent access on database managements on private networks with IP named hosts (to allow system managment).
This module has to be loaded on server startup. In a buildout config append on section [odoo]

    server_wide_modules = web,dbfilter_cogitoweb,...
