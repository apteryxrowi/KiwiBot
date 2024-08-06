from random import choice

text = []
with open('log.txt', 'r') as file:
    for _ in file:
        text.append(_.strip())
print(text)


def markov_dict() -> dict:
    dictionary = {}
    for i in text:
        words = i.split()
        for current, following in zip(words[0:-1], words[1:]):
            key = current
            dictionary.setdefault(key, []).append(following)
    print('Successfully Trained', dictionary)
    return dictionary


def predict(chain: dict, first: list, number: int) -> str:
    for j in text:
        first.append((j.split())[0])
    print('first list', first)
    word1 = choice(first)
    if word1 in list(chain.keys()):
        message = word1.capitalize()
        for k in range(number - 1):
            try:
                word2 = choice(chain[word1])
            except Exception as e:
                print(e)
                return message
            word1 = word2
            message += ' ' + word2
        return message
    else:
        return 'i don even know lol' + word1 + str(list(chain.keys()))


markov = markov_dict()
print('markov', markov)
print(predict(markov, [], 10))
