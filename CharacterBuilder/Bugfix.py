#This is the main file
#This is where it all connects to..
import imp
import Laws
import RaceDesc
#This is used to bring in the file from the get-go
#meaning all the info will travel between them
#import Races
#Race info! Not Rascism


#The main aim of this project is to create a simple DnD Character builder
#This may even be useful but I will never know
#Also something something GUI


print('Begin \n')


    
print('')
print('Let\'s start with a race. You can choose any from the following list:')
print(*Laws.race_list, sep='\n')
    

    
while True:
    Laws.user_race = input('\n Race: ').title()
    if Laws.user_race not in Laws.race_list:
        print('That isn\'t a race you can choose!')
        continue

        
    print('')
    imp.reload(RaceDesc)
    print('')

        
    print('Is ', Laws.user_race, ' the race you want?')

    user_response = input('Yes/No/List \n').title()
    if user_response == 'Yes':
        break

    if user_response == 'No':
        continue

    if user_response == 'List':
        print(*Laws.race_list, sep='\n')
        continue

    


    
    


