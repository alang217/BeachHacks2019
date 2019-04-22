# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2

import nltk
from nltk.corpus import wordnet


def tone_analysis(client, doc):
    response = client.analyze_sentiment(document=doc)
    sentiment = response.document_sentiment

    message_response = ""
    if abs(sentiment.score) < 0.5:
        if sentiment.score > 0.25:
            message_response += "positively "
        elif sentiment.score < -0.25:
            message_response += "negatively "
        message_response += "neutral"
    elif sentiment.score >= 0.5:
        if sentiment.score >= 0.75:
            message_response += "very "
        message_response += "positive"
    else:
        if sentiment.score <= -0.75:
            message_response += "very "
        message_response += "negative"
    return message_response
    # return sentiment.magnitude, sentiment.score, message_response


def emotion_analysis(client, doc):
    return ""


def professionalism_analysis(client, doc):
    # for now use grammar and syntax check
    tokens = client.analyze_syntax(document=doc).tokens
    errors = 0
    for token in tokens:
        if not wordnet.synsets(token):
            if '\'' not in token:
                errors += 1
    if errors == 0:
        return 5
    elif 0 < errors < 3:
        return 3
    else:
        return 1


def offensiveness_analysis(client, doc):
    prediction_client = automl_v1beta1.PredictionServiceClient()

    name = 'projects/{}/locations/us-central1/models/{}'.format("beachhacks2019-238300", "TCN3574124264920733547")
    payload = {'text_snippet': {'content': doc.content, 'mime_type': 'text/plain'}}
    params = {}
    request = prediction_client.predict(name, payload, params)
    return request.payload[0].display_name


# reading_level helper functions


def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)


def unusual_words(tokens):
    text_vocab = set(w.lower() for w in tokens)
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)


def reading_level_analysis(client, doc):
    # for now use rarity density of words vs stopwords, slang words or non-existant words penalized
    value = 1

    tokens = client.analyze_syntax(document=doc).tokens
    cf = content_fraction(doc.content)
    if cf > .6:
        value += 1

    uw = unusual_words(tokens)
    errors = 0
    for word in uw:
        if not wordnet.synsets(word):
            if '\'' not in word:
                errors += 1
    if errors == 0:
        value += 3
    elif 0 < errors < 3:
        value += 2
    elif 3 < errors < 5:
        value += 1
    else:
        value += 0

    return value


def instantiate_client():
    return language.LanguageServiceClient()


def make_document(text):
    return types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT
    )


def __main__():
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    text = u'Hello, world!'
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    print("Testing Custom API")
    offensiveness_analysis(client, document)

    tokens = client.analyze_syntax(document=document).tokens
    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
                   'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')

    # Detects the sentiment of the text
    # sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Text: {}'.format(text))

    # print('Sentiment: \n\tScore = {}, \n\tMagnitude = {}'.format(sentiment.score, sentiment.magnitude))

    print('Syntax: ')

    for token in tokens:
        print('\t{}: {}'.format(token.text.content, pos_tag[token.part_of_speech.tag]))


if __name__ == '__main__':
    __main__()
