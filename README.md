# The Speaking Portal Project

**CONTEXT**: Kukarella text to speech converter gives you easy access to 750 AI voices across 130 languages and accents. Kukarella users can create a professional voiceover in real-time with multiple languages.  Imagine that you are listening to a blog post read by an AI voice. You hear the voice, but you also want to see the person who is reading this text, sort of a personal assistant. Today, there are few solutions which can be used to enable this. You can use pre-recorded videos and sync them with the text; or you can use AI to animate photographs of people or hand-drawn images. We would prefer the latter one because it gives more freedom to a user.

**DESCRIPTION**:  The team will build a web app compatible with Kukarella’s tech stack. The output of the web app should be something that is embeddable into a website, ideally an image or video. The input should ideally be via a web HTTP request or as a JS API. Kukarella's code base is written in TypeScript, with a React front-end and a NodeJS Express backend API server; as long as the input is accessible from our backend in some way, it is acceptable. Ideally, for a user, the process of creating a speaking portrait would look something like this: The user enters the text he wants to listen to; uploads a photo of a person or illustration of a character who will read the text; selects a language and voice; presses the "speak" button; and then he can watch and listen to the resulting animated image with a voice over.  

## Steps of Installation
### Language Requirements
1. Install Python
2. Run ```pip install json``` command to install json package which is required in this application.
### Environmental Requirements
1. Install Conda with command ```pip install conda```.
2. Install mfa with command ```conda install montreal-forced-aligner```.
3. To create a mfa environment inside conda, run command ```conda create -n aligner -c conda-forge montreal-forced-aligner```.
#### MFA Requirements
To use mfa on a specific language, both a dictionary and a model are needed.
1. Get the installation of desired dictionaries on https://mfa-models.readthedocs.io/en/latest/dictionary/index.html#dictionary. Install the dictionary within aligner by command ```mfa model download dictionary xxx``` where "xxx" is the name shows on the disctionary page.
2. Get the installation of desired models which are accessable on dictionary page. Install the model within aligner by command ```mfa model download```. Notice there are two models which are g2p and acoustic models. The model of this application is acoustic model.
3. Here are the installation commands that are used for three existing languages, English, French and Japanese:
English: ```mfa model download dictionary english_us_arpa``` and ```mfa model download dictionary english_us_mfa```.
French: ```mfa model download dictionary french_mfa``` and ```mfa model download acoustic french_mfa```.
Japanese: ```mfa model download dictionary japanese_mfa``` and ```mfa model download acoustic japanese_mfa```.
### Extra
1. For testing purposes, postman can be a good option to test how the api works.

## Structure of Repository
We have a "src" folder inside the repository which is where the code and api are at. 

## Step by Step Instruction
After install all the required packages and environment, the application is ready for using. This instruction will cover how to test the application with postman.
1. Before using the application, make sure to run ```conda activate aligner``` in the terminal and run ```conda deactivate``` after finishing with the application.
2. Within aligner, use cd commands to get to the src/api folder inside the application.
3. Use ```flask run``` command to start the api server and copy the address after ```Running on```
4. Inside the Speaking-Portal-B/data/mfadata folder, the test files of three languages are prepared.
5. Start postman, paste the address in step3 after PUT.
6. Select the text file and aduio file, then enter the corresponding language names.
7. Click send and wait for the video to pop up.
8. Enjoy your video!
