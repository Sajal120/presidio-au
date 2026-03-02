"""Australian BSB (Bank State Branch) number recognizer."""
from typing import List, Optional

from presidio_analyzer import Pattern, PatternRecognizer


class AuBsbRecognizer(PatternRecognizer):
    """
    Recognizes Australian BSB (Bank State Branch) numbers.
    
    BSB is a 6-digit number used to identify Australian bank branches.
    Format: XXX-XXX or XXXXXX
    
    :param patterns: List of patterns to be used by this recognizer
    :param context: List of context words to increase confidence in detection
    :param supported_language: Language this recognizer supports
    :param supported_entity: The entity this recognizer can detect
    """

    PATTERNS = [
        Pattern(
            "BSB (XXX-XXX)",
            r"\b\d{3}-\d{3}\b",
            0.85,
        ),
        Pattern(
            "BSB (XXXXXX)",
            r"\b\d{6}\b",
            0.5,  # Lower confidence without hyphen
        ),
    ]

    CONTEXT = [
        "bsb",
        "bank",
        "branch",
        "account",
        "transfer",
        "eft",
        "direct debit",
        "payment",
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        context: Optional[List[str]] = None,
        supported_language: str = "en",
        supported_entity: str = "AU_BSB",
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
