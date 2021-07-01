morse_alphabet = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',
        "À": "· − − · −", "Ä": "· − · −",
        "È": "· − · · −", "É": "· · − · ·",
        "Ö": "− − − ·", "Ü": "· · − −", "ß": "· · · − − · ·",
        "CH": "− − − −", "Ñ": "− − · − −",
        " ": "... --- ...", ".": "· − · − · −", ",": "− − · · − −", ":": "− − − · · ·",
        ";": "− · − · − ·", "?": "· · − − · ·", "!": "− · − · − −",
        "-": "− · · · · −", "_": "· · − − · −", "(": "− · − − ·", ")": "− · − − · −", "'": "· − − − − ·",
        '"': '· − · · − ·', "=": "− · · · −", "+": 	"· − · − ·", "/": "− · · − ·", "@": '· − − · − ·'
        }

morse_alphabet_reversed = {value:key for key,value in morse_alphabet.items()}

def encode():
        text_in_normal = str(input("Please write the text you want to convert into morse alphabet: ")).upper()
        check_letters(text_in_normal)
        text_in_morse = convert_letters(text_in_normal)
        print(f"This is your text in morse code: {text_in_morse}")
        print(f"Your text has {len(text_in_morse)} characters.")


def check_letters(text_in_normal):
    for letter in text_in_normal:
        if letter not in morse_alphabet:
            print("At least one the letters you wrote are invalid")
            encode()

    print("Your entry is valid")


def convert_letters(text_in_normal):
    morsed_code = ""
    for letter in text_in_normal:
            morsed = morse_alphabet[letter]
            morsed_code += morsed
    return morsed_code


encode()






