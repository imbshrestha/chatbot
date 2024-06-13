from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import os

chatbot = ChatBot(
    'NLPChatbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

def load_cornell_movie_dialogs(file_path):
    conversations = []
    with open(file_path, 'r', encoding='iso-8859-1') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('L'):
                conversation_line = line.split(" +++$+++ ")
                if len(conversation_line) == 5:
                    conversations.append(conversation_line[4].strip())
    return conversations

cornell_movie_dialogs_path = 'cornell_movie_dialogs.txt'
if os.path.exists(cornell_movie_dialogs_path):
    movie_conversations = load_cornell_movie_dialogs(cornell_movie_dialogs_path)
else:
    print(f"Dataset file not found at {cornell_movie_dialogs_path}")
    movie_conversations = []

if movie_conversations:
    trainer = ListTrainer(chatbot)
    trainer.train(movie_conversations)
else:
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('chatterbot.corpus.english')

def chat_with_bot():
    print("Start chatting with the bot (type 'exit' to stop)!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        bot_response = chatbot.get_response(user_input)
        print(f"Bot: {bot_response}")

chat_with_bot()
