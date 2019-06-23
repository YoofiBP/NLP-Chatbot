# Automated Chatbot for Chalkboard Education using Natural Language Processing by Yoofi Brown-Pobee

## Purpose of the Chatbot
I work for Chalkboard Education and we make learning materials accessiblle via SMS, USSD and the internet. With the internet we provide an online that allows schools to disseminate their digitised content to their students efficiently at low cost. Sometimes students have problems with their accounts (they have forgotten their login tokens or do not know how to navigate the platform) and personnel are not always available to assist. The Chatbot eliminates this problem by automating some repetitive functionality to reduce the amount of time personnel spend troubleshooting as well as enabling more students to be assisted during odd hours. 
The bot is built to run on Facebook Messenger and presently I am working on deploying it to a live server and configuring the web hooks. For now you can view, download and test the files in your own console. 

The bot is able to:
* Understand user input expressed in a variety of ways to determine the ultimate intent
* Collect and learn from user inputs to improve intent identification
* Resolve Login Issues
* Enrol students in courses
* Send walkthrough and other onboarding materials

Check out the paper I wrote on this year-long project [here](https://drive.google.com/file/d/1SzDJjEasXYUsCR5AcsCCwd9Q_mZgOUVq/view?usp=sharing)

Check out my presentation on my project [here](https://aucampus-my.sharepoint.com/:p:/g/personal/joseph_brown-pobee_alumni_ashesi_edu_gh/Eagz_EDlPwlHlhHfyH6uUvEBvzChr_FasMuS06L_YOXoBw?e=tSq565)

Check out a video demo that was part of my presentation (in case you have difficulty downloading the files to test) [here](https://aucampus-my.sharepoint.com/:v:/g/personal/akorsah_ashesi_edu_gh/EW8gFblP3a9Gq83WNxTVcKsBPy511SAGUheQXOmJbO6ZRQ?e=wJ4hSn)

Chatbot Architecture
<img src="NLU Interpreter_ Responsible for understanding user input by determining intent and extracting entities.png">

## Setup and installation

If you haven’t installed Rasa NLU and Rasa Core yet, you can do it by navigating to the project directory and running:  
```
pip install -r requirements.txt
```

You also need to install a spaCy English language model. You can install it by running:

```
python -m spacy download en
```


### Files for Rasa NLU model

- **data/nlu_data.md** file contains training examples of intents: 
	- greet
	- goodbye
	- thanks
	- deny
	- joke
	- login
	
- **nlu_config.yml** file contains the configuration of the Rasa NLU pipeline:  
```yaml
language: "en"

pipeline: spacy_sklearn
```	

### Files for Rasa Core model

- **data/stories.md** file contains some training stories which represent the conversations between a user and the assistant. 
- **domain.yml** file describes the domain of the assistant which includes intents, entities, slots, templates and actions the assistant should be aware of.  
- **actions.py** file contains the code of a custom action which retrieves a Chuck Norris joke by making an external API call.
- **endpoints.yml** file contains the webhook configuration for custom action.  
- **policies.yml** file contains the configuration of the training policies for Rasa Core model.

## How to use this starter-pack?
- NOTE: If running on Windows, you will either have to [install make](http://gnuwin32.sourceforge.net/packages/make.htm) or copy the following commands from the [Makefile](https://github.com/RasaHQ/starter-pack-rasa-stack/blob/master/Makefile)
1. You can train the Rasa NLU model by running:  
```make train-nlu```  
This will train the Rasa NLU model and store it inside the `/models/current/nlu` folder of your project directory.

2. Train the Rasa Core model by running:  
```make train-core```  
This will train the Rasa Core model and store it inside the `/models/current/dialogue` folder of your project directory.

3. In a new terminal start the server for the custom action by running:  
```make action-server```  
This will start the server for emulating the custom action.

4. Test the assistant by running:  
```make cmdline```  
This will load the assistant in your terminal for you to chat.

