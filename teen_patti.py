import random
from collections import Counter

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

def rank_value(card):
    r = card.split()[0]
    if r == 'A': return 14
    if r == 'K': return 13
    if r == 'Q': return 12
    if r == 'J': return 11
    return int(r)

def classify_hand(hand):
    values = sorted([rank_value(c) for c in hand])
    suits = {c.split()[-1] for c in hand}
    unique_vals = len(set(values))

    seq = values[2] - values[0] == 2 and unique_vals == 3
    ace_low = set(values) == {2, 3, 14}
    flush = len(suits) == 1

    if unique_vals == 1:
        return (6, values[0])  # Trail
    elif flush and (seq or ace_low):
        return (5, values[-1]) # Pure Sequence
    elif seq or ace_low:
        return (4, values[-1]) # Sequence
    elif flush:
        return (3, tuple(sorted(values, reverse=True))) # Color
    elif unique_vals == 2:
        pair = max(set(values), key=values.count)
        kicker = min(set(values), key=values.count)
        return (2, pair, kicker)
    else:
        return (1, tuple(sorted(values, reverse=True))) # High Card

def win_probability(your_hand, num_players=5, trials=10000):
    deck = [f"{r} of {s}" for r in RANKS for s in SUITS]
    for c in your_hand:
        deck.remove(c)
    your_rank = classify_hand(your_hand)
    wins, ties = 0, 0

    for _ in range(trials):
        random.shuffle(deck)
        opponents = [[deck[i + j*3] for i in range(3)] for j in range(num_players - 1)]
        opp_ranks = [classify_hand(o) for o in opponents]
        best = max(opp_ranks + [your_rank])
        tie_size = sum(r == best for r in opp_ranks + [your_rank])
        if your_rank == best:
            wins += (tie_size == 1)
            ties += (tie_size > 1) / tie_size

    return round((wins + ties) / trials, 4)
