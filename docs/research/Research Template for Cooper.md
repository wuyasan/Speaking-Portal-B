# Research Template for Cooper
## Research Notes
This research is dedicated to the purpose of finding a technical way of animating a still image into narrating a section of provided text with relatively life-like qualities. There are approaches available with limited success, and enclosed is even a test run of the technology described in action. Problems with this approach include requiring to convert text selected for reading to an audio file prior to generating the animated image. On top of needing to call this service from Kukarella in the first place, this could result in long wait times. Realism is debatable as the animation has a robot-like quality to it, but ultimately this is decided by the project proponent.
### Basic Approaches
For a starting point into the animated image method, I began researching github for similar repositories that aimed to accomplish a similar feat. Many others have attempted to animate a still image, but the one that stood out to me was MakeItTalk by user yzhou359. The project works by dissecting an audio file, and creating an outline of a person, or an intermediate representation of the audio file in the form of an mp4. Simultaneously the user inputted image is analyzed using an AI for its key features like eyes mouth and nose. After this is done the points on the image are locked to the points of the intermediate representation, and combined into the final product of the users image animated, and reading text in the form of an embeddable mp4. 

### Test Run
Below is the sample run I produced using an image and audio recording of myself. On the left is the original image submitted to the program, the middle is the final animated image and the right is the audio file in the form of an intermediate representation. In this example you can see how the representation attaches anchors to the provided image and simulates movement. 


https://user-images.githubusercontent.com/77300788/194159774-1fe9bc78-f1c8-4ee5-b835-32321ae4dcea.mp4



### Difficult Points
- Animating an image in browser is resource costly
- Generating the animated image video takes upwards of 1 min to complete in Google Colab
- This method is only capable of working with images of size 256x256
- The animation style struggles to capture the realism of a human being
- Coming up with a version of our own may be a project in itself

## References
### Links to Articles/Research Papers
https://sites.google.com/view/facialsynthesis/home

### Links to Relevant Repositories 
https://github.com/yzhou359/MakeItTalk  
https://github.com/DinoMan/speech-driven-animation
## Choice of Tech Stack
Python is a very possible choice for this project due to its simplicity and accessibility. It runs on all major platforms, and there is no need for a native compiler to translate at runtime. It is relatively easy to understand even if you have no major experience in python and other programming skills transfer over nicely. Python is also home to thousands of external libraries that can make development a lot smoother. In the case of this project, popular python libraries such as Tensor Flow will be integral for resources such as image recognition and natural language processing.  
