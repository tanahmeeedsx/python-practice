#Python program

#Data types
print("we are learning python, it is awesome") #str
print(6/3) #int
print(7/2) #float
print(5>4) #bool

fruits=['apple', 'banana', 'cherry'] #list
print(fruits) #list
list=['apple', '2', '3', '4', 'True'] #list
print(list) #list

#Dictionary
x={
    "name": "John", #key: value
    "age": 30,
}
print(x) #Dictionary    

list1=['apple', 'banana', 'cherry'] #list

print(list1[0]) 


#typecasting
x = 20
y = ('10')
sum = str(x) + (y)
print(sum)

#string interpolation

name = "Tomal"
age = "25"
bio = f"My name is {name}, and My age is {age}"
# print(bio)
# print(f"His name is {name}, and his age is {age}")
bio = "My name i {}, and my age is {}".format(name,age) #dot_format
print(bio)


#user_input

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")

full_name = f_name + " " + l_name
print(full_name)