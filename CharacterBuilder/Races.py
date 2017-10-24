#Why is there so many races
#This is the holding file for information on all the races
#I hate this. So much

import Laws
#This means that it will have access to the laws set out in other files


#This shall be long winded and unfun

if Laws.user_race == 'Aarakocra':
    print('Something about being BS')
    Laws.user_stats['Dex'] += 2
    Laws.user_stats['Wis'] += 1
    Laws.user_other_traits.append('Flight')
    Laws.user_other_traits.append('Talons')

    
if Laws.user_race == 'Aasimar':
    print('I always say this wrong')
    Laws.user_stats['Cha'] += 2
    Laws.user_other_traits.append('Darkvision')
    Laws.user_other_traits.append('Celestial')

    
if Laws.user_race == 'Bugbear':
    print('More like HUGbear amirite!')
    Laws.user_stats['Str'] += 2
    Laws.user_stats['Dex'] += 1
    Laws.user_other_traits.append('Darkvision')
    Laws.user_other_traits.append('Long-Limbed')
    Laws.user_other_traits.append('Powerful Build')
    Laws.user_other_traits.append('Sneaky')
    Laws.user_other_traits.append('Surprise Attack')

    
if Laws.user_race == 'Dragonborn':
    print('1 of many edgelord races')
    Laws.user_stats['Str'] += 2
    Laws.user_stats['Cha'] += 1
    Laws.user_other_traits.append('Draconic Ancestry')
    Laws.user_other_traits.append('Breath Weapon')
    Laws.user_other_traits.append('Damage Resistance')

    
if Laws.user_race == 'Dwarf':
    print('Staples')
    Laws.user_stats['Con'] += 2
    Laws.user_other_traits.append('Darkvision')
    Laws.user_other_traits.append('Dwarven Resilience')
    Laws.user_other_traits.append('Dwarven Combat Training')
    Laws.user_other_traits.append('Stonecunning')
    
    
if Laws.user_race == 'Elf':
    print('Even more Staples')
    Laws.user_stats['Dex'] += 2
    Laws.user_other_traits.append('Darkvision')
    Laws.user_other_traits.append('Keen Senses')
    Laws.user_other_traits.append('Fey Ancestry')
    Laws.user_other_traits.append('Trance')

    
if Laws.user_race == 'Feral Tiefling':
    print('Why is there "Feral" at the front')
    Laws.user_stats['Dex'] += 2
    Laws.user_stats['Int'] += 1
    Laws.user_other_traits.append('Darkvision')
    Laws.user_other_traits.append('Hellish Resistance')
    Laws.user_other_traits.append('Infernal')
    
    
if Laws.user_race == 'Firbolg':
    print('I don\'t know what this is...')
    Laws.user_stats['Str'] += 2
    Laws.user_stats['Dex'] += 1
    Laws.user_other_traits.append('Firbolg')

    
if Laws.user_race == 'Genasi':
    print('I say this one wrong too')
    Laws.user_stats['Con'] += 2
    

    
if Laws.user_race == 'Gnome':
    print('Gnomeo oh Gnomeo where art thou my Gnomeo')
    Laws.user_stats['Int'] += 2
    Laws.user_other_traits.append('Darkvision')
    Laws.user_other_traits.append('Gnome Cunning')

    
if Laws.user_race == 'Goblin':
    print('This is an enemy not a race')
    Laws.user_stats['Dex'] += 2
    Laws.user_stats['Con'] += 1
    Laws.user_other_traits.append('Darkvision')
    Laws.user_other_traits.append('Fury of the Small')
    Laws.user_other_traits.append('Nimble Escape')

    
if Laws.user_race == 'Goliath':
    print('Large individual')
    Laws.user_stats['Str'] += 2
    Laws.user_stats['Con'] += 1
    Laws.user_other_traits.append('Natural Athlete')
    Laws.user_other_traits.append('Stone\'s Endurance')
    Laws.user_other_traits.append('Powerful Build')
    Laws.user_other_traits.append('Mountain Born')

    
if Laws.user_race == 'Half-Elf':
    print('Half-this, half-that, whole lot of uselessness')
    Laws.user_stats['Cha'] += 2
    Laws.user_other_traits.append('Darkvision')
    Laws.user_other_traits.append('Fey Ancestry')
    Laws.user_other_traits.append('Skill Versatility')

    
if Laws.user_race == 'Halfling':
    print('Half-a-thing!')
    Laws.user_stats['Dex'] += 2
    Laws.user_other_traits.append('Lucky')
    Laws.user_other_traits.append('Brave')
    Laws.user_other_traits.append('Halfling Nimbleness')

    
