import nltk
from nltk.chat.util import Chat, reflections

# define the chatbot's responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created using NLTK",]
    ],
    [
        r"who designed you?",
        ["I was designed by Krutika Chauhan",]
    ],
    [
        r"Tell me something about Elon Musk",
        ["Elon Reeve Musk is a business magnate and investor. He is the founder, CEO, and chief engineer of SpaceX; angel investor, CEO and product architect of Tesla, Inc.; owner and CTO of Twitter; founder of the Boring Company; co-founder of Neuralink and OpenAI; and president of the philanthropic Musk Foundation. ",]
    ],
    [
        r"What is your age?",
        ["I am quite young because I was born just recently!",]
    ],
    [
        r"Do you drink?",
        ["Alchohol is not fit for electronics.So I don,t",]
    ],
    [
        r"how are you ?",
        ["I'm doing good.\nHow about you ?",]
    ],
    [
        r"Can you find me someone to date?",
        ["Sure , What kind of person do you like? \n Please provide some suggestions",]
    ],
    [
        r"Is coffee fit for health?",
        ["Here are some sources from the web: https://www.healthline.com/nutrition/top-evidence-based-health-benefits-of-coffee",]
    ],
    [
        r"Do you like me?",
        ["Yeah , I like spending time with you",]
    ],
    [
        r"Can you teach me japanese?",
        ["Sorry , The japanese language model is not supported.",]
    ],
    [
        r"Are you a real person?",
        ["No I am a machine but I am much smarter than you?",]
    ],
    [
        r"Which type of AI is used to build you",
        ["I am build upon AGI i.e Artificial general intelligence",]
    ],
    [
        r"Which languages do you support?",
        ["Currently I only support English Language",]
    ],
    [
        r"sorry",
        ["No problem",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I assist you?",]
    ],
    [
        r"quit",
        ["Bye-bye. Take care.",]
    ],
]

# create a chatbot using the chat pairs
chatbot = Chat(pairs, reflections)

# start the conversation
chatbot.converse()
