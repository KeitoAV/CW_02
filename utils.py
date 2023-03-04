import requests
import json
import random
import class_


def load_random_word():
    """Вернет случайно выбранный экземпляр из класса BasicWord."""
    words = requests.get('https://www.jsonkeeper.com/b/3K7J')
    # print(words.status_code)
    words_json = json.loads(words.text)  # перевести в словарь или список, вызвав метод json объекта
    # print(words_json)
    word_choice = random.choice(words_json)  # получаем случайный элемент
    instance_class_1 = class_.BasicWord(word_choice['word'], word_choice['subwords'])  # экземпляр класса BasicWord
    return instance_class_1


# print(load_random_word())




