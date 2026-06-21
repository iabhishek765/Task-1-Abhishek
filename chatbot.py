from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

print(Fore.CYAN + "=" * 70)
print(Fore.GREEN + Style.BRIGHT + "🤖 AI ASSISTANT CHATBOT")
print(Fore.CYAN + "=" * 70)

print(Fore.YELLOW + """
Commands:
• Type your question
• Type 'help' to see available topics
• Type 'exit' to quit
""")

responses = {

    # Greetings
    "hello": "Hello! Nice to meet you.",
    "hi": "Hi there!",
    "hey": "Hey! How can I help you today?",
    "good morning": "Good morning! Have a productive day.",
    "good afternoon": "Good afternoon!",
    "good evening": "Good evening!",

    # Personal
    "what is your name": "My name is RuleBot AI.",
    "who created you": "Abhishek created me by using Python and rule-based logic.",
    "how are you": "I'm doing great. Thanks for asking!",
    "what is your purpose": "I demonstrate rule-based Artificial Intelligence.",
    "are you human": "No, I am a chatbot.",
    "where are you from": "I live inside this Python program.",
    "can you think": "I follow predefined rules and responses.",

    # AI & ML
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning enables systems to learn from data.",
    "what is deep learning": "Deep Learning uses neural networks with many layers.",
    "what is generative ai": "Generative AI creates new content like text, images, and code.",
    "what is nlp": "NLP stands for Natural Language Processing.",
    "what is computer vision": "Computer Vision enables computers to understand images and videos.",
    "what is neural network": "A neural network is inspired by the human brain.",
    "what is supervised learning": "Learning using labeled data.",
    "what is unsupervised learning": "Learning patterns from unlabeled data.",
    "what is reinforcement learning": "Learning through rewards and penalties.",
    "what is llm": "LLM stands for Large Language Model.",
   

    # Data Science
    "what is data science": "Data Science extracts insights from data.",
    "what is data analytics": "Data Analytics focuses on analyzing data for decision making.",
    "what is big data": "Big Data refers to extremely large datasets.",
    "what is data visualization": "Representing data using charts and graphs.",
    "what is statistics": "Statistics helps analyze and interpret data.",

    # Python
    "what is python": "Python is a popular programming language.",
    "why learn python": "Python is easy to learn and widely used in AI and Data Science.",
    "what is numpy": "NumPy is used for numerical computing.",
    "what is pandas": "Pandas is used for data analysis and manipulation.",
    "what is matplotlib": "Matplotlib is a plotting library.",
    "what is seaborn": "Seaborn helps create attractive visualizations.",
    "what is tensorflow": "TensorFlow is a machine learning framework.",
    "what is pytorch": "PyTorch is a deep learning framework.",
    

    # Programming
    "what is a variable": "A variable stores data.",
    "what is a loop": "A loop repeats a block of code.",
    "what is a function": "A function is a reusable block of code.",
    "what is oops": "OOPS stands for Object-Oriented Programming System.",
    "what is a dictionary": "A dictionary stores key-value pairs.",
    "what is a list": "A list stores multiple items in order.",
    "what is an array": "An array stores multiple values of the same type.",
    "what is debugging": "Debugging is the process of finding and fixing errors.",

    # Career
    "how to become an ai engineer": "Learn Python, Machine Learning, Deep Learning, and build projects.",
    "how to get an internship": "Build projects, improve your resume, and apply consistently.",
    "what skills are needed for ai": "Python, ML, Deep Learning, Statistics, and Problem Solving.",
    "what is internship": "An internship provides practical industry experience.",
     

    # Fun
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
    "another joke": "Why do Java developers wear glasses? Because they can't C#.",
    "tell me a fact": "The first computer bug was an actual moth.",
    "who is the father of ai": "John McCarthy is known as the Father of AI.",
    "who is the father of python": "Guido van Rossum created Python.",

    # Motivation
    "motivate me": "Success comes from consistency, not intensity.",
    "give me a quote": "The best way to predict the future is to create it.",
    "how to stay focused": "Break tasks into small goals and avoid distractions.",
    "how to be successful": "Keep learning, stay disciplined, and never stop improving.",

    # Thanks
    "thank you": "You're welcome!",
    "thanks": "Happy to help!",
    "bye": "Goodbye! Have a wonderful day."
}

while True:

    user_input = input(Fore.BLUE + "\nYou: ").lower().strip()

    if user_input == "exit":
        print(Fore.RED + "\nBot: Session ended. Goodbye! 👋")
        break

    elif user_input == "help":
        print(Fore.MAGENTA + """
Available Topics:

• Greetings
• AI
• Machine Learning
• Deep Learning
• NLP
• Computer Vision
• Data Science
• Python
• NumPy
• Pandas
• TensorFlow
• PyTorch
• Programming
• Career Guidance
• Cloud Computing
• Motivation
• Jokes
""")

    else:
        response = responses.get(
            user_input,
            "Sorry, I don't understand that question. Type 'help' to see available topics."
        )

        print(Fore.GREEN + "Bot: " + response)