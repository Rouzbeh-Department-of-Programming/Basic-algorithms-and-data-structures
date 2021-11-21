flowers = {}
flower = input()

while flower != "+":
    upper_case = flower.upper()
    if upper_case in flowers:
        flowers[upper_case] += 1
    else:
        flowers[upper_case] = 1
    flower = input()

sorted_flowers = sorted(flowers)
s = 0
for f in sorted_flowers:
    print(f'{f} : {flowers[f]}')  # What does this line mean? (Search String formatting in python on Google!)
    s += flowers[f]
    
print()
print(f'total : {s}')
