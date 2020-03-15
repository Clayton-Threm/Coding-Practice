#Project Euler Question 54
#Poker hands

poker_file = open(r"C:\Users\Clayton\Documents\Python Other Files\p054_poker.txt")
content = poker_file.read()
content = content.replace(" ", "")
content = content.split("\n")

card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

def royal_flush(hand, suits):
    if len(suits) == 1:
        pass
    else:
        return []
    royal_values = ["T", "J", "Q", "K", "A"]
    for value in royal_values:
        if value in hand:
            pass
        else:
            return []
    return ["A"]

def straight_flush(hand, suits):
    if len(suits) == 1:
        pass
    else:
        return []
    hand = [card_values[card] for card in hand]
    hand.sort()
    c1 = 1
    for card in hand[0:4]:
        if hand[c1] - card == 1:
            pass
        else:
            return []
        c1 += 1
    hand = [list(card_values.keys())[list(card_values.values()).index(card)] for card in hand]
    return [hand[4]]

def four_of_a_kind(hand, suits):
    for card in hand:
        if hand.count(card) > 3:
            return card
    return []

def full_house(hand, suits):
    hand_check = hand.copy()
    high_cards = []
    for card in hand_check:
        if hand_check.count(card) > 2:
            high_cards.append(card)
            while card in hand_check:
                hand_check.remove(card)
            break
    else:
        return []
    for card in hand_check:
        if hand_check.count(card) > 1:
            return high_cards
        else:
            return []

def flush(hand, suits):
    if len(suits) == 1:
        hand.sort()
        return [hand[4]]
    else:
        return []

def straight(hand, suits):
    low_values = ["A", "2", "3", "4", "5"]
    for value in low_values:
        if value in hand:
            pass
        else:
            break
    else:
        return ["5"]
    hand = [card_values[card] for card in hand]
    hand.sort()
    c1 = 1
    for card in hand[0:4]:
        if int(hand[c1]) - int(card) == 1:
            pass
        else:
            return []
        c1 += 1
    hand = [list(card_values.keys())[list(card_values.values()).index(card)] for card in hand]
    return hand[4]

def three_of_a_kind(hand, suits):
    for card in hand:
        if hand.count(card) > 2:
            return card
    return []

def two_pair(hand, suits):
    hand_check = hand.copy()
    hand_check = [card_values[card] for card in hand]
    counter = 0
    high_cards = []
    for card in hand_check:
        if hand_check.count(card) > 1:
            counter += 1
            high_cards.append(card)
            while card in hand_check:
                hand_check.remove(card)
        if counter == 2:
            high_cards.sort()
            high_cards = [list(card_values.keys())[list(card_values.values()).index(card)] for card in high_cards]
            return high_cards
    return []


def one_pair(hand, suits):
    for card in hand:
        if hand.count(card) > 1:
            return card
    return []

def high_card(hand, suits):
    highest = 2
    for card in hand:
        high_card = card_values[card]
        if high_card > highest:
            highest = high_card
            highest_card = card
    return highest_card

