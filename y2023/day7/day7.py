import functools

#was not able to get part 2 done. but fuck it. 

@functools.total_ordering
class Hand:

    cards: str
    bid: int
    def __init__(self, s: str) -> None:
        [cards, bid_str] = s.split(maxsplit=1)
        self.cards = cards \
            .replace('T', 'a') \
            .replace('J', 'b') \
            .replace('Q', 'c') \
            .replace('K', 'd') \
            .replace('A', 'e')
        self.bid = int(bid_str)

    def count_same(self):
        hand = self.cards
        label_counts = [hand.count(label) for label in set(hand)]

        if 5 in label_counts:
            return 6 # Five of a kind

        if 4 in label_counts:
            return 5 # Four of a kind

        if 3 in label_counts:
            if  2 in label_counts:
                return 4 # Full House
            else:
                return 3 # Three of a kind

        if label_counts.count(2) == 2:
            return 2 # Two pair

        if label_counts.count(2) == 1:
            return 1 # One pair

        return 0 # High card

    def __lt__(self, other: 'Hand'):
        if self.count_same() == other.count_same():
            return self.cards < other.cards
        return self.count_same() < other.count_same()

    def __str__(self) -> str:
        return f'Card{{cards = {self.cards}, bid = {self.bid}}}'

lines = open('y2023/day7/input.txt').readlines()

def part_1():
    hands = [Hand(ln) for ln in lines]
    hands.sort()
    # for hand in hands:
    #     print(hand, f'matching = {hand.count_same()}')
    print(sum([
        (i + 1) * hand.bid
        for i, hand in enumerate(hands)
    ]))

def part_2():
    hands = [Hand(ln.replace('J', '0', 1)) for ln in lines]
    hands.sort()
    # for hand in hands:
    #     print(hand, f'matching = {hand.count_same()}')
    print(sum([
        (i + 1) * hand.bid
        for i, hand in enumerate(hands)
    ]))

if __name__ == '__main__':
    part_1()