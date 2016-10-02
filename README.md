# dbfilter_cogitoweb

* host name based dbfiler
* host name based disable manage databases
* fix css login and reset pwd css

odoo dbfilter requires host dbfilter enabled on odoo config
In a buildout config append on section [config] 
> dbfilter = ^%d$

dbfilter remaps host name to dbdname for all hosts except odoo (rempapped to cogitoweb)
dbfilter does not acts on ip named hosts (to allow system managment)

this module has to be loaded on server startup
In a buildout config append on section [odoo]
> server_wide_modules = web,dbfilter_cogitoweb,...
    
