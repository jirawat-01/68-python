phonebook = {'Anirach': '777-1111', 'Mickey': '777-2222', 'Donald': '777-3333'}
print(phonebook)

print(phonebook['Mickey'])
print(phonebook.get('Donald'))

Key = 'pluto'
if Key in phonebook:
    print(phonebook['pluto'])
else:
    print(Key + 'not in phonebook')

phonebook['Simpson'] = '777-4567'
phonebook['pluto'] = '777-4444'
phonebook['Mickey'] = '777-2122'
print(phonebook)

del phonebook['Simpson']
print(phonebook)