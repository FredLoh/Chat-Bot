"""
    Wolfram Alpha:
    /query <term>
    key = "KYPHH3-83LWW2GT5T"
"""


from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
import unirest
import wikipedia



def wikipedia_query(self, message, match):
    query = match.group("query")
    result = wikipedia.summary(query, sentences=1)
    return TextMessageProtocolEntity(result, to=message.getFrom())
