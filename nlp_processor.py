"""
Enhanced NLP Processor for Jarvis AI
Processes natural language commands and maps them to appropriate intents
"""


def process_command(query):
    """
    Process natural language query and return intent with parameters

    Args:
        query (str): User's natural language query

    Returns:
        tuple: (intent, parameters)
    """
    q = query.lower().strip()

    # Network Commands (Hindi + English)
    if any(word in q for word in ["internet", "connection", "connectivity", "इंटरनेट", "नेटवर्क", "कनेक्शन"]):
        if any(word in q for word in ["check", "status", "चेक", "स्टेटस", "देखो", "बताओ"]):
            return "check_internet", {}

    if "ping" in q:
        # Extract host from query
        words = q.split()
        host = "google.com"  # default
        if len(words) > 1:
            # Look for domain-like word
            for word in words:
                if "." in word and not word.startswith("."):
                    host = word
                    break
        return "ping_website", {"host": host}

    if any(phrase in q for phrase in ["network info", "network information"]):
        return "network_info", {}

    if any(phrase in q for phrase in ["network speed", "internet speed"]):
        return "network_speed", {}  # Basic speed monitoring

    if "diagnose network" in q or "network diagnosis" in q:
        return "diagnose_network", {}

    # LiveKit Commands
    if "livekit" in q:
        if "status" in q:
            return "livekit_status", {}
        elif "room info" in q or "room information" in q:
            return "livekit_room_info", {}
        elif "stats" in q or "statistics" in q:
            return "livekit_stats", {}

    if "room" in q:
        if "connect" in q or "join" in q:
            # Extract room name
            words = q.split()
            room_name = "jarvis-room"  # default
            participant = "Jarvis"  # default

            if "room" in words:
                idx = words.index("room")
                if idx + 1 < len(words):
                    room_name = words[idx + 1]

            return "connect_room", {"room": room_name, "participant": participant}

        elif "disconnect" in q or "leave" in q:
            return "disconnect_room", {}

        elif "info" in q or "information" in q:
            return "livekit_room_info", {}

        elif "stats" in q or "statistics" in q:
            return "livekit_stats", {}

    if "wifi" in q:
        if "connect" in q:
            # Extract network name
            words = q.split()
            ssid = ""
            if "connect" in words:
                idx = words.index("connect")
                if idx + 1 < len(words):
                    ssid = " ".join(words[idx+1:])
            return "connect_wifi", {"ssid": ssid}
        elif "show" in q or "list" in q or "networks" in q:
            return "show_wifi", {}

    # OpenAI Commands - Direct AI requests
    openai_patterns = [
        "openai", "open ai", "ai explain", "ai answer", "ask ai", "ai help",
        "artificial intelligence explain", "use ai", "ai response"
    ]

    # Google Search Commands - Direct search requests
    google_search_patterns = [
        "google search", "search google", "search for", "find", "look up", "web search", "internet search"
    ]

    # Check for OpenAI requests first
    if any(pattern in q for pattern in openai_patterns):
        query_text = q
        # Remove AI keywords
        for keyword in ["openai", "open ai", "ai explain", "ai answer", "ask ai", "ai help", "use ai", "ai response", "artificial intelligence explain"]:
            query_text = query_text.replace(keyword, "").strip()

        if len(query_text) < 2:
            query_text = q

        return "openai_explain", {"query": query_text}

    # Check for Google search requests
    elif any(pattern in q for pattern in google_search_patterns):
        query_text = q
        # Remove search keywords
        for keyword in ["google search", "search google", "search for", "find", "look up", "web search", "internet search", "google"]:
            query_text = query_text.replace(keyword, "").strip()

        if len(query_text) < 2:
            query_text = q

        return "google_search", {"query": query_text}

    # Academic/Knowledge queries - Hindi + English patterns
    hindi_question_patterns = [
        "kya hai", "kya hota hai", "kya hoti hai", "kya he", "kya hain",
        "kaise", "kaise karte hain", "kaise karte hai", "kaise hota hai",
        "kyun", "kyun hota hai", "kyu", "kyu hota hai",
        "kahan", "kahan hai", "kahan hota hai", "kahan milta hai",
        "kaun", "kaun hai", "kaun hota hai", "kaun sa",
        "kab", "kab hota hai", "kab hai",
        "kitna", "kitne", "kitni",
        "matlab kya hai", "arth kya hai", "meaning kya hai",
        "samjhao", "batao", "bataiye", "explain karo"
    ]

    english_question_patterns = [
        "what is", "what are", "define", "explain", "meaning of", "definition of",
        "how to", "how does", "why is", "why does", "when is", "when does",
        "where is", "where does", "who is", "who was", "which is"
    ]

    all_question_patterns = hindi_question_patterns + english_question_patterns

    if any(pattern in q for pattern in all_question_patterns):
        return "google_search", {"query": q}

    elif "image search" in q or "search image" in q:
        query_text = q.replace("image", "").replace("search", "").strip()
        return "image_search", {"query": query_text}

    elif "video search" in q or "search video" in q:
        query_text = q.replace("video", "").replace("search", "").strip()
        return "video_search", {"query": query_text}

    elif "lucky search" in q or "feeling lucky" in q:
        query_text = q.replace("lucky", "").replace(
            "search", "").replace("feeling", "").strip()
        return "lucky_search", {"query": query_text}

    elif "open website" in q:
        url = q.replace("open", "").replace("website", "").strip()
        return "open_website", {"url": url}

    # Weather Commands
    elif "weather" in q or "mausam" in q:
        # Extract city name
        words = q.split()
        city = "Delhi"  # default
        for word in words:
            if word not in ["weather", "mausam", "in", "of", "get", "show"]:
                city = word.title()
                break
        return "get_weather", {"city": city}

    # System Commands
    elif "open" in q and "app" in q:
        app_name = q.replace("open", "").replace("app", "").strip()
        return "open_app", {"app": app_name}

    elif "screenshot" in q:
        return "take_screenshot", {}

    elif "open file" in q:
        path = q.replace("open", "").replace("file", "").strip()
        if not path:
            path = "Documents"
        return "open_file", {"path": path}

    # AI and Conversation
    elif "motivate" in q or "motivation" in q:
        return "motivate", {}

    # Greetings and basic conversation (Hindi + English)
    elif any(word in q for word in ['hello', 'hi', 'hey', 'namaste', 'om', 'ॐ']):
        return "greeting", {"message": query}

    # Time queries (Hindi + English)
    elif any(word in q for word in ['time', 'samay', 'clock', 'what time']):
        return "get_time", {}

    # Date queries
    elif any(word in q for word in ['date', 'today', 'tarikh', 'what date']):
        return "get_date", {}

    # How are you
    elif any(phrase in q for phrase in ['how are you', 'kaise ho', 'kaisa hai']):
        return "how_are_you", {}

    # Thank you
    elif any(word in q for word in ['thank', 'thanks', 'dhanyawad']):
        return "thank_you", {}

    # Introduction
    elif any(phrase in q for phrase in ['introduce yourself', 'introduction', 'who are you', 'tell me about yourself']):
        return "introduction", {}

    # Capabilities
    elif any(phrase in q for phrase in ['what can you do', 'capabilities', 'help me']):
        return "show_capabilities", {}

    # Database Commands
    elif any(phrase in q for phrase in ['conversation history', 'chat history', 'previous conversations']):
        return "get_conversation_history", {}

    elif any(phrase in q for phrase in ['database stats', 'db stats', 'database status']):
        return "get_database_stats", {}

    elif "add knowledge" in q or "save knowledge" in q:
        # Extract topic and content
        content = q.replace("add knowledge", "").replace(
            "save knowledge", "").strip()
        return "add_knowledge", {"content": content}

    elif "search knowledge" in q or "find knowledge" in q:
        query_text = q.replace("search knowledge", "").replace(
            "find knowledge", "").strip()
        return "search_knowledge", {"query": query_text}

    # Daily Life Management Commands
    elif any(phrase in q for phrase in ['add task', 'create task', 'new task', 'task add karo', 'task banao']):
        return "add_task", {"title": q.replace('add task', '').replace('create task', '').replace('new task', '').replace('task add karo', '').replace('task banao', '').strip()}

    elif any(phrase in q for phrase in ['show tasks', 'get tasks', 'today tasks', 'aaj ke tasks', 'tasks dikhao']):
        return "get_tasks", {}

    elif any(phrase in q for phrase in ['complete task', 'task complete', 'task done', 'task khatam', 'task complete karo']):
        return "complete_task", {"task_id": 1}  # Would need task ID extraction

    elif any(phrase in q for phrase in ['add habit', 'new habit', 'habit add karo', 'habit banao', 'create habit']):
        habit_name = q.replace('add habit', '').replace('new habit', '').replace(
            'habit add karo', '').replace('habit banao', '').replace('create habit', '').strip()
        return "add_habit", {"habit_name": habit_name}

    elif any(phrase in q for phrase in ['log habit', 'habit done', 'habit complete', 'habit kiya', 'habit log karo']):
        habit_name = q.replace('log habit', '').replace('habit done', '').replace(
            'habit complete', '').replace('habit kiya', '').replace('habit log karo', '').strip()
        return "log_habit", {"habit_name": habit_name}

    elif any(phrase in q for phrase in ['journal entry', 'write journal', 'diary entry', 'journal likhna', 'diary likhna']):
        return "add_journal", {"mood_rating": 5}

    elif any(phrase in q for phrase in ['log health', 'health data', 'fitness log', 'health track', 'sehat ka data']):
        return "log_health", {}

    elif any(phrase in q for phrase in ['add expense', 'expense add', 'kharcha add', 'expense log', 'money spent']):
        return "add_expense", {"amount": 100, "category": "general"}

    elif any(phrase in q for phrase in ['expense summary', 'expense report', 'kharcha report', 'spending summary']):
        return "expense_summary", {"period": "month"}

    elif any(phrase in q for phrase in ['control device', 'smart home', 'device control', 'light on', 'light off', 'ac on', 'ac off']):
        device_name = "light"
        action = "on"
        if "light" in q:
            device_name = "light"
        elif "ac" in q or "air conditioner" in q:
            device_name = "ac"
        elif "fan" in q:
            device_name = "fan"
        elif "tv" in q:
            device_name = "tv"

        if "off" in q:
            action = "off"
        elif "on" in q:
            action = "on"

        return "control_device", {"device_name": device_name, "action": action}

    elif any(phrase in q for phrase in ['add device', 'new device', 'device add karo', 'smart device add']):
        return "add_device", {"device_name": "new device", "device_type": "light", "location": "home"}

    elif any(phrase in q for phrase in ['log learning', 'study session', 'learning log', 'padhai log', 'study time']):
        return "log_learning", {"skill_name": "general", "source": "self-study", "time_spent": 30}

    elif any(phrase in q for phrase in ['add contact', 'new contact', 'contact add karo', 'friend add']):
        return "add_contact", {"contact_name": "friend", "relationship": "friend"}

    elif any(phrase in q for phrase in ['contact reminders', 'who to call', 'social reminders', 'contact karna hai']):
        return "contact_reminders", {}

    elif any(phrase in q for phrase in ['daily summary', 'today summary', 'aaj ka summary', 'day report']):
        return "daily_summary", {}

    # Advanced Memory System Commands
    elif any(phrase in q for phrase in ['remember this', 'yaad rakhna', 'memory mein store karo', 'remember that']):
        return "remember_this", {"user_input": q, "ai_response": "", "intent_type": "user_request"}

    elif any(phrase in q for phrase in ['recall memory', 'yaad hai kya', 'memory search', 'find in memory', 'kya bola tha']):
        query = q.replace('recall memory', '').replace('yaad hai kya', '').replace(
            'memory search', '').replace('find in memory', '').replace('kya bola tha', '').strip()
        return "recall_memory", {"query": query}

    elif any(phrase in q for phrase in ['my context', 'user context', 'mera context', 'about me']):
        return "get_context", {}

    elif any(phrase in q for phrase in ['schedule this', 'task banao from conversation', 'conversation se task', 'yaad rakhke karna hai']):
        return "schedule_from_conversation", {"task_title": "Task from conversation", "task_description": q, "scheduled_time": "tomorrow"}

    elif any(phrase in q for phrase in ['pending reminders', 'reminders dikhao', 'kya yaad dilana hai', 'upcoming tasks']):
        return "get_reminders", {}

    elif any(phrase in q for phrase in ['memory stats', 'memory statistics', 'memory ka status', 'kitna yaad hai']):
        return "memory_stats", {}

    # Task Scheduler System Commands
    elif any(phrase in q for phrase in ['start scheduler', 'scheduler start karo', 'task scheduler on', 'automatic tasks start']):
        return "start_scheduler", {}

    elif any(phrase in q for phrase in ['stop scheduler', 'scheduler stop karo', 'task scheduler off', 'automatic tasks stop']):
        return "stop_scheduler", {}

    elif any(phrase in q for phrase in ['schedule advanced task', 'advanced task banao', 'automatic task schedule', 'recurring task']):
        return "schedule_advanced_task", {"task_name": "Advanced Task", "task_description": q, "scheduled_time": "tomorrow"}

    elif any(phrase in q for phrase in ['scheduled tasks', 'scheduled tasks dikhao', 'kya tasks scheduled hain', 'upcoming scheduled tasks']):
        return "get_scheduled_tasks", {}

    elif any(phrase in q for phrase in ['complete scheduled task', 'scheduled task complete', 'automatic task done']):
        return "complete_scheduled_task", {"task_id": 1}

    elif any(phrase in q for phrase in ['snooze task', 'task snooze karo', 'thoda der baad yaad dilana', 'postpone task']):
        return "snooze_task", {"task_id": 1, "snooze_minutes": 15}

    elif any(phrase in q for phrase in ['task history', 'task ka history', 'task execution history', 'task logs']):
        return "task_history", {"task_id": 1}

    elif any(phrase in q for phrase in ['scheduler stats', 'scheduler statistics', 'scheduler ka status', 'task scheduler info']):
        return "scheduler_stats", {}

    # Default to enhanced AI chat
    else:
        return "chat_ai", {"message": query}
