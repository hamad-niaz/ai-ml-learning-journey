##### list
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)
print(fruits[0])

##### Tuple

numbers = (10, 20, 30, 40, 50)

print(numbers)
print(numbers[2])


##### Set

numbers = {10, 20, 30, 20, 40, 10}

print(numbers)


###### Dictionary

student = {
    "name": "Rahim",
    "age": 20,
    "marks": 85
}

print(student)
print(student["name"])
print(student["marks"])


#### if-else Examples

##Even or odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
    
    
    ######Positive and negative
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
else:
    print("Negative")
    
    
    #####Voting age
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
    
    
    ### pass and fail
    
marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")
    
    #####find greater Number
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("First number is greater")
else:
    print("Second number is greater")