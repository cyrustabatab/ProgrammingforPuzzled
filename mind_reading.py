import random
import unittest
import numpy as np
from collections import defaultdict

class Card:

    value_ordering = {c: i + 1 for i,c in enumerate(['Ace'] + list(range(2,11)) + ['Jack','Queen','King'])}
    


    suit_ordering = {'CLUBS':0,'DIAMONDS':1,'HEARTS':2,'SPADES':3}


    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    def __lt__(self,other):
        if isinstance(other,Card):
            if self.value != other.value:
                return Card.value_ordering[self.value] < Card.value_ordering[other.value]
            else:
                return Card.suit_ordering[self.suit] < Card.suit_ordering[other.suit]

    def __eq__(self,other):
        if isinstance(other,Card):
            return self.value == other.value and self.suit == other.suit

    def __repr__(self):

        return f"{self.value} of {self.suit}"

class Deck:

    SUITS = ["CLUBS","DIAMONDS","HEARTS","SPADES"]
    VALUES = ['ACE'] + list(range(2,11)) + ['Jack','Queen','King']
    
#    deck_ordering = {c: i for i,c in enumerate([Card(value,suit) for value in ['ACE'] + list(range(2,11)) + ['Jack','Queen','King'] for suit in ["CLUBS","DIAMONDS","HEARTS","SPADES"]])}
    def __init__(self):
        self.deck = [Card(v,s) for s in Deck.SUITS for v in Deck.VALUES]
        self.shuffle()

    @property
    def cards_remaining(self):
        return len(self.deck)

    @property
    def empty(self):
        return not self.deck
    
    def reset(self):
        self.deck = [Card(v,s) for s in Deck.SUITS for v in Deck.VALUES]
        self.shuffle()

    def draw_card(self):
        return self.deck.pop()

    def shuffle(self):
        random.shuffle(self.deck)

def encode_information(cards_drawn,card_picked,secret_card,distance):
    

    three_cards = [c for c in cards_drawn if (c != card_picked and c != secret_card)]
    three_cards.sort()
    print(three_cards)

    if distance == 1:
        indices = [0,1,2]
    elif distance == 2:
        indices = [0,2,1]
    elif distance == 3:
        indices = [1,0,2]
    elif distance == 4:
        indices = [1,2,0]
    elif distance == 5:
        indices = [2,0,1]
    else:
        indices = [2,1,0]

    return [card_picked] + [three_cards[i] for i in indices]

def get_pair_minimum_distance(suits_to_cards):
    
    min_distance = float("inf")  
    card_picked = secret_card = None
    for suit,cards in suits_to_cards.items():
        if len(cards) >= 2:
            for i in range(len(cards) - 1):
                card_1 = cards[i]
                for j in range(i+ 1,len(cards)):
                    card_2 = cards[j]
                    distance_1 = (Card.value_ordering[card_2.value] - Card.value_ordering[card_1.value]) % 13
                    card_picked_here,secret_card_here,distance = (card_1,card_2,distance_1) if distance_1 <= 6 else (card_2,card_1,13 - distance_1)
                    if distance < min_distance:
                        min_distance = distance
                        card_picked = card_picked_here
                        secret_card= secret_card_here
    
    return card_picked,secret_card,min_distance

def get_minimum_2(cards_drawn):

    suit_to_cards = defaultdict(list)
    minimum_distance = float("inf")
    card_picked = secret_card = None
    for card in cards_drawn:
        if card.suit in suit_to_cards:
            for other_card in suit_to_cards[card.suit]:
                distance_1 = (Card.value_ordering[card_2.value] - Card.value_ordering[card_1.value]) % 13
                card_picked_here,secret_card_here,distance = (card_1,card_2,distance_1) if distance_1 <= 6 else (card_2,card_1,13 - distance_1)
                if distance < min_distance:
                    min_distance = distance
                    card_picked = card_picked_here
                    secret_card = secret_card_here

        suit_to_cards[card.suit].append(card)

def assistants_job():

    deck = Deck()

    cards_drawn = []

    for i in range(5):
        card = deck.draw_card()
        cards_drawn.append(card)
    print("CARDS DRAWN: ",cards_drawn)
    card_1 = card_2 = None
    suit_to_card = defaultdict(list)
    #for card in cards_drawn:
    #    if card.suit in suit_to_card:
    #        card_1,card_2 = card,suit_to_card[card.suit]
    #        break
    #    suit_to_card[card.suit] = card
    
    for card in cards_drawn:
        suit_to_card[card.suit].append(card)

    card_picked,secret_card,distance = get_pair_minimum_distance(suit_to_card)
    print("SECRET CARD:", secret_card)

    #if abs(Card.value_ordering[card_1.value] - Card.value_ordering[card_2.value]) <= 6: 
    #    card_picked = min(card_1,card_2,key=lambda x: Card.value_ordering[x.value])
    #else:
    #    card_picked = max(card_1,card_2,key=lambda x: Card.value_ordering[x.value])
    #secret_card = card_1 if card_picked is card_2 else card_2
    #distance_between_cards = abs(Card.value_ordering[card_1.value] - Card.value_ordering[card_2.value])
    #if distance_between_cards > 6:
    #    distance_between_cards = 13 - distance_between_cards
    return (encode_information(cards_drawn,card_picked,secret_card,distance))


