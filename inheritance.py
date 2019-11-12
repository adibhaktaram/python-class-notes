class  Card:
    '''Represents a standard playing card.'''

    def __init__(self, suit = 0, ranke = 2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                  'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    



if __name__ == '__main__':
    queen_of_diamonds = Cards(1, 12)
