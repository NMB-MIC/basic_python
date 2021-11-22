# #simple dictionary

# alien_0 = {'color':'green','point':5}

# #Access values of dictionary
# print(alien_0['color'])
# print(alien_0['point'])

# new_points = alien_0['point']
# print(f"You just earned {new_points} points!")


# #Adding new key-value

# alien_0['x_position'] = 0
# print(alien_0)
# alien_0['y_position'] = 25
# print(alien_0)

# #change values in key
# alien_0['y_position'] = 30
# print(alien_0)


#create dictionary from empty 
# alien_0 = {}
# print(alien_0)
# alien_0['color'] = 'green'
# print(alien_0)
# alien_0['point'] = 5
# print(alien_0)


#del dictionary
# alien_0 = {'color':'green','point':5}
# print(alien_0)

# del alien_0['point']
# print(alien_0)


#Using get() to access values
alien_0 = {'color':'green','point':5}
# print(alien_0['speed'])

speed_value = alien_0.get('speed','no speed value assingned')
print(speed_value)

point_value = alien_0.get('point','no point value assingned')
print(point_value)