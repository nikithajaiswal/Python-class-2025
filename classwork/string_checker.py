class StringChecker:
    def __init__(self, text):
        self.text = text

    def has_alnum(self):
        return any(c.isalnum() for c in self.text)

    def has_alpha(self):
        return any(c.isalpha() for c in self.text)

    def has_digit(self):
        return any(c.isdigit() for c in self.text)

    def has_lower(self):
        return any(c.islower() for c in self.text)

    def has_upper(self):
        return any(c.isupper() for c in self.text)
