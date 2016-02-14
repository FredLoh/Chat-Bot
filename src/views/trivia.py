#!/usr/bin/env python
# -*- coding: utf-8 -*-
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
import random
import json
from fuzzywuzzy import fuzz
from ..server import t

class Trivia:
    def __init__(self):
        self.active_question_bool = False
        self.active_question = ""
        self.active_index = 0
        self.fuzziness_ratio = 0.65

        with open('Trivia_Questions.json') as data_file:
            self.data = json.load(data_file)

        self.routes = [
            ("^!q", self.ask_question())
        ]

    def ask_question(self):
        if not self.active_question_bool:
            random_val = random.randint(1, (len(self.data)-1))
            self.active_index = random_val
            self.active_question_bool = True
            self.active_question = self.data[self.active_index]['question']
            print self.data[self.active_index]['question']

    def check_answer(self, answer):
        if self.active_question_bool:
            if fuzz.ratio(answer.lower() == self.data[self.active_index]['answer'].lower()) >= self.fuzziness_ratio:
                self.active_question_bool = False
                self.active_index = 0
                self.active_question = ""
                return True
            else:
                return False

    def provide_answer(self):
        if self.active_index != 0:
            print self.data[self.active_index]['answer']
            self.active_question_bool = False
            self.active_index = 0
            self.active_question = ""

        else:
            print "No active question"

    def skip_question(self):
        self.active_question_bool = False
        self.active_index = 0
        self.active_question = ""


t = Trivia()

t.ask_question()
print t.check_answer("copernicus")