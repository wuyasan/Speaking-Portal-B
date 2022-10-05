# Research Template for Cooper
## Research Notes
This research is dedicated to the purpose of finding a technical way of animating a still image into narrating a section of provided text with relatively life-like qualities. There are approaches available with limited success, and enclosed is even a test run of the technology described in action. Problems with this approach include requiring to convert text selected for reading to an audio file prior to generating the animated image. On top of needing to call this service from Kukarella in the first place, this could result in long wait times. Realism is debatable as the animation has a robot-like quality to it, but ultimately this is decided by the project proponent.
### Basic Approches


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
#
https://github.com/DinoMan/speech-driven-animation
## Choice of Tech Stack
Python is a very possible choice for this project due to its simplicity and accessibility. It runs on all major platforms, and there is no need for a native compiler to translate at runtime. It is relatively easy to understand even if you have no major experience in python and other programming skills transfer over nicely. Python is also home to thousands of external libraries that can make development a lot smoother. In the case of this project, popular python libraries such as Tensor Flow will be integral for resources such as image recognition and natural language processing.  
