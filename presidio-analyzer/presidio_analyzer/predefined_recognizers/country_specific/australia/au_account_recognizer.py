"""Australian Bank Account Number recognizer."""
from typing import List, Optional

from presidio_analyzer import Pattern, PatternRecognizer


class AuAccountRecognizer(PatternRecognizer):
    """
    Recognizes Australian bank account numbers.
    
    Australian bank account numbers are typically 6-9 digits.
    
    :param patterns: List of patterns to be used by this recognizer
    :param context: List of context words to increase confidence in detection
    :param supported_language: Language this recognizer supports
    :param supported_entity: The entity this recognizer can detect
    """

    PATTERNS = [
        Pattern(
            "Account Number (6-9 digits)",
            r"\b\d{6,9}\b",
            0.4,  # Low confidence without context due to ambiguity
        ),
    ]

    CONTEXT = [
        "account",
        "acc",
        "account number",
        "acc number",
        "acc no",
        "bank account",
        "account name",
        "bsb",
        "transfer",
        "payment",
        "eft",
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        context: Optional[List[str]] = None,
        supported_language: str = "en",
        supported_entity: str = "AU_ACCOUNT_NUMBER",
        name: Optional[str] = None,
    ):
        """Initialize the recognizer."""
        patterns = patterns if patterns else self.PATTERNS
        context = context if context else self.CONTEXT
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
