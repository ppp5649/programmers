from collections import Counter

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

total_share = Counter()

for name,share,price in portfolio:
    total_share[name] += share

print(total_share)