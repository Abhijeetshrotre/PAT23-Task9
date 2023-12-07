data = [7, 'Name', 42, 'Lname', 84, 'orange', 90, 'email']

check_type = lambda x: 'Integer' if isinstance(x, int) else 'String'

result = list(map(check_type, data))

print(result)