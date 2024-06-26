# A program to translate text from French to English

# Imports
import os
from google.oauth2 import service_account
import six
from google.cloud import translate_v2 as translate

# API credentials

credentials = service_account.Credentials.from_service_account_file(
    # Insert a Google API key here
    '')

def translate_text(text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client(credentials=credentials)
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language='en')
    return result["translatedText"]

    # print(u"Text: {}".format(result["input"]))
    # print(u"Translation: {}".format(result["translatedText"]))
    # print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))

def main():
    translate_text("Bonjour")

if __name__ == "__main__":
    main()
