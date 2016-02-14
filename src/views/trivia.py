#!/usr/bin/env python
# -*- coding: utf-8 -*-
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
import random
import json
from fuzzywuzzy import fuzz


class Trivia:
    def __init__(self):
        self.active_question_bool = False
        self.active_question = ""
        self.active_index = 0
        self.fuzziness_ratio = 85

        with open('Trivia_Questions.json') as data_file:
            self.data = json.load(data_file)

    def ask_question(self, message, match):
        if not self.active_question_bool:
            random_val = random.randint(1, (len(self.data)-1))
            self.active_index = random_val
            self.active_question_bool = True
            self.active_question = self.data[self.active_index]['question']
            return TextMessageProtocolEntity(str(self.data[self.active_index]['question']), to=message.getFrom())
        else:
            return TextMessageProtocolEntity("There is an active question already!", to=message.getFrom())

    def check_answer(self, message, match):
        answer = match.group("answer")
        print answer
        if self.active_question_bool:
            if fuzz.ratio((answer.lower()), (self.data[self.active_index]['answer'].lower())) >= self.fuzziness_ratio:
                self.active_question_bool = False
                self.active_index = 0
                self.active_question = ""
                name = self.nombre(message.getParticipant())
                return TextMessageProtocolEntity("Correct " + name + "!", to=message.getFrom())
            else:
                name = self.nombre(message.getParticipant())
                return TextMessageProtocolEntity("Incorrect " + name + "!", to=message.getFrom())

    def provide_answer(self, message, match):
        if self.active_index != 0:
            ans = self.data[self.active_index]['answer']
            self.active_question_bool = False
            self.active_index = 0
            self.active_question = ""
            return TextMessageProtocolEntity(ans, to=message.getFrom())
        else:
            return TextMessageProtocolEntity("No active question!", to=message.getFrom())

    def skip_question(self):
        self.active_question_bool = False
        self.active_index = 0
        self.active_question = ""

    def nombre(self, id):
        if id == "5218110663456@s.whatsapp.net":
            return "Rana"

        elif id == "5218117471775@s.whatsapp.net":
            return "Edrel"

        elif id == "5218116618135@s.whatsapp.net":
            return "Eduardo"

        elif id == "5218183660872@s.whatsapp.net":
            return "Beban"

        elif id == "17204742885@s.whatsapp.net":
            return "Fred"

        elif id == "5218110801239@s.whatsapp.net":
            return "Guerra"

        elif id == "5218112807383@s.whatsapp.net":
            return "Ortiz"

        elif id in ("353892498794@s.whatsapp.net", "5218117793991@s.whatsapp.net"):
            return "Jorge"

        elif id == "14389985110@s.whatsapp.net":
            return "Justin"

        elif id == "5218121217755@s.whatsapp.net":
            return "Manuel"

        elif id == "5218110778105@s.whatsapp.net":
            return "Cantu"

        elif id == "5218112114862@s.whatsapp.net":
            return "Garcia Garcia"

        elif id == "447463772183@s.whatsapp.net":
            return "Marchand"

        elif id == "5218112422227@s.whatsapp.net":
            return "Europeña"

        elif id == "5218115445683@s.whatsapp.net":
            return "Memo"

        elif id == "5218117862786@s.whatsapp.net":
            return "Olaf"

        elif id == "19564839570@s.whatsapp.net":
            return "Oscar"

        elif id == "5218115995291@s.whatsapp.net":
            return "Patfuck"

        elif id == "5218115448028@s.whatsapp.net":
            return "Vela"

        elif id == "5218182560710@s.whatsapp.net":
            return "Ricky"

        elif id == "14255057149@s.whatsapp.net":
            return "Chavo"

        elif id == "16785766095@s.whatsapp.net":
            return "Echeverry"

        elif id == "5218114976723@s.whatsapp.net":
            return "Baumann"

        else:
            return ""