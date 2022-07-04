def calculator(number):
    numbers = []
    steps = 0
    x = number
    while x != 1:
        numbers.append(x)
        if x % 2 == 0:
            x /= 2
        else:
            x = 3*x + 1
        steps += 1
        
    numbers.append(x)
    return {
        "number": number,
        "steps": steps,
        "numbers": numbers
    }