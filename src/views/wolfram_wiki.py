"""
    Wolfram Alpha:
    /wa <term>
    key = "KYPHH3-83LWW2GT5T"
"""


from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
import unirest
import wikipedia

class WolframWiki():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        self.routes = [
            # ("^/wa", self.beban_spell_checker),
            ("^/q(uery))?\s(?P<query>[^$]+)$", self.wikipedia_query)
        ]

    def wikipedia_query(self, message, match):
        query = match.group("query")
        result = wikipedia.summary(query, sentences=1)
        return TextMessageProtocolEntity(result, to=message.getFrom())
