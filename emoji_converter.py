
def emoji_converter(message):
    words = message.split(" ")
    emoji = {
        "love" : "❤",
    "miss" : "😭",
    "kiss" : "💋",
    ":-)" : "😊",
    ":-(" : "😣"

    }
    output = ""
    for ch in words:
        output += emoji.get(ch, ch) + " "
    return output


print(emoji_converter(input('>')))
