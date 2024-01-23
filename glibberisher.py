from random import choice, randint, random

def pick_letter():
    rare_letters = 'qwxz'
    vovels = 'aeoiuy'
    consonants = 'bcdfghjklmnprstv'
    
    pick = random()
    if pick > 0.9:
        return choice(rare_letters)
    elif pick > 0.35:
        return choice(vovels)
    else:
        return choice(consonants)

def gen_word():
    word_len = randint(2, 9)
    return ''.join(pick_letter() for _ in range(word_len))

def gen_sentence(num_words=7):
    words = (gen_word() for _ in range(num_words))
    return ' '.join(words).capitalize() + '. '

def gen_text(num_sentences=10, the=False):
    sizes = (randint(3,12) for _ in range(num_sentences))
    sentences = ''
    for size in sizes:
        sentences += f'{gen_sentence(size)}'
        if the:
            sentences += '\n'
    return ''.join(sentences)

print(gen_text())