from email.mime.text import MIMEText
import smtplib
import globalval as gv

# send mail function

def sendmymail(InMsg,subj):
    msg_content = InMsg
    message = MIMEText(msg_content, 'plain')
    message['From'] = gv.fromme
    message['To']   = gv.recipient
    message['Subject'] = subj
    msg_full = message.as_string()
    server = smtplib.SMTP(gv.server)
    server.starttls()
    server.login(gv.username, gv.password)
    server.sendmail(gv.fromme, gv.recipient, msg_full)
    server.quit()
