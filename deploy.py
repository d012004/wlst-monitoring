print' Connecting to the Weblogic ...... '
connect('weblogic','weblogic','t3://localhost:7001')

print'Checking the state of  Server ...........'
state('AdminServer','Server')

edit()
startEdit()

print'Stopping the sample-app'
stopApplication('sample-app')

print'Undeploying the sample-app'
ustatus=undeploy('sample-app','AdminServer')

print'Deploying the new sample-app ' 
progress=deploy('sample-app','J:/WD/BEA/WLS/sample-codes/ejb/ejb1.jar','AdminServer',block=true)

if progress.getState() == "completed":
	print "Deployment completed successfully."
else:
	print "Deployment Failed. Please do manually"
	exit()

print'Starting the sample-app application to accept the request'
sstatus=startApplication('sample-app',stageMode='STAGE',targets='AdminServer')
sstatus.getState()

save()
activate()


