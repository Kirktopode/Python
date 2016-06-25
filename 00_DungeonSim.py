import random

class Creature(object):


    

    hp = 1
    atk = 0
    ac = 13
    gp = 0
    size = 1

    def __init__(self):
        pass

    def loot(self, target):
        if target.gp > 0:
            self.gp += target.gp
            print "{} has taken {} gold pieces from the body of {}.".format(self.name, target.gp, target.name)
            target.gp = 0

   # def death(self):
        #this shouldn't remove the object from lists, but should make it unable to act

    def eaten(self, eater):
        print "{} has eaten {}.".format(eater.name, self.name)
        #remove the object from lists in order to free up memory space and clean up random corpses

class Goblin(Creature):

    atk = 2
    ac = 14
    starve = 0
    size = 2
    species = "goblin"

    def __init__(self):
        self.hp = random.randint(1,8)
        self.name = gobnamer(gobnamelist) # Pass the namelist to the function so I can make sure that all the names are unique.
        self.gp = random.randint(2, 8)
        self.location = randomroom(rooms)

    def attack(self, target):
        if self.hp < 1:
            return
        atkwords = ["lunges at", "tries to bite", "jabs at", "claws at"]
        print "{} the {} {} {} the {}.".format(self.name, self.species, atkwords[random.randint(0, 3)], target.name, target.species)
        if random.randint(1, 20) + self.atk >= target.ac:
            dmg = random.randint(1,5)
            target.hp -= dmg
            if target.hp < 1:
                print "{} has killed {}!".format(self.name, target.name)
            else:
                print "{} has struck {} for {} damage!".format(self.name, target.name, dmg)
        else:
            print "{} misses.".format(self.name)

    def eat(self, target):
        target.size -= 1
        self.starve -= 1
        self.hp += 1
        if target.size < 0:
            target.eaten()
            print "{} has eaten {}.".format(self.name, target.name)
            return
        print "{} has eaten part of {}.".format(self.name, target.name)

    def fight(self):
        manlist = []
        glist = []
        for creature in dungeon[self.location]:
            if creature.species == "goblin":
                glist.append(creature)
            if creature.species == "adventurer":
                manlist.append(creature)
        while not alldead(glist) and not alldead (manlist):
            for creature in glist:
                if alldead(manlist): break
                t = manlist[random.randint(0, len(manlist)-1)]
                while t.hp < 1:
                    t = manlist[random.randint(0, len(manlist)-1)]
                creature.attack(t)
            for man in manlist:
                if alldead(glist): break
                t = glist[random.randint(0, len(glist)-1)]
                while t.hp < 1:
                    t = glist[random.randint(0, len(glist)-1)]
                man.attack(t)
        if alldead(glist):
            print "The adventurers have won the battle and take their spoils!"
            for creature in glist:
                m = manlist[random.randint(0, len(manlist)-1)]
                while m.hp < 1:
                    m = manlist[random.randint(0, len(manlist)-1)]
                m.loot(creature)
            for creature in manlist:
                if creature.hp < 1:
                    print "The adventurers mourn their fallen comrade, {}, but they also rifle through their pockets".format(creature.name)
                    for man in manlist:
                        if man.hp > 1:
                            man.loot(creature)
        elif alldead(manlist):
            print "The goblins have won the battle and take their spoils!"
            for creature in manlist:
                g = glist[random.randint(0, len(glist)-1)]
                while g.hp < 1:
                    g = glist[random.randint(0, len(glist)-1)]
                g.loot(creature)
            for creature in glist:
                if creature.hp < 1:
                    print "The goblins mourn their fallen clanmate, {}, before taking his shinies.".format(creature.name)
                    for gob in glist:
                        if gob.hp > 1:
                            gob.loot(creature)
                            break



    #def hunt(self):
        #This should facilitate the goblins' search for corpses and rats to eat

    def hunt(self):
        if self.hp < 1:
            return
        if self.starve >= 3 and not contains_food(dungeon[self.location]):     
            if self.location in rooms:
                print "{} is leaving {} and entering the halls.".format(self.name, self.location)
                dungeon[self.location].pop(dungeon[self.location].index(self))
                dungeon["the halls"].append(self)
                self.location = "the halls"
            else:
                destination = randomroom(rooms)
                print "{} is leaving the halls and entering {}.".format(self.name, destination)
                dungeon["the halls"].pop(dungeon["the halls"].index(self))
                dungeon[destination].append(self)
                self.location = destination
        elif contains_food(dungeon[self.location]):
            if self.starve > -2:
                found = False
                for creature in dungeon[self.location]:
                    if creature.hp < 1 and creaure.size > 0:
                        self.eat(creature)
                        found = True
                        break
                if found = True: return
                for creature in dungeon[self.location]:
                    if creature.type == "rat":
                        print "{} tries to catch {}.".format(self.name, creature.name)
                        if random.randint(1,20) + self.atk >= creature.ac:
                            print "{} catches and eats {}!".format(self.name, creature.name)
                            self.eat(creature)
                        else:
                            print "{} fails.".format(self.name)
                            
            
                

class Rat(Creature):

    species = "rat"
    name = "a rat"
    size = 1

    def __init__(self):
        self.location = randomplace(self, dungeon.keys())

    #def roam(self):
        #This causes rats to go where they are least likely to find danger.
        #Rats are good at avoiding the gelatinous cube

