list=['ali','ahmed','aya','rasha']
name=input('Enter your name:')
grade=int(input('Enter your grade:'))
if grade >= 60:
    print("graduated")
    list.append(name)
    print(list)
else:
    print("you are not graduated")
    
