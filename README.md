**PS: this repo is an expression of my very personal view and process of going through a new programming language, plus some random thoughts of mine included in the process. It is also my proposal of solution to a nice coding challenge**

# hello-suggestions
Sample api in REST built on python that provides autocomplete suggestion for cities. 

This repo is a fork of [Coveo Backend Coding Challenge](https://github.com/coveo/backend-coding-challenge) and represents my solution proposal to its challenge at the date of the fork.

## IDE, Tools and Languages
Tools that I used to develop this sample application.

### Python 3.6
I built this application using Python version 3.6, which is the language most recent's version by the time this app was built. By the time I coded this, I was not literate in this language. I didn't have any previous background prior to this small test. Even its famous libraries are relativelly unknown to me. But altough it's the first time I write in python, I do take responsability for the design choices I made with the languages capabilities that I discovered whlist building this simple app.

I didn't overthink in order to chose this language. I sticked to it because it's widely appreciated, mature (still have its way to grow though), has a lot of scripting traits and it seemed easy to understand. 

##### My firsts impressions while building this
Very cool language, succinct, easy to grasp, fast to code. On the other hand, a little too much permissive for my personal taste. Maybe it's just a shift of perception that's needed, but this kind of openess is a little odd for me, since it might open space to some unwanted, non-orthodox creativity from unexperienced developers.

### Visual Studio Community 2017
I consider myself relatively proficient on Visual Studio, so it was my first choice of IDE. The idea was to invest time on the learning curve through the core concepts of the language and gain time on the tools. My intention was to lever that VS way of creating some closed tiers of abstraction on the IDE in order to hide and handle some command lines, marginal downloads, installations, etc. Not the wisest choice, I guess. Identation/spacing bugs on the text editor has been annoyingly painful and cost me some precious time. Besides, I'm missing some alerts and errors on compilation time.

## External dependencies

### Flask
I was between [Flask](http://flask.pocoo.org/) and [Django](https://www.djangoproject.com/), since both are well stablished web frameworks for python. I decided to go with Flask because from what I saw Django uses a "batteries included" approach that brings the gorilla and whole forest when all you asked for was a banana. Flask on the other hand is this web microframework that contains only the core tools for web development, which seems a better fit for a simple scenario such as this.

### Typings
[Typings](https://docs.python.org/3/library/typing.html) is a library that adds hint typings. It helps mitigate some basic compilation issues.

## Third-partiy attributions

This sample application uses Geonames's dataset to build autocomplete recommendation for cities in Canada and the USA. Geoname is governed by a CC3 license. More information is available at http://download.geonames.org/export/dump/readme.txt
