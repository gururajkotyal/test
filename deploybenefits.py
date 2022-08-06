#!/u01/app/oracle/apr2022/wls12c/oracle_common/common/bin/wlst.sh
appname="benefits"
location="/u01/app/oracle/apr2022/apps/benefits.war"
targets="dizzy1"
connect('weblogic','weblogic1','t3://192.168.56.102:7001')
print 'Deploying application'+appname
deploy(appname,location,targets)
print 'Deployment completed successfully'+appname
disconnect()
exit()
