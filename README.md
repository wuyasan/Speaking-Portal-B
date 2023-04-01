# The Speaking Portal Project
Client Name: Kukarella

Team: B

Team Members: Yash Atreya (PM), Sarvagya Pandey (QA), Mawanli Cui (TL), Cooper Smith (CL)

## Context

Kukarella is a product that converts text to speech in many different languages and even more accents in each language. 
## Project Description

The team has built has an API server using flask, that accepts a text file, a corresponding audio file, and a language paramenter as an input. It then parses the files to make sure the files are safe or proper for further processing. 
In further processing, it uses the Montreal Forced Aligner (MFA) to align the audio file with the text file and generate the phones for the given language. It then uses the phones to generate the mouth shapes for the given language. The mouth shapes are then used to generate the animation. The animation is then saved as a video file and sent back to the user.

## Teck Stack and Tools

1. Python v3
2. Conda v22.9
3. Montreal Forced Aligner v2.2.4.
4. Flask v2.2.3


## Sturcture of the Repository
### Data Folder
This folder contains all the text files with their corresponding audio files that is used to test the application.
### Docs Folder
All files that are use for documentation purpose are stored in this folder.
### Src Folder
This is where we store all the files that are related to code and anime generation like mouth shape, character's poses and background of the animation. Also we have our api server files inside this folder.

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
1. Before using the application, make sure to run ```conda activate aligner``` in the terminal.
2. Within aligner, use cd commands to get to the src/api folder inside the application.
3. Use ```flask run``` command to start the api server and copy the address after ```Running on```
4. Inside the Speaking-Portal-B/data/mfadata folder, the test files of three languages are prepared.
5. Start postman, paste the address in step3 after PUT.
6. Select the text file and aduio file, then enter the corresponding language names.
7. Click send and wait for the video to pop up.
8. Enjoy your video!
9. After finish video generation, run ```conda deactivate``` in the terminal to stop the aligner.