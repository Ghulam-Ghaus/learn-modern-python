# boundries
# 'string text', "string text ", '''string text''', """ string"""
# `string text` type script

name : str = 'Muhammad Qasim'
fname : str = "Muhammad Aslam"
education : str = "Master in Data Science"
age : int = 30

card : str = "PIAIC Student Card\nStudent Name: " + name + "\nAge:" + str(age)

print(card)
print(type(str(age)))