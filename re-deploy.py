print' Connecting to the Weblogic console'
connect('weblogic','weblogic','t3://localhost:7001')

print'Checking the state of Admin and Manage Server'
state('AdminServer','Server')

edit()
startEdit()

print'Stopping the sample-app'
stopApplication('sample-app')

print'Re-Deploying the new sample-app '
progress=updateApplication('sample-app',stageMode='STAGE')

if progress.getState() == "completed":
	print "Deployment completed successfully."
else:
	print "Deployment Failed. Please do manually"
	exit()
	stopEdit()

print'Starting the sample-app application to accept the request'
sstatus=startApplication('sample-app',stageMode='STAGE',targets='AdminServer')
sstatus.getState()

save()
activate()