def get_pair_within_13(cards):

    ordering = {}
    for i,c in zip(range(0,52,4),['ACE'] + list(range(2,11)) + ['Jack','Queen','King']):
        ordering[c] = i


    for i in range(len(cards) - 1):
        card_1 = cards[i]
        card_1_value = ordering[card_1.value] + Card.suit_ordering[card_1.suit]

        for j in range(i + 1,len(cards)):
            card_2 = cards[j]
            card_2_value = ordering[card_2.value] + Card.suit_ordering[card_2.suit]
            
            distance = (card_2_value - card_1_value) % 52
            if distance <= 13:
                return card_1,card_2,distance
            
            distance = (card_1_value - card_2_value) % 52
            if distance <= 13:
                return card_2,card_1,distance

def encode_information(cards,first_card,secret_card,distance):
    hidden = "HIDDEN CARD"
    
    card_order = [first_card] + [c for c in cards if c != first_card and c != secret_card]
    
    left = 0
    right = 0
    
    if distance == 1:
        position = [0,0,0,0]
    elif distance == 2:
        position = [0,0,0,1]
    elif distance == 3:
        position = [0,0,1,0]
    elif distance == 4:
        position = [0,0,1,1]
    elif distance == 5:
        position = [0,1,0,0]
    elif distance == 6:
        position = [0,1,0,1]
    elif distance == 7:
        position = [0,1,1,0]
    elif distance == 8:
        position = [0,1,1,1]
    elif distance == 9:
        position = [1,0,0,0]
    elif distance == 10:
        position = [1,0,0,1]
    elif distance == 11:
        position = [1,0,1,0]
    elif distance == 12:
        position = [1,0,1,1]
    else:
        position = [1,1,0,0]

    faceup = position[0] == 1
    card_placements = [hidden]
    for pos,card in zip(position[1:],card_order):
        print(f"Placing {card} to {'left' if pos == 0 else 'right'} of secret card {'faceup' if faceup else 'facedown'}")
        card = [card] if faceup else ['FACEDOWN']
        card_placements = card + card_placements if pos == 0 else card_placements + card
    
    print(card_placements)
    return position

    
def assistant_four_cards():

    deck = Deck()
    cards_drawn = []

    for i in range(4):
        cards_drawn.append(deck.draw_card())

    first_card,secret_card,distance = get_pair_within_13(cards_drawn)
    print("First Card:",first_card)
    print("Secret Card:",secret_card)

    positions = encode_information(cards_drawn,first_card,secret_card,distance)
    return first_card,positions




def decode(three_cards):

    indices = tuple(np.argsort(three_cards))

    if indices == (0,1,2):
        return 1
    elif indices == (0,2,1):
        return 2
    elif indices == (1,0,2):
        return 3
    elif indices == (2,0,1):
        return 4
    elif indices == (1,2,0):
        return 5
    else:
        return 6


def magicians_jobs(four_cards):

    print(four_cards)
    first_card,three_cards = four_cards[0],four_cards[1:]
    distance = decode(three_cards)

    cards = ['Ace'] + list(range(2,11)) + ['Jack','Queen','King']

    secret_card_value = cards[((Card.value_ordering[first_card.value] + distance) % 13) - 1]

    return Card(secret_card_value,first_card.suit)

def magicians_job_four_cards(first_card,positions):
    
    ordering = {}
    reverse_ordering = {}
    for i,c in zip(range(0,52,4),['ACE'] + list(range(2,11)) + ['Jack','Queen','King']):
        ordering[c] = i
        reverse_ordering[i] = c
    
    if positions == [0,0,0,0]:
        distance = 1
    elif positions == [0,0,0,1]:
        distance = 2
    elif positions == [0,0,1,0]:
        distance = 3
    elif positions == [0,0,1,1]:
        distance = 4
    elif positions == [0,1,0,0]:
        distance = 5
    elif positions == [0,1,0,1]:
        distance = 6
    elif positions == [0,1,1,0]:
        distance = 7
    elif positions == [0,1,1,1]:
        distance = 8
    elif positions == [1,0,0,0]:
        distance = 9 
    elif positions == [1,0,0,1]:
        distance = 10
    elif positions == [1,0,1,0]:
        distance = 11
    elif positions == [1,0,1,1]:
        distance = 12
    else:
        distance = 13
    
    first_card_value = ordering[first_card.value] + Card.suit_ordering[first_card.suit]
    
    second_card_value = (first_card_value + distance) % 52
    second_card_true_value = reverse_ordering[(second_card_value // 4) * 4]
    second_card_suit = Deck.SUITS[second_card_value - (second_card_value //4) * 4]
    print("THE SECRET CARD IS:",Card(second_card_true_value,second_card_suit))



if __name__ == "__main__":

    #while True:
    #    choice = input("Play? (Type q to quit and any other character to continue) ")
    #    if choice.lower().startswith('q'):
    #        print("Thank You For Playing")
    #        break
    #    cards =assistants_job()
    #    print(f"The fifth card is {magicians_jobs(cards)}")
    
    first_card,positions = assistant_four_cards()
    magicians_job_four_cards(first_card,positions)
    class CardTest(unittest.TestCase):

        def test_case_1(self):
            card_1 = Card('Ace','DIAMONDS')
            card_2 = Card('Ace','SPADES')
            self.assertLess(card_1,card_2)

        def test_case_2(self):
            card_1 = Card(1,'HEARTS')
            card_2 = Card(1,'CLUBS')
            self.assertGreater(card_1,card_2)

#    unittest.main(verbosity=2)




