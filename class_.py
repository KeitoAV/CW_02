class BasicWord:
    def __init__(self, original_word, valid_subwords):
        self.original_word = original_word
        self.valid_subwords = valid_subwords

    def get_valid_words(self, user_answer):
        """Проверка введенного слова в списке допустимых подслов (вернет bool)."""
        for word in self.valid_subwords:
            if user_answer == word:
                return True
        return False

    def get_check_subwords(self):
        """Подсчет количества подслов (вернет int)."""
        return int(len(self.valid_subwords))

    # print(get_check_subwords())


class Player:
    def __init__(self, user_name):
        self.user_name = user_name
        self.user_words = []

    def get_check_words(self):
        """Получение количества слов (возвращает int)."""
        return int(len(self.user_words))

    def add_words(self, used_words):
        """Добавление слова в использованные слова (ничего не возвращает)."""
        self.user_words.append(used_words)
        return

    def check_words_before(self, used_words):
        """Проверка использования данного слова до этого (возвращает bool)."""
        for word in self.user_words:
            if word == used_words:
                return True
        return False



