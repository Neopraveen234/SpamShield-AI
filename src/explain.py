def explain_prediction(prediction,spam_probability,keywords):
    reasons=[]

    if keywords:
        reasons.append(
            f"Detected suspicious keyword: {','.join(keywords)}."
        )

    if spam_probability>=90:
        reasons.append(
            "The model is high confidence this message is spam."
        )

    elif spam_probability>=70:
        reasons.appemd(
            "The message contains several spam characteristics."
        )

    else:
        reasons.append(
            "The message mostly resembles a normal conversation."
        )

    if prediction=="spam":
        reasons.append(
            "Avoid clickiing links or sharing personal informations."
        )

    else:
        reasons.append(
            "The message appears legitimate, but always verify unexpected requests."
        )

    return reasons