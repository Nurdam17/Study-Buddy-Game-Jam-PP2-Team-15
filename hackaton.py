import numpy
def res(brain_length):
    if brain_length < 15:
        result = ["Win", "Lose"]
        prob = [0.02, 0.98]
        return numpy.random.choice(result, p=prob)
    elif brain_length >= 15 and brain_length < 60:
        result = ["Win", "Lose"]
        prob = [0.6, 0.4]
        return numpy.random.choice(result, p=prob)
    elif brain_length >= 60 and brain_length < 90:
        result = ["Win", "Lose"]
        prob = [0.9, 0.1]
        return numpy.random.choice(result, p=prob)
    else:
        result = ["Win", "Lose"]
        prob = [0.98, 0.02]
        return numpy.random.choice(result, p=prob)