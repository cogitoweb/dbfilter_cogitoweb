# dbfilter_cogitoweb

* host name based dbfiler
* disable manage databases in public networks
* fix css for login and reset pwd

odoo dbfilter requires host dbfilter enabled on odoo config
In a buildout config append on section [config] 
> dbfilter = ^%d$

dbfilter remaps host name to dbdname for all hosts except mainhost (rempapped to maindatabase)
add these entries in your byildout [odoo] section

> options.main_host = mymainhost
> options.main_db = mymaindb

dbfilter does not acts on private networks with IP named hosts (to allow system managment)

this module has to be loaded on server startup
In a buildout config append on section [odoo]

> server_wide_modules = web,dbfilter_cogitoweb,...
    
