class Value:
    ALL_STRAIGHT_LOW_VALUES = [
        14,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
    ]

    conversion = {
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Jack',
        12: 'Queen',
        13: 'King',
        14: 'Ace',
    }

    @classmethod
    def translate(cls, value):
        return cls.conversion[value]