def winning_hand(h1, s1, h2, s2):
    check_1 = royal_flush(h1, s1)
    check_2 = royal_flush(h2, s2)
    if len(check_1) > 0:
        return True
    elif len(check_2) > 0:
        return False
    else:
        check_1 = straight_flush(h1, s1)
        check_2 = straight_flush(h2, s2)
    #Royal Flush to Straight Flush
    if len(check_1) > 0:
        if len(check_2) > 0:
            if card_values[check_1] > card_values[check_2]:
                return True
            else:
                return False
        else:
            return True
    elif len(check_2) > 0:
        return False
    else:
        check_1 = four_of_a_kind(h1, s1)
        check_2 = four_of_a_kind(h2, s2)
    #Straight Flush to Four of a Kind
    if len(check_1) > 0:
        if len(check_2) > 0:
            if card_values[check_1] > card_values[check_2]:
                return True
            else:
                return False
        else:
            return True
    elif len(check_2) > 0:
        return False
    else:
        check_1 = full_house(h1, s1)
        check_2 = full_house(h2, s2)
    #Four of a Kind to Full House
    if len(check_1) > 0:
        if len(check_2) > 0:
            if card_values[check_1] > card_values[check_2]:
                return True
            else:
                return False
        else:
            return True
    elif len(check_2) > 0:
        return False
    else:
        check_1 = flush(h1, s1)
        check_2 = flush(h2, s2)
    #Full House to Flush
    if len(check_1) > 0:
        if len(check_2) > 0:
            if card_values[check_1] > card_values[check_2]:
                return True
            else:
                return False
        else:
            return True
    elif len(check_2) > 0:
        return False
    else:
        check_1 = straight(h1, s1)
        check_2 = straight(h2, s2)
    #Flush to Straight
    if len(check_1) > 0:
        if len(check_2) > 0:
            if card_values[check_1] > card_values[check_2]:
                return True
            else:
                return False
        else:
            return True
    elif len(check_2) > 0:
        return False
    else:
        check_1 = three_of_a_kind(h1, s1)
        check_2 = three_of_a_kind(h2, s2)
    #Straight to Three of a Kind
    if len(check_1) > 0:
        if len(check_2) > 0:
            if card_values[check_1] > card_values[check_2]:
                return True
            else:
                return False
        else:
            return True
    elif len(check_2) > 0:
        return False
    else:
        check_1 = two_pair(h1, s1)
        check_2 = two_pair(h2, s2)
    #Three of a Kind to Two Pair
    if len(check_1) > 0:
        if len(check_2) > 0:
            if card_values[check_1[1]] > card_values[check_2[1]]:
                return True
            elif card_values[check_2[1]] > card_values[check_1[1]]:
                return False
            elif card_values[check_1[0]] > card_values[check_2[0]]:
                return True
            elif card_values[check_2[0]] > card_values[check_1[0]]:
                return False
            else:
                h1_copy = h1.copy()
                h2_copy = h2.copy()
                for term in check_1:
                    while term in h1_copy:
                        h1_copy.remove(term)
                for term in check_2:
                    while term in h2_copy:
                        h2_copy.remove(term)
                check_1 = one_pair(h1_copy, s1)
                check_2 = one_pair(h2_copy, s2)
                if len(check_1) > 0:
                    if len(check_2) > 0:
                        if card_values[check_1] > card_values[check_2]:
                            return True
                        elif card_values[check_2] > card_values[check_1]:
                            return False
                        else:
                            h1_copy = h1.copy()
                            h2_copy = h2.copy()
                            while check_1 in h1_copy:
                                h1_copy.remove(check_1)
                            while check_2 in h2_copy:
                                h2_copy.remove(check_2)
                            check_1 = high_card(h1_copy, s1)
                            check_2 = high_card(h2_copy, s2)
                            if card_values[check_1] > card_values[check_2]:
                                return True
                            elif card_values[check_2] > card_values[check_1]:
                                return False
                            else:
                                return None
                    else:
                        return True
        else:
            return True
    elif len(check_2) > 0:
        return False
    else:
        check_1 = one_pair(h1, s1)
        check_2 = one_pair(h2, s2)
    #Two Pair to One Pair
    if len(check_1) > 0:
        if len(check_2) > 0:
            if card_values[check_1] > card_values[check_2]:
                return True
            elif card_values[check_2] > card_values[check_1]:
                return False
            else:
                h1_copy = h1.copy()
                h2_copy = h2.copy()
                while check_1 in h1_copy:
                    h1_copy.remove(check_1)
                while check_2 in h2_copy:
                    h2_copy.remove(check_2)
                check_1 = high_card(h1_copy, s1)
                check_2 = high_card(h2_copy, s2)
                for x in range(0,3):
                    if card_values[check_1] > card_values[check_2]:
                        return True
                    elif card_values[check_2] > card_values[check_1]:
                        return False
                    else:
                        while check_1 in h1_copy:
                            h1_copy.remove(check_1)
                        while check_2 in h2_copy:
                            h2_copy.remove(check_2)
                        check_1 = high_card(h1_copy, s1)
                        check_2 = high_card(h2_copy, s2)
        else:
            return True
    elif len(check_2) > 0:
        return False
    else:
        check_1 = high_card(h1, s1)
        check_2 = high_card(h2, s2)
    #One Pair to High Card
    h1_copy = h1.copy()
    h2_copy = h2.copy()
    for x in range(0,5):
        if card_values[check_1] > card_values[check_2]:
            return True
        elif card_values[check_2] > card_values[check_1]:
            return False
        else:
            while check_1 in h1_copy:
                h1_copy.remove(check_1)
            while check_2 in h2_copy:
                h2_copy.remove(check_2)
            check_1 = high_card(h1_copy, s1)
            check_2 = high_card(h2_copy, s2)

        
win1_list = 0
for row in content:
    if len(row) == 0:
        continue
    hand_1 = [card for card in row[0:10:2]]
    suits_1 = {card for card in row[1:11:2]}
    hand_2 = [card for card in row[10::2]]
    suits_2 = {card for card in row[11::2]}
    #print (hand_1, hand_2)
    #print (suits_1, suits_2)
    winner_1 = winning_hand(hand_1, suits_1, hand_2, suits_2)
    #print (winner_1)
    #print ()
    if winner_1 is True:
        win1_list += 1

print (win1_list)

poker_file.close()