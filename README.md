# Iris
![](https://dkaushik94.github.io/assets/IRIS.jpeg)
Iris is an application that helps users generate code without typing anything. Any user can just speak into the application and the application will generate code related to that. The best thing is, you can talk in free-form (natural language) and we parse everything to generate the code! Currently we support only English to Python.

### Approach

The approach we adopt is quite simple. We get speech from user, pass it to Google Speech API and get the text back, pass that text through to Microsoft Luis for intent classification, get back the JSON response, and parse the response for appropriate code generation. The code generation and processing is handled through our custom VS Code extension (written in Typescript).

### Intents Supported (can be extended)

|     intents    |   intents         | intents      |
|:--------------:|:-----------------:|:------------:|
|  add_function  | add_main_function |  delete_line |
|    add_class   |   add_try_catch   |   goto_line  |
|   add_if_else  |   add_variables   |   run_file   |
|   add_newline  |     add_while     |   save_file  |
| add_breakpoint |   call_function   | undo_changes |

## Getting Started

The main modules needed to setup the application and get everything running are:

1. Electron JS Application
2. Message Broker + Speech to code/action engine.
3. VS Code Extension

You will need Python (preferably Python3), all packages listed in requirements.txt, and npm package for Electron app.

### Prerequisites

The Python package requirements (pip) are (also available in requirements.txt for easy install):
```
pika==0.12.0
requests==2.19.1
SpeechRecognition==3.8.1
google==2.0.1
google-api-core==1.4.1
google-api-python-client==1.7.4
google-auth==1.5.1
google-auth-httplib2==0.0.3
google-cloud-speech==0.36.0
google-cloud-texttospeech==0.2.0
googleapis-common-protos==1.5.3
```

Run ```pip install -r path/to/requirements.txt``` for easy install.

### Installing

The following steps are to run the package:
1. Make sure you have RabbitMQ installed on your machine.
2. Run ```rabbitmq-server``` or you can use brew to start the broker server by running ```brew services start rabbitmq```. This will start the message-broker server on port ```localhost:15672``` on Unix machines.
3. Next, go to the project directory and start the message broker script, message_broker.py by typing in ```python3 message_broker.py```. This will start the engine listening for jobs published in the queue by any process.
4. Next go to the directory of the electron app. You can find the code for the application [here.](https://github.com/sandeepjoshi1910/Speech2Code_JS).
5. Run ```npm install``` to installed the required packages.
6. Once the dependencies are installed, run ```npm start``` to start the application.
7. Click on Click & Speak to start coding through speech!

NOTE:
- To get the VS Code extension working
    > Please use [VSCode Insiders](https://code.visualstudio.com/insiders/) to build the extension. Normal VSCode does not build the extension for the development build.

## Testing

For testing,

1. Open VSCode Insiders repo and click *debug*. This creates a new VSCode window where our extension is enabled (due to not being in production).
2. Open Command Pallete (```cmd+shit+P```) and enable our extension.
3. Run ```message_broker.py```.
4. Run ```npm start``` inside ElectronJS application folder.
5. ???
6. Profit!

## Built With

1. [ElectronJS](https://electronjs.org/)
2. [Google Speech-to-Text](https://cloud.google.com/speech-to-text/)
3. [Google Text-to-Speech](https://cloud.google.com/text-to-speech/)
4. [Microsoft Luis](https://www.luis.ai/)
5. [RabbitMQ](https://www.rabbitmq.com/)
6. [npm](https://www.npmjs.com/)

## Issues

Current issues include:
- The audio quality when recording to ```speech_recognizer``` can be improved to send a better quality audio to Google Speech API.
- Ambient noise needs to be better handled in order to enable a more complete experience.

## Authors
- [Sandeep Joshi](https://sandeepjoshi1910.github.io)
- [Debojit Kaushik](https://dkaushik94.github.io)
- [Amlaan Bhoi](https://abhoi.github.io)
- [Shubadra Govindan](https://www.linkedin.com/in/shubadra-govindan)

## Acknowledgements

Made at [HackHarvard 2018](http://hackharvard2018.devpost.com). \
Devpost submission: [Link](https://devpost.com/software/iris-1f36ns) \
Made with <3 by LitLabs.
