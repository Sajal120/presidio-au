"""Predefined recognizers package. Holds all the default recognizers."""

# Australia recognizers
from presidio_analyzer.predefined_recognizers.nlp_engine_recognizers.transformers_recognizer import (  # noqa: E501
    TransformersRecognizer,
)

from .country_specific.australia.au_abn_recognizer import AuAbnRecognizer
from .country_specific.australia.au_acn_recognizer import AuAcnRecognizer
from .country_specific.australia.au_medicare_recognizer import AuMedicareRecognizer
from .country_specific.australia.au_tfn_recognizer import AuTfnRecognizer

# Generic recognizers
from .generic.credit_card_recognizer import CreditCardRecognizer
from .generic.crypto_recognizer import CryptoRecognizer
from .generic.date_recognizer import DateRecognizer
from .generic.email_recognizer import EmailRecognizer
from .generic.iban_recognizer import IbanRecognizer
from .generic.ip_recognizer import IpRecognizer
from .generic.mac_recognizer import MacAddressRecognizer
from .generic.phone_recognizer import PhoneRecognizer
from .generic.url_recognizer import UrlRecognizer

# NER recognizers
from .ner.gliner_recognizer import GLiNERRecognizer
from .ner.huggingface_ner_recognizer import HuggingFaceNerRecognizer
from .ner.medical_ner_recognizer import MedicalNERRecognizer

# NLP Engine recognizers
from .nlp_engine_recognizers.spacy_recognizer import SpacyRecognizer
from .nlp_engine_recognizers.stanza_recognizer import StanzaRecognizer
from .third_party.ahds_recognizer import AzureHealthDeidRecognizer

# Third-party recognizers
from .third_party.azure_ai_language import AzureAILanguageRecognizer
from .third_party.azure_openai_langextract_recognizer import (
    AzureOpenAILangExtractRecognizer,
)
from .third_party.basic_langextract_recognizer import BasicLangExtractRecognizer
from .third_party.langextract_recognizer import LangExtractRecognizer

PREDEFINED_RECOGNIZERS = [
    "PhoneRecognizer",
    "CreditCardRecognizer",
    "CryptoRecognizer",
    "DateRecognizer",
    "EmailRecognizer",
    "IpRecognizer",
    "IbanRecognizer",
    "UrlRecognizer",
]

NLP_RECOGNIZERS = {
    "spacy": SpacyRecognizer,
    "stanza": StanzaRecognizer,
    "transformers": TransformersRecognizer,
}

__all__ = [
    "CreditCardRecognizer",
    "CryptoRecognizer",
    "DateRecognizer",
    "EmailRecognizer",
    "IbanRecognizer",
    "IpRecognizer",
    "MacAddressRecognizer",
    "PhoneRecognizer",
    "UrlRecognizer",
    "SpacyRecognizer",
    "StanzaRecognizer",
    "NLP_RECOGNIZERS",
    "AuAbnRecognizer",
    "AuAcnRecognizer",
    "AuTfnRecognizer",
    "AuMedicareRecognizer",
    "TransformersRecognizer",
    "GLiNERRecognizer",
    "HuggingFaceNerRecognizer",
    "AzureAILanguageRecognizer",
    "AzureHealthDeidRecognizer",
    "LangExtractRecognizer",
    "AzureOpenAILangExtractRecognizer",
    "BasicLangExtractRecognizer",
    "MedicalNERRecognizer",
]
