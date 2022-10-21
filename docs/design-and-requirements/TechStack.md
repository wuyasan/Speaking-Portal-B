# Tech Stack

This is a comprehensive document highlighting the tech stack we will be using to build this project. Our tech stack has a lot of similarities with Kukarella's stack enable smooth integration. Moreover, we we shall create API endpoints in NodeJS to interact with Python video generation scripts.

## Front End
---

### Languages
- Javascript
    
    Used to implement state logic and call APIs from the frontend.
- JSX 

    Used for writing components in NextJS and React.
- CSS

    Used for creating styled components.

### Frameworks
- NextJS(React)

    NextJS is an industry standard framework based on ReactJS. It enables optimised server-side rendering and fast response times.
    It was developed by Vercel.
- TailwindCSS

    CSS Framework for designing responsive web apps.

### Tools
- Vercel

    Vercel is the company behind NextJS, it enables quick deployments of website using its CI tools and web hosting services
- Figma

    Figma is used to design UI components.

## Back End
---
### Languages
- Javascript

    Used to implement performant web servers and API endpoints.
- Python

    Used for video generation from the still image and text files. May also be used for running ML models to generate animations.

### Frameworks
- NodeJS and Express 
    
    Runtime environment and framework for creating API endpoints using Javascript.
    Kukarella stack also uses NodeJS and Express which enables seamless integration.
- Compute Engine

    Compute instances from Google cloud used to run heavy operations of animating still images, create frame, overlay audio to create a video.
    If necessary, replacement for this is EC2 instances from AWS.

### Tools
- Google Cloud Functions

    Used to create serverless functions for the backend. It is a serverless framework which enables us to create functions without having to worry about the underlying infrastructure. It enables infinite scalability and 99.9% uptime.
    If necessary, replacement for this is AWS Lambda.
- Google Cloud Storage

    Used to store images and videos. It is a scalable and secure storage solution from Google Cloud.
    If necessary, replacement for this is AWS S3.


