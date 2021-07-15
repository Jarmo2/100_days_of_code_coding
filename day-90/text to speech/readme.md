### Convert PDF to Audiobook

I followed this Udemy Course: https://www.udemy.com/course/100-days-of-code/

This course finalises with 20 challenges covering all aspects which were introduced during this course.

This project covers the challenge from day 90 (10th challenge). One of those challenges was building my own website:
https://jarmo2.github.io/ 
On this website you can find all the projects I have built inspired by _100 days of code_.
The instructions given for this project were as follows:
_Write a Python script that takes a PDF file and converts it into speech._

For this program I used the tika, gtts and playsound.

This program uses the parser functionality from tika. Tika parses a pdf file containing a few Shakespeare poems.
The output of tika is a dictionary. The text of the pdf is stored in the _content_ key of the dictionary as a string.

Gtts converts the string into an audio file, and the playsound module plays this audio file which is stored locally.

### Badges

#### 1. GitHub Stats
[My repository stats](https://github-readme-stats.vercel.app/api?username=Jarmo2&show_icons=true)
#### 2. Most Used Languages
![The top programming languages used by me](https://github-readme-stats.vercel.app/api/top-langs/?username=Jarmo2&theme=blue-green)

##### 3. Random Joke Generator
![Jokes Card](https://readme-jokes.vercel.app/api)

##### 4. Profile View Counter
![Profile views](https://komarev.com/ghpvc/?username=Jarmo2)



### Installation

For this simple program you need Python and the following libraries:
- tika 
- gtts 
- playsound


### Usage

To run this program you need to execute the main.py file. As the parsing process and the conversion into audio takes a while please be patient.


### Support

If you need help or if you have a comment please feel free to leave a comment on Github.

This version is stable. It's a really simple script showing how easy it is to use Python for an idea if you find the right libraries.


### License

gpl-3.0