#file: homework4.py

#3.1
favorite_foods = ["fried rice", "ramen", "pizza", "yogurt", "curry"]
print(favorite_foods[1])
print(favorite_foods[-1])
favorite_foods.append("cake")
favorite_foods.insert(0, "apple")
del favorite_foods[2]
'''
I encountered this error:
ValueError: list.remove(x): x not in list
I originally wrote: favorite_foods.remove(2)
.remove() does not work with indices. remove with del
'''
print(len(favorite_foods))
for item in favorite_foods:
    print(item.upper())
new_list=favorite_foods[-1:1]
if "potato" in new_list:
    print("A potato!")
else:
    print("No potato!")
    
#3.2
numbers = range(0,21)

def get_first_15(l):
    return l[0:16]
def get_every_5th(l):
    z = []
    for n in range(0, len(l), 5):
        z.append(n)
    return z
def reverse_and_stride(l):
    x = l[::-1]
    z = []
    for n in range(0, len(x), 3):
        z.append(x[n])
    return z
step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(numbers[2])
print(numbers[1][1])
numbers.append([10,11,12])
def sum_nested(nested_list):
    total = 0
    for sub in nested_list:
        total += sum(sub)
    return total
print(sum_nested(numbers))

def create_5x5_list():
    output = []
    n = 1
    for i in range(0,5):
        row = []
        for j in range(0, 5):
            row.append(n)
            n += 1
        output.append(row)
    return output
def replace_3_multiples(matrix):
    for i in range(0,5):
        for j in range(0, 5):
            if matrix[i][j] % 3 == 0: matrix[i][j] = "?"
    return matrix
def not_question_sum(matrix):
    s = 0
    for i in range(0,5):
        for j in range(0, 5):
            if matrix[i][j] != "?": s += matrix[i][j]
    '''
    I encountered this error:
    UnboundLocalError: cannot access local variable 'sum' where it is not associated with a value
    I originally wrote: if matrix[i][j] != "?": sum += matrix[i][j]
    sum is a function which is not associated with a value so operations cannot be performed on it. Replaced sum with s
    '''
    return s
matrix = create_5x5_list()
new_matrix = replace_3_multiples(matrix)
s = not_question_sum(new_matrix)

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
ages.pop("Mariam")



for person in ages:
    '''
    I encountered this error:
    TypeError: can only concatenate str (not "int") to str
    I originally wrote: print(person + ": "+ ages[person])
    ages[person] is an int. I cast ages[person] to str
    '''
    print(person + ": "+ str(ages[person]))
    
hahaha = create_5x5_list()
print(hahaha)

