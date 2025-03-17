""" QUESTION 1: Alice has some cards with numbers written
on them. She arranges the cards in decreasing order, and lays 
them out face down in a sequence on a table. 
She challenges Bob to pick out the card containing a given 
number by turning over as few cards as possible. 
Write a function to help Bob locate the card. """

from random import randrange

def locate_card(cards, query):
    med = cards[len(cards)//2]
    if query > med:
        for i in range(0,len(cards)//2):
            if cards[i] == query:
                return True 
    elif query < med:
        for i in range(len(cards)//2, len(cards)):
            if cards[i] == query:
                return True 
    elif query == med:
        return True 
    return False 
                   
    
    
card = [randrange(40, 2, -1) for i in range(10)]
cards = sorted(card, reverse=True)
print(locate_card(cards, 10))
print(locate_card(cards, 2))
print(locate_card(cards, 7))
print(cards[len(cards)//2])
print(cards)



########################################################
def binary_search(lo, hi, condition):
    """TODO - add docs"""
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def locate_card(cards, query):
    
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
    
    return binary_search(0, len(cards) - 1, condition)
    
    
card = [randrange(40, 2, -1) for i in range(10)]
cards = sorted(card, reverse=True)
find = randrange(40, 2, -1)
print(find)
print(cards)
print(locate_card(cards, find))
