vowels = ["A","E", "I", "O", "U"]
consonants = ["B", "C", "D", "F","G", "H" ]

my_list = [vowels,consonants]
print(my_list) 

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

print(dirty_dozen[0]) #from the nested list this prints the first list 
print(dirty_dozen[1])

print(dirty_dozen[0][2])# from the nested list it selects f=first list and then the item present on the 2th index 
print(dirty_dozen[1][1])