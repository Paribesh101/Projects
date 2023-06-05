#import smtplib

#sender = "Paribesh101@gmail.com"
#receiver = "Paribesh101@gmail.com"
#password = "UTDComet25"
#subject = "Python email test"
#body = "I wrote an email! :D"

# header
#message = f"""From: Snoop Dogg{sender}
#To: Paribesh Upreti{receiver}
#Subject: {subject}\n
#{body}
#"""

#server = smtplib.SMTP("smtp.gmail.com", 587)
#server.starttls()

#try:
#    server.login(sender, password)
#    print("Logged in..")
#    server.sendmail(sender, receiver, message)
#    print("Email has been sent")

#except smtplib.SMTPAuthenticationError:
#    print("unable to sign in")

print("Hello World!")

name = input("What's your name?: ")

print("Hello "+name)










