from src.keywords import SPAM_KEYWORDS

def detect_keywords(message):
    """"
        Return suspicious keywords found in the message.
    """

    message=message.lower()

    detected=[]

    for word in SPAM_KEYWORDS:
        if word in message:
            detected.append(word)


    return sorted(list(set(detected)))