if Laws.user_race == 'Half-Orc':
    print('Half the practicality, twice the angst')
    Laws.user_stats['Str'] += 2
    Laws.user_stats['Con'] += 1
    Laws.user_other_traits.append('Darkvision')
    Laws.user_other_traits.append('Menacing')
    Laws.user_other_traits.append('Relentless')
    Laws.user_other_traits.append('Endurance')
    Laws.user_other_traits.append('Savage Attack')

    
if Laws.user_race == 'Hobgoblin':
    print('Somehow better than Goblins')
    Laws.user_stats['Con'] += 2
    Laws.user_stats['Int'] += 1
    Laws.user_other_traits.append('Darkvision')
    Laws.user_other_traits.append('Martial Training')
    Laws.user_other_traits.append('Saving Face')

    
if Laws.user_race == 'Human':
    print('Also BS because science')
    Laws.user_stats['Str'] += 1
    Laws.user_stats['Dex'] += 1
    Laws.user_other_traits.append('Extra Language')

    
if Laws.user_race == 'Kenku':
    print('Like edgy but with more(?) RP')
    Laws.user_stats['Dex'] += 2
    Laws.user_stats['Wis'] += 1
    Laws.user_other_traits.append('Expert Forgery')
    Laws.user_other_traits.append('Kenku Training')
    Laws.user_other_traits.append('Mimicry')

    
if Laws.user_race == 'Kobald':
    print('Not what people think they are')
    Laws.user_stats['Str'] -= 2
    Laws.user_stats['Dex'] += 2
    Laws.user_other_traits.append('Darkvision')
    Laws.user_other_traits.append('Grovel, Cower, and Beg')
    Laws.user_other_traits.append('Pack Tactics')
    Laws.user_other_traits.append('Sunlight Sensitivity')

    
if Laws.user_race == 'Lizardfolk':
    print('I\'m running out of creativity')
    Laws.user_stats['Con'] += 2
    Laws.user_stats['Wis'] += 1
    Laws.user_other_traits.append('Bite')
    Laws.user_other_traits.append('Cunning Artisan')
    Laws.user_other_traits.append('Hold Breath')
    Laws.user_other_traits.append('Hunte\'s Lore')
    Laws.user_other_traits.append('Natural Armour')

    
if Laws.user_race == 'Orc':
    print('AngstAngstAngstRageAngst')
    Laws.user_stats['Str'] += 2
    Laws.user_stats['Con'] += 1
    Laws.user_stats['Int'] -= 2
    Laws.user_other_traits.append('Darkvision')
    Laws.user_other_traits.append('Aggressive')
    Laws.user_other_traits.append('Menacing')
    Laws.user_other_traits.append('Powerful Build')
    

    
if Laws.user_race == 'Tabaxi':
    print('Literally a race from Skyrim')
    Laws.user_stats['Dex'] += 2
    Laws.user_stats['Cha'] += 1
    Laws.user_other_traits.append('Darkvision')
    Laws.user_other_traits.append('Feline Agility')
    Laws.user_other_traits.append('Cat\'s Claws')
    Laws.user_other_traits.append('Cat\'s Talent')

    
if Laws.user_race == 'Tiefling':
    print('I had this already?')
    Laws.user_stats['Cha'] += 2
    Laws.user_stats['Int'] += 1
    Laws.user_other_traits.append('Darkvision')
    Laws.user_other_traits.append('Hellish Resistance')
    Laws.user_other_traits.append('Infernal Legacy')

    
if Laws.user_race == 'Tortle':
    print('What\'t not to love!')
    Laws.user_stats['Str'] += 2
    Laws.user_stats['Wis'] += 1
    Laws.user_other_traits.append('Claws')
    Laws.user_other_traits.append('Hold Breath')
    Laws.user_other_traits.append('Natural Armour')
    Laws.user_other_traits.append('Shell Defense')
    Laws.user_other_traits.append('Survival Instinct')

    
if Laws.user_race == 'Triton':
    print('Fish people?')
    Laws.user_stats['Str'] += 1
    Laws.user_stats['Con'] += 1
    Laws.user_stats['Cha'] += 1
    Laws.user_other_traits.append('Amphibious')
    Laws.user_other_traits.append('Control Air and Water')
    Laws.user_other_traits.append('Emissary of the Sea')
    Laws.user_other_traits.append('Guardians of the Depths')

    
if Laws.user_race == 'Yuan-ti Pureblood':
    print('Snake people')
    Laws.user_stats['Cha'] += 2
    Laws.user_stats['Int'] += 1
    Laws.user_other_traits.append('Darkvision')
    Laws.user_other_traits.append('Innate Spellcasting')
    Laws.user_other_traits.append('Magic Resistance')
    Laws.user_other_traits.append('Poison Imminity')
    

#I have done it this way, mostly because I don't know any other way
#and because this is suppposedly the correct way?
#My god it was long though
