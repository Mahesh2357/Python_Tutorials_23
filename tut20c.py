# class CountFromBy:
#     def __init__(self, v: int = 0, i: int = 1) -> None:
#         self.v = v
#         self.i = i

#     def increase(self) -> None:
#         self.val += self.incr

#     def __repr__(self) -> str:
#         return str(self.val)


print('******************')

# import collections
# Card = collections.namedtuple('Card', ['rank', 'suit'])


# class FrenchDeck:
#     ranks = [str(i) for i in range(2, 11) + list('JQKA')]

#     def __init__(self):
#         self._cards = [Card(rank, suit) for suit in self.suit
#                        for rank in self.ranks]

#     def__len__(self):
#         return len(self._cards)

#     def __getitem__(self, position):
#         return self._cards[position]

print('***** ** ** ')


class Rectangle():
     def __init__(self, w, h):
       self.w = w
       self.h = h
     
     def area(self):
       return self.w * self.h
     
     def perimeter(self):
       return 2 * (self.w + self.h)