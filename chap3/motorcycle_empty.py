#empty list
motorcycles = []
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles.append('yamaha')
print(motorcycles)

motorcycles.append('suzuki')
print(motorcycles)

#insert
motorcycles.insert(0,'ducati')
print(motorcycles)

motorcycles.insert(1,'bmw')
print(motorcycles)


#del
del motorcycles[0]
print(motorcycles)

#pop
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#remove
motorcycles.remove('bmw')
print(motorcycles)