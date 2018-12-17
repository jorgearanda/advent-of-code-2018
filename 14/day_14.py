recipes = '37'
a = 0
b = 1
input = 824501
goal = input + 10

while len(recipes) < goal * 100:
    new_recipes = int(recipes[a]) + int(recipes[b])
    recipes += str(new_recipes)
    a = (a + 1 + int(recipes[a])) % len(recipes)
    b = (b + 1 + int(recipes[b])) % len(recipes)

print('Part 1:', recipes[goal - 10:goal])

if str(input) in recipes:
    print('Part 2:', recipes.find(str(input)))
else:
    print('Not yet')
