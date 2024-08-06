from random import choice, randint


def fileread() -> list[str]:
    text = []
    with open('log.txt', 'r') as file:
        for _ in file:
            text.append(_.strip())
    return text


def markov_dict() -> dict:
    dictionary = {}
    text = fileread()
    for i in text:
        words = i.split()
        for current, following in zip(words[0:-1], words[1:]):
            key = current
            dictionary.setdefault(key, []).append(following)
    return dictionary


def predict(chain: dict, first: list, number: int) -> str:
    text = fileread()
    for j in text:
        if len(j.split()) > 1:
            first.append((j.split())[0])
    word1 = choice(first)
    if word1 in list(chain.keys()):
        message = word1.capitalize()
        for k in range(number - 1):
            try:
                word2 = choice(chain[word1])
            except KeyError:
                print(KeyError)
                message += '. '
                word2 = choice(first)
                return message
            word1 = word2
            message += ' ' + word2
        return message
    else:
        return 'i don even know lol' + word1 + str(list(chain.keys()))


def get_response(user_input: str) -> str:
    dictionary: dict = markov_dict()
    lowered: str = user_input.lower()
    if lowered == '':
        return "SPEAK UP I CAN\'T HEAR YA"
    else:
        return predict(dictionary, [], randint(2, 100))
