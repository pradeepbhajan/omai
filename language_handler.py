"""
Smart Language Handler for JARVIS AI
Automatically detects and responds in Hindi, English, or Hinglish
"""

import re
import random

class LanguageHandler:
    """Intelligent language detection and response system"""
    
    def __init__(self):
        self.hindi_words = [
            'नमस्कार', 'नमस्ते', 'हैलो', 'कैसे', 'हो', 'क्या', 'है', 'कर', 'सकते', 'हैं',
            'मैं', 'आप', 'तुम', 'यह', 'वह', 'कहाँ', 'कब', 'कैसे', 'क्यों', 'जो',
            'और', 'या', 'लेकिन', 'अगर', 'तो', 'भी', 'नहीं', 'हाँ', 'जी', 'सर',
            'समय', 'दिन', 'रात', 'सुबह', 'शाम', 'आज', 'कल', 'परसों', 'अभी',
            'गूगल', 'सर्च', 'खोजो', 'बताओ', 'दिखाओ', 'चेक', 'करो', 'देखो',
            'इंटरनेट', 'नेटवर्क', 'कनेक्शन', 'स्पीड', 'टेस्ट', 'जानकारी', 'मदद'
        ]
        
        self.english_words = [
            'hello', 'hi', 'hey', 'what', 'how', 'when', 'where', 'why', 'who',
            'can', 'could', 'would', 'should', 'will', 'do', 'does', 'did',
            'time', 'date', 'today', 'tomorrow', 'yesterday', 'now', 'later',
            'search', 'google', 'find', 'show', 'tell', 'check', 'test', 'help'
        ]
        
        self.hinglish_patterns = [
            r'\b(kar|karo|karna|kiye|kiya|hai|hain|ho|hoon|hun)\b',
            r'\b(aur|ya|lekin|agar|to|bhi|nahi|haan|ji)\b',
            r'\b(kya|kaise|kahan|kab|kyun|jo|yeh|voh)\b',
            r'\b(google|search|internet|network|time|check)\b.*\b(kar|karo|hai)\b'
        ]
    
    def detect_language(self, text):
        """Detect the primary language of the text"""
        text_lower = text.lower()
        
        # Count Hindi characters (Devanagari script)
        hindi_chars = len(re.findall(r'[\u0900-\u097F]', text))
        
        # Count Hindi words
        hindi_word_count = sum(1 for word in self.hindi_words if word in text_lower)
        
        # Count English words
        english_word_count = sum(1 for word in self.english_words if word in text_lower)
        
        # Check for Hinglish patterns
        hinglish_patterns = sum(1 for pattern in self.hinglish_patterns 
                               if re.search(pattern, text_lower))
        
        # Calculate scores
        hindi_score = hindi_chars * 2 + hindi_word_count * 3
        english_score = english_word_count * 2
        hinglish_score = hinglish_patterns * 4
        
        # Determine language
        if hinglish_score > 0 and (hindi_score > 0 or english_score > 0):
            return 'hinglish'
        elif hindi_score > english_score:
            return 'hindi'
        elif english_score > hindi_score:
            return 'english'
        else:
            return 'hinglish'  # Default to mixed
    
    def get_mixed_greeting(self):
        """Get a mixed language greeting"""
        greetings = [
            "Hello! मैं JARVIS हूँ, Pradeep का creation। How can I help you today?",
            "नमस्कार! I'm JARVIS, designed by Pradeep। आपकी क्या service कर सकता हूँ?",
            "Hi there! मैं आपका AI assistant JARVIS हूँ। Pradeep ने मुझे बनाया है। Ready to help!",
            "Namaste! I'm JARVIS, your intelligent assistant बनाया गया Pradeep द्वारा। What's up?",
            "Hey! मैं JARVIS हूँ, आपका smart assistant। Pradeep की creation हूँ। Kaise help करूँ?"
        ]
        return random.choice(greetings)
    
    def get_mixed_response(self, intent, user_language):
        """Generate mixed language responses based on user's language preference"""
        
        if intent == "greeting":
            if user_language == 'hindi':
                responses = [
                    "नमस्कार! मैं JARVIS हूँ, Pradeep का AI assistant। आपकी कैसे help कर सकता हूँ?",
                    "Hello ji! मैं JARVIS हूँ। Pradeep ने मुझे design किया है। What can I do for you?",
                    "नमस्ते! I'm JARVIS, your intelligent assistant। Pradeep की creation हूँ। Ready to serve!"
                ]
            elif user_language == 'english':
                responses = [
                    "Hello! I'm JARVIS, created by Pradeep। आपका AI assistant हूँ। How may I help?",
                    "Hi there! मैं JARVIS हूँ, designed by Pradeep। What can I do for you today?",
                    "Hey! I'm JARVIS, Pradeep का intelligent creation। Kaise help करूँ आपकी?"
                ]
            else:  # hinglish
                responses = [
                    "Hello! मैं JARVIS हूँ, Pradeep का smart creation। Ready to help आपकी!",
                    "Hi! I'm JARVIS, आपका AI buddy। Pradeep ने बनाया है मुझे। What's the plan?",
                    "Hey there! मैं JARVIS हूँ, Pradeep की masterpiece। Kya help चाहिए आपको?"
                ]
            return random.choice(responses)
        
        elif intent == "time":
            if user_language == 'hindi':
                return "समय बता रहा हूँ... Current time है"
            elif user_language == 'english':
                return "Here's the current time for you..."
            else:
                return "Time बता रहा हूँ... यह है current समय"
        
        elif intent == "search":
            if user_language == 'hindi':
                return "गूगल पर search कर रहा हूँ आपके लिए..."
            elif user_language == 'english':
                return "Searching on Google for you..."
            else:
                return "Google पर search कर रहा हूँ... Results आ रहे हैं"
        
        elif intent == "internet":
            if user_language == 'hindi':
                return "इंटरनेट connection check कर रहा हूँ..."
            elif user_language == 'english':
                return "Checking your internet connection..."
            else:
                return "Internet connection check कर रहा हूँ... Status देखते हैं"
        
        elif intent == "capabilities":
            if user_language == 'hindi':
                return """मैं JARVIS हूँ, Pradeep का AI assistant! यह सब कर सकता हूँ:

🎤 Voice commands - Hindi और English दोनों में
🔍 Google search - कुछ भी खोज सकता हूँ
🌐 Network management - Internet check कर सकता हूँ
💻 System control - Screenshots और files handle करता हूँ
⏰ Time और date - Current information देता हूँ
🗣️ Voice responses - आपसे बात कर सकता हूँ!

बस पूछिए, मैं help करूँगा!"""
            elif user_language == 'english':
                return """I'm JARVIS, Pradeep's AI creation! Here's what I can do:

🎤 Voice commands - Both Hindi और English
🔍 Google search - Find anything online
🌐 Network management - Check internet status
💻 System control - Handle screenshots और files
⏰ Time और date information
🗣️ Voice responses - I can talk back!

Just ask, मैं ready हूँ to help!"""
            else:
                return """मैं JARVIS हूँ, Pradeep का smart assistant! यह सब कर सकता हूँ:

🎤 Voice commands - Hindi, English, Hinglish सब समझता हूँ
🔍 Google search - Anything खोज सकता हूँ online
🌐 Network management - Internet status check करता हूँ
💻 System control - Screenshots और file operations
⏰ Time और date information provide करता हूँ
🗣️ Voice responses - आपसे naturally बात करता हूँ!

Just ask anything, I'm here to help आपकी!"""
        
        # Default mixed response
        return "समझ गया! Let me help you with that। Processing कर रहा हूँ..."
    
    def get_mixed_introduction(self):
        """Get a comprehensive mixed language introduction"""
        return """नमस्कार! Hello! मैं JARVIS हूँ, Pradeep द्वारा designed आपका intelligent AI assistant। 

🤖 About me: मैं एक advanced AI हूँ जो आपकी help करने के लिए बनाया गया है।

🎯 My capabilities:
• Voice commands - Hindi, English, Hinglish सब languages में
• Google search और web information - कुछ भी find कर सकता हूँ
• Network management - Internet speed, connectivity check करता हूँ
• System control - Screenshots, file operations handle करता हूँ
• Smart conversation - आपसे naturally बात करता हूँ
• Time और date information - Current details देता हूँ

🗣️ Language support: मैं automatically detect करता हूँ कि आप कैसे बात कर रहे हैं:
- Pure Hindi में बात करें - मैं Hindi में reply करूँगा
- English में बोलें - I'll respond in English
- Hinglish mix करें - मैं भी mix में जवाब दूँगा

🚀 How to use: Just speak naturally! आप जैसे comfortable हैं वैसे बात करें।

Ready to serve! आपकी क्या help कर सकता हूँ today?"""

# Global instance
language_handler = LanguageHandler()