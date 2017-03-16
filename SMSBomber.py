import random


print ("\n")
print("DISCLAIMER: USE WITHIN LEGAL BOUNDARIES!\n DO NOT SPAM ANYONE BUT YOURSELF!")
print ("\n")
agreement = raw_input("Type YES in all caps if you agree: ")

print ("\n")
if agreement != "YES":
    quit()

to = input("Number to be spammed: ")
print ("\n\n")
print("--- Enter the message you want spammed below ---")
print("- PS: Use more than a few letters to avoid spam protection -")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
messagefrominput = raw_input("MESSAGE: ")

print ("\n\n")




numberoftimes = input("How many times do you want it spammed: ")
print ("\n\n\n")

SMTPserver = 'mail.webservertest3737.info'
sender = ''
destination = ''
USERNAME = "000@webservertest3737.info"
PASSWORD = "WebServerTest3737"
text_subtype = 'plain'

content="""\
%s
""" % (messagefrominput)

subject = ""

carriernumb = 0
carrier = ""
timesent = 0

xxxint = 0
stringxxx = ""
finalxxx = ""
print("---------------")
print("| 1 = Verizon |\n| 2 = AT&T |\n| 3 = Sprint |\n| 4 = T-Mobile |\n| 5 = Virgin Mobile |\n| 6 = Alltel |\n| 7 = Nextel |\n| 8 = US Cellular |")
print("-------------------")
carriernumb =  int(input("Which carrier is the phone number associated with? "))

if carriernumb == 1:
    carrier = "@vtext.com"
elif carriernumb == 2:
    carrier = "@txt.att.net"
elif carriernumb == 3:
    carrier = "@messaging.sprintpcs.com."
elif carriernumb == 4:
    carrier = "@tmomail.net"
elif carriernumb == 5:
    carrier = "@vmobl.com"
elif carriernumb == 6:
    carrier = "@message.alltel.com"
elif carriernumb == 7:
    carrier = "@messaging.nextel.com"
elif carriernumb == 8:
    carrier = "@mms.uscc.net"


createreciever = str(to) + carrier
destination = [createreciever]


def emailcycler():
    global xxxint
    global finalxxx
    global sender
    global stringxxx
    xxxint = random.randint(1,25)    #creates int 1-25
    stringxxx = str(xxxint)          #takes int and converts to string, in order to use len it has to be a string
    if len(stringxxx) == 1:          #if len of string is 1 (e.g #6)
        finalxxx = "00" + stringxxx  #  6 --> 006
    elif len(stringxxx) == 2:        #if len of string is 2 (e.g #16)
        finalxxx = "0" + stringxxx   # 16 --> 016
    sender = finalxxx+ '@webservertest3737.info' # 016@webservertest3737.info
    print(sender)





def sendmessage():
    global timesent
    try:
        msg = MIMEText(content, text_subtype)
        msg['Subject'] = subject
        msg['From'] = sender  # some SMTP servers will do this automatically, not all

        conn = SMTP(SMTPserver)
        conn.set_debuglevel(False)
        conn.login(sender, PASSWORD)
        try:
            conn.sendmail(sender, destination, msg.as_string())
        finally:
            conn.quit()
            timesent +=1

    except:
        print("Something went wrong.")






import sys
import os
import re

from smtplib import SMTP_SSL as SMTP


from email.mime.text import MIMEText

while timesent < numberoftimes:
    emailcycler()
    sendmessage()

if timesent == numberoftimes:
    print("Thank you for using SMSBomber!")