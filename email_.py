import smtplib

from email.mine.text import MIMEText
from email.mine.image import MIMEImage
from email.mine.multipart import MIMEMultipart
from email.mine.audio import MIMEAudio

def addimg(src, imgid):
	with open(src, 'rb') as fd:
		image = MIMEImage(fd.read())
	image.add_header('Content-ID', imgid)
	return image

message = MIMEMultipart('related')

html = MIMEText("""\
<img src="cid:io"> #io use at addimg function
html""", 'html', 'utf-8')

message.attach(html)
message.attach(addimg("src.png", "io"))
message = message.as_string()


#添加附件的方法
attach = MIMEText(open("pathname", 'rb').read(), 'base64', 'utf-8')
attach['Content-Type'] = 'application/octet-stream' #指定类型
attach['Content-Disposition'] = "attachment; filename=filename".encode('gb18030')
#attachment 出现下载保存对话框 filename为文件名
#qqmail gb18030
message.attach(attach)



body = """\
From: 
To:
Subject:

test main body"""

message = MIMEText("""\
<img src="cid:io"> #io use at addimg function
html body""", 'html', 'utf-8')

message['Subject'] = SUBJECT
message['From'] = FROM
message['To'] = TO

HOST = 'smtp.gmail.com'
SUBJECT = 'Email Subject'
TO = 'mail@qq.com'
FROM = 'me@qq.com'
test = 'email content'

BODY = '\r\n'.join(['From: %s' % FROM,
					'To: %s' % TO,
					'Subject %s' % SUBJECT,
					'',
					text])

server = smtplib.SMTP()
server.connect(HOST, '25')
#server.starttls()
server.login("me@mail.com", "password")
server.sendmail(FROM, [TO], BODY)
server.quit()