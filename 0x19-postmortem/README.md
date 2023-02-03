## WordPress website Postmortem
# Issue Summary
 From 6:00 am to 7:00 am WAT on Jan 30th, Holberton WordPress website was down and users were unable to access the website. Every time the website was queried, it returned a 404 page not found error.

# Impact
The incident caused the website to become unavailable to users for about 1 hour. During this time, users were unable to access the site or any of its features. The incident also impacted the website's ability to process transactions and handle any client requests. The issue was noticed by a client who sent a mail to an employee who notified the engineering team.

# Root Cause
The root cause of the incident upon investigation was a reconfiguration in the server's resource allocation settings. The site engineer made some updates to some server files which caused a silent bug. The bug was  triggered upon a system reboot and this caused the server to fail to locate a vital resource, resulting in the website becoming unavailable.

# Resolution
The error was found by running a strace on the Apache server process id(PID) which was then logged onto a file. Upon investigation into the logs, the file with the bug was located. The issue was resolved by correcting the earlier changes made to the server's resource allocation settings and files, then restarting the server. This allowed the server to properly locate the resources, and the website was restored to full functionality.

# Recommendations
 To prevent similar incidents from occurring in the future, the following recommendations are being made:
* Implement a regular check of the server's resource allocation settings to ensure they are properly configured two days after maintenance
* Implementing cloud monitoring and alerting service such as Datadog on the servers to quickly detect and alert any unusual server behavior. 
* Develop a plan for periodic testing of the website's critical resources to ensure they are functioning as expected.

#Conclusion 
The website downtime incident was caused by a reconfiguration in the server's resource allocation settings, resulting in the server failing to locate a vital resource. The issue was resolved by correcting the configuration and restarting the server, and the website was restored to full functionality. The recommendations made in this postmortem will help to prevent similar incidents from occurring in the future.
