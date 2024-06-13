# chatbot
A simple NLP chatbot that uses the ChatterBot library
Project Description
This repository contains the final version of the NLP Chatbot project developed using the ChatterBot library. The chatbot is designed to interact with users in natural language, leveraging both supervised and unsupervised learning techniques. It is trained on a dataset derived from the Cornell Movie Dialogs, enabling it to provide coherent and contextually relevant responses.

Features
Natural Language Processing (NLP): Utilizes ChatterBot for natural language understanding and response generation.
Training Data: Trained on the Cornell Movie Dialogs dataset to understand and respond to a wide range of conversational inputs.
Logic Adapters: Includes a BestMatch logic adapter with a default response for unrecognized inputs.
Docker Integration: Dockerfile provided for easy setup and deployment in a containerized environment.
Project Structure
chatbot.py: Main executable file for the chatbot.
cornell_movie_dialogs.txt: Dataset used for training the chatbot.
Dockerfile: Dockerfile for building and running the chatbot in a Docker container.
requirements.txt: List of dependencies required to run the chatbot.
Installation and Setup
Prerequisites
Docker
Python 3.8+
Running the Chatbot
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/chatbot_project.git
cd chatbot_project
Build and Run with Docker:

bash
Copy code
docker build -t chatbot .
docker run -it -v $(pwd)/chatterbot_corpus:/app/chatterbot_corpus chatbot
Run Without Docker:

Ensure you have the required dependencies installed:

bash
Copy code
pip install -r requirements.txt
Then run the chatbot:

bash
Copy code
python chatbot.py
Usage
Start chatting with the bot by following the instructions after running the program. Type your messages and the bot will respond accordingly. Type 'exit' to end the chat session.

Files Included
chatbot.py: Main script to initialize and run the chatbot.
cornell_movie_dialogs.txt: Training dataset from the Cornell Movie Dialogs.
Dockerfile: Instructions to build the Docker image.
requirements.txt: Dependencies needed for the project.
Documentation
The repository includes a PDF document that provides a detailed analysis of the project structure, tools and libraries used, and the type of NLP model implemented. It also includes screenshots of the program's execution and output.

Contribution
Feel free to contribute by submitting a pull request or opening an issue for any bugs or feature requests.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

