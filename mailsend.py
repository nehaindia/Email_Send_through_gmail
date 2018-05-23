#!/usr/bin/python2

#smtp.gmail.com

#Requires SSL: Yes

#Requires TLS: Yes (if available)

#Requires Authentication: Yes

#Port for SSL: 465

#Port for TLS/STARTTLS: 587

#Access for less secure apps :ON on gmail in order to send email#

import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.set_debuglevel(True)
server.starttls()
sender_email=raw_input("enter sender email")
sender_pass=raw_input("enter sender pasword")
rec_email=raw_input("enter receiver email")
server.login(sender_email, sender_pass)
 
msg = "YOUR MESSAGE!"
server.sendmail(sender_email, rec_email, msg)
server.quit()
