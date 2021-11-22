for value in range(1,6):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print("\neven number:")
print(even_numbers)

#squares
squares = []
for value in range(1,11):
    square = value **2
    print(square)
    squares.append(square)
print(squares)

#list conprehensions
squares_compreh = [value**2 for value in range(1,11)]
print(squares_compreh)

#simple statisrics
print(f'min: {min(squares_compreh)}')
print(f'max: {max(squares_compreh)}')
print(f'sum: {sum(squares_compreh)}')
print(f'count: {len(squares_compreh)}')


