#
# @author: D Rai Copyright (c) 1999,2010, Oracle and/or its affiliates. All Rights Reserved.
#

domain_name="ssl-domain"
print' Connecting to the Weblogic ...... '
connect('weblogic','weblogic','t3://10.159.16.156:8001')
cd('/SecurityConfiguration/'+domain_name+'/Realms/myrealm/AuthenticationProviders/DefaultAuthenticator')
cmo.resetUserPassword('weblogic','drai-newpassword')
disconnect()

connect('weblogic','drai-newpassword','t3://10.159.16.156:8001')
print '####   Successfully Connected Using New Credentials !!!!    ####'
print ' '
disconnect()
