numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers[1:]:
    is_prime = True
    for j in numbers[1:i:]:
        if i % j == 0 and i > j:
            is_prime = False
        else:
            if is_prime:
                primes.append(i)
                break
            else:
                not_primes.append(i)
                break

print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')

# Сначала написал такое решение, потом, согласно прравилам, что находится выше.

print("----------------------")

# for i in numbers:
#     if i >= 2:
#         if i % 2 == 0 or i % 3 == 0:
#             if i != 3 and i != 2:
#                 not_primes.append(i)
#             else:
#                 primes.append(i)
#         else:
#             primes.append(i)
#
# print(f'Primes: {primes}')
# print(f'Not Primes: {not_primes}')