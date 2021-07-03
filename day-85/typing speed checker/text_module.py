import random
import config


class TextMachine:

    def __init__(self):
        self.texts = ['''Ein ersoffener Bierfahrer wurde auf den Tisch gestemmt. lrgendeiner hatte ihm eine dunkelhellila Aster zwischen die Zähne geklemmt.
Als ich von der Brust aus
unter der Haut
mit einem langen Messer
Zunge und Gaumen herausschnitt,
muß ich sie angestoßen haben, denn sie glitt
in das nebenliegende Gehirn.
Ich packte sie ihm in die Brusthöhle
zwischen die Holzwolle,
als man zunähte.
Trinke dich satt in deiner Vase!
Ruhe sanft,
kleine Aster!''', '''

Wer allein ist, ist auch im Geheimnis,
immer steht er in der Bilder Flut,
ihrer Zeugung, ihrer Keimnis,
selbst die Schatten tragen ihre Glut.

Trächtig ist er jeder Schichtung
denkerisch erfüllt und aufgespart,
mächtig ist er der Vernichtung
allem Menschlichen, das nährt und paart.

Ohne Rührung sieht er, wie die Erde
eine andere ward, als ihm begann,
nicht mehr Stirb und nicht mehr Werde:
formstill sieht ihn die Vollendung an.
''', '''Wir thronen hoch auf kahlen Katafalken,
mit schwarzen Lappen garstig überdeckt.
Der Mörtel fällt. Und aus der Decke Balken
auf uns ein Christus große Hände streckt.

Vorbei ist unsere Zeit. Es ist vollbracht.
Wir sind herunter. Seht, wir sind nun tot.
In weißen Augen wohnt uns schon die Nacht,
wir schauen nimmermehr ein Morgenrot''']
        self.word_list_template = None
        self.number_of_words = 0
        self.selected_text = None

    def choose_text(self):
        choose_random_index = random.randint(0, len(self.texts)-1)
        config.selected_text = self.texts[choose_random_index]
        return config.selected_text


    def count_words(self):
        self.word_list_template = self.choose_text().split()
        config.number_of_words = len(self.word_list_template)
        print(config.number_of_words)
        return self.word_list_template, config.number_of_words

    def check_words_typed(self, words_typed):
        clean_word_list = []
        word_list = words_typed.split()
        for word in word_list:
            if word in self.word_list_template:
                clean_word_list.append(word)

        config.number_of_words_typed = len(clean_word_list)
        return config.number_of_words_typed



