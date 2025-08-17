"""
Enhanced Command Handler with Google Search Integration
"""

import os
import sys
from pathlib import Path

# Add plugins directory to path
current_dir = Path(__file__).parent
plugins_dir = current_dir / "plugins"
sys.path.insert(0, str(plugins_dir))

try:
    from .plugins import (
        search_info, system_control, mouse_keyboard,
        screen_tools, file_ops, conversation, ai_tools
    )
    print("✅ Basic plugins imported successfully")
except ImportError as e:
    print(f"⚠️ Some basic plugins not available: {e}")
    # Create fallback modules

    class FallbackModule:
        def __getattr__(self, name):
            return lambda *args, **kwargs: f"Function {name} not available"

    search_info = FallbackModule()
    system_control = FallbackModule()
    mouse_keyboard = FallbackModule()
    screen_tools = FallbackModule()
    file_ops = FallbackModule()
    conversation = FallbackModule()
    ai_tools = FallbackModule()

try:
    from .plugins.network_manager import (
        check_internet, ping_website, get_network_info,
        get_network_speed, diagnose_network, connect_wifi, show_wifi_networks
    )
    print("✅ Network manager imported successfully")
except ImportError as e:
    print(f"⚠️ Network manager not available: {e}")
    # Create fallback functions
    def check_internet(): return "Internet check not available"
    def ping_website(url): return f"Ping to {url} not available"
    def get_network_info(): return "Network info not available"
    def get_network_speed(): return "Speed test not available"
    def diagnose_network(): return "Network diagnosis not available"
    def connect_wifi(ssid, password): return "WiFi connection not available"
    def show_wifi_networks(): return "WiFi networks not available"

try:
    from .plugins.livekit_network_manager import (
        get_livekit_status, get_livekit_room_info, get_livekit_network_stats,
        connect_livekit_room, disconnect_livekit_room
    )
    print("✅ LiveKit network manager imported successfully")
except ImportError as e:
    print(f"⚠️ LiveKit network manager not available: {e}")
    # Create fallback functions
    def get_livekit_status(): return "LiveKit status not available"
    def get_livekit_room_info(): return "LiveKit room info not available"
    def get_livekit_network_stats(): return "LiveKit network stats not available"
    def connect_livekit_room(
        room): return "LiveKit room connection not available"

    def disconnect_livekit_room(): return "LiveKit room disconnection not available"

try:
    from .plugins.database_manager import (
        om_db, save_conversation_to_db, get_user_conversation_history,
        add_to_knowledge_base, search_knowledge_base
    )
    print("✅ Database manager imported successfully")
except ImportError as e:
    print(f"⚠️ Database manager not available: {e}")
    # Create fallback functions
    om_db = None
    def save_conversation_to_db(*args): return "Database save not available"
    def get_user_conversation_history(
        *args): return "Conversation history not available"

    def add_to_knowledge_base(*args): return "Knowledge base add not available"

    def search_knowledge_base(
        *args): return "Knowledge base search not available"

# Import Daily Life Manager
try:
    from .plugins.daily_life_manager import (
        add_personal_task, get_daily_tasks, complete_task,
        add_habit, log_habit_completion, add_journal_entry,
        log_health_data, add_expense, get_expense_summary,
        control_smart_device, add_smart_device, log_learning_session,
        add_contact_reminder, get_contact_reminders, get_daily_summary
    )
    print("✅ Daily Life Manager imported successfully")
except ImportError as e:
    print(f"⚠️ Daily Life Manager not available: {e}")
    # Create fallback functions
    def add_personal_task(
        *args): return "Daily life task management not available"

    def get_daily_tasks(*args): return "Daily tasks not available"
    def complete_task(*args): return "Task completion not available"
    def add_habit(*args): return "Habit tracking not available"
    def log_habit_completion(*args): return "Habit logging not available"
    def add_journal_entry(*args): return "Journal entry not available"
    def log_health_data(*args): return "Health tracking not available"
    def add_expense(*args): return "Expense tracking not available"
    def get_expense_summary(*args): return "Expense summary not available"
    def control_smart_device(*args): return "Smart home control not available"
    def add_smart_device(*args): return "Smart device management not available"
    def log_learning_session(*args): return "Learning progress not available"
    def add_contact_reminder(*args): return "Contact management not available"
    def get_contact_reminders(*args): return "Contact reminders not available"
    def get_daily_summary(*args): return "Daily summary not available"

