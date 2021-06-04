import wikipedia

def give_details(monument):
    s = wikipedia.summary(monument, sentences = 2)
    return s
