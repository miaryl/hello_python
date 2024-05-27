# Display all the prime numbers between 1 to 250.
def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# List to hold prime numbers
prime_numbers = []

# Iterate through the range from 1 to 250
for number in range(1, 251):
    if is_prime(number):
        prime_numbers.append(number)

# Print the prime numbers
print("Prime numbers between 1 and 250 are:")
print(prime_numbers)
