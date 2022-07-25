import smtplib

gmailaddress =input("Input Your Email Address \n")
gmailpassword = input("Input Your Gmail password \n")
mailto = input("Receiver\'s Email Address \n")
msg = input("Enter Email Message \n")

try:
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.starttls()
    mailServer.login(gmailaddress, gmailpassword)
    mailServer.sendmail(gmailaddress, mailto, msg)
    print(" \n Message Delivered!")
    mailServer.quit()
except:
    print("Email Failed to Deliver!")
