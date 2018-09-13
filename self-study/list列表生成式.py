print(list(i**2 for i in range(1,11)))

print([x * x for x in range(1, 11) if x % 2 == 0])    
print(list(range(1, 11)))

print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)