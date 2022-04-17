# coding=utf-8
from random import choice
'''
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный",
"мягкий"]
Например:
# >>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
'''


# def get_jokes(steps):
    # YOUR CODE HERE
    # nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    # adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    # adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    # jokes = []
    # for s in range(0, steps):
    #     joke = f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"
    #     jokes.append(joke)
    #
    # return jokes  # YOUR CODE HERE

def get_jokes(steps, flag=False):
    """False - повторы слов разрешены. True - повторы слов запрещены"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []

    for s in range(0, steps):
        noun_joke = choice(nouns)
        adv_joke = choice(adverbs)
        adj_joke = choice(adjectives)
        offset_nouns = 0
        offset_adverbs = 0
        offset_adjectives = 0
        joke = f"{noun_joke} {adv_joke} {adj_joke}"
        jokes.append(joke)
        if flag:
            for i in range(0, len(nouns)):
                i += offset_nouns
                if nouns[i] == noun_joke:
                    nouns.pop(i)
                    offset_nouns = offset_nouns - 1
                    #print(nouns)
            for i in range(0, len(adverbs)):
                i += offset_adverbs
                if adverbs[i] == adv_joke:
                    adverbs.pop(i)
                    offset_adverbs = offset_adverbs - 1
                    #print(adverbs)
            for i in range(0, len(adjectives)):
                i += offset_adjectives
                if adjectives[i] == adj_joke:
                    adjectives.pop(i)
                    offset_adjectives = offset_adjectives - 1
                    #print(adjectives)

    return jokes  # YOUR CODE HERE


if __name__ == "__main__":
    print(get_jokes(2, True))
