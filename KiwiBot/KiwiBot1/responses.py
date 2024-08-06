from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    if lowered == '':
        return "SPEAK UP I CAN\'T HEAR YA"
    elif 'true' in lowered:
        return 'false'
    else:
        return choice(['erm',
                       'excusez moi?',
                       'そう'])
