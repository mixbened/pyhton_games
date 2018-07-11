# Get Words 
def get_words():
    global noun
    global verb
    global pro
    global adjective
    noun = input('Provide a Noun')
    verb = input('Provide a Verb')
    pro = input('Provide a Pronoun')
    adjective = input('Provide an adjective')

# build sentence
def build_sentence():
    return pro + " " + verb + " " + adjective + " " + noun

# start game
get_words()
print(build_sentence())

