def email(devEmail, subj, message_text):
    fromaddr = "noreply@apigee.com"
    toaddrs  = [ devEmail ]

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (fromaddr, ", ".join(toaddrs), subj, message_text)
    
    # Send the mail
    server = smtplib.SMTP(
    host = smtp_host,
    port = smtp_port
    )
    # identify ourselves to smtp gmail client
    server.set_debuglevel(10)
    server.starttls()
    server.ehlo()
    server.login(username, password)
    
    server.sendmail(fromaddr, toaddrs, message)
    server.quit()