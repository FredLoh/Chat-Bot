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
    print("QUERY: " + query)
    result = wikipedia.summary(str(query), sentences=1)
    return TextMessageProtocolEntity(result, to=message.getFrom())
