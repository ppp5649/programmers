# fizz buzz 문제 3의 배수 5의 배수 3과 5의 공배수

def fizz_buzz(n):
    for i in range(1,n):
        if i%15 == 0:
            print("FizzBuzz")
        
        elif i%3 == 0:
            print("Fizz")
        
        elif i%5 == 0:
            print("Buzz")
        
        else:
            print(i)
    

fizz_buzz(101)


