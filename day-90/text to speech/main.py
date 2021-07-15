from gtts import gTTS
from playsound import playsound
from tika import parser


raw = parser.from_file('selections_short.pdf')
print(raw['content'])

tts = gTTS(raw['content'])
tts.save('hello.mp3')

playsound('hello.mp3')



