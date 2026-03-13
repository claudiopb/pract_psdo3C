####### encuentra y cambia elemento de un arreglo

listOfNames = ['Jones','Jill','Lisa','Stan','Bob','Alice']

print(listOfNames)

print('######## for #####')

for i in range(len(listOfNames)):
  print(listOfNames[i])
  if listOfNames[i] == 'Jill':
    print('Encontro a Jill')
    listOfNames[i] = 'Gilberto'
  elif listOfNames[i] == 'Alice':
    print('Encontro a Alice')
    listOfNames[i] = 'Alicia'

print (listOfNames)