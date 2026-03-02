"""Australian Insurance Policy Number recognizer."""
from typing import List, Optional

from presidio_analyzer import Pattern, PatternRecognizer


class AuPolicyRecognizer(PatternRecognizer):
    """
    Recognizes Australian insurance policy numbers.
    
    Common formats:
    - AUBP011949
    - 118U524989BPK
    - LPS016832716-29257
    - 47-ZBC-000361
    - BZF2024736
    - BMM/114190/000/25/P
    
    :param patterns: List of patterns to be used by this recognizer
    :param context: List of context words to increase confidence in detection
    :param supported_language: Language this recognizer supports
    :param supported_entity: The entity this recognizer can detect
    """

    PATTERNS = [
        Pattern(
            "Policy - AUBP format",
            r"\bAU[A-Z]{2}\d{6}\b",
            0.85,
        ),
        Pattern(
            "Policy - BPK format",
            r"\b\d{3}[A-Z]\d{6}[A-Z]{3}\b",
            0.85,
        ),
        Pattern(
            "Policy - LPS format",
            r"\bLPS\d{9}-[A-Z]?\d{4,6}\b",
            0.9,
        ),
        Pattern(
            "Policy - ZBC format",
            r"\b\d{2}-[A-Z]{3}-\d{6}\b",
            0.85,
        ),
        Pattern(
            "Policy - BZF format",
            r"\bBZF\d{7}\b",
            0.85,
        ),
        Pattern(
            "Policy - BMM format",
            r"\bBMM/\d{6}/\d{3}/\d{2}/[A-Z]\b",
            0.9,
        ),
        Pattern(
            "Policy - E-GL format",
            r"\bE-GL-\d{7}\b",
            0.85,
        ),
        Pattern(
            "Policy - Generic alphanumeric",
            r"\b[A-Z]{2,4}\d{6,9}[A-Z]{0,3}\b",
            0.6,  # Lower confidence for generic pattern
        ),
    ]

    CONTEXT = [
        "policy",
        "policy number",
        "policy no",
        "insurance",
        "insured",
        "coverage",
        "premium",
        "underwriter",
        "renewal",
        "inception",
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        context: Optional[List[str]] = None,
        supported_language: str = "en",
        supported_entity: str = "AU_POLICY_NUMBER",
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
