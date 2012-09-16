class RegistrationForm(dict)
    def __init__(self, data=None):
        pass

    def is_valid(self):
        return all(x.is_valid() for x in self.values())

    def save(self):
        raise NotImplementedError()
