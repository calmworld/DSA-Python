def fizz_buzz(n):
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))
    return result
            

print(f'When input is 15, the output would be: {fizz_buzz(15)}') # FizzBuzz
print(fizz_buzz(30)) # FizzBuzz
print(fizz_buzz(10)) # FizzBuzz

print(fizz_buzz(4)) 
print(fizz_buzz(5))
print(fizz_buzz(6))