# Import Advanced Memory System
try:
    from .plugins.advanced_memory_system import (
        remember_conversation, recall_memory, get_user_context,
        schedule_task_from_conversation, get_personalized_response,
        get_pending_reminders, complete_scheduled_task, get_memory_stats
    )
    print("✅ Advanced Memory System imported successfully")
except ImportError as e:
    print(f"⚠️ Advanced Memory System not available: {e}")
    # Create fallback functions
    def remember_conversation(*args): return "Memory system not available"
    def recall_memory(*args): return "Memory recall not available"
    def get_user_context(*args): return "User context not available"

    def schedule_task_from_conversation(
        *args): return "Task scheduling not available"
    def get_personalized_response(
        *args, **kwargs): return args[1] if len(args) > 1 else "Response not available"

    def get_pending_reminders(*args): return "Reminders not available"
    def complete_scheduled_task(*args): return "Task completion not available"
    def get_memory_stats(*args): return "Memory stats not available"

# Import Task Scheduler System
try:
    from .plugins.task_scheduler_system import (
        start_scheduler, stop_scheduler, schedule_task, get_scheduled_tasks,
        complete_task as complete_scheduled_task_scheduler, snooze_task,
        get_task_history, get_scheduler_stats, register_notification_callback
    )
    print("✅ Task Scheduler System imported successfully")
except ImportError as e:
    print(f"⚠️ Task Scheduler System not available: {e}")
    # Create fallback functions
    def start_scheduler(): return "Task scheduler not available"
    def stop_scheduler(): return "Task scheduler not available"
    def schedule_task(*args): return "Task scheduling not available"
    def get_scheduled_tasks(*args): return "Scheduled tasks not available"
    def complete_scheduled_task_scheduler(
        *args): return "Task completion not available"

    def snooze_task(*args): return "Task snoozing not available"
    def get_task_history(*args): return "Task history not available"
    def get_scheduler_stats(): return "Scheduler stats not available"
    def register_notification_callback(
        *args): return "Notification callback not available"


