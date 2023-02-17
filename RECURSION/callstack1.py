def funcThree():
    print("Three")

def funcTwo():
    funcThree()
    print("Two")

def funcOne():
    funcTwo()   #here it will wait for the functiontwo to finish it **this is not calling a function ***
    print("One")

funcOne()