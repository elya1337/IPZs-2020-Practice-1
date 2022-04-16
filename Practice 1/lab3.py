def prime_generator(end):
    for n in range(2, end):     
        for x in range(2, n):   
            if n % x == 0:     
                break
        else:                   
            yield n             


g = prime_generator(1000)     
print(list(g))