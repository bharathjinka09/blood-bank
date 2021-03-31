import smtplib

content = "Hello "
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('helpafriend.bloodbank@gmail.com', 'bloodbank.project')
mail.sendmail('helpafriend.bloodbank@gmail.com', 'ritikabokde@gmail.com', content)
