import random
import os
import time

class Card:
	def __init__(self, suit, value, card_value):
		self.suit = suit
		self.value = value
		self.card_value = card_value

def clear():
	os.system("clear")

def print_cards(cards, hidden):
		
	s = ""
	for card in cards:
		s = s + "\t ________________"
	if hidden:
		s += "\t ________________"
	print(s)

	s = ""
	for card in cards:
		s = s + "\t|                |"
	if hidden:
		s += "\t|                |"		
	print(s)

	s = ""
	for card in cards:
		if card.value == '10':
			s = s + "\t|  {}            |".format(card.value)
		else:
			s = s + "\t|  {}             |".format(card.value)	
	if hidden:
		s += "\t|                |"		
	print(s)

	s = ""
	for card in cards:
		s = s + "\t|                |"
	if hidden:
		s += "\t|      * *       |"	
	print(s)	

	s = ""
	for card in cards:
		s = s + "\t|                |"
	if hidden:
		s += "\t|    *     *     |"	
	print(s)	

	s = ""
	for card in cards:
		s = s + "\t|                |"
	if hidden:
		s += "\t|   *       *    |"	
	print(s)	

	s = ""

	for card in cards:
		s = s + "\t|       {}        |".format(card.suit)
	if hidden:
		s += "\t|          *     |"	
	print(s)	

	s = ""
	for card in cards:
		s = s + "\t|                |"
	if hidden:
		s += "\t|         *      |"	
	print(s)	

	s = ""
	for card in cards:
		s = s + "\t|                |"
	if hidden:
		s += "\t|        *       |"	
	print(s)

	s = ""
	for card in cards:
		s = s + "\t|                |"
	if hidden:
		s += "\t|                |"	
	print(s)

	s = ""
	for card in cards:
		s = s + "\t|                |"
	if hidden:
		s += "\t|                |"	
	print(s)	

	s = ""
	for card in cards:
		if card.value == '10':
			s = s + "\t|            {}  |".format(card.value)
		else:
			s = s + "\t|            {}   |".format(card.value)
	if hidden:
		s += "\t|        *       |"			
	print(s)	
		
	s = ""
	for card in cards:
		s = s + "\t|________________|"
	if hidden:
		s += "\t|________________|"	
	print(s)		

	print()

def blackjack_game(deck):

	player_cards = []
	dealer_cards = []

	player_score = 0
	dealer_score = 0


	while len(player_cards) < 2:

		player_card = random.choice(deck)
		player_cards.append(player_card)
		deck.remove(player_card)

		player_score += player_card.card_value

		if len(player_cards) == 2:
			if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
				player_cards[0].card_value = 1
				player_score -= 10
	
		print("Your cards: ")
		print_cards(player_cards, False)
		print("Player score = ", player_score)

		input()

		dealer_card = random.choice(deck)
		dealer_cards.append(dealer_card)
		deck.remove(dealer_card)

		dealer_score += dealer_card.card_value

		print("Dealers hand: ")
		if len(dealer_cards) == 1:
			print_cards(dealer_cards, False)
			print("Dealers score = ", dealer_score)
		else:
			print_cards(dealer_cards[:-1], True)	
			print("Dealers score = ", dealer_score - dealer_cards[-1].card_value)


		if len(dealer_cards) == 2:
			if dealer_cards[0].card_value == 11 and dealer_cards[1].card_value == 11:
				dealer_cards[1].card_value = 1
				dealer_score -= 10

		input()

	if player_score == 21:
		print("Black Jack!")
		print("You Win!\n")
		quit()

	while player_score < 21:
		choice = input("Enter H to Hit or S to Stand : ")

		if len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S'):
			print("Wrong choice! Try Again\n")

		if choice.upper() == 'H':

			player_card = random.choice(deck)
			player_cards.append(player_card)
			deck.remove(player_card)

			player_score += player_card.card_value

			c = 0
			while player_score > 21 and c < len(player_cards):
				if player_cards[c].card_value == 11:
					player_cards[c].card_value = 1
					player_score -= 10
					c += 1
				else:
					c += 1		

			print("Dealer cards: ")
			print_cards(dealer_cards[:-1], True)
			print("Dealer score = ", dealer_score - dealer_cards[-1].card_value)

			print()

			print("Player cards: ")
			print_cards(player_cards, False)
			print("Player score = ", player_score)
			
		if choice.upper() == 'S':
			break

	print("Your hand: ")
	print_cards(player_cards, False)
	print("Player score = ", player_score)

	print()
	print("Dealer is revealing cards....\n")

	print("Dealer cards: ")
	print_cards(dealer_cards, False)
	print("Dealer score = ", dealer_score)

	if player_score == 21:
		print("Black Jack!")
		quit()

	if player_score > 21:
		print("\nBusted! Dealer Wins!\n")
		quit()

	input()	

	while dealer_score < 17:

		print("Dealer decides to Hit.....")

		dealer_card = random.choice(deck)
		dealer_cards.append(dealer_card)
		deck.remove(dealer_card)

		dealer_score += dealer_card.card_value

		c = 0
		while dealer_score > 21 and c < len(dealer_cards):
			if dealer_cards[c].card_value == 11:
				dealer_cards[c].card_value = 1
				dealer_score -= 10
				c += 1
			else:
				c += 1

		print("Your hand: ")
		print_cards(player_cards, False)
		print(" score = ", player_score)

		print()

		print("D: ")
		print_cards(dealer_cards, False)
		print("Dealer score = ", dealer_score)		

		input()

	if dealer_score > 21:		
		print("Dealer busted! You win!\n") 
		quit()	

	if dealer_score == 21:
		print("Dealer has black jack! You lose\n")
		quit()

	if dealer_score == player_score:
		print("It's a tie!")

	elif player_score > dealer_score:
		print("You Win!\n")					

	else:
		print("Dealer Wins! Nice try\n")					

if __name__ == '__main__':

	suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

	suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}

	cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

	cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

	deck = []

	for suit in suits:

		for card in cards:

			deck.append(Card(suits_values[suit], card, cards_values[card]))
	
	blackjack_game(deck)