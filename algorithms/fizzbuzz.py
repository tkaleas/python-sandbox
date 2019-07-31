def FizzBuzz():
    for i in range(1,101):

        fiveDivis = i % 5 == 0
        threeDivis = i % 3 == 0

        if fiveDivis and threeDivis:
            print("FizzBuzz")
        elif fiveDivis:
            print("Buzz")
        elif threeDivis:
            print("Fizz")
        else:
            print(i)