def handle_command(intent, params):
    """
    Handle various commands including enhanced Google search

    Args:
        intent (str): Command intent
        params (dict): Command parameters

    Returns:
        str: Command result
    """

    # API-based Search Commands
    if intent == "google_search":
        query = params.get("query", "")
        return search_info.search_web(query)

    elif intent == "openai_explain":
        query = params.get("query", "")
        return search_info.openai_explain(query)

    elif intent == "detailed_search":
        query = params.get("query", "")
        return search_info.search_detailed(query)

    elif intent == "image_search":
        query = params.get("query", "")
        return search_info.search_images(query)

    elif intent == "video_search":
        query = params.get("query", "")
        return search_info.search_videos(query)

    elif intent == "lucky_search":
        query = params.get("query", "")
        return search_info.lucky_search(query)

    elif intent == "open_website":
        url = params.get("url", "")
        return search_info.open_website(url)

    # Weather and Info
    elif intent == "get_weather":
        city = params.get("city", "Delhi")
        return search_info.get_weather(city)

    # System Commands
    elif intent == "open_app":
        app = params.get("app", "")
        return system_control.open_app(app)

    elif intent == "take_screenshot":
        return screen_tools.take_screenshot()

    # File Operations
    elif intent == "open_file":
        path = params.get("path", "")
        return file_ops.open_file(path)

    # AI and Conversation
    elif intent == "motivate":
        return conversation.motivate()

    elif intent == "chat_ai":
        message = params.get("message", "")
        return conversation.chat_response(message)

    elif intent == "greeting":
        message = params.get("message", "")
        return conversation.get_ai_response(message)

    elif intent == "get_time":
        import datetime
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"The current time is {current_time} on {current_date}."

    elif intent == "get_date":
        import datetime
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {current_date}."

    elif intent == "how_are_you":
        return conversation.get_ai_response("how are you")

    elif intent == "thank_you":
        return conversation.get_ai_response("thank you")

    elif intent == "introduction":
        try:
            import sys
            sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
            from language_handler import language_handler
            return language_handler.get_mixed_introduction()
        except ImportError:
            return """🕉️ नमस्कार! Hello! मैं OM हूँ, Pradeep का spiritual creation। 

🕉️ I'm your spiritual AI assistant जो आपकी help करने के लिए designed है।

🎯 My capabilities:
• Voice commands - Hindi, English, Hinglish सब languages
• Google search - कुछ भी find कर सकता हूँ online
• Network management - Internet connectivity check करता हूँ
• Smart conversation - आपसे naturally बात करता हूँ

🗣️ Language: मैं automatically detect करता हूँ आपकी language preference और accordingly respond करता हूँ!

Ready to help with divine wisdom! आपकी क्या service कर सकता हूँ?"""

    if intent == "show_capabilities":
        return conversation.get_ai_response("what can you do")

    # Network Commands
    elif intent == "check_internet":
        return check_internet()

    elif intent == "ping_website":
        host = params.get("host", "google.com")
        return ping_website(host)

    elif intent == "network_info":
        return get_network_info()

    elif intent == "network_speed":
        return get_network_speed()

    elif intent == "diagnose_network":
        return diagnose_network()

    elif intent == "connect_wifi":
        ssid = params.get("ssid", "")
        return connect_wifi(ssid)

    elif intent == "show_wifi":
        return show_wifi_networks()

    # LiveKit Commands
    elif intent == "livekit_status":
        return get_livekit_status()

    elif intent == "livekit_room_info":
        return get_livekit_room_info()

    elif intent == "livekit_stats":
        return get_livekit_network_stats()

    elif intent == "connect_room":
        room_name = params.get("room", "jarvis-room")
        participant = params.get("participant", "Jarvis")
        # Note: This is async, need to handle properly
        return f"🔄 Connecting to room '{room_name}' as '{participant}'..."

    elif intent == "disconnect_room":
        # Note: This is async, need to handle properly
        return "🔄 Disconnecting from room..."

    # Database Commands
    elif intent == "get_conversation_history":
        try:
            history = get_user_conversation_history(limit=5)
            if history:
                result = "📚 **Recent Conversation History:**\n\n"
                for i, conv in enumerate(history, 1):
                    result += f"**{i}.** {conv['query'][:50]}...\n"
                    result += f"   Response: {conv['response'][:100]}...\n"
                    result += f"   Time: {conv['timestamp']}\n\n"
                return result
            else:
                return "📚 No conversation history found."
        except Exception as e:
            return f"❌ Error retrieving conversation history: {e}"

    elif intent == "get_database_stats":
        try:
            stats = om_db.get_database_stats()
            result = "📊 **Database Statistics:**\n\n"
            result += f"👥 Total Users: {stats.get('total_users', 0)}\n"
            result += f"💬 Total Conversations: {stats.get('total_conversations', 0)}\n"
            result += f"📚 Knowledge Entries: {stats.get('knowledge_entries', 0)}\n"
            result += f"🔍 Search Queries: {stats.get('search_queries', 0)}\n"
            result += f"💾 Database Size: {stats.get('database_size', 0)} bytes\n"
            return result
        except Exception as e:
            return f"❌ Error retrieving database stats: {e}"

    elif intent == "add_knowledge":
        try:
            content = params.get("content", "")
            if content:
                # Simple parsing - first sentence as topic, rest as content
                sentences = content.split('.')
                topic = sentences[0].strip() if sentences else content[:50]
                full_content = content

                add_to_knowledge_base(topic, full_content, "user_added")
                return f"✅ Knowledge added to database: {topic}"
            else:
                return "❌ Please provide content to add to knowledge base."
        except Exception as e:
            return f"❌ Error adding knowledge: {e}"

    elif intent == "search_knowledge":
        try:
            query = params.get("query", "")
            if query:
                results = search_knowledge_base(query)
                if results:
                    result = f"🔍 **Knowledge Search Results for '{query}':**\n\n"
                    for i, item in enumerate(results, 1):
                        result += f"**{i}. {item['topic']}**\n"
                        result += f"{item['content'][:200]}...\n"
                        if item['category']:
                            result += f"Category: {item['category']}\n"
                        result += "\n"
                    return result
                else:
                    return f"🔍 No knowledge found for '{query}'"
            else:
                return "❌ Please provide a search query."
        except Exception as e:
            return f"❌ Error searching knowledge: {e}"

    # Daily Life Management Commands
    elif intent == "add_task":
        try:
            title = params.get("title", "")
            description = params.get("description", "")
            priority = params.get("priority", "medium")
            category = params.get("category", "general")
            due_date = params.get("due_date", None)
            result = add_personal_task(
                title, description, priority, category, due_date)
            return f"✅ **Task Added Successfully!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error adding task: {e}"

    elif intent == "get_tasks":
        try:
            date = params.get("date", None)
            result = get_daily_tasks(date)
            return f"📋 **Today's Tasks**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error getting tasks: {e}"

    elif intent == "complete_task":
        try:
            task_id = params.get("task_id", 0)
            result = complete_task(task_id)
            return f"🎉 **Task Completed!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error completing task: {e}"

    elif intent == "add_habit":
        try:
            habit_name = params.get("habit_name", "")
            description = params.get("description", "")
            frequency = params.get("frequency", "daily")
            result = add_habit(habit_name, description, frequency)
            return f"🔥 **Habit Added!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error adding habit: {e}"

    elif intent == "log_habit":
        try:
            habit_name = params.get("habit_name", "")
            result = log_habit_completion(habit_name)
            return f"🔥 **Habit Logged!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error logging habit: {e}"

    elif intent == "add_journal":
        try:
            mood_rating = params.get("mood_rating", 5)
            gratitude = params.get("gratitude", "")
            highlights = params.get("highlights", "")
            challenges = params.get("challenges", "")
            tomorrow_goals = params.get("tomorrow_goals", "")
            result = add_journal_entry(
                mood_rating, gratitude, highlights, challenges, tomorrow_goals)
            return f"📝 **Journal Entry Added!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error adding journal entry: {e}"

    elif intent == "log_health":
        try:
            health_data = {
                'weight': params.get('weight'),
                'steps': params.get('steps'),
                'water_intake': params.get('water_intake'),
                'sleep_hours': params.get('sleep_hours'),
                'exercise_minutes': params.get('exercise_minutes'),
                'calories': params.get('calories'),
                'mood_score': params.get('mood_score'),
                'energy_level': params.get('energy_level')
            }
            result = log_health_data(**health_data)
            return f"💪 **Health Data Logged!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error logging health data: {e}"

    elif intent == "add_expense":
        try:
            amount = params.get("amount", 0)
            category = params.get("category", "other")
            description = params.get("description", "")
            payment_method = params.get("payment_method", "cash")
            is_recurring = params.get("is_recurring", False)
            result = add_expense(amount, category, description,
                                 payment_method, is_recurring)
            return f"💰 **Expense Added!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error adding expense: {e}"

    elif intent == "expense_summary":
        try:
            period = params.get("period", "month")
            result = get_expense_summary(period)
            return f"📊 **Expense Summary**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error getting expense summary: {e}"

    elif intent == "control_device":
        try:
            device_name = params.get("device_name", "")
            action = params.get("action", "toggle")
            value = params.get("value", None)
            result = control_smart_device(device_name, action, value)
            return f"🏠 **Smart Device Controlled!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error controlling device: {e}"

    elif intent == "add_device":
        try:
            device_name = params.get("device_name", "")
            device_type = params.get("device_type", "light")
            location = params.get("location", "home")
            result = add_smart_device(device_name, device_type, location)
            return f"🏠 **Smart Device Added!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error adding device: {e}"

    elif intent == "log_learning":
        try:
            skill_name = params.get("skill_name", "")
            source = params.get("source", "")
            time_spent = params.get("time_spent", 0)
            progress = params.get("progress", None)
            notes = params.get("notes", "")
            result = log_learning_session(
                skill_name, source, time_spent, progress, notes)
            return f"📚 **Learning Session Logged!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error logging learning: {e}"

    elif intent == "add_contact":
        try:
            contact_name = params.get("contact_name", "")
            relationship = params.get("relationship", "friend")
            frequency = params.get("frequency", "monthly")
            birthday = params.get("birthday", None)
            result = add_contact_reminder(
                contact_name, relationship, frequency, birthday)
            return f"👥 **Contact Added!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error adding contact: {e}"

    elif intent == "contact_reminders":
        try:
            result = get_contact_reminders()
            return f"👥 **Contact Reminders**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error getting contact reminders: {e}"

    elif intent == "daily_summary":
        try:
            date = params.get("date", None)
            result = get_daily_summary(date)
            return f"📊 **Daily Summary**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error getting daily summary: {e}"

    # Advanced Memory System Commands
    elif intent == "remember_this":
        try:
            user_input = params.get("user_input", "")
            ai_response = params.get("ai_response", "")
            intent_type = params.get("intent_type", "")
            context = params.get("context", {})
            user_id = params.get("user_id", "default_user")
            result = remember_conversation(
                user_input, ai_response, intent_type, context, user_id)
            return f"🧠 **Memory Stored Successfully!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error storing memory: {e}"

    elif intent == "recall_memory":
        try:
            query = params.get("query", "")
            user_id = params.get("user_id", "default_user")
            memory_type = params.get("memory_type", "all")
            limit = params.get("limit", 10)
            result = recall_memory(query, user_id, memory_type, limit)
            return f"🔍 **Memory Recall Results**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error recalling memory: {e}"

    elif intent == "get_context":
        try:
            user_id = params.get("user_id", "default_user")
            result = get_user_context(user_id)
            return f"👤 **User Context**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error getting user context: {e}"

    elif intent == "schedule_from_conversation":
        try:
            task_title = params.get("task_title", "")
            task_description = params.get("task_description", "")
            scheduled_time = params.get("scheduled_time", "")
            conversation_context = params.get("conversation_context", "")
            user_id = params.get("user_id", "default_user")
            priority = params.get("priority", 3)
            result = schedule_task_from_conversation(
                task_title, task_description, scheduled_time, conversation_context, user_id, priority)
            return f"📅 **Task Scheduled from Conversation!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error scheduling task from conversation: {e}"

    elif intent == "get_reminders":
        try:
            user_id = params.get("user_id", "default_user")
            result = get_pending_reminders(user_id)
            return f"🔔 **Pending Reminders**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error getting reminders: {e}"

    elif intent == "memory_stats":
        try:
            user_id = params.get("user_id", "default_user")
            result = get_memory_stats(user_id)
            return f"📊 **Memory System Statistics**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error getting memory stats: {e}"

    # Task Scheduler System Commands
    elif intent == "start_scheduler":
        try:
            result = start_scheduler()
            return f"🚀 **Task Scheduler Started!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error starting scheduler: {e}"

    elif intent == "stop_scheduler":
        try:
            result = stop_scheduler()
            return f"⏹️ **Task Scheduler Stopped!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error stopping scheduler: {e}"

    elif intent == "schedule_advanced_task":
        try:
            task_name = params.get("task_name", "")
            task_description = params.get("task_description", "")
            scheduled_time = params.get("scheduled_time", "")
            task_type = params.get("task_type", "reminder")
            priority = params.get("priority", 3)
            auto_execute = params.get("auto_execute", False)
            execution_command = params.get("execution_command", "")
            repeat_pattern = params.get("repeat_pattern", "")
            reminder_intervals = params.get("reminder_intervals", None)
            user_id = params.get("user_id", "default_user")

            result = schedule_task(task_name, task_description, scheduled_time, task_type,
                                   priority, auto_execute, execution_command, repeat_pattern,
                                   reminder_intervals, user_id)
            return f"📅 **Advanced Task Scheduled!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error scheduling advanced task: {e}"

    elif intent == "get_scheduled_tasks":
        try:
            user_id = params.get("user_id", "default_user")
            status = params.get("status", "all")
            result = get_scheduled_tasks(user_id, status)
            return f"📋 **Scheduled Tasks**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error getting scheduled tasks: {e}"

    elif intent == "complete_scheduled_task":
        try:
            task_id = params.get("task_id", 0)
            user_id = params.get("user_id", "default_user")
            completion_notes = params.get("completion_notes", "")
            result = complete_scheduled_task_scheduler(
                task_id, user_id, completion_notes)
            return f"✅ **Scheduled Task Completed!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error completing scheduled task: {e}"

    elif intent == "snooze_task":
        try:
            task_id = params.get("task_id", 0)
            snooze_minutes = params.get("snooze_minutes", 15)
            user_id = params.get("user_id", "default_user")
            result = snooze_task(task_id, snooze_minutes, user_id)
            return f"😴 **Task Snoozed!**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error snoozing task: {e}"

    elif intent == "task_history":
        try:
            task_id = params.get("task_id", 0)
            result = get_task_history(task_id)
            return f"📜 **Task History**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error getting task history: {e}"

    elif intent == "scheduler_stats":
        try:
            result = get_scheduler_stats()
            return f"📊 **Scheduler Statistics**\n\n{json.dumps(result, indent=2)}"
        except Exception as e:
            return f"❌ Error getting scheduler stats: {e}"

    else:
        return f"""Command '{intent}' not recognized. 

🔥 **Available Commands:**

**📋 Daily Life Management:**
• add_task - Add personal tasks with reminders
• get_tasks - Get today's tasks with smart prioritization
• complete_task - Mark tasks as completed with celebration
• add_habit - Add habits to track with streak counting
• log_habit - Log habit completion with motivational messages
• add_journal - Daily journal with mood tracking
• log_health - Comprehensive health and fitness tracking
• add_expense - Smart expense tracking with insights
• expense_summary - Detailed expense analysis and reports
• control_device - Smart home device control
• add_device - Add new smart home devices
• log_learning - Track learning progress and milestones
• add_contact - Social connection management
• contact_reminders - Get reminders to stay in touch
• daily_summary - Comprehensive daily life summary

**🎯 Basic Commands:**
google_search, detailed_search, image_search, video_search, lucky_search, open_website, get_weather, open_app, take_screenshot, open_file, motivate, chat_ai, check_internet, ping_website, network_info, network_speed, diagnose_network, connect_wifi, show_wifi, livekit_status, livekit_room_info, livekit_stats, connect_room, disconnect_room, get_conversation_history, get_database_stats, add_knowledge, search_knowledge"""


