
# # #### Functions & Return Values

# # def funn(a, b):
# #     result = a + b
# #     return result
# # total = funn(4, 5)
# # print(total)


# ####Task 1

# # def square(n):
# #     result = (n * n)
# #     return result
# # total= square(7)
# # print(total) 
# # total= square(5)
# # print(total)
# # total =  square(6)
# # print(total)

# ### Task 2 

# # def greet(name):
# #     result = "Hello " + name
# #     return result
# # show_name = greet("Bhaloo")
# # print(show_name)



# ###Function Scope

# # x = 10
# # def my_fun():
# #     y = 5
# #     print(x + y)
    
#     ##### Lambda  Function
    
# # square = lambda x: x*x
# # print(square(4))


# # add = lambda a, b: a + b
# # print(add(9,12))



# # ##### Task1
# # mult = lambda a, b: a * b
# # print(mult(8, 8))
# # print(mult(3, 4))


# ### Task 2

# # Whether_check = lambda n: n % 2 == 0
# # print(Whether_check)














# # #### Map and Filter...

# nums =[30,32,36, 38]

# squared = list(map(lambda x: x*x, nums))
# print(squared)
# even = list(filter(lambda x: x%2 ==0, nums))
# print(even)



# ####### Task......
# lis =[32, 34, 36, 38]
# temp = list(map(lambda a: (a * 9/5) + 32, lis))
# print(temp)










######Inner/ Nested functions


############Task
# def process_order(item):
#     def receipt_li():
#         print("Item:", item)
#     receipt_li()
# process_order("Pizza")


############Task

# def process_Order(item, price):
#     def receipt_linee():
#         discount = price * 0.10
#         print(item, price - discount)
#     receipt_linee()
# process_Order("Pizza", 1000)





# ####### file Handling.....
# with open('notes.txt', 'w') as f:
#     f.write('Hello AI Class')
    
# with open ('notes.txt', 'r') as f:
#     content = f.read()
#     print(content)
    
    ####### Task 
subjects = ["Computer", "math", "AI"]
with open("scores.txt", "w")as file:
    for subject in subjects:
        file.write(subject + "\n")
print("Scores .txt with subjects")
        
# #     ######### Task
    
# with open("scores.txt", "r") as file:
#     content = file.read()    
# print("Contant of Score")
# print (content)