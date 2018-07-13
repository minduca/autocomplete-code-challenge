**PS: this repo is an expression of my very personal view and process of going through a new programming language, plus some random thoughts of mine included in the process. It is also my proposal of solution to a nice coding challenge**

# hello-suggestions
Sample api in REST built on python that provides autocomplete suggestion for cities. 

This repo is a fork of [Coveo Backend Coding Challenge](https://github.com/coveo/backend-coding-challenge) and represents my solution proposal to its challenge at the date of the fork.

## Language of choice : Python (v3.6)
I built this application using Python version 3.6. By the time I coded this, I was not literate in this language. I didn't have any previous background prior to this small test. Even its famous libraries are relativelly unknown to me. But altough it's the first time I write in python, I do take responsability for the design choices I made with the languages capabilities that I discovered whlist building this simple app.

### Why this language ?
Honestly, I didn't overthink in order to chose Python for this challenge this language. 
- I wanted to use a language that I didn't have any previous knowledge because my primary intention is to learn and stimulate my brain, not to show off. It also has a lot of scripting traits (which envolves a different mindset from what I am used to) and it seemed easy to take a grasp.
- It's validated by the community : widely appreciated, trending, relatively mature (still have its way to grow though).

### Popular choice on academic research
Another reason that I considered for this was the fact that this language has become very popular inside universities. Altough I've never an autocomplete algorithm before, I foresaw that I would need some specialized data structures and/or ML algorithms, ressources that are constantly improved on academic research and are largely available with permissive licenses in this language.

### My firsts impressions while building this
Very cool language, succinct, easy to grasp, fast to code. On the other hand, a little too much permissive for my personal taste. Maybe it's just a shift of perception that's needed, but this kind of openess is a little odd for me, since it might open space to some unwanted, non-orthodox creativity from unexperienced developers.

## IDE of choice : Visual Studio Community 2017
I consider myself relatively proficient on Visual Studio, so it was my first choice of IDE. The idea was to invest time on the learning curve through the core concepts of the language and gain time on the tools. My intention was to lever from that VS way of creating some closed tiers of abstraction on the IDE in order to hide and handle some command lines, marginal downloads, installations, etc. Not the wisest choice, I guess. Identation/spacing bugs on the text editor has been annoyingly painful and cost me some precious time. Besides, I'm missing some alerts and errors on compilation time.

## Project structure
- ```src``` : Application code
- ```test``` : Test project

### Notes on the test project

I was considering to add pytest as test framework. But I decided to only stay with 'unittest' because it integrates better with the IDE that I'm using.

About the project structure, I found two main streams of thoughts :
- (1) test files inside the src project and side-by-side to the content it tests (with some name convention, like, 'test_foo.py' to test 'foo.py' or 'test_foo_sufix1.py' if multiple test files are preferable)
- (2) test project in a different module
    
I'm going with (2) the test project in a different module because I don't like the idea of doubling the size of the deployable and send test code mixed with production code. The path to the tests is the same path of the source element it tests in 'src'.
    
There is however a somewhat hidden beauty on the simplicity of (1) : you keep phisically together things there are semantically related and intuitively supposed to be close.  Maybe a decent solution to this would be to go with (1) but skipping the compilation of every test related content (including eventual external dependencies).

All test methods have a 'test_' prefix.  This name convention is necessary for the IDE I'm using to find the tests on compilation time.

## External dependencies

### Flask
I was between [Flask](http://flask.pocoo.org/) and [Django](https://www.djangoproject.com/), since both are well stablished web frameworks for python. I decided to go with Flask because from what I saw Django uses a "batteries included" approach that brings the gorilla and whole forest when all you asked for was a banana. Flask on the other hand is this web microframework that contains only the core tools for web development, which seems a better fit for a simple scenario such as this.

### Flask-RESTPlus + Swagger UI
[Flask-RESTplus](http://flask-restplus.readthedocs.io/en/stable/) is a lightweight plugin that improves Flask by adding better annotations to describes the REST API and expose its documentation as a [Swagger](https://swagger.io/tools/swagger-ui/) interface, which is pretty clean and free from heavy dependencies.

### Typings
[Typings](https://docs.python.org/3/library/typing.html) is a library that adds hint typings. It helps mitigate some basic compilation issues.

## Third-party attributions

This sample application uses Geonames's dataset to build autocomplete recommendation for cities in Canada and the USA. Geoname is governed by a CC3 license. More information is available at http://download.geonames.org/export/dump/readme.txt
