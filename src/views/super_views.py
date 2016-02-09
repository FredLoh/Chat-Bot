from utils.media_sender import UrlPrintSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random
import enchant
import re


class SuperViews():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [
            # ("/(?P<evenOrOdd>even|odd)$", self.even_or_odd),
            (".*", self.beban_spell_checker)
        ]

    def about(self, message=None, match=None, to=None):
        self.url_print_sender.send_by_url(message.getFrom(), "https://github.com/joaoricardo000/whatsapp-bot-seed", ABOUT_TEXT)

    def even_or_odd(self, message=None, match=None, to=None):
        is_odd = len(match.group("evenOrOdd")) % 2
        num = random.randint(1, 10)
        if (is_odd and num % 2) or (not is_odd and not num % 2):
            return TextMessageProtocolEntity("[%d]\nYou win." % num, to=message.getFrom())
        else:
            return TextMessageProtocolEntity("[%d]\nYou lose!" % num, to=message.getFrom())

    def help(self, message=None, match=None, to=None):
        print()
        return TextMessageProtocolEntity(HELP_TEXT, to=message.getFrom())

    def beban_spell_checker(self, message=None, match=None, to=None):
        # print(message.getBody())
        correctionList = ""
        text = message.getBody()
        d = enchant.DictWithPWL("es_MX","wordList.txt")
        d_en = enchant.Dict("en_US")

        wordList = text.split()
        for word in wordList:
          if(word.isalnum() == True):
            print(word)
            if(d.check(word) == False):
                # if(d_en.check(word) == False):
              solutions = d.suggest(word)
              print(solutions)
              sol = str(solutions[0])
              if(sol.isalnum() == False):
                correctionList += sol + "* "
        if (correctionList != ""):
            print(correctionList)
            return TextMessageProtocolEntity(correctionList, to=message.getFrom())


HELP_TEXT = """ [HELP]
- Commands
/help - Show this message.
/about - About
/ping - Pong.
/echo - Echo.
/roll - Roll a dice.

Automatic:
    - Url (http://...) print screen.
    - Image (jpeg, gif, png) download.
    - Videos (mp4, webm) downloads.
    - Youtube videos.
"""

ABOUT_TEXT = """My name is Boto-San"""
