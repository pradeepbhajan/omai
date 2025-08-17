#!/usr/bin/env python3
"""
Fixed NLP Processor for Jarvis AI
Enhanced natural language processing with better intent recognition
"""

import re
import json
from typing import Dict, List, Tuple, Optional


class EnhancedNLPProcessor:
    """Enhanced NLP processor with improved intent recognition"""

    def __init__(self):
        self.intent_patterns = self._load_intent_patterns()
        self.entity_extractors = self._setup_entity_extractors()

    def _load_intent_patterns(self) -> Dict[str, List[str]]:
        """Load intent recognition patterns"""
        return {
            # Search intents
            "google_search": [
                r"search (?:for )?(.+)",
                r"google (.+)",
                r"find (?:information about )?(.+)",
                r"look up (.+)",
                r"what is (.+)",
                r"tell me about (.+)"
            ],

            "detailed_search": [
                r"detailed search (?:for )?(.+)",
                r"comprehensive (?:search|info) (?:about )?(.+)",
                r"in-depth (?:search|information) (?:on )?(.+)"
            ],

            "image_search": [
                r"(?:search|find|show) (?:me )?images? (?:of )?(.+)",
                r"picture(?:s)? (?:of )?(.+)",
                r"photo(?:s)? (?:of )?(.+)"
            ],

            "video_search": [
                r"(?:search|find|show) (?:me )?videos? (?:of )?(.+)",
                r"youtube (?:search )?(.+)",
                r"video(?:s)? (?:about )?(.+)"
            ],

            "lucky_search": [
                r"(?:i'm )?feeling lucky (.+)",
                r"lucky search (.+)",
                r"first result (?:for )?(.+)"
            ],

            # Weather intents
            "get_weather": [
                r"weather (?:in )?(.+)",
                r"(?:what's|how's) the weather (?:in )?(.+)",
                r"temperature (?:in )?(.+)",
                r"mausam (.+)"
            ],

            # System intents
            "get_time": [
                r"(?:what )?time (?:is it)?",
                r"current time",
                r"tell me the time",
                r"samay kya hai"
            ],

            "get_date": [
                r"(?:what's )?(?:the )?date (?:today)?",
                r"today's date",
                r"current date",
                r"aaj ki tarikh"
            ],

            # AI intents
            "chat_ai": [
                r"chat (.+)",
                r"talk (?:to me )?about (.+)",
                r"discuss (.+)",
                r"conversation (?:about )?(.+)"
            ],

            "openai_explain": [
                r"explain (.+)",
                r"describe (.+)",
                r"what does (.+) mean",
                r"definition (?:of )?(.+)"
            ],

            # Utility intents
            "motivate": [
                r"motivate (?:me)?",
                r"motivation",
                r"inspire (?:me)?",
                r"encouragement"
            ],

            "introduction": [
                r"(?:who are you|introduce yourself)",
                r"what (?:can you do|are your capabilities)",
                r"about (?:you|yourself)"
            ],

            # Network intents
            "check_internet": [
                r"check internet",
                r"internet (?:status|connection)",
                r"am i online",
                r"network (?:status|check)"
            ],

            "ping_website": [
                r"ping (.+)",
                r"test connection (?:to )?(.+)",
                r"check (?:if )?(.+) (?:is )?(?:up|online|working)"
            ],

            # Greetings and social
            "greeting": [
                r"(?:hi|hello|hey|namaste)",
                r"good (?:morning|afternoon|evening)",
                r"greetings"
            ],

            "how_are_you": [
                r"how are you",
                r"how (?:are )?things",
                r"kaise ho",
                r"what's up"
            ],

            "thank_you": [
                r"thank(?:s| you)",
                r"dhanyawad",
                r"shukriya",
                r"appreciate (?:it|this)"
            ]
        }

    def _setup_entity_extractors(self) -> Dict[str, callable]:
        """Setup entity extraction functions"""
        return {
            "city": self._extract_city,
            "website": self._extract_website,
            "app_name": self._extract_app_name,
            "file_path": self._extract_file_path
        }

    def process_text(self, text: str) -> Tuple[str, Dict[str, any]]:
        """
        Process natural language text and extract intent and parameters

        Args:
            text (str): Input text to process

        Returns:
            Tuple[str, Dict]: Intent and extracted parameters
        """
        if not text or not text.strip():
            return "unknown", {}

        # Clean and normalize text
        cleaned_text = self._clean_text(text)

        # Extract intent
        intent = self._extract_intent(cleaned_text)

        # Extract parameters based on intent
        params = self._extract_parameters(cleaned_text, intent)

        return intent, params

    def _clean_text(self, text: str) -> str:
        """Clean and normalize input text"""
        # Convert to lowercase
        text = text.lower().strip()

        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)

        # Remove punctuation at the end
        text = re.sub(r'[.!?]+$', '', text)

        return text

    def _extract_intent(self, text: str) -> str:
        """Extract intent from cleaned text"""
        # Check each intent pattern
        for intent, patterns in self.intent_patterns.items():
            for pattern in patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    return intent

        # Default fallback - if it looks like a question, search it
        if any(word in text for word in ['what', 'how', 'why', 'when', 'where', 'who']):
            return "google_search"

        # If it contains search-like keywords
        if any(word in text for word in ['search', 'find', 'lookup', 'google']):
            return "google_search"

        # Default to search for unknown intents
        return "google_search"

    def _extract_parameters(self, text: str, intent: str) -> Dict[str, any]:
        """Extract parameters based on intent"""
        params = {}

        if intent in ["google_search", "detailed_search", "image_search", "video_search", "lucky_search"]:
            params["query"] = self._extract_search_query(text, intent)

        elif intent == "get_weather":
            params["city"] = self._extract_city(text)

        elif intent == "ping_website":
            params["host"] = self._extract_website(text)

        elif intent in ["chat_ai", "openai_explain"]:
            params["message"] = self._extract_message(text, intent)

        elif intent == "open_app":
            params["app"] = self._extract_app_name(text)

        elif intent == "open_file":
            params["path"] = self._extract_file_path(text)

        return params

    def _extract_search_query(self, text: str, intent: str) -> str:
        """Extract search query from text"""
        # Remove intent-specific prefixes
        query_patterns = {
            "google_search": [
                r"search (?:for )?(.+)",
                r"google (.+)",
                r"find (?:information about )?(.+)",
                r"look up (.+)",
                r"what is (.+)",
                r"tell me about (.+)"
            ],
            "detailed_search": [
                r"detailed search (?:for )?(.+)",
                r"comprehensive (?:search|info) (?:about )?(.+)"
            ],
            "image_search": [
                r"(?:search|find|show) (?:me )?images? (?:of )?(.+)",
                r"picture(?:s)? (?:of )?(.+)"
            ],
            "video_search": [
                r"(?:search|find|show) (?:me )?videos? (?:of )?(.+)",
                r"video(?:s)? (?:about )?(.+)"
            ]
        }

        if intent in query_patterns:
            for pattern in query_patterns[intent]:
                match = re.search(pattern, text, re.IGNORECASE)
                if match:
                    return match.group(1).strip()

        # Fallback: return the whole text
        return text

    def _extract_city(self, text: str) -> str:
        """Extract city name from text"""
        # Common weather patterns
        patterns = [
            r"weather (?:in )?(.+)",
            r"temperature (?:in )?(.+)",
            r"mausam (.+)"
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                city = match.group(1).strip()
                # Remove common words
                city = re.sub(r'\b(?:city|weather|temperature)\b',
                              '', city, flags=re.IGNORECASE).strip()
                return city if city else "Delhi"

        return "Delhi"  # Default city

    def _extract_website(self, text: str) -> str:
        """Extract website/hostname from text"""
        # Look for URL patterns
        url_pattern = r'(?:https?://)?(?:www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
        match = re.search(url_pattern, text)
        if match:
            return match.group(1)

        # Look for ping patterns
        ping_patterns = [
            r"ping (.+)",
            r"test connection (?:to )?(.+)",
            r"check (?:if )?(.+) (?:is )?(?:up|online|working)"
        ]

        for pattern in ping_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                host = match.group(1).strip()
                # Clean up common words
                host = re.sub(r'\b(?:website|site|server)\b', '',
                              host, flags=re.IGNORECASE).strip()
                return host if host else "google.com"

        return "google.com"  # Default host

    def _extract_message(self, text: str, intent: str) -> str:
        """Extract message for AI chat/explanation"""
        if intent == "chat_ai":
            patterns = [
                r"chat (.+)",
                r"talk (?:to me )?about (.+)",
                r"discuss (.+)"
            ]
        else:  # openai_explain
            patterns = [
                r"explain (.+)",
                r"describe (.+)",
                r"what does (.+) mean"
            ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()

        return text  # Fallback to full text

    def _extract_app_name(self, text: str) -> str:
        """Extract application name"""
        patterns = [
            r"open (.+)",
            r"launch (.+)",
            r"start (.+)"
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                app = match.group(1).strip()
                # Remove common words
                app = re.sub(r'\b(?:app|application|program)\b',
                             '', app, flags=re.IGNORECASE).strip()
                return app

        return ""

    def _extract_file_path(self, text: str) -> str:
        """Extract file path"""
        patterns = [
            r"open (?:file )?(.+)",
            r"show (?:me )?(?:file )?(.+)"
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()

        return ""

    def get_confidence_score(self, text: str, intent: str) -> float:
        """Get confidence score for intent recognition"""
        if intent == "unknown":
            return 0.0

        if intent not in self.intent_patterns:
            return 0.5

        # Check how well the text matches the intent patterns
        patterns = self.intent_patterns[intent]
        max_confidence = 0.0

        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                # Exact pattern match gets high confidence
                max_confidence = max(max_confidence, 0.9)
            elif any(word in text.lower() for word in pattern.split()):
                # Partial match gets medium confidence
                max_confidence = max(max_confidence, 0.6)

        return max_confidence

    def suggest_alternatives(self, text: str) -> List[str]:
        """Suggest alternative intents for ambiguous text"""
        suggestions = []

        for intent, patterns in self.intent_patterns.items():
            confidence = self.get_confidence_score(text, intent)
            if 0.3 <= confidence < 0.8:  # Medium confidence range
                suggestions.append(intent)

        return suggestions[:3]  # Return top 3 suggestions


# Create global instance
nlp_processor = EnhancedNLPProcessor()


def process_natural_language(text: str) -> Tuple[str, Dict[str, any]]:
    """
    Main function to process natural language input

    Args:
        text (str): Natural language input

    Returns:
        Tuple[str, Dict]: Intent and parameters
    """
    return nlp_processor.process_text(text)
