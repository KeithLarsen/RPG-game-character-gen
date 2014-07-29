from random import randint

Name = input("Enter your character's name ")

Str = randint (3, 18)
Int = randint (3, 18)
Con = randint (3, 18)
Dex = randint (3, 18)
Wis = randint (3, 18)
Chr = randint (3, 18)

Race = randint (1,4)

Gender = randint (1, 2)

Wizvote = 1 #These are votes, which will allow several factors to be weighed
Fitvote = 1 #By my excuse for an "AI" to pick the best class
Thfvote = 1
Clrvote = 1





#1 for fighter 2 for wizzard 3 for theif 4 for cleric 5 means broken code
Class = "String here"

#Human = 1, Elf = 2, Dwarf = 3, Gnome = 4, Gnuvian = 5
#Modify attributes in regards to race before class is picked


if Race == 2:
    Con = Con - 1
    Chr = Chr + 1
elif Race == 3:
    Con = Con + 1
    Chr = Chr - 1
elif Race == 4:
    Str = Str - 2
    Dex = Dex + 1
    Int = Int + 2



#The voting system gives points to certain canidate outcomes from simple operator
#We can gives some conditions more votes than others if they are more important    
#Fitvotes
if Str > Int:
    Fitvote = int(Fitvote) + 2
else:
    Wizvote = int(Wizvote) + 2
    
if Str > Wis:
    Fitvote = int(Fitvote) + 2
else:
    Clrvote = int(Clrvote) + 2

if Str > Dex:
    Fitvote = int(Fitvote) + 2
else:
    Thfvote = int(Thfvote) + 2

#Wizvotes
#We already did strength versus int, so only two must be weighed
if Int > Wis:
    Wizvote = int(Wizvote) + 2
else:
    Clrvote = int(Clrvote) + 2

if Int > Dex:
    Wizvote = int(Wizvote) + 2
else:
    Thfvote = int(Thfvote) + 2
#Thfvotes

if Dex > Wis:
    Thfvote = int(Thfvote) + 2
else:
    Clrvote = int(Clrvote) + 2

#up until now the contest have all been about picking the highest number
#Now lets make conditions that are secondary numbers
#this vote system is nice and modular so parts of logic can be deleted
#But the system should still work.

#Higher con than dex means fighter or cleric
#Higher dex than con means wizzard or theif
if Con > Dex:
    Clrvote = Clrvote + 1
    Fitvote = Fitvote + 1
else:
    Thfvote = Thfvote + 1
    Wizvote = Wizvote + 1

#High charisma is good for all, but fighter and wizzard

if Chr > Con:
    Thfvote = Thfvote + 1

if Chr > Str:
    Wizvote = Wizvote + 1

if Chr > Dex:
    Clrvote = Clrvote + 1

#High dex is actually better than high chr for a fighter
#But better for a theif

if Dex > Chr:
    Fitvote = Fitvote + 1
else:
    Thfvote = Thfvote + 1


#Now we need to count the votes
#THis block works if there is no tye for the lead.

if Fitvote > Wizvote and Fitvote > Thfvote and Fitvote > Clrvote:
    Class = "Fighter"
    
if Wizvote > Fitvote and Wizvote > Thfvote and Wizvote > Clrvote:
    Class = "Wizzard"

if Thfvote > Fitvote and Thfvote > Wizvote and Thfvote > Clrvote:
    Class = "Theif"

if Clrvote > Fitvote and Clrvote > Wizvote and Clrvote > Thfvote:
    Class = "Cleric"

    

#Results of logic done
print ("You are a ")
if Gender == 1:
    print ("Female")
elif Gender == 2: print ("Male")


if Race == 1: print ("Human")
elif Race == 2: print ("Elf")
elif Race == 3: print ("Dwarf")
elif Race == 4: print ("Gnome")

print (Class)


print ("Strength of", Str,"\n"
       "Dexterity of", Dex,"\n"
       "Intelect of", Int,"\n"
       "Wisdom of", Wis,"\n"
       "Constitution of", Con,"\n"
       "Charismaa of", Chr)
#print ("Fighter", Fitvote, "Wizzard", Wizvote, "Theif", Thfvote, "Cleric", Clrvote) Test function to watch logic
  
