class Value:
    conversion = {
        1: 'Ace',
        11: 'Jack',
        12: 'Queen',
        13: 'King',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten'
    }

    @classmethod
    def translate(cls, value):
        return cls.conversion[value]
