# --------------
# Code starts here

# Create the lists 
class1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class2=['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class=class1 + class2
print(new_class)

# Append the list
new_class.append('Peter Warden')
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)


# Create the Dictionary
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}


# Slice the dict and stores  the all subjects marks in variable
total=sum(courses.values())

# Store the all the subject in one variable `Total`

# Print the total
print(total)
# Insert percentage formula
percentage= total/500*100
# Print the percentage
print(percentage)



# Create the Dictionary
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}
max_marks_scored=max(mathematics,key=mathematics.get)
print(max_marks_scored)


# Given string
topper= max_marks_scored
topper.split()
first_name=topper.split()[0]
second_name=topper.split()[1]
full_name= second_name+' '+first_name
certificate_name= full_name.upper()
print(certificate_name)

# Create variable first_name 

# Create variable Last_name and store last two element in the list

# Concatenate the string

# print the full_name

# print the name in upper case

# Code ends here


