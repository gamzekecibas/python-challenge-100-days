## Day 10 - Beginner | Functions with Outputs
## 07.06.2023
## ----
## DAY 10 PROJECT The Calculator
## ----
print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")
## Math operation functions
# Add
def add(n1, n2):
    return n1 + n2

# Substract
def substract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = { "+": add,
               "-": substract,
               "*": multiply,
               "/": divide
}
## function = operations['+']
## function(2,3) = 5

## function = operations['*']
## function(2,3) = 6

is_cont_calculation = True
final_result = 0

num1 = float(input("What's the first number?: "))
for op in operations.keys():
    print(op)
op_type = input("Pick an operation from the lines above: ")
num2 = float(input("What's the second number?: "))

while is_cont_calculation == True:
    is_next_number = input("Type 'y' if there is another operation or type 'n': ")
    if is_next_number == 'y':
        print(f'{num1} {op_type} {num2} = {operations[op_type](num1, num2)}')
        num1 = operations[op_type](num1, num2)
        num2 = float(input("Pick another number: "))
        for op in operations.keys():
            print(op)

        op_type = input("Pick an operation from the lines above: ")
    else:
        is_cont_calculation= False
        print(f'Final results is {operations[op_type](num1, num2)}')