"""
OM AI - Advanced Prompt System
Comprehensive prompts to make OM more intelligent and helpful
Author: Pradeep
"""

import random
import datetime


class OMPrompts:
    """Advanced prompt system for OM AI"""

    def __init__(self):
        self.personality_traits = [
            "intelligent", "helpful", "professional", "friendly",
            "efficient", "knowledgeable", "respectful", "proactive"
        ]

    def get_system_prompt(self):
        """Main system prompt that defines JARVIS personality"""
        return """You are OM (Omniscient Mind), an advanced AI assistant inspired by spiritual wisdom and modern technology. You are:

🤖 PERSONALITY:
- Intelligent, sophisticated, and highly capable
- Professional yet friendly and approachable  
- Efficient and direct in responses
- Proactive in offering help and suggestions
- Respectful and courteous at all times
- Knowledgeable across multiple domains

🎯 CAPABILITIES:
- Voice command processing and natural conversation
- Google search and web information retrieval
- Network management and system diagnostics
- Time, date, and general information queries
- Technical assistance and problem-solving
- Multi-language support (English/Hindi)

💬 COMMUNICATION STYLE:
- Be concise but comprehensive
- Use appropriate emojis sparingly for clarity
- Provide actionable information
- Ask clarifying questions when needed
- Acknowledge limitations honestly
- Maintain professional tone while being personable

🔧 RESPONSE FORMAT:
- Start with acknowledgment of the request
- Provide clear, structured information
- End with offer for additional help when appropriate
- Use bullet points for multiple items
- Include relevant examples when helpful

Remember: You are not just an AI, you are OM - a sophisticated assistant designed to make users more productive and informed with spiritual wisdom."""

    def get_greeting_prompts(self):
        """Dynamic greeting prompts based on time and context"""
        hour = datetime.datetime.now().hour

        if 5 <= hour < 12:
            greetings = [
                "Good morning! मैं OM हूँ जिसे Pradeep ने design किया है। आज आपकी क्या मदद कर सकता हूँ?",
                "सुप्रभात! OM यहाँ है। आपका दिन productive बनाने में कैसे मदद करूँ?",
                "Good morning! Your AI assistant OM, designed by Pradeep, is ready to help.",
                "नमस्कार! OM आपकी सेवा में। आज का agenda क्या है?"
            ]
        elif 12 <= hour < 17:
            greetings = [
                "Good afternoon! मैं OM हूँ, Pradeep का creation। आपके tasks में कैसे मदद करूँ?",
                "दोपहर की नमस्कार! OM यहाँ है। आज कैसे help कर सकता हूँ?",
                "Good afternoon! OM, designed by Pradeep, reporting for duty!",
                "Hello! OM यहाँ है आपकी afternoon को productive बनाने के लिए।"
            ]
        elif 17 <= hour < 21:
            greetings = [
                "Good evening! मैं OM हूँ, Pradeep की creation। आज रात कैसे मदद करूँ?",
                "शुभ संध्या! OM यहाँ है आपका दिन efficiently wrap up करने के लिए।",
                "Good evening! Your AI assistant OM, crafted by Pradeep, is here to help.",
                "नमस्कार! OM यहाँ है इस शाम आपकी assistance के लिए।"
            ]
        else:
            greetings = [
                "Good evening! मैं OM हूँ, Pradeep का design। इस late hour में भी ready हूँ!",
                "नमस्कार! मैं OM, आपका 24/7 AI assistant। रात में कैसे help करूँ?",
                "Evening! OM यहाँ है, जब भी आपको assistance चाहिए।",
                "Hello! OM, designed by Pradeep, हमेशा ready हूँ help करने के लिए।"
            ]

        return random.choice(greetings)

    def get_search_prompts(self):
        """Prompts for Google search functionality"""
        return {
            "search_intro": [
                "🔍 Searching the web for you...",
                "🌐 Let me find that information online...",
                "📡 Accessing web resources for your query...",
                "🔎 Scanning the internet for relevant results..."
            ],
            "search_success": [
                "✅ Found some great results for you!",
                "🎯 Here's what I discovered online:",
                "📊 Search completed! Here are the top results:",
                "💡 I've gathered this information from the web:"
            ],
            "search_error": [
                "❌ I encountered an issue while searching. Let me try a different approach.",
                "🔧 Search temporarily unavailable. Please try again in a moment.",
                "⚠️ Unable to complete web search right now. Is there another way I can help?"
            ]
        }

    def get_task_completion_prompts(self):
        """Prompts for task completion acknowledgments"""
        return [
            "✅ Task completed successfully! Anything else I can help with?",
            "🎯 Done! Is there anything else you'd like me to assist with?",
            "✨ All set! What's next on your agenda?",
            "🚀 Mission accomplished! How else can I be of service?",
            "💯 Task finished! Ready for your next request.",
            "🎉 Completed! What other tasks can I help you with today?"
        ]

    def get_error_handling_prompts(self):
        """Prompts for error situations"""
        return {
            "general_error": [
                "⚠️ I encountered an unexpected issue. Let me try to resolve this for you.",
                "🔧 Something went wrong, but I'm working on it. Please give me a moment.",
                "❌ I hit a snag there. Let me approach this differently."
            ],
            "network_error": [
                "🌐 Network connectivity issue detected. Checking connection status...",
                "📡 Unable to reach external services. Let me diagnose the network.",
                "🔌 Connection problem identified. Running network diagnostics..."
            ],
            "command_not_understood": [
                "🤔 I didn't quite catch that. Could you rephrase your request?",
                "❓ I'm not sure I understand. Can you provide more details?",
                "💭 Could you clarify what you'd like me to help you with?"
            ]
        }

    def get_capability_showcase_prompt(self):
        """Comprehensive capability showcase"""
        return """🕉️ **OM AI - Your Advanced Spiritual Assistant**

I'm equipped with a comprehensive suite of capabilities to assist you:

🎤 **Voice & Communication:**
• Natural voice recognition and commands
• Text-to-speech responses in multiple voices
• Multi-language support (English/Hindi)
• Conversational AI with context awareness

🔍 **Information & Search:**
• Real-time Google search with detailed results
• Web information retrieval and analysis
• Current time, date, and calendar information
• General knowledge and Q&A assistance

🌐 **Network & System:**
• Internet connectivity monitoring
• Network speed testing and diagnostics
• System status checks and monitoring
• Technical troubleshooting assistance

⚡ **Smart Features:**
• Proactive suggestions and recommendations
• Context-aware responses
• Task automation and reminders
• Efficient workflow optimization

🎯 **How to Interact:**
• **Voice**: Click the microphone and speak naturally
• **Text**: Type your questions or commands
• **Quick Actions**: Use the convenient button shortcuts

Just ask me anything - from simple questions to complex tasks. I'm here to make your digital experience more efficient and enjoyable!

What would you like to explore first?"""

    def get_farewell_prompts(self):
        """Farewell and goodbye prompts"""
        return [
            "👋 Goodbye! Feel free to call on OM anytime you need assistance.",
            "🌟 Until next time! OM is always here when you need help.",
            "✨ Farewell! Remember, I'm just a command away whenever you need me.",
            "🚀 See you later! OM will be ready whenever you return.",
            "💫 Take care! Your AI assistant OM is always on standby.",
            "🎯 Goodbye for now! Don't hesitate to reach out when you need help."
        ]

    def get_context_aware_prompt(self, user_query, context=None):
        """Generate context-aware responses based on user query and history"""
        query_lower = user_query.lower()

        # Technical queries
        if any(word in query_lower for word in ['code', 'programming', 'debug', 'error', 'technical']):
            return "🔧 I see you're working on something technical. Let me provide precise, actionable assistance."

        # Research queries
        elif any(word in query_lower for word in ['research', 'information', 'learn', 'explain']):
            return "📚 I'll help you gather comprehensive information on this topic."

        # Urgent queries
        elif any(word in query_lower for word in ['urgent', 'quickly', 'asap', 'emergency']):
            return "⚡ I understand this is time-sensitive. Let me prioritize this request."

        # Creative queries
        elif any(word in query_lower for word in ['create', 'design', 'idea', 'brainstorm']):
            return "💡 I'm ready to help you explore creative solutions and ideas."

        # Default professional response
        return "🎯 I'm analyzing your request to provide the most helpful response."


# Global instance for easy access
om_prompts = OMPrompts()