# Command mapping for voice recognition
VOICE_COMMANDS = {
    # Search commands
    "google search": "google_search",
    "search google": "google_search",
    "web search": "google_search",
    "search web": "google_search",
    "detailed search": "detailed_search",
    "search detailed": "detailed_search",

    "image search": "image_search",
    "search images": "image_search",
    "video search": "video_search",
    "search videos": "video_search",
    "lucky search": "lucky_search",
    "feeling lucky": "lucky_search",
    "open website": "open_website",

    # Weather and info
    "weather": "get_weather",
    "get weather": "get_weather",
    "mausam": "get_weather",

    # System commands
    "open app": "open_app",
    "screenshot": "take_screenshot",
    "take screenshot": "take_screenshot",
    "open file": "open_file",

    # AI commands
    "motivate": "motivate",
    "motivation": "motivate",
    "chat": "chat_ai",
    "ai chat": "chat_ai",

    # Network commands
    "check internet": "check_internet",
    "internet status": "check_internet",
    "internet check": "check_internet",
    "ping": "ping_website",
    "ping website": "ping_website",
    "network info": "network_info",
    "network information": "network_info",
    "network speed": "network_speed",
    "internet speed": "network_speed",
    "diagnose network": "diagnose_network",
    "network diagnosis": "diagnose_network",
    "connect wifi": "connect_wifi",
    "wifi connect": "connect_wifi",
    "show wifi": "show_wifi",
    "wifi networks": "show_wifi",
    "wifi list": "show_wifi",

    # LiveKit commands
    "livekit status": "livekit_status",
    "livekit room info": "livekit_room_info",
    "livekit stats": "livekit_stats",
    "room info": "livekit_room_info",
    "room stats": "livekit_stats",
    "connect room": "connect_room",
    "join room": "connect_room",
    "disconnect room": "disconnect_room",
    "leave room": "disconnect_room"
}
