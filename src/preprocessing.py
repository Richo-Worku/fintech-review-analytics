import spacy

# Load model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text, remove_stopwords=True, lemmatize=True):
    doc = nlp(str(text).lower())
    tokens = []

    for token in doc:
        # remove punctuation, numbers, spaces
        if not token.is_alpha:
            continue

        # remove stopwords
        if remove_stopwords and token.is_stop:
            continue

        # apply lemmatization
        if lemmatize:
            tokens.append(token.lemma_)
        else:
            tokens.append(token.text)

    return " ".join(tokens)