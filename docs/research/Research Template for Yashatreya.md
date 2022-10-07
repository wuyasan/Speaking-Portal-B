# Research Template for Yash
## Research Notes
Research with respect to animating still images and adding audio syncing capabilities to it.
### Basic Approches
1. Leverage the open source image animation models to animate the still images.
- Most of these ML models are written in python. The backend architecture will consist of a server which gets the image from the user and passes it to the python script that can be run on Google's Compute Engine or Amazon's EC2.
The instance will produce an animated image and pass it to another script running to superimpose the audio and speech capabilities. 
- This approach will be very scalable from the get-go.
2. The more harder approach is to programmatically is to make multiple versions of the provided image with expressions relevant to the speech and then combining this into a video.

### Difficult Points

## References

## Choice of Tech Stack

