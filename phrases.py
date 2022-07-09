from random import randint, sample
from english_words import english_words_alpha_set

def get_random_number(num_chars):
    return "".join([str(randint(0, 9)) if x > 0
                    else str(randint(1, 9)) for x in range(num_chars)])

def get_random_word(num_chars):
    word = ""

    while word == "":
        sample_words = sample(english_words_alpha_set, 100)     # Randomly sample 100 words
        word = next((x for x in sample_words if len(x) == num_chars and x[0].islower()), "")
    return word.upper()
