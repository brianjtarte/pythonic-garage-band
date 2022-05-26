class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"


class Musician:
    pass


class Guitarist:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    @classmethod
    def get_instrument(cls):
        return f'guitar'


class Bassist:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

    @classmethod
    def get_instrument(cls):
        return f'bass'


class Drummer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    @classmethod
    def get_instrument(cls):
        return f'drums'


if __name__ == '__main__':
    pass
joan = Guitarist('Joan Jett')
sheila = Drummer("Sheila E.")
meshell = Bassist("Meshell Ndegeocello")
nirvana = Band("Nirvana", [])
jimi = Guitarist("Jimi Hendrix")
flea = Bassist("Flea")
ginger = Drummer("Ginger Baker")

