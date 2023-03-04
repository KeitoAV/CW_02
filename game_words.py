import utils
import class_


def main():
    player_name = input('Введите имя игрока\n').title()
    instance_class_2 = class_.Player(player_name)  # экземпляр класса Player
    word = utils.load_random_word()  # случайно выбранный экземпляр класса BasicWord
    print(f"Привет, {player_name}!\nСоставьте {word.get_check_subwords()} слов из слова {word.original_word.upper()}")
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print(f'Слова должны быть не короче 3 букв.\nПоехали, ваше первое слово?')

    for subwords in word.valid_subwords:
        user_subwords = input().lower()
        if user_subwords == 'стоп' or user_subwords == 'stop':
            quit(f'игра завершена!\nвы угадали {len(instance_class_2.user_words)} слов')

        if word.get_valid_words(user_subwords) is True and instance_class_2.check_words_before(user_subwords) is False:
            print('верно')
            instance_class_2.add_words(user_subwords)  # добавляем слово в использованные слова
        else:
            print('неверно')
        # print(instance_class_2.user_words)

    print('слова закончились, игра завершена!')
    print(f'вы угадали {len(instance_class_2.user_words)} слов')


if __name__ == "__main__":
    main()
