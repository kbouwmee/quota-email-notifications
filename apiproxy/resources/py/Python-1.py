import smtplib
import datetime

# get variables
percentages = flow.getVariable("verifyapikey.verify-api-key.apiproduct.quota.notification.threshold.precentages")
dev_limit = flow.getVariable("verifyapikey.verify-api-key.developer.quota.limit")
dev_timeunit = flow.getVariable("verifyapikey.verify-api-key.developer.quota.timeunit")
dev_interval = flow.getVariable("verifyapikey.verify-api-key.developer.quota.interval")
dev_last_email = flow.getVariable("verifyapikey.verify-api-key.developer.quota.last.email")
quota = int(flow.getVariable("ratelimit.impose-quota.allowed.count"))
used = int(flow.getVariable("ratelimit.impose-quota.used.count"))
devEmail = flow.getVariable("verifyapikey.verify-api-key.developer.email")
appName = flow.getVariable("developer.app.name")
apiProduct = flow.getVariable("apiproduct.name")
timestamp = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

# calculate current percentage
#usedPercentage = int(round((used / quota) * 100))

# get percentages into array
percentageList = percentages.split(",")

# check all percentages
for threshold in percentageList:
    thresholdCalls = int(round(quota * (float(threshold)/100.0)))
    flow.setVariable("threshold.calls"+threshold,thresholdCalls)
    if used == thresholdCalls:
        
        message = "Dear developer,\n\nYour personal quota is over " + threshold + "%.\n\nQuota details:\n"+dev_limit+" per "+ dev_interval + " " + dev_timeunit+"\n\nThis was triggered on "+timestamp+" by app ["+ appName + "] for product ["+apiProduct+"]."
        subject = "Your quota is over " + threshold + "%"
        email(devEmail, subject, message)
        flow.setVariable("quota.notification.sent",True)
        flow.setVariable("quota.notification.to",devEmail)
        flow.setVariable("email.notification.msg",message)



        




