uname = "weblogic"
pwd = "welcome1"
url = "t3://localhost:7001"

def modifySharedCapacityForWorkManagers():
    startTransaction()
    serverNames = getRunningServerNames()
    for name in serverNames:
    	print 'Now Configuring '+name.getName()
    	cd("/Servers/"+name.getName()+"/OverloadProtection/"+name.getName())
    	set("SharedCapacityForWorkManagers",256)
    endTransaction()

def startTransaction():
    edit()
    startEdit()

def endTransaction():
    save()
    activate(block="true")
    
def getRunningServerNames():
    return cmo.getServers()

if __name__== "main":
    connect(uname, pwd, url)
    modifySharedCapacityForWorkManagers()
   



        

