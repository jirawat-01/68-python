heroes = ['Ironman', 'Thor', 'Hulk', 'Superman', 'Spiderman']
h2 = ['Dr. Strange', 'Cpt. America', 'Black Panther', 'Ant Man']

# Insert ‘Dr. Strange’ at the beginning
heroes.insert(0, h2[0])
print(heroes.index('Thor'))  # Print the index of ‘Thor’

# Insert ‘Cpt. America’ before ‘Thor’
heroes.insert(heroes.index('Thor'), h2[1])
print(heroes)

# Remove ‘Superman’ and append ‘Ant Man’
heroes.remove('Superman')
heroes.append('Ant Man')
print(heroes)

# Sort and reverse the list
heroes.sort()
print(heroes)
heroes.reverse()
print(heroes)

# Assign reference of list to new variable
newheroes = heroes
newheroes[0] = 'Wonder Women'
print(heroes)  # Affects original list because both point to the same list

# Create a copy using list addition
copyheroes = [] + heroes
print(copyheroes)

# Modify copy, original stays unaffected
copyheroes[0] = 'Hanuman'
print(heroes)
print(copyheroes)