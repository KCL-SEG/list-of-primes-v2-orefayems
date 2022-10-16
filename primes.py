"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
	numbers = [0]
	primeNumbers = []
	if number_of_primes <=0:
		raise ValueError("cannot have zero or negative number of primes")
	for i in numbers:
		if i!=2 and i!=3 and i!=5 and i!=7:
			if i/1!=1 and i%2 != 0 and i%3 !=0 and i%5 !=0 and i%7 !=0:
				primeNumbers.append(i)
		else: 
			primeNumbers.append(i)
		if len(primeNumbers) < number_of_primes:
			i +=1
			numbers.append(i)
	return primeNumbers
