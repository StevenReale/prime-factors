input = 600851475143

#initializes variables for main while loop
lastPrime = 2
testInput = input
allPrimeFactors = list()

#given a prime number, function returns next largest prime
def findNextPrime(previousPrime):

    #sets incrementer to one greater than the previous prime
    i = previousPrime + 1

    while True:
        #loop tests whether any integers from passed prime down to 2 divides the incrementer. If not, function returns incrementer as next prime.
        for j in range(i-1, 1, -1):
            if (i % j == 0):
                break
            print(i, "is prime")
            return i
        #if any for loop values divided incrementer, increase incrementer by 1
        i = i + 1

#this is the main loop, which tests primes returned from function on the input value as long as the prime is no greater than the tested value
while lastPrime <= testInput:
    print("Now Testing", lastPrime, "on", testInput)

    #if the tested prime is not a factor of the input, find next prime and restart while loop
    if testInput % lastPrime != 0:
        lastPrime = findNextPrime(lastPrime)
        continue

    #if the tested prime is a factor of the input, add it to list of primes and divide input by prime to generate next test input
    allPrimeFactors.append(lastPrime)
    testInput = testInput / lastPrime


print("All prime factors of", input, "are", allPrimeFactors)
print("The greatest prime factor is", lastPrime)
