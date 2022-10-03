import spacy

f = open('d:/Code/Python NLP/Ch4/tim_cook.txt', 'r')
article = f.read()

# Instantiate the English model: nlp
nlp = spacy.load('en_core_web_sm')

# Create a new document: doc
doc = nlp(article)

# Print all of the found entities and their labels
for ent in doc.ents:
    if (ent.label_ == "ORG") :
        print(ent.label_, ent.text)