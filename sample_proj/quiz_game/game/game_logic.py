import json
import os
import random


class GameLogic:
    def __init__(self):
        self.data_list = []
        self.question_index = 0
        self.score = 0
        self.upload_data()



    def upload_data(self):
        '''
        Reads a JSON file and upload it to the memory
        '''
        file_name = 'data.json'
        file_path = os.path.dirname(os.path.realpath(__file__))
        data_file = os.path.join(file_path, '..','resource', file_name)
        try:
            with open(data_file) as file:
                self.data_list = json.load(file)

            random.shuffle(self.data_list)
        except FileNotFoundError:
            print(f"Error: File not found at {data_file}")
            return None
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {data_file}")
            return None

    def has_question(self):
        return self.question_index < len(self.data_list)

    def ask_next_question(self):
        question = self.data_list[self.question_index]

        user_answer = input(f'Q:{self.question_index + 1} {question['question']} - (true or false) ?\n').lower()

        if user_answer == 'stop':
            self.question_index = len(self.data_list)
            return

        answer_correctness = self.validate_answer(user_answer=user_answer)

        self.question_index += 1

        if answer_correctness:
            self.score += 1

    def get_score(self):
        return self.score

    def validate_answer(self, user_answer):
        correct_answer = self.data_list[self.question_index]['correct_answer'].lower()

        return user_answer == correct_answer

