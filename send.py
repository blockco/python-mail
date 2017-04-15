import smtplib

sender = '@student.42.us.org'
receiver = ['@student.42.us.org']

name = raw_input("Who are you? Enter Name\n")
person = raw_input("Who are you sending this to? Enter Name\n")
raw = raw_input("Who are you? Enter intra Name\n")
sender = raw + sender
raw = raw_input("Who are sending to? Enter intra Name\n")
receiver[0] = raw + receiver[0]
sub = raw_input("Please type your Subject\n")
text = raw_input("Please type your message\n")

message = "From: " + name + " " + "<" + sender + ">\n" + "To: " + person + " <" + receiver[0] + ">\n" + "Subject: " + sub + "\n" + text + "\n"
smtpObj = smtplib.SMTP('smtp.42.us.org')
smtpObj.sendmail(sender, receiver, message)
print "\n" + "Here is your email check it over It has been sent!\n\n"  + message
