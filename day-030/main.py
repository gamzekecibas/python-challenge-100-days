### Common Error Types

## FileNotFound Error
#with open("a_file.txt") as file:
#    file.read()

## KeyError
#a_dict = {"key": "error"}
#val = a_dict["non_exist_key"]

## IndexError
#fruit_list = ["apple", "banana", "pear"]
#fruit = fruit_list[4]

## TypeError
#text = "abc"
#print(text + 5)


## Catching Exceptions
try:
    file = open("a_file.txt")
    a_dict = {"key":"error"}
    print(a_dict["new_key"])
except FileNotFoundError:
    #print("There was an error!")
    file = open("a_file.txt", "w")
    file.write("Sth")
except KeyError as error_message:
    print(f"The key {error_message} does not exist!")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed!")
    #raise FileNotFoundError("This is an error I made up!")

## Raise error message example
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters!!!")

bmi = weight / height ** 2
print(bmi)