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

import Laws
#This is used to bring in the file from the get-go
#meaning all the info will travel between them

import RaceDesc
import ClassDesc
#Race info! Not Rascism and Class info! Not Classism..?
#Also because import is silly I need to reimport on every run to ensure witty comments

import imp
#I need this to reimport RaceDesc and ClassDesc so it runs everytime it passes over them


class mainProgram:
    """The main class to start this program of witty banter and muchos adventure
    
    Usage:  The main aim of this project is to create a simple DnD Character builder
            This may even be useful but I will never know
    """
    
    def __init__(self):
        """Placeholder ready to setup some nice shiney objects!"""
        pass
    
    def run(self):
        """Where all the magic happens, or not depending on your race!"""
        print('Begin \n')
        #I was always bad at openings
        
        
        # ---------------- Race Setup ----------------    
        print('')
        print('Let\'s start with a race. You can choose any from the following list:')
        print(*Laws.race_list, sep='\n')
            
        while True:
            #This is the loop for picking a race
                
            #A loop is used so that they can keep going back and forth
            #This also lets me give descriptions on each pick
                
            Laws.user_race = input('\n Race: ').title()
            #the \n gives me a new line, I just like the format
            
            if Laws.user_race not in Laws.race_list:
                print('That isn\'t a race you can choose!')
                continue
            #Safety net to ensure only available races are picked
            #also .titled() for simplicity
                
            print('')
            imp.reload(RaceDesc)
            #This means everytime we pass over this it re loads the module
            print('')
            #Calls the description of the race
                
            print('Is ', Laws.user_race, ' the race you want?')
            #I know what it's asking doens't mean the user does
            user_response = input('Yes/No/List \n').title()
            #I couldn't decide how to explain what the options were so this seemed easiest.
            if user_response == 'Yes':
                print('')
                break
            #This was very witty and slightly complex, then I encountered 2 different bugs
            #So now it just breaks if it's the race they want
                
            if user_response == 'No':
                continue
            #Obviously if they say no, they want to re-pick, I haven't made it loop into the
            #main block because I don't want to fill the output with constant lists
            #So "No" just lets them re-pick with a third option for re-veiwing the list
        
            if user_response == 'List':
                print(*Laws.race_list, sep='\n')
                continue
            #This proved to be the easiest way to do this, so "List" just re-prints the list
            #and then goes back to the beginning of the internal block.
                
            
            if user_response == 'List':
                continue
            #The list catch, if someone said "List" then it can bring them back around
        
            else:
                print('I\'ll take that as a no')
                continue
            ##Sassy bitch
               
            
        # ---------------- Class Setup ----------------
        print('\n With a race chosen, now you need a class! \n')
        print(*Laws.class_list, sep='\n')
        
        #This will be another while loop
        #infact this will be pretty indentical but with classes instead of races
        while True:
            Laws.user_class = input('\n Class: ').title()
            if Laws.user_class not in Laws.class_list:
                print('That isn\'t a class you can be!')
                continue
        
            print('')
            imp.reload(ClassDesc)
            print('')
        
            print('Is ', Laws.user_class, ' the class you want?')
            #See above
        
            user_response = input('Yes/No/List \n').title()
            #Copied and pasted so everything going forward is the same
            
            if user_response == 'Yes':
                break
                
            if user_response == 'No':
                continue
        
            if user_response == 'List':
                print(*Laws.class_list, sep='\n')
                continue
                
            if user_response == 'List':
                continue
        
            else:
                print('I\'ll take that as a no')
                continue
            ##Still a sassy bitch
    
    
def main():
    run = mainProgram()                     #Initialise the main program
    run.run()                               #Run the mian program

if __name__ == '__main__':main()