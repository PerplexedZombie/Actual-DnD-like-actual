#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Terry Dullaghan
@date:   27/10/2017
@rev:    1
@lang:   Python 3.6
@deps:   <None>
@desc:   Laws, settings, same thing but more adventure!
"""

#This is the settings folder
#I've named it Laws because apparently 'Settings' is taken
#Who names their files 'Settings' anyway

user_race = ''
user_class = ''
#These are all placeholders for when they come up in the main file


race_list = ['Aarakocra', 'Aasimar', 'Bugbear', 'Dragonborn', 'Dwarf', 'Elf',
             'Feral Tiefling', 'Firbolg', 'Genasi', 'Gnome', 'Goblin', 'Goliath',
             'Half-Elf', 'Halfling', 'Half-Orc', 'Hobgoblin', 'Human', 'Kenku',
             'Kobold', 'Lizardfolk', 'Orc', 'Tabaxi', 'Tiefling', 'Tortle',
             'Triton', 'Yuan-ti Pureblood']
#The race list to make it easier to call and check
#Do I really want to code all this, because there is more there than anticipated...

class_list = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin',
              'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
#Same idea but for class

#Things that will come to fruition in the end
user_stats = {'Str':0, 'Dex':0, 'Con':0, 'Int':0, 'Wis':0, 'Cha':0}
#The stats

user_HP = 0
#User's final HP at level 1

user_AC = 0
#User's AC assuming no Armour.. maybe?

user_spd = 0
#User's Speed, quite straight forward

user_initiative = 0
#I haven't abbreviated initiative because I haven't

user_hit_die = 0
#The user's Hit dice

user_other_traits = []
#Other racial/class traits to be listed
