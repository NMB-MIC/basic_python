players = ['john','phop','nut','martin','harry']
print(players[0:3])
print(players[:3])
print(players[2:])
print(players[1:5])

print(players[-3:])


#looping
for player in players[:3]:
    print(player.title())

#copy list
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(f"myfoods: {my_foods}")
print(f"friend food: {friend_foods}")
