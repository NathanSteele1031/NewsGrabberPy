class Algorithm:
    def __init__(self):
        self.interest_words = []

    def add_interest_word(self, words: list[str]):
        if not words:
            return
        for word in words:
            self.interest_words.append(word)
            self.check_word_limit()
        
    def remove_last_word(self):
        self.interest_words.pop(0)
    
    def check_word_limit(self):
        if len(self.interest_words) > 10:
            self.remove_last_word()
        
    def get_words(self):
        return self.interest_words