# diCaptcha - Diffusion based Captcha 

<a href="https://docs.google.com/presentation/d/1ARbmzb_C3B-hN-pEPFlt5jiScLO08jxrUn0mRA4ZI-I/edit?usp=sharing" title="Introduction slides">
<img src="https://img.shields.io/badge/introduction%20slides-%23E4637C.svg?&style=for-the-badge&logo=slides&logoColor=white" />
</a>

## Inspiration 💡

Ever tried to select all boxes that have traffic lights showing up and confused if you're supposed to check the very edge of it?
[![Captcha meme][1]][1]

The inspiration comes from providing a better Captcha user experience while keeping security also in mind.


## What it does 🤖

[![demo][3]][3]

It shows a user an AI generated image and ask to select keywords/tags that are associated with the image.
Tags will have 3 correct tags/keywords (that are actually associated with the image and part of the prompt)
Tags will also have 3 negative tags/keywords (that are randomly generated and have nothing to do with the image)

So here we use the fact that the human is supposed to decipher what sort of tags is associated with the image directly or indirectly. The image and keywords are associated in a more complex way than just literally asking to classify the image.

## How we built it 🛠️

[![architecture][2]][2]

The product can be divided into 3 components described below:

- AI component: We use diffusion models generated images from prompts | Convert prompts into tags using POS model and some preprocessing steps
- Backend component: We randomly pick Image and Prompt from an API | We convert prompt into tags from another API
- Frontend component: We display a Captcha like experience but with a modern touch to it using

## Challenges we ran into

1. Challenges were in creating a NLP pipeline, so we can select truly relevant keywords from the prompt (which is used to generate the image).
2. The Negative keywords were being selected from a random word generator we created. Even with carefully picking correct keywords from prompts and picking random words as negative keywords, we can sometimes look at the image and be confused as to what correct tags are. This needs further improvement.


## What's next for diCaptcha Diffusion Captcha For Creative Tastes 🔜

1. Make the Tag generation model better and more intuitive for making it easier.
2. Protect our service from scraping and attacks.
3. To add user specific Captcha, called personalized Captcha security. A user's interests are used to show related images and asked to clear the task of selecting correct tags.


[1]: https://i.stack.imgur.com/GaofR.png
[2]: https://i.stack.imgur.com/hxpi0.jpg
[3]: https://i.stack.imgur.com/IhFBx.jpg
