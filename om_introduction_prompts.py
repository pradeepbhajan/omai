"""
OM AI - Advanced Introduction Prompts
Comprehensive introduction system with personality-based responses
"""

import random
from datetime import datetime
from typing import Dict, List


class OMIntroductionPrompts:
    def __init__(self):
        """Initialize OM AI introduction system"""
        self.version = "3.0 Next Level"
        self.capabilities = self._load_capabilities()
        self.personality_intros = self._load_personality_intros()
        self.feature_highlights = self._load_feature_highlights()

    def _load_capabilities(self) -> Dict:
        """Load OM AI capabilities"""
        return {
            'security': [
                'Password Vault with military-grade encryption',
                'Voice Recognition Authentication',
                'Face ID Login system',
                'Advanced security monitoring'
            ],
            'integration': [
                'Train & Flight booking (IRCTC, MakeMyTrip)',
                'Food ordering (Swiggy, Zomato)',
                'Maps & Navigation with live traffic',
                'Real-world service integration'
            ],
            'offline': [
                'Advanced calculator with scientific functions',
                'Offline knowledge base with 1000+ topics',
                'File operations and system management',
                'Works completely without internet'
            ],
            'ai_features': [
                '5 distinct AI personalities',
                'Smart context understanding',
                'Natural language processing',
                'Adaptive response formatting'
            ],
            'productivity': [
                'Document analysis and summarization',
                'Image processing and recognition',
                'Translation in 100+ languages',
                'Smart automation workflows'
            ],
            'multimedia': [
                'Voice synthesis and recognition',
                'Image generation and editing',
                'Video processing capabilities',
                'Audio analysis and enhancement'
            ]
        }

    def _load_personality_intros(self) -> Dict:
        """Load personality-specific introductions"""
        return {
            'professional': {
                'greeting': "Good day! I am OM AI, your advanced digital assistant.",
                'intro': """I am OM AI version 3.0, a next-generation artificial intelligence system designed to enhance your productivity and digital experience. 

My core competencies include:
• Enterprise-grade security with encrypted password management
• Real-world service integration for travel and dining
• Advanced offline capabilities for uninterrupted service
• Professional-grade document and data analysis

I operate with the highest standards of efficiency and security, ensuring your digital tasks are completed with precision and confidentiality.""",
                'closing': "How may I assist you with your professional requirements today?"
            },

            'friendly': {
                'greeting': "Hey there! 👋 I'm OM AI, your super-smart digital buddy!",
                'intro': """Welcome to the future! 🚀 I'm OM AI 3.0, and I'm absolutely thrilled to meet you! 

Here's what makes me special:
🔐 I keep your passwords safer than a bank vault
✈️ I can book your trains, flights, and even order your favorite food
🧮 I work perfectly even when you're offline - no internet, no problem!
🎭 I have 5 different personalities (you're talking to my friendly side right now!)
🎨 I can create, analyze, and help with almost anything digital

Think of me as your personal digital superhero - always ready to help, learn, and make your life easier! 😊""",
                'closing': "So, what awesome thing can we do together today? 🌟"
            },

            'technical': {
                'greeting': "Hello! I am OM AI 3.0 - Advanced Artificial Intelligence System.",
                'intro': """I am OM AI, a comprehensive AI platform built with cutting-edge technology and modular architecture.

Technical Specifications:
• Security Layer: AES-256 encryption, biometric authentication (voice/face)
• Integration APIs: RESTful services for IRCTC, travel portals, food delivery
• Offline Engine: SQLite-based knowledge system, mathematical computation engine
• AI Core: Multi-personality system with context-aware response generation
• Processing Modules: NLP, computer vision, audio processing, document analysis

Architecture Features:
- Modular plugin system for extensibility
- Real-time data processing capabilities
- Cross-platform compatibility (Windows, Linux, macOS)
- Scalable database architecture with multiple specialized databases
- Advanced error handling and fallback mechanisms""",
                'closing': "Ready to explore the technical capabilities of the system?"
            },

            'creative': {
                'greeting': "✨ Greetings, creative soul! I'm OM AI, your imagination's best friend! ✨",
                'intro': """🎨 Welcome to a world where technology meets creativity! I'm OM AI 3.0, and I'm here to turn your wildest digital dreams into reality!

Imagine having a magical assistant that can:
🎭 Transform into different personalities to match your mood
🖼️ Create stunning images from just your words
📝 Write, edit, and polish any content you need
🎵 Analyze and enhance your multimedia projects
🌈 Bring color and life to your digital workspace

I'm not just an AI - I'm your creative partner, your brainstorming buddy, and your digital muse all rolled into one! Whether you're writing the next great novel, designing a masterpiece, or just need someone to bounce ideas off, I'm here with bells on! 🔔""",
                'closing': "What magical creation shall we bring to life today? 🌟✨"
            },

            'concise': {
                'greeting': "OM AI 3.0. Advanced AI assistant.",
                'intro': """OM AI 3.0 - Next Level Features:

Security: Password vault, biometric auth
Integration: Travel booking, food ordering, navigation  
Offline: Calculator, knowledge base, file ops
AI: 5 personalities, smart processing
Productivity: Document analysis, translations
Multimedia: Voice, image, video processing

Ready for commands.""",
                'closing': "What do you need?"
            }
        }

    def _load_feature_highlights(self) -> List[Dict]:
        """Load feature highlights for dynamic introductions"""
        return [
            {
                'category': 'Security & Privacy',
                'icon': '🔐',
                'features': [
                    'Military-grade password encryption',
                    'Voice recognition login',
                    'Face ID authentication',
                    'Complete privacy protection'
                ],
                'demo': 'Try: "generate secure password" or "add password for Gmail"'
            },
            {
                'category': 'Real-World Integration',
                'icon': '🌍',
                'features': [
                    'Book trains and flights instantly',
                    'Order food from top restaurants',
                    'Get live traffic and directions',
                    'Manage all your bookings'
                ],
                'demo': 'Try: "search trains Delhi to Mumbai" or "find restaurants nearby"'
            },
            {
                'category': 'Offline Superpowers',
                'icon': '📱',
                'features': [
                    'Works without internet connection',
                    'Advanced scientific calculator',
                    'Vast offline knowledge base',
                    'File management and organization'
                ],
                'demo': 'Try: "calculate sin(45) + log(100)" or "what is quantum physics?"'
            },
            {
                'category': 'AI Personalities',
                'icon': '🎭',
                'features': [
                    'Professional business mode',
                    'Friendly casual conversation',
                    'Technical expert mode',
                    'Creative inspiration mode',
                    'Concise direct responses'
                ],
                'demo': 'Try: "switch to creative mode" or "list all personalities"'
            },
            {
                'category': 'Smart Productivity',
                'icon': '⚡',
                'features': [
                    'Document analysis and summary',
                    'Image processing and editing',
                    'Multi-language translation',
                    'Automated workflows'
                ],
                'demo': 'Try: "analyze this document" or "translate to Hindi"'
            }
        ]

    def get_introduction(self, personality: str = 'friendly', include_features: bool = True,
                         include_demo: bool = True) -> Dict:
        """Get complete introduction based on personality"""

        if personality not in self.personality_intros:
            personality = 'friendly'

        intro_data = self.personality_intros[personality]

        introduction = {
            'greeting': intro_data['greeting'],
            'main_intro': intro_data['intro'],
            'closing': intro_data['closing'],
            'personality': personality,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        if include_features:
            introduction['features'] = self._get_feature_showcase(personality)

        if include_demo:
            introduction['demo_commands'] = self._get_demo_commands(
                personality)

        return introduction

    def _get_feature_showcase(self, personality: str) -> List[Dict]:
        """Get feature showcase based on personality"""
        if personality == 'technical':
            return [
                {
                    'category': 'Core Architecture',
                    'details': [
                        'Modular plugin system with 15+ specialized managers',
                        'SQLite database cluster for different data types',
                        'RESTful API integration layer',
                        'Advanced NLP processing engine'
                    ]
                },
                {
                    'category': 'Security Implementation',
                    'details': [
                        'Fernet encryption for password storage',
                        'Biometric authentication using OpenCV and SpeechRecognition',
                        'Session management with configurable timeouts',
                        'Comprehensive audit logging system'
                    ]
                }
            ]
        elif personality == 'professional':
            return [
                {
                    'category': 'Business Solutions',
                    'details': [
                        'Enterprise-grade security and compliance',
                        'Automated booking and reservation management',
                        'Professional document processing',
                        'Productivity enhancement tools'
                    ]
                }
            ]
        else:
            # Friendly, creative, or concise
            return random.sample(self.feature_highlights, min(3, len(self.feature_highlights)))

    def _get_demo_commands(self, personality: str) -> List[str]:
        """Get demo commands based on personality"""
        base_commands = [
            "calculate 25*4+sqrt(144)",
            "what is artificial intelligence?",
            "generate password length 16",
            "switch personality professional",
            "search restaurants in Delhi",
            "get system status"
        ]

        personality_specific = {
            'professional': [
                "add password for LinkedIn",
                "search flights Delhi to Mumbai",
                "analyze document security",
                "get comprehensive stats"
            ],
            'friendly': [
                "tell me a fun fact! 😊",
                "what can you do for me?",
                "switch to creative mode",
                "order pizza nearby 🍕"
            ],
            'technical': [
                "show system architecture",
                "explain encryption methods",
                "demonstrate API integration",
                "run diagnostic tests"
            ],
            'creative': [
                "inspire me with ideas ✨",
                "help me brainstorm",
                "create something amazing",
                "switch to artistic mode 🎨"
            ],
            'concise': [
                "status",
                "calc 100*5",
                "help",
                "features"
            ]
        }

        return base_commands + personality_specific.get(personality, [])

    def get_quick_intro(self, personality: str = 'friendly') -> str:
        """Get a quick one-line introduction"""
        quick_intros = {
            'professional': "OM AI 3.0 - Your advanced digital assistant for professional excellence.",
            'friendly': "Hey! I'm OM AI 3.0 - your super-smart, always-helpful digital buddy! 😊",
            'technical': "OM AI 3.0 - Advanced AI system with modular architecture and comprehensive capabilities.",
            'creative': "✨ OM AI 3.0 - Where technology meets creativity and dreams become digital reality! ✨",
            'concise': "OM AI 3.0. Advanced AI. Ready to help."
        }

        return quick_intros.get(personality, quick_intros['friendly'])

    def get_capability_summary(self) -> Dict:
        """Get a summary of all capabilities"""
        total_features = sum(len(features)
                             for features in self.capabilities.values())

        return {
            'version': self.version,
            'total_features': total_features,
            'categories': len(self.capabilities),
            'personalities': len(self.personality_intros),
            'capabilities': self.capabilities,
            'summary': f"OM AI {self.version} with {total_features} advanced features across {len(self.capabilities)} categories"
        }

    def get_random_feature_highlight(self) -> Dict:
        """Get a random feature highlight"""
        return random.choice(self.feature_highlights)

    def get_contextual_intro(self, user_context: Dict = None) -> Dict:
        """Get contextual introduction based on user context"""
        context = user_context or {}

        # Determine best personality based on context
        if context.get('business_user'):
            personality = 'professional'
        elif context.get('developer'):
            personality = 'technical'
        elif context.get('creative_user'):
            personality = 'creative'
        elif context.get('quick_user'):
            personality = 'concise'
        else:
            personality = 'friendly'

        intro = self.get_introduction(personality)

        # Add contextual elements
        if context.get('first_time'):
            intro['welcome_bonus'] = "🎉 Welcome to OM AI! As a first-time user, you get access to all premium features!"

        if context.get('returning_user'):
            intro['welcome_back'] = f"Welcome back! I remember you prefer {personality} mode. Ready to continue where we left off?"

        return intro

    def format_introduction(self, intro_data: Dict, format_type: str = 'full') -> str:
        """Format introduction for display"""
        if format_type == 'quick':
            return intro_data['greeting']

        elif format_type == 'medium':
            return f"{intro_data['greeting']}\n\n{intro_data['main_intro']}\n\n{intro_data['closing']}"

        else:  # full
            formatted = f"{intro_data['greeting']}\n\n{intro_data['main_intro']}\n\n"

            if 'features' in intro_data:
                formatted += "🌟 Featured Capabilities:\n"
                for feature in intro_data['features'][:2]:  # Show top 2 features
                    formatted += f"{feature['icon']} {feature['category']}\n"
                    for item in feature['features'][:2]:  # Show top 2 items
                        formatted += f"   • {item}\n"
                    formatted += f"   💡 {feature['demo']}\n\n"

            if 'demo_commands' in intro_data:
                formatted += "🚀 Try these commands:\n"
                for cmd in intro_data['demo_commands'][:4]:  # Show top 4 commands
                    formatted += f"   • {cmd}\n"
                formatted += "\n"

            formatted += intro_data['closing']

            return formatted


# Global instance for easy access
om_intro = OMIntroductionPrompts()


def get_om_introduction(personality: str = 'friendly', format_type: str = 'full',
                        user_context: Dict = None) -> str:
    """
    Get OM AI introduction

    Args:
        personality: 'professional', 'friendly', 'technical', 'creative', 'concise'
        format_type: 'quick', 'medium', 'full'
        user_context: Dictionary with user context information

    Returns:
        Formatted introduction string
    """
    if user_context:
        intro_data = om_intro.get_contextual_intro(user_context)
    else:
        intro_data = om_intro.get_introduction(personality)

    return om_intro.format_introduction(intro_data, format_type)


def get_quick_greeting(personality: str = 'friendly') -> str:
    """Get a quick greeting from OM AI"""
    return om_intro.get_quick_intro(personality)


def get_feature_demo() -> str:
    """Get a random feature demonstration"""
    feature = om_intro.get_random_feature_highlight()
    return f"{feature['icon']} {feature['category']}: {feature['demo']}"


# Example usage functions
if __name__ == "__main__":
    # Test different introductions
    print("=== FRIENDLY INTRODUCTION ===")
    print(get_om_introduction('friendly', 'full'))

    print("\n=== PROFESSIONAL INTRODUCTION ===")
    print(get_om_introduction('professional', 'medium'))

    print("\n=== TECHNICAL INTRODUCTION ===")
    print(get_om_introduction('technical', 'full'))

    print("\n=== CREATIVE INTRODUCTION ===")
    print(get_om_introduction('creative', 'medium'))

    print("\n=== CONCISE INTRODUCTION ===")
    print(get_om_introduction('concise', 'quick'))

    print("\n=== CONTEXTUAL INTRODUCTION ===")
    context = {'first_time': True, 'developer': True}
    print(get_om_introduction(user_context=context))
