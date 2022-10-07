# Research - Sarvagya Pandey
## Research Notes
Trying to understand the different approaches to 3D Speech-Driven Facial Animation.
### Basic Approches

1. Generating animated video using existing animation software - Lets look at the iClone 8 Real-Time 3D Animation software as an example. This software only requires an audio/speech file, which it then uses to extract text and visemes, aligns them automatically with the audio, and generates an animation using a pre-made 3D facial rig by stringing together the mouth shapes associated with the aligned sequence of visemes generated from the audio file. The viseme alignment can be improved further by directly uploading the text file containing the speech transcript.


2. Creating sequence of visemes and applying them to a 3D model with the help of text and speech data - In this method, we generate the list of phonemes and associated timestamps aligned with the input speech file through a process known as forced alignment. This sequence can then be used to generate the required viseme sequence to be used for animation. Viseme sequence generation looks to be slightly more complicated as one phoneme can map to several different visemes depending on the content/style of the speech(normal conversation, angry/yelling, etc). More research needs to done on accurate viseme generation.

    There are many libraries available that can help perform forced alignment. For example, 'pyfoal' and 'pypar' are a set of Python libraries that generate a phoneme-synchronization map between the input text and audio file, and allow us to access this map for further tasks.

    The JALI viseme model generates a viseme field for both the jaw and lip motions for each individual phoneme, which can then be applied to a 3D rig to generate an animated video. There are also some other models (FLAME) that I need to do more research on.
### Difficult Points

1. Using iClone 8, or any other existing animation software, will come with a high cost. Also, I'm not sure how we will even have the software running to generate the video for the user and/or interact with the software to enter our input data.

2. Many of the pre-trained models for viseme generation seem to be licensed for non-commercial/research use only, so I need to dig deeper to find something that we can actually use in our software. Also, further testing needs to be done to check if we can even generate the animated video within a reasonable timeframe using these models. 
## References
### Links to Articles/Research Papers

1. iClone 8 Website - https://www.reallusion.com/iclone/lipsync-animation.html
2. Paper on the JALI Model - https://www.dgp.toronto.edu/~elf/JALISIG16.pdf
3. Video on the JALI Model - https://www.youtube.com/watch?v=vniMsN53ZPI
4. VOCA audio-driven 3D animation - https://voca.is.tue.mpg.de/index.html
5. Viseme Explanations - https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-speech-synthesis-viseme?tabs=visemeid&pivots=programming-language-csharp
### Links to Relevant Repositories

1. pyfoal Repository - https://github.com/maxrmorrison/pyfoal
2. pypar Repository - https://github.com/maxrmorrison/pypar
