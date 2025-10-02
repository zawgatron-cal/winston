def say_goodbye(name):
    print("Goodbye, ", name)
    
def area_of_a_circle(radius):
    area = 3.14 * radius * radius
    print(area)
    
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
    
def divide(a, b):
    return a / b

def what_to_wear(temperatures):
    return [min(temperatures), max(temperatures)]

def is_weekend(day):
    if day == 6 or day == 7:
        return "It's the weekend!"
    return "It's not the weekend."

def fuel_efficiency(distance_in_miles, fuel_in_gallons):
    return distance_in_miles / fuel_in_gallons

def secret_code(n):
    last_digit = n % 10
    n = n // 10
    return int(str(last_digit) + str(n))

# Loops

def powpow(x, y):
    s = 1
    for i in range(y):
        s = s* x
    return s

def return_min(list):
    min = list[0]
    for i in range(1, len(list)):
        if list[i] < min:
            min = list[i]
    return min

def return_max(list):
    max = list[0]
    for i in range(1, len(list)):
        if list[i] > max:
            max = list[i]
    return max

def return_min_while(list):
    min = list[0]
    i = 0
    while i < len(list):
        if list[i] < min:
            min = list[i]
        i = i + 1
    return min

def return_max_while(list):
    max = list[0]
    i = 0
    while i < len(list):
        if list[i] > max:
            max = list[i]
        i = i + 1
    return max

def calc_sum(n):
    if n <= 9:
        return n
    else:
        return (n % 10) + calc_sum(n // 10)



x = 7257124912

result = calc_sum(x) # sum of x's digits

print(f"The result of Calculate the Sum (6.3) with x = {x} is {result}.")