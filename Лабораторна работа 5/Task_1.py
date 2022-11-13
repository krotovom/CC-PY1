from pprint import pprint

numbers = [{'bin': bin(number), 'dec': number, 'hex': hex(number), 'oct': oct(number)} for number in range(16)]
pprint(numbers)
