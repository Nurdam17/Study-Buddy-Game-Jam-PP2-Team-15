import numpy
def res(brain_length):
    if brain_length < 15:
        result = ["Win", "Lose"]
        prob = [0.1, 0.9]
        result = numpy.random.choice(result, p=prob)
        if result == "Win":
            return 20
        else:
            return 0
    elif brain_length >= 15 and brain_length < 60:
        result = ["Win", "Lose"]
        prob = [0.6, 0.4]
        result = numpy.random.choice(result, p=prob)
        if result == "Win":
            return 15
        else:
            return 0
    elif brain_length >= 60 and brain_length < 90:
        result = ["Win", "Lose"]
        prob = [0.9, 0.1]
        result = numpy.random.choice(result, p=prob)
        if result == "Win":
            return 10
        else:
            return 0
    else:
        result = ["Win", "Lose"]
        prob = [0.98, 0.02]
        result = numpy.random.choice(result, p=prob)
        if result == "Win":
            return 5
        else:
            return 0