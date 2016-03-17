# Quota Email Notifications

This is a proxy I created for a PoC. 

## Setup steps
1. Create an API Product with the following custom attribute: `quota.notification.threshold.percentage`. The value of the attribute is a comma-seperated list of percentages on which an email needs to be send. For example: `50,80,100`.
2. The quota can be enforced on developer, apps or product. By default the quota is enforced on a developer. This means you need to add the following three custom attributes on your developer: `quota.limit` `quota.interval` and `quota.timeunit`
3. Set the SMTP details you would like to use in the config.py script. I have not provided working username and password in the zip.
 