class Adventurer(Creature):

    species = "adventurer"
    size = 3
    location = "the halls"

    def __init__(self):

        self.name = adventurernamer(adventurernamelist) #Same idea as with the gobname generator
        self.hp = 10 + random.randint(-2,2)
        self.atk = random.randint(0, 4)
        self.ac = 15 + random.randint(-2,2)
        self.gp = random.randint(10, 15)

    def attack(self, target):
        if self.hp < 1:
            return
        atkwords = ["swings at", "attacks", "attempts to smite", "thrusts at"]
        print "{} the {} {} {} the {}.".format(self.name, self.species, atkwords[random.randint(0, 3)], target.name, target.species)
        if random.randint(1, 20) + self.atk >= target.ac:
            dmg = random.randint(2,9)
            target.hp -= dmg
            if target.hp < 1:
                #target.death() I think I will use this to change an object's type to "corpse"
                print "{} has killed {}!".format(self.name, target.name)
            else:
                print "{} has struck {} for {} damage!".format(self.name, target.name, dmg)
        else:
            print "{} misses.".format(self.name)

    def hunt(self): # My current task is to design the Adventurer Hunt method. ###

    def fight(self):
        manlist = []
        glist = []
        for creature in dungeon[self.location]:
            if creature.species == "goblin":
                glist.append(creature)
            if creature.species == "adventurer":
                manlist.append(creature)
        while not alldead(glist) and not alldead (manlist):
            for man in manlist:
                if alldead(glist): break
                t = glist[random.randint(0, len(glist)-1)]
                while t.hp < 1:
                    t = glist[random.randint(0, len(glist)-1)]
                man.attack(t)
            for creature in glist:
                if alldead(manlist): break
                t = manlist[random.randint(0, len(manlist)-1)]
                while t.hp < 1:
                    t = manlist[random.randint(0, len(manlist)-1)]
                creature.attack(t)
        if alldead(glist):
            print "The adventurers have won the battle and take their spoils!"
            for creature in glist:
                m = manlist[random.randint(0, len(manlist)-1)]
                while m.hp < 1:
                    m = manlist[random.randint(0, len(manlist)-1)]
                m.loot(creature)
            for creature in manlist:
                if creature.hp < 1:
                    print "The adventurers mourn their fallen comrade, {}, but they also rifle through their pockets".format(creature.name)
                    for man in manlist:
                        if man.hp > 1:
                            man.loot(creature)
        elif alldead(manlist):
            print "The goblins have won the battle and take their spoils!"
            for creature in manlist:
                g = glist[random.randint(0, len(glist)-1)]
                while g.hp < 1:
                    g = glist[random.randint(0, len(glist)-1)]
                g.loot(creature)
            for creature in glist:
                if creature.hp < 1:
                    print "The goblins mourn their fallen clanmate, {}, before taking his shinies.".format(creature.name)
                    for gob in glist:
                        if gob.hp > 1:
                            gob.loot(creature)
                            break

   # def raid(self):

class GelatinousCube(Creature):

    species = "Gelatinous Cube"
    name = "The Gelatinous Cube"
    hp = 50
    ac = 5
    location = "the halls"

    def __init__(self):

        self.gp = random.randint(15,50)

    #def engulf(self, target):
        
        
def adventurernamer(namelist): #Generate adventurer names with this
    syl1 = ("Vael", "Ned", "Arn", "Bol", "Shan", "Mur", "Kal", "Zin", "Erst", "Wil", "War", "Dael", "Fen", "Gaur", "Hoen", "Jaal", "Leon", "Pan", "Ruan")
    syl2 = ("wick", "mar", "lan", "iam", "ias", "dir", "mis", "han", "gas", "thas", "ran", "kaz", "saar", "ter", "par", "ven")
    epith = ("Righteous", "Radiant", "Foolish", "Wise", "Mighty", "Feeble", "Incompetent", "Incontinent", "Brave", "Pansy", "Cupcake", "Cuddly", "Vain", "Skullcleaver", "Beautiful", "Generally Unpleasant", "Misunderstood", "Unintelligible", "Angry", "Sad", "Hungry", "Omniscient", "Violent", "Robber", "Racist", "Schizophrenic", "Misogynist", "Misandrist", "Baker")
    name = syl1[random.randint(0, len(syl1)-1)] + syl2[random.randint(0, len(syl2)-1)] + " the " + epith[random.randint(0, len(epith)-1)]
    return name

def gobnamer(namelist): #As above, but with goblin names
    con = ("b", "f", "g", "k", "l", "m", "n", "p", "r", "d", "t", "v", "y", "z", "sh", "ch")
    vow = ("a", "e", "i", "o", "u")
    name = con[random.randint(0, len(con)-1)] + vow[random.randint(0, len(vow)-1)] + con[random.randint(0, len(con)-1)]
    name = name.capitalize()
    while name in namelist:
        name = "Other {}".format(name)
    return name

def randomroom(placelist):
    room = placelist[random.randint(0,len(placelist)-1)]
    return room

def contains_food(place):
    for creature in place:
        if creature.hp < 1 or creature.species == "rat":
            return True
    return False

def adventurer_spawn():
    for i in range(random.randint(2, 5)):
        dude = Adventurer()
        adventurerlist.append(dude)
        dungeon["the halls"].append(dude)
        print "{} has entered the dungeon. Goblins beware!".format(dude.name)

def alldead(creaturelist):
    for creature in creaturelist:
        if creature.hp > 0:
            return False
    return True

cube = GelatinousCube()

rooms = ("the north room", "the west room", "the east room", "the south room", "the central room")
dungeon = {"the north room":[], "the west room":[], "the east room":[], "the south room":[], "the central room":[], "the halls":[cube]}
gobnamelist = []
adventurernamelist = []
goblist = []
adventurerlist = []

for i in range(random.randint(15, 25)):
    gob = Goblin()
    goblist.append(gob)
    gobnamelist.append(gob.name)
    dungeon[gob.location].append (gob)
    
    print "{} the {} has been spawned in {}.".format(gob.name, gob.species, gob.location)

    



