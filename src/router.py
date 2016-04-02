"""
    The Route Layer.
    Here the message is routed to its proper view.
    The routes are defined with regular expressions and callback functions (just like any web framework).
"""
import threading
import re
import logging

from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback

from views import basic_views, wolfram_wiki
from views.media import MediaViews
from views.super_views import SuperViews
from views.group_admin import GroupAdminViews
from views.google import GoogleViews
from views.bing import BingViews

ilyregex = "(Te Amo|te amo|Te amo|I love you|i love you|ily|ILY|Ily|TE AMO|I LOVE YOU|\<3)"
tyregex = "(Thanks|thanks|THANKS|THANK YOU|Thank you|Thank You|thank you|thankyou|Thankyou|THANKYOU|Gracias|gracias|GRACIAS|thx|THX|Thx|TY|Ty|ty)"
gnregex = "(Gute nacht|Good night|good night|Good Night|GOOD NIGHT|BUENAS NOCHES|Buenas noches|buenas noches|Buenas Noches|Hasta ma.ana|hasta ma.ana|Hasta Ma.ana|HASTA MA.ANA)"
hregex = "(Que Onda|que onda|Que onda|Hola|hola|HOLA|HELLO|Hello|hello|Good morning|GOOD MORNING|good morning|buenos d.as|Buenos d.as)"
gbregex = "(Adi.s|adi.s|ADI.S|Good bye|GOODBYE|Good Bye|goodbye|Goodbye|good bye|GOOD BYE)"
bsregex = "(Boto-san|BotoSan|boto-san|Boto-San|Boto San|botosan|boto san|Boto san|Botosan|BOTOSAN|BOTO SAN|BOTO-SAN)"

# Basic regex routes
routes = [("Status", basic_views.ping),("^o(k)?\s(?P<alerta>[^$]+)$",basic_views.echo)
          ]


class RouteLayer(YowInterfaceLayer):
    def __init__(self):
        """
            The definition of routes and views (callbacks)!

            For the simple message handling, just calls the callback function, and expects a message entity to return.
            For more complex handling, like asynchronous file upload and sending, it creates a object passing 'self',
            so the callback can access the 'self.toLower' method
        """
        super(RouteLayer, self).__init__()

        # Google views to handle tts, search and youtube
        self.views = [(re.compile(pattern), callback) for pattern, callback in routes]

    def route(self, message):
        "Get the text from message and tests on every route for a match"
        text = message.getBody()
        #print("Participant: " + message.getParticipant())
        print(text)
        # text = "123"
        # - Beban Spell checker
        #
        # if(str(message.getFrom()) == "17204742885@s.whatsapp.net"):
        #     routes.append((".*", self.beban_spell_checker))
        # print("Participant: " + message.getParticipant())
        #
        #  Ban Ed
        if(str(message.getParticipant()) == "5218116618135@s.whatsapp.net"):
            text = ""
        #  Correct beban spelling
        if(str(message.getParticipant()) == "5218183660872@s.whatsapp.net"):
            if(str(message.getBody())[0] != "/"):
                if(str(message.getBody())[0] != "h"):
                    text = "beban"
        #  Correct ed spelling
        if(str(message.getParticipant()) == "5218116618135@s.whatsapp.net"):
            if(str(message.getBody())[0] != "/"):
                if(str(message.getBody())[0] != "h"):
                    text = "beban"
        #     routes.extend(SuperViews(self).routes)
        #     text = message.getBody()
        for route, callback in self.views:
            match = route.match(text)
            if match:  # in case of regex match, the callback is called, passing the message and the match object
                threading.Thread(target=self.handle_callback, args=(callback, message, match)).start()
                break

    def handle_callback(self, callback, message, match):
        try:
            # log message request
            if (message.isGroupMessage()):
                logging.info("(GROUP)[%s]-[%s]\t%s" % (message.getParticipant(), message.getFrom(), message.getBody()))
            else:
                logging.info("(PVT)[%s]\t%s" % (message.getFrom(), message.getBody()))
            # execute callback request
            data = callback(message, match)
            if data: self.toLower(data)  # if callback returns a message entity, sends it.
        except Exception as e:
            logging.exception("Error routing message: %s\n%s" % (message.getBody(), message))

    @ProtocolEntityCallback("message")
    def on_message(self, message):
        "Executes on every received message"
        self.toLower(message.ack())  # Auto ack
        self.toLower(message.ack(True))  # Auto ack (double blue check symbol)
        # Routing only text type messages, for now ignoring other types. (media, audio, location...)
        if message.getType() == 'text':
            self.route(message)

    @ProtocolEntityCallback("receipt")
    def on_receipt(self, entity):
        "Auto ack for every message receipt confirmation"
        self.toLower(entity.ack())
