from datetime import datetime
import pandas
from sample_proj.smtp_email_sender.helper.io import get_file_path as path
from sample_proj.smtp_email_sender.src.email_sender import SendEmail

class BirtDayDateTimeManager:
    def __init__(self):
        self.today = (datetime.now().day, datetime.now().month)
        self.csv_data = self.read_csv_data()
        self.b_mapping = self.generate_dict_from_csv()

        # print(self.csv_data)


    def read_letter_data(self):
        file_name = 'b_letter.txt'
        with open(path(file_name=file_name)) as file:
            letter_content = file.read()

            # print(letter_content)
            return letter_content

    def read_csv_data(self):
        file_name = 'birthdays.csv'
        csv_content = pandas.read_csv(path(file_name=file_name))

        # print(csv_content)
        return csv_content

    def build_email_template(self):
        birth_day_data = self.b_mapping.get(self.today)
        letter = self.read_letter_data()

        year = birth_day_data.year
        name = birth_day_data.person_name

        letter = letter.replace('[NAME]', name)
        letter = letter.replace('[AGE]', str(datetime.now().year - year))
        # print(letter)
        return letter

    def generate_dict_from_csv(self):
        b_dict = {(row.day ,row.month): row for (index, row) in self.csv_data.iterrows()}

        return b_dict

    def validate_current_date(self):
        return self.today in self.b_mapping

    def send_email(self, letter):
        sender = SendEmail()
        sender.send_email(letter=letter, name=self.b_mapping.get(self.today).person_name,
                          to=self.b_mapping.get(self.today).email)

    def birth_day_greeting(self):
        if self.validate_current_date():
            letter = self.build_email_template()
            self.send_email(letter=letter)
        else:
            print(f'No birth day was on {self.today[0]}/{self.today[1]}')




