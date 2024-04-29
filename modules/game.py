from random import *

def execute():
    ActivePlayers = []
    ActiveCards = []

    class Player:
        def __init__(self, name, debt):
            self.name = str(name)
            self.debt = int(debt)
            self.cards = []

    class Card:
        def __init__(self, type, value):
            self.type = int(type)
            self.value = int(value)
            self.owner = None

    class Deck:
        def __init__(self):
            self.cards = []
        def addCard(self, card):
            self.cards.append(card)
        def distribute(self):
            cardsperplr = len(self.cards) // len(ActivePlayers)
            remainingcards = len(self.cards)

            for plr in ActivePlayers:
                plr.cards.extend(self.cards[:cardsperplr])
                self.cards = self.cards[cardsperplr:]
                remainingcards -= cardsperplr

            for i in range(remainingcards): # why does this get super math-y k nvm it was broken
                ActivePlayers[i].cards.append(self.cards[i])

    def calculateScore(cards):
        joker = any(card.type == 4 for card in cards)
        if joker:
            return -1 #we'll assign value -1 to represent the unluckiness of the player (dont step foot in a casino)

        score = 0
        for card in cards:
            if 1 <= card.type <= 3: # card = king queen or jack
                score += 10
            elif 5 <= card.type <= 8: #card = other (spade, hearts, etc)
                score += card.value
        return score

    def determineWinner():
        maxscore = 0
        winner = None

        scores = []

        for i, plr in enumerate(ActivePlayers, 1):
            score = calculateScore(plr.cards)
            scores.append((plr.name, score))

        if score == -1:
            print(f"{plr.name} has a joker in their deck! 🃏")
        elif score > maxscore:
            winner = plr
            maxscore = score
        elif score == maxscore:
            print(f"{plr.name} and {winner.name} have tied with {maxscore} points! 💵")
            scores.sort(key=lambda x: x[1], reverse=True)
    
        for i, (player_name, player_score) in enumerate(scores, 1):
            print(f"{i}. {player_name}\t\t{player_score}")

        return scores    

    plrCount = int(input('Number of players to participate: '))
    for i in range(plrCount):
        plr_name = input(f"Name of Player {str(i)}: ")
        ActivePlayers.append(Player(plr_name, 0))

# Choose card configuration
    cardstodistribute = int(input("Number of cards to distribute evenly: "))
    if cardstodistribute >= plrCount:
        for i in range(cardstodistribute):
            card_type = randint(1, 8)
            card_value = 0 # why does python make it none and not nil or null or something actually relevant (nvm i made it 0 to avoid errors lol)
            if card_type >= 5:
                card_value = randint(1, 10)
            card = Card(card_type, card_value)
            ActiveCards.append(card)

        shuffle(ActiveCards) #this is literally 50% of the assignement lol
        deck = Deck() #initiate the deck

        for card in ActiveCards:
            deck.addCard(card)

        deck.distribute()
    
        for player in ActivePlayers:
            print(f"{player.name}'s Cards: {[f'{card.type}: {card.value}' for card in player.cards]}")
            print('------------------') # Seperate card list
        determineWinner()
    else:
        print('Number of cards too small. Exiting process...')
        exit()

metadata = {
    "name": "game",
    "description": "Play a simple card game.",
    "args": ""
}

__all__ = ['execute', 'metadata']