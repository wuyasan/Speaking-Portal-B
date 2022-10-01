# Meeting notes
## Sept 23rd

### Not a separate app, envisions as add on to kukarella app
### Program started 3 years ago
### Have you had capstone before?
2 years ago, 2 groups. Worked on different project. One didn’t work, one was virtual messenger that worked internationally, 3d object. Select point on the map and send virtual message, Prototype project. Check out kukarella table reads. Resolve issue with where character is sourced, is the image provided? Do we code animation? This is where we need to brainstorm because client isn’t sure. Possibly animating still photos, could be done with AI. All groups maybe work on same model, could save us effort. Research on the animating tech first, decide what is possible what is not early on
### Meeting expectations
same time Friday at 4, expected online, maybe every 2 weeks we do in person. Client has no problem with Friday at 4 on zoom. Client uses and prefers Discord for communication. Client suggested making a server on Discord for the project, he will invite us. Questions will be in the client discord. Client says if we need help, we can possibly ask their developers, however they are quite busy so don’t pester them too much.
### Minimal viable product: 
user can select an avatar, enter text, and have it recited back via animation. Project focus is animated image. Project focus is EXTENDING kukarells text to speech. Many functions are built, such as input text that outputs an audio file. Speech API is present in kukarellas project already.
### How can we create something that gives the user the ability to upload an image or multiple images, and it is made to ‘come alive’ in a sense in pair with kukarellas speech to text.
Preferred goal is user upload of an image, have to research to see if this is possible to do. This is not necessary but preferred.
Sizing of the avatars window while narrating text?
#
Avatar can be used anywhere, doesn’t belong to Kukarella.
Program is fully portable. Generates video, that video is downloadable/embeddable
### Milestones/important criteria. Do research on which path for animation. Get it done in the next week, max 2. Discuss approaches with client.
Flow of API. Focus is on the backend application. This process should create the image as well as source the text to speech from kukarella. 
Markers in an audio file to match up with text so lips are synced. Kukarella does not process this tech.
Backend app consumes input img/avatar, as well as the text/audio.
Backend app for kukarella is where we will run. Kukarellas written in TypeScript.
Shouldn’t be too much of a language constriction. Should be a few options to access Kukarellas backend
Mostly be working on our own repo, not a lot of outside help. If it becomes impossible we may get a hand.
Kukarella can make an API endpoint we can REQUEST to utilize their text to speech. Down the line
### What is the most important aspect? Important it works and works fast. Not too much buffer time, lip sync looks realistic, even in different languages. Be better than competitors. Main competitor Is DID for animated still images. 
Set a goal, important to release in chunks, every 2 weeks (atleast) there should be new functionality.
Client will be available for the full duration of the course
Client suggests time is plenty, try and come above and beyond, we will reassess at Christmas and see the progress we have made.
Have research done for next weeks meeting. Prepare options. Go over pros and cons of each, see client opinion. Decide what is achievable and unachievable.

