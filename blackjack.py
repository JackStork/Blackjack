# blackjack
# notes:
# need to flesh out ace mechanics
# could just use one variable for all card dealings, would have to determine card total before reusing variable
# need split mechanic
# if ace is pulled with 20, make it convert to 1
import random
doubleDown = "No"
cardDeck = list()
cardDeck.append(1)
cardDeck.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52])
playerCard1 = random.choice(cardDeck)
cardDeck.remove(playerCard1)
playerCard1 = playerCard1 % 13
if playerCard1 == 0 or playerCard1 == 11 or playerCard1 == 12:
    playerCard1 = 10
elif playerCard1 == 1:
    playerCard1 = 11
dealerCard1 = random.choice(cardDeck)
cardDeck.remove(dealerCard1)
dealerCard1 = dealerCard1 % 13
if dealerCard1 == 0 or dealerCard1 == 11 or dealerCard1 == 12:
    dealerCard1 = 10
elif dealerCard1 == 1:
    dealerCard1 = 11
playerCard2 = random.choice(cardDeck)
cardDeck.remove(playerCard2)
playerCard2 = playerCard2 % 13
if playerCard2 == 0 or playerCard2 == 11 or playerCard2 == 12:
    playerCard2 = 10
elif playerCard2 == 1:
    playerCard2 = 11
dealerCard2 = random.choice(cardDeck)
cardDeck.remove(dealerCard2)
dealerCard2 = dealerCard2 % 13
if dealerCard2 == 0 or dealerCard2 == 11 or dealerCard2 == 12:
    dealerCard2 = 10
elif dealerCard2 == 1:
    dealerCard2 = 11
print("Your first card value: " + str(playerCard1))
print("Dealer showing: " + str(dealerCard1))
playerTotal = playerCard1 + playerCard2
print("Your card value now: " + str(playerTotal))
dealerTotal = dealerCard1 + dealerCard2

if playerTotal == 21:
    print("Player has blackjack! Just survive the dealer...")
    print("Dealer checks and has...")
    if (playerTotal == 21) and (dealerTotal == 21):
        print(dealerTotal)
        print("Dealer wins!")
        quit()
    else:
        print("Not 21! Player wins!")
        quit()

if playerTotal % 11 == 0:
    doubleDown = input("Double down? Yes or no: ")
    if len(doubleDown) == 3:
        playerCard3 = random.choice(cardDeck)
        cardDeck.remove(playerCard3)
        playerCard3 = playerCard3 % 13
        if playerCard3 == 0 or playerCard3 == 11 or playerCard3 == 12:
            playerCard3 = 10
        elif playerCard3 == 1:
            playerCard3 = 11
        playerTotal = playerTotal + playerCard3

while playerTotal < 21:
    if len(doubleDown) == 3:
        print("Player total is now: " + str(playerTotal))
        break
    else:
        hit1 = input("Want to hit? Yes or no: ")
        if len(hit1) == 3:
            playerCard3 = random.choice(cardDeck)
            cardDeck.remove(playerCard3)
            playerCard3 = playerCard3 % 13
            if playerCard3 == 0 or playerCard3 == 11 or playerCard3 == 12:
                playerCard3 = 10
            elif playerCard3 == 1:
                playerCard3 = 11
            playerTotal = playerTotal + playerCard3
            print("Your total is now: " + str(playerTotal))
            if playerTotal > 21:
                if playerCard1 % 11 == 0:
                    playerTotal = playerTotal - 10
                    print("Changing an ace to a one, your total is now: " + str(playerTotal))
                elif playerCard2 % 11 == 0:
                    playerTotal = playerTotal - 10
                    print("Changing an ace to a one, your total is now: " + str(playerTotal))
                else:
                    print("Bust!")
                    quit()
        else:
            print("Your total is now: " + str(playerTotal))
            break

print("Dealer Total: " + str(dealerTotal))

while dealerTotal < 18:
    dealerCard3 = random.choice(cardDeck)
    cardDeck.remove(dealerCard3)
    dealerCard3 = dealerCard3 % 13
    if dealerCard3 == 0 or dealerCard3 == 11 or dealerCard3 == 12:
        dealerCard3 = 10
    elif dealerCard3 == 1:
        dealerCard3 = 11
    dealerTotal = dealerTotal + dealerCard3
    print("Dealer Total: " + str(dealerTotal))

if (playerTotal > dealerTotal) and (playerTotal <= 21):
    print("Player Wins!")
elif (dealerTotal > playerTotal) and (dealerTotal <= 21):
    print("Dealer Wins!")
elif (dealerTotal == playerTotal):
    print("Tie!")
else:
    print("Player Wins!")