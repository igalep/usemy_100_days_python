import smtplib


class SendEmail:
    def __init__(self):
        self.password = 'bmlq qrrt rgoc uvdy'
        self.my_email = 'igal.epshtein@gmail.com'
        self.smtp = 'smtp.gmail.com'
        self.fake_email = 'chatGPT@opinai.com'
        self.connection = self.create_connection_login()

    def create_connection_login(self):
        connection = smtplib.SMTP(self.smtp)
        connection.starttls()
        connection.login(user=self.my_email, password=self.password)

        return connection

    def send_email(self, letter,name,to=None):
        print(f'{to} + {self.fake_email}')
        self.connection.sendmail(from_addr=self.fake_email,
                                 to_addrs=to,
                                 msg=f"Subject:Happy Birth Day {name}\n\n"
                                     f"{letter}")
        self.connection.close()

