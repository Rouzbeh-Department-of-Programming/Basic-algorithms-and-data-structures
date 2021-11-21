# # A solution using a list

n = int(input())
honey_pots = []
for i in range(n):
    honey_pots.append(int(input()))

pot = int(input())
pot_found = False
for i in range(len(honey_pots)):
    if honey_pots[i] == pot:
        pot_found = True
        print(i + 1)
if not pot_found:
    print("Out of Honey :(")

# Another solution using a dictionary
# n = int(input())
# honey_pots = {}
# for i in range(n):
#     honey_pots[int(input())] = i + 1  # key: pot number value: Cabinet number
#
# pot = int(input())
# print(honey_pots.get(pot, "Out of Honey :("))
