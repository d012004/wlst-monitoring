connect('weblogic','weblogic','t3://localhost:7001')
edit()
startEdit()
svrs = adminHome.getMBeansByType('Server')
for s in svrs:
   name = s.getName()
   cd('/Servers/' + name + '/Log/' + name)
   cmo.setNumberOfFilesLimited(true)
   cmo.setFileCount(100)
   cmo.setDomainLogBroadcastSeverity('Warning')
   cmo.setMemoryBufferSeverity('Warning')
   cmo.setLogFileSeverity('Warning')
   cmo.setStdoutSeverity('Warning')
activate()
disconnect()
