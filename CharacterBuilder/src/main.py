#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Terry Dullaghan
@date:   27/10/2017
@rev:    1
@lang:   Python 3.6
@deps:   <None>
@desc:   The main file to start this program of witty banter and muchos adventure
"""

#This is the main file
#This is where it all connects to..

import yamlImport

class mainProgram:
    """The main class to start this program of witty banter and muchos adventure
    
    Usage:  The main aim of this project is to create a simple DnD Character builder
            This may even be useful but I will never know
    """
    
    def __init__(self):
        """Pull in the data ready to make an epic adventurer!"""
        self.classes = yamlImport.yamlImport.importYAML("../cfg/Classes.yaml")
        self.races   = yamlImport.yamlImport.importYAML("../cfg/Races.yaml")
        self.law     = yamlImport.yamlImport.importYAML("../cfg/Laws.yaml")
    
    
    def __listRaces(self):
        """Prints all configured races"""
        for key in self.races.keys():
            print(key, sep='\n')

    def __listRaceDetails(self,Race):
        """Prints a races attributes"""
        for key, value in self.races[Race].items():
            print(key, value, sep=':')
    
    def __listClasses(self):
        """Prints all configured classes"""
        for key in self.classes.keys():
            print(key, sep='\n')
    
    def __listClassDetails(self,Class):
        """Prints a classes attributes"""
        print('')
        for key, value in self.classes[Class].items():
            print(key, value, sep=':')
    
    def raceSetup(self):
        """Function allows a user to pick their race"""
        print('Let\'s start with a race. You can choose any from the following list:')
        
        self.__listRaces()
        
        #This is the loop for picking a race
        #A loop is used so that they can keep going back and forth
        #This also lets me give descriptions on each pick
        while True:
            
            #the \n gives me a new line, I just like the format
            user_race = input('\n Race: ').title()
            
            #Safety net to ensure only available races are picked
            if self.races.get(user_race, None) == None:
                print('That isn\'t a race you can choose!')
                continue
            
            #Calls the description of the race
            print('\n',self.races[user_race]["Witty"],'\n')            
            
            #I know what it's asking doens't mean the user does
            print('Is ', user_race, ' the race you want?')
            
            #I couldn't decide how to explain what the options were so this seemed easiest.
            user_response = input('Yes/No/List \n').title()
            
            #This was very witty and slightly complex, then I encountered 2 different bugs
            #So now it just breaks if it's the race they want
            if user_response == 'Yes':
                #Alas the race hath been chosen! Crack on!
                print('')
                return user_race
            
            elif user_response == 'No':
                #Obviously if they say no, they want to re-pick, I haven't made it loop into the
                #main block because I don't want to fill the output with constant lists
                #So "No" just lets them re-pick with a third option for re-veiwing the list
                continue
            
            elif user_response == 'List':
                #This proved to be the easiest way to do this, so "List" just re-prints the list
                #and then goes back to the beginning of the internal block.
                self.__listRaces()
                continue
            
            else:
                #Sassy bitch
                print('I\'ll take that as a no')
                continue
            
    
    def classSetup(self):
        """Function allows a user to pick their class"""
        print('\n With a race chosen, now you need a class! \n')
        
        self.__listClasses()
        
        while True:
            
            user_class = input('\n Class: ').title()
            
            if self.classes.get(user_class, None) == None:
                print('That isn\'t a class you can choose!')
                continue

            self.__listClassDetails(user_class)            
            
            print('\n', 'Is ', user_class, ' the class you want?')
            
            user_response = input('Yes/No/List \n').title()
            
            if user_response == 'Yes':
                return user_class
            
            elif user_response == 'No':
                continue
            
            elif user_response == 'List':
                self.__listClasses()
                continue
            
            else:
                #Still a sassy bitch
                print('I\'ll take that as a no')
                continue
    
    def run(self):
        """Main run method"""
        #I was always bad at openings
        print('Begin \n')
        myRace  = self.raceSetup()
        myClass = self.classSetup()
        print('Youve chosen: ', myRace,myClass)
    
def main():
    run = mainProgram()                     #Initialise the main program
    run.run()                               #Run the mian program

if __name__ == '__main__':main()
