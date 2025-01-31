def impliedProbability(odds):
    if odds > 0:
        return 100 / (odds + 100)
    else:
        return -odds / (-odds + 100)


def probabilityToAmerican(probability):

    if probability <= 0 or probability >= 1:
        raise ValueError("Probability must be between 0 and 1.")

    if probability > 0.5:
        return -100 * (probability / (1 - probability))
    else:
        return 100 * ((1 - probability) / probability)

def novig(odds1,odds2):
    impliedProb1 = impliedProbability(odds1)
    impliedProb2 = impliedProbability(odds2)

    fairProb1 = impliedProb1 / (impliedProb1+impliedProb2)
    fairProb2 = impliedProb2 / (impliedProb1+impliedProb2)

    fairOdds1 = probabilityToAmerican(fairProb1)
    fairOdds2 = probabilityToAmerican(fairProb2)

    return impliedProb1,impliedProb2,fairProb1,fairProb2,fairOdds1,fairOdds2






    
    


