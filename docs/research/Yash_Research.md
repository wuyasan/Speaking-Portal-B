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
1. In the first approach, it will be easy to animate an image but it will be difficult to sync the expressions with the speech and audio.
2. The second approach requires a lot of trial and error fine-tuning to first get the animation right and then superimposing the audio on it. It will be tedious and time consuming.
## References

- [Google Compute Engine](https://cloud.google.com/compute)
- [Amazon EC2](https://aws.amazon.com/ec2/)
- [University of Washington - Animating Faces Paper](http://grail.cs.washington.edu/projects/realface/)
- [First Order Image Animation Model](https://github.com/AliaksandrSiarohin/first-order-model)
- [Spline Motion Model](https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model)
- [Talking Head Animation](https://github.com/harlanhong/awesome-talking-head-generation)
- [Speaker Aware Talking Head Animation](https://github.com/yzhou359/MakeItTalk)

## Choice of Tech Stack

### Front End

- [NextJS by Vercel](https://nextjs.org/) is probably the highest performing industry-standard framework that we can use. Deploying and maintaining with Vercel is 10x easier as CI/CD is automatically handled.
- NextJS is based on one of the most popular frontend frameworks i.e, [ReactJS](https://reactjs.org/)
- JavaScript/TypeScript is the standard for using NextJS and creating highly performant server-side rendered web apps.

### Back End

- Server could be run using any language but JS or Python frameworks such as NodeJS or Django increase flexibilty and reduce development time as they have prebuilt methods and handle edges easily.
- Image Animation Script and Audio Syncing scripts could be run independently on cloud instances from Google or Amazon. This enables  scalability.
- Cloud Firestore NoSQL DB could be used to store metadata.
- Amazon S3 or Google Cloud Storage for storing the media files if necessary.