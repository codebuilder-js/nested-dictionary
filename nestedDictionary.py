import pprint

guests = {'Alice': {'apples': 5, 'pretzels': 12},
          'Bob': {'ham sandwiches': 3, 'apples': 2},
          'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0

    for k, v in guests.items():
        numBrought += v.get(item, 0)
    
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(guests, 'apples')))
print(' - Cups           ' + str(totalBrought(guests, 'cups')))
print(' - Cakes          ' + str(totalBrought(guests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(guests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(guests, 'apple pies')))
print(' - Pretzels       ' + str(totalBrought(guests, 'pretzels')))