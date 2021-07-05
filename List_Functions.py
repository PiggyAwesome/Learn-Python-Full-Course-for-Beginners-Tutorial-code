# List Functions
lucky_numbers = [4, 8, 15, 16, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)

friends.extend(lucky_numbers)
print(friends)

lucky_numbers = [4, 8, 15, 16, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.append
print(friends)

lucky_numbers = [4, 8, 15, 16, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]


friends.insert(1, "Kelly")  # Where to insert item
print(friends)

lucky_numbers = [4, 8, 15, 16, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.remove("Jim")
print(friends)
lucky_numbers = [4, 8, 15, 16, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.clear()
print(friends)

lucky_numbers = [4, 8, 15, 16, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.pop()  # Pops last element from list
print(friends)

lucky_numbers = [4, 8, 15, 16, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends.index("Oscar"))

# lucky_numbers = [4, 8, 15, 16, 16, 23, 42]
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# print(friends.index("Mike"))

lucky_numbers = [4, 8, 15, 16, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

print(friends.count("Jim"))

lucky_numbers = [4, 8, 15, 16, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.sort()  # Alphabetical Order
print(friends)

lucky_numbers = [4, 8, 15, 16, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
lucky_numbers.reverse()
print(lucky_numbers)

lucky_numbers = [4, 8, 15, 16, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends2 = friends.copy()
print(lucky_numbers)
