import random
# you can change the name of the file, but IT MUST be in the same folder as this program
fichier = open("char-sheet.txt", "a")

# definitions character race
# nb : no distinction between high elf and wood elf, nor between mountain dwarf and hill dwarf

races = ['Dwarf', 'Elf', 'Halfling', 'Human']
sexes = ['Male', 'Female']
stats = [0, 0, 0, 0, 0, 0]
classes = ['Cleric', 'Warrior', 'Rogue', 'Wizard']
moral = ['Good', 'Neutral', 'Evil']
attitude = ['Lawful', 'Neutral', 'Chaotic']


# definition of stats
# 4 d6 and we keep the best 3
def _stat():
    dice_a = random.randint(1, 6)
    dice_b = random.randint(1, 6)
    dice_c = random.randint(1, 6)
    dice_d = random.randint(1, 6)
    _stat = [dice_a, dice_b, dice_c, dice_d]
    _stat.sort()
    del _stat[0]
    return int(sum(_stat))


# for each stat give a value


for i in range(0, 6):
    if stats[i] == 0:
        stats[i] = _stat()

# define race

r = random.randint(0, 3)
race = races[r]


# define sex

s = random.randint(0, 1)
sex = sexes[s]


m = random.randint(0, 2)
a = random.randint(0, 2)
alignment = [attitude[a], moral[m]]

# Define name

# Dwarf names
dwarf_male_names = ['Adrik', 'Alberich', 'Baern', 'Barendd', 'Brottor',
                    'Bruenor', 'Dain', 'Darrak', 'Delg', 'Eberk', 'Einkil',
                    'Fargrim', 'Flint', 'Gardain', 'Harbek', 'Kildrak',
                    'Morgran', 'Orsik', 'Oskar', 'Rangrim', 'Rurik',
                    'Taklinn', 'Thoradin', 'Thorin', 'Tordek',
                    'Traubon', 'Travok', 'Ulfgar', 'Veit', 'Vondal']

dwarf_female_names = ['Amber', 'Artin', 'Audhild', 'Bardryn', 'Dagnal',
                      'Diesa', 'Eldeth', 'Falkrunn', 'Finellen', 'Gunnloda',
                      'Gurdis', 'Helja', 'Hlin', 'Kathra', 'Kristryd', 'Ilde',
                      'Liftrasa', 'Mardred', 'Riswynn', 'Sannl', 'Torbera', 'Torgga', 'Vistra']

dwarf_clan_names = ['Balderk', 'Battlehammer', 'Brawnanvil',
                    'Dankil', 'Fireforge', 'Frostbeard', 'Gorunn',
                    'Holderhek', 'Ironfist', 'Loderr', 'Lutgehr',
                    'Rumnaheim', 'Strakeln', 'Torunn', 'Ungart']

# Elf Names
elf_male_names = ['Adran', 'Aelar', 'Aramil', 'Arannis',
                  'Aust', 'Beiro', 'Berrian', 'Carric',
                  'Enialis', 'Erdan', 'Erevan', 'Galinndan',
                  'Hadarai', 'Heian', 'Himo', 'Immeral',
                  'Ivellios', 'Laucian', 'Mindartis', 'Paelias',
                  'Peren', 'Quarion', 'Riardon', 'Rolen',
                  'Soveliss', 'Thamior', 'Tharivol', 'Theren', 'Varis']

elf_female_names = ['Adrie', 'Althaea', 'Anastrianna', 'Andraste',
                    'Antinua', 'Bethrynna', 'Birel', 'Caelynn', 'Drusilia',
                    'Enna', 'Felosial', 'Ielenia', 'Jelenneth', 'Keyleth',
                    'Leshanna', 'Lia', 'Meriele', 'Mialee', 'Naivara',
                    'Quelenna', 'Quillathe', 'Sariel', 'Shanairra', 'Shava',
                    'Silaqui', 'Theirastra', 'Thia', 'Vadania', 'Valanthe', 'Xanaphia']

elf_family_names = ['Amakiir Gemflower', 'Amastacia Starflower',
                    'Galanodel Moonwhisper', 'Holimion Diamonddew',
                    'Ilphelkiir Gemblossom', 'Liadon Silverfrond',
                    'Meliamne Oakenheel', 'Naïlo Nightbreeze',
                    'Siannodel Moonbrook', 'Xiloscient Goldpetal']

# Halfling names
halfling_male_names = ['Alton', 'Ander', 'Cade', 'Corrin', 'Eldon', 'Errich',
                       'Finnan', 'Garret', 'Lindal', 'Lyle', 'Merric', 'Milo',
                       'Osborn', 'Perrin', 'Reed', 'Roscoe', 'Wellby']
halfling_female_names = ['Andry', 'Bree', 'Callie', 'Cora', 'Euphemia', 'Jillian',
                         'Kithri', 'Lavinia', 'Lidda', 'Merla', 'Nedda', 'Paela',
                         'Portia', 'Seraphina', 'Shaena', 'Trym', 'Vani', 'Verna']

halfling_family_names = ['Brushgather', 'Goodbarrel', 'Greenbottle',
                         'High-hill', 'Hilltopple', 'Leagallow', 'Tealeaf',
                         'Thorngage', 'Tosscobble', 'Underbough']

# Human names (Calishite only but you can change the name list)
human_male_names = ['Aseir', 'Bardeid', 'Haseid',
                    'Khemed', 'Mehmen', 'Sudeiman', 'Zasheir']
human_female_names = ['Atala', 'Ceidil', 'Hama', 'Jasmal', 'Meilil',
                      'Seipora', 'Yasheira', 'Zasheida']
human_family_names = ['Basha', 'Dumein', 'Jassan', 'Khalid',
                      'Mostana', 'Pashar', 'Rein']

if race == "Dwarf" and sex == "Male":
    f_n = random.randint(0, (len(dwarf_male_names) - 1))
    first_name = dwarf_male_names[f_n]
    s_n = random.randint(0, (len(dwarf_clan_names) - 1))
    second_name = dwarf_clan_names[s_n]

elif race == "Dwarf" and sex == "Female":
    f_n = random.randint(0, (len(dwarf_female_names) - 1))
    first_name = dwarf_female_names[f_n]
    s_n = random.randint(0, (len(dwarf_clan_names) - 1))
    second_name = dwarf_clan_names[s_n]

elif race == "Elf" and sex == "Male":
    f_n = random.randint(0, (len(elf_male_names) - 1))
    first_name = elf_male_names[f_n]
    s_n = random.randint(0, (len(elf_family_names) - 1))
    second_name = elf_family_names[s_n]

elif race == "Elf" and sex == "Female":
    f_n = random.randint(0, (len(elf_female_names) - 1))
    first_name = elf_female_names[f_n]
    s_n = random.randint(0, (len(elf_family_names) - 1))
    second_name = elf_family_names[s_n]

elif race == "Halfling" and sex == "Male":
    f_n = random.randint(0, (len(halfling_male_names) - 1))
    first_name = elf_male_names[f_n]
    s_n = random.randint(0, (len(halfling_family_names) - 1))
    second_name = halfling_family_names[s_n]

elif race == "Halfling" and sex == "Female":
    f_n = random.randint(0, (len(halfling_female_names) - 1))
    first_name = halfling_female_names[f_n]
    s_n = random.randint(0, (len(halfling_family_names) - 1))
    second_name = halfling_family_names[s_n]

# if you add another race do it here with the same pattern new race_female_names
# new race_male_names, new race_family_names don't forget to create these lists before line 149

elif race == "Human" and sex == "Female":
    f_n = random.randint(0, (len(human_female_names) - 1))
    first_name = human_female_names[f_n]
    s_n = random.randint(0, (len(human_family_names) - 1))
    second_name = human_family_names[s_n]

# if human male (last choice)

else:
    f_n = random.randint(0, (len(human_male_names) - 1))
    first_name = human_male_names[f_n]
    s_n = random.randint(0, (len(human_family_names) - 1))
    second_name = human_family_names[s_n]

# Let's print our name in capital letters
first_name = first_name.upper()
second_name = second_name.upper()


# race modifier note : race modifier does not take sub-races in account.
# if you add sub-races change the modifier

human = [1, 1, 1, 1, 1, 1]
dwarf = [2, 0, 2, 0, 1, 0]
elf = [0, 2, 0, 1, 1, 0]
halfling = [0, 2, 1, 0, 0, 1]

# race modifier for speed
human_speed = 30
dwarf_speed = 25
elf_speed = 30
halfling_speed = 25

# list of cantrips and spells : if you add a new spell class, write the cantrips here in the same way
# because some races (ex : elfs) can use cantrips
# and it is easier to have all the lists in the same place (ex : spells of second level could be
# written here as "wizard_spells_2"

wizard_cantrip = ["Acid Splash", "Dancing Lights", "Fire Bolt", "Light", "Mage Hand",
                  "Minor Illusion", "Poison Spray", "Prestidigitation", "Ray of Frost", "Shocking Grasp"]
wizard_spells = ["Burning Hands", "Charm Person", "Comprehend Languages", "Detect Magic", "Disguise Self",
                 "Identify", "Mage Armor", "Magic Missile", "Shield", "Silent Image", "Sleep", "Thunderwave"]
cleric_cantrip = ["Guidance", "Light", "Resistance", "Sacred Flame", "Spare the Dying", "Thaumaturgy"]
cleric_spells = ["Bless", "Command", "Cure Wounds", "Detect Magic", "Guiding Bolt", "Healing Word",
                 "Inflict Wounds", "Sanctuary", "Shield of Faith"]

res_lt = [0, 0, 0, 0, 0, 0]

if race == "Human":
    for x in range(0, 6):
        res_lt[x] = stats[x] + human[x]
    speed = human_speed
    weight = 110 + (random.randint(1, 4) + random.randint(1, 4))
    heigth = 56 + (random.randint(1, 10) + random.randint(1, 10))

if race == "Dwarf":
    for x in range(0, 6):
        res_lt[x] = stats[x] + dwarf[x]
    speed = dwarf_speed
    weight = 115 + (random.randint(1, 6) + random.randint(1, 6))
    heigth = 42 + (random.randint(1, 4) + random.randint(1, 4))

if race == "Elf":
    for x in range(0, 6):
        res_lt[x] = stats[x] + elf[x]
    speed = elf_speed
    weight = elf_weight = 90 + random.randint(1, 4)
    height = 48 + (random.randint(1, 10) + random.randint(1, 10))

else:
    # race == "Halfling":
    for x in range(0, 6):
        res_lt[x] = stats[x] + halfling[x]
    speed = halfling_speed
    weight = 35
    height = 31 + (random.randint(1, 4) + random.randint(1, 4))

# define armor class

d_m = int((res_lt[1] - 10)//2)
armor = 10 + d_m

# change height in metres
height_m = round(height * 0.0254, 2)

# Send all the data to our file

fichier.write("Name : ")
fichier.write(first_name)
fichier.write(" ")
fichier.write(second_name)
fichier.write(" Race : ")
fichier.write(race)
fichier.write(" Sex : ")
fichier.write(sex)
fichier.write(" \nAlignment : ")
fichier.write(str(alignment))
fichier.write("\nheight : ")
fichier.write(str(height // 12))
fichier.write(" ft ")
fichier.write(str(int(height % 12)))
fichier.write(" inches. i.e : ")
fichier.write(str(round(height_m, 2)))
fichier.write(" m")
fichier.write(" weight : ")
fichier.write(str(weight))
fichier.write(" lb. ie : ")
fichier.write(str(round(weight * 0.45, 2)))
fichier.write(" kg. ")
fichier.write("\nSpeed (in ft. per round) : ")
fichier.write(str(speed))
fichier.write("\nArmor class : ")
fichier.write(str(armor))
fichier.write("\n")
fichier.write("\nSTATS : ")
fichier.write("\nSTRENGTH : ")
fichier.write(str(res_lt[0]))
fichier.write("\nDEXTERITY : ")
fichier.write(str(res_lt[1]))
fichier.write("\nCONSTITUTION : ")
fichier.write(str(res_lt[2]))
fichier.write("\nINTELLIGENCE : ")
fichier.write(str(res_lt[3]))
fichier.write("\nWISDOM : ")
fichier.write(str(res_lt[4]))
fichier.write("\nCHARISMA : ")
fichier.write(str(res_lt[5]))
fichier.write("\n")
fichier.write("\n")
fichier.write("as a first level, your proficiency bonus is : +2")
fichier.write("\n")
fichier.write("\n")

# define constitution modifier
c_m = int(res_lt[2]//2)

# Create class

def maximum_stat(res_lt):
    maxi = res_lt[0]
    for i in range(len(res_lt)):
        if res_lt[i] >= maxi:
            maxi = res_lt[i]
    return maxi


if maximum_stat(res_lt) == res_lt[0]:
    fichier.write("You are a WARRIOR")
    fichier.write("\nHit Die : d10, Primary Ability : Strength or Dexterity, ")
    fichier.write("\nSaving Throw Proficiencies : Strength & Constitution, ")
    fichier.write("\nHit points : ")
    hp = random.randint(1, 10) + c_m
    fichier.write(str(hp))
    fichier.write("\n")
    _klass = classes[1]

# define fighting styles
    fighting_style = ["archery", "defense", "dueling", "great weapon fighting", "protection", "two weapons fighting"]
    fi1, f12 = random.sample(fighting_style, 2)
    fichier.write("\n Your fighting styles are : ")
    fichier.write(str(fi1))
    fichier.write(" and ")
    fichier.write(str(f12))

# define warrior skills
    warrior_skills = ["Acrobatics", "Animal Handling", "Athletics", "History",
                      "Insight", "Intimidation", "Perception", "Survival"]
    sk1, sk2 = random.sample(warrior_skills, 2)
    fichier.write("\nYour skills are : ")
    fichier.write(str(sk1))
    fichier.write(" and ")
    fichier.write(str(sk2))

elif maximum_stat(res_lt) == res_lt[1]:
    fichier.write("You are a ROGUE")
    fichier.write("\nHit Die : d8, Primary Ability : Dexterity ")
    fichier.write("\nSaving Throw Proficiencies : Dexterity & Intelligence ")
    fichier.write("\nHit points : ")
    hp = random.randint(1, 8) + c_m
    fichier.write(str(hp))
    _klass = classes[2]

# define rogue skills
    rogue_skills = ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation",
                    "Investigation", "Perception", "Performance", "Persuasion",
                    "Sleight of Hand", "Stealth"]
    sk1, sk2, sk3, sk4 = random.sample(rogue_skills, 4)
    fichier.write("\nYour skills are : ")
    fichier.write(str(sk1))
    fichier.write(", ")
    fichier.write(str(sk2))
    fichier.write(", ")
    fichier.write(str(sk3))
    fichier.write(" and ")
    fichier.write(str(sk4))

elif maximum_stat(res_lt) == res_lt[3]:
    fichier.write("You are a WIZARD")
    fichier.write("\nHit Die : d6, Primary Ability : Intelligence ")
    fichier.write("\nSaving Throw Proficiencies : Intelligence & Wisdom ")
    fichier.write("\nHit points : ")
    hp = random.randint(1, 6) + c_m
    fichier.write(str(hp))
    fichier.write("\n")
    _klass = classes[3]

# define wizard skills
    wizard_skills = ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
    sk1, sk2 = random.sample(wizard_skills, 2)
    fichier.write("\nYour skills are : ")
    fichier.write(str(sk1))
    fichier.write(" and ")
    fichier.write(str(sk2))

# define wizard cantrips and spells
    fichier.write("\nYou begin with 3 cantrips and 2 first level spells.")

    wl1, wl2, wl3 = random.sample(wizard_cantrip, 3)
    wls1, wls2 = random.sample(wizard_spells, 2)

    fichier.write("\nYour 3 cantrips are : ")
    fichier.write("\n-")
    fichier.write(wl1)
    fichier.write("\n-")
    fichier.write(wl2)
    fichier.write("\n-")
    fichier.write(wl3)

    fichier.write("\n and your 2 first level spells are :")
    fichier.write("\n-")
    fichier.write(wls1)
    fichier.write("\n-")
    fichier.write(wls2)
    fichier.write("\n")
    fichier.write("\nDescription of spells on page 86 of the DnD_BasicRules_2018.pdf")

elif maximum_stat(res_lt) == res_lt[4]:
    fichier.write("You are a CLERIC")
    fichier.write("\nHit Die : d8, Primary Ability : Wisdom ")
    fichier.write("\nSaving Throw Proficiencies : Wisdom & Charisma ")
    fichier.write("\nHit points : ")
    hp = random.randint(1, 8) + c_m
    fichier.write(str(hp))
    fichier.write("\n")
    _klass = classes[0]

# define cleric skills
    cleric_skills = ["History", "Insight", "Medicine", "Persuasion", "Religion"]
    sk1, sk2 = random.sample(cleric_skills, 2)
    fichier.write("\nYour skills are : ")
    fichier.write(str(sk1))
    fichier.write(" and ")
    fichier.write(str(sk2))

# define cleric cantrips and spells
    fichier.write("\nYou begin with 3 cantrips and 2 first level spells.")

    cl1, cl2, cl3 = random.sample(cleric_cantrip, 3)
    cls1, cls2 = random.sample(cleric_spells, 2)

    fichier.write("\nYour 3 cantrips are : ")
    fichier.write("\n- ")
    fichier.write(cl1)
    fichier.write("\n- ")
    fichier.write(cl2)
    fichier.write("\n- ")
    fichier.write(cl3)

    fichier. write("\nand your 2 first level spells are :")
    fichier.write("\n- ")
    fichier.write(cls1)
    fichier.write("\n- ")
    fichier.write(cls2)
    fichier.write("\n ")
    fichier.write("\nDescription of spells on page 86 of the DnD_BasicRules_2018.pdf")


# if you want to add a new class do it here with same pattern :
# the number after "res_lt" is the same as the stat value (0 = Strength, 1 = Dexterity etc)

# Sometimes choosing a class is not easy

else:
    fichier.write("\nyou can choose your class ... or re-run the program.")

# If you re-run the program, another character will be printed on the same file, under the first
# You can do this 6 or 7 times before having to delete the "data.txt" file.
# A better choice is to "select all" and "delete all" the "data.txt" file.

# define background

background = ["Acolyte", "Criminal", "Folk Hero", "Noble", "Sage", "Soldier"]
b_ground = random.randint(0, 5)
back_ground = background[int(b_ground)]

fichier.write("\n")
fichier.write("\nYOUR BACKGROUND :")
fichier.write("\n")

# Acolyte background & bond & flaw

if back_ground == "Acolyte":
    fichier.write("\nYou are an acolyte :")
    fichier.write("\nThese  are your personality trait, bond, flaw and Ideal :")
    gold = 15
    p_trait = random.randint(1, 8)

    if p_trait == 1:
        fichier.write("\nI idolize a particular hero of my faith, and constantly"
                      " refer to that person’s deeds and example.")
    if p_trait == 2:
        fichier.write("\nI can find common ground between the fiercest"
                      " enemies, empathizing with them and always working"
                      " toward peace.")
    if p_trait == 3:
        fichier.write("\nI see omens in every event and action. The gods try to"
                      " speak to us, we just need to listen.")
    if p_trait == 4:
        fichier.write("\nNothing can shake my optimistic attitude.")
    if p_trait == 5:
        fichier.write("\nI quote (or misquote) sacred texts and proverbs in"
                      " almost every situation.")
    if p_trait == 6:
        fichier.write("\nI am tolerant (or intolerant) of other faiths and respect"
                      " (or condemn) the worship of other gods.")
    if p_trait == 7:
        fichier.write("\nI’ve enjoyed fine food, drink, and high society among"
                      " my temple’s elite. Rough living grates on me.")
    if p_trait == 8:
        fichier.write("\nI’ve spent so long in the temple that I have little"
                      " practical experience dealing with people in the"
                      " outside world.")
    bond = random.randint(1, 6)
    if bond == 1:
        fichier.write("\nI would die to recover an ancient relic of my faith that"
                      " was lost long ago.")
    if bond == 2:
        fichier.write("\nI will someday get revenge on the corrupt temple"
                      " hierarchy who branded me a heretic.")
    if bond == 3:
        fichier.write("\nI owe my life to the priest who took me in when my"
                      " parents died.")
    if bond == 4:
        fichier.write("\nEverything I do is for the common people.")
    if bond == 5:
        fichier.write("\nI will do anything to protect the temple where I served.")
    if bond == 6:
        fichier.write("\nI seek to preserve a sacred text that my enemies"
                      " consider heretical and seek to destroy.")

    flaw = random.randint(1, 6)
    if flaw == 1:
        fichier.write("\nI judge others harshly, and myself even more severely.")
    if flaw == 2:
        fichier.write("\nI put too much trust in those who wield power within"
                      " my temple’s hierarchy.")
    if flaw == 3:
        fichier.write("\nMy piety sometimes leads me to blindly trust those that"
                      " profess faith in my god.")
    if flaw == 4:
        fichier.write("\nI am inflexible in my thinking.")
    if flaw == 5:
        fichier.write("\nI am suspicious of strangers and expect the"
                      " worst of them.")
    if flaw == 6:
        fichier.write("\nOnce I pick a goal, I become obsessed with it to the"
                      " detriment of everything else in my life.")

    ideal = random.randint(1, 6)
    if ideal == 1:
        fichier.write("\n Your Ideal is : Tradition. The ancient traditions of worship and sacrifice"
                      " must be preserved and upheld. (Lawful)")
    if ideal == 2:
        fichier.write("\n Your Ideal is : Charity. I always try to help those in need, no matter"
                      " what the personal cost. (Good)")
    if ideal == 3:
        fichier.write("\n Your Ideal is : Change. We must help bring about the changes the"
                      " gods are constantly working in the world. (Chaotic)")
    if ideal == 4:
        fichier.write("\n Your Ideal is : Power. I hope to one day rise to the top of my faith’s"
                      " religious hierarchy. (Lawful)")
    if ideal == 5:
        fichier.write("\n Your Ideal is : Faith. I trust that my deity will guide my actions. I have"
                      " faith that if I work hard, things will go well. (Lawful)")
    if ideal == 6:
        fichier.write("\n Your Ideal is : Aspiration. I seek to prove myself worthy of my god’s"
                      " favor by matching my actions against his or her teachings. (Any)")

    fichier.write("\nYour skill Proficiencies: Insight, Religion"
                  "\n You speak 2 languages of your choice,"
                  "\nEquipment: A holy symbol (a gift to you when youentered the priesthood),"
                  "a prayer book or prayer wheel, 5 sticks of incense, vestments and a set of common clothes")


# Criminal background & bond

if back_ground == "Criminal":
    fichier.write("\nYou are a criminal : ")
    fichier.write("\nThese  are your personality trait, bond, flaw and speciality :")
    gold = 15
    p_trait = random.randint(1, 8)
    if p_trait == 1:
        fichier.write("\nI always have a plan for what to do when"
                      " things go wrong.")
    if p_trait == 2:
        fichier.write("\nI am always calm, no matter what the situation. I never"
                      " raise my voice or let my emotions control me.")
    if p_trait == 3:
        fichier.write("\nThe first thing I do in a new place is note the locations"
                      " of everything valuable—or where such things"
                      " could be hidden.")
    if p_trait == 4:
        fichier.write("\nI would rather make a new friend than a new enemy.")
    if p_trait == 5:
        fichier.write("\nI am incredibly slow to trust. Those who seem the"
                      " fairest often have the most to hide.")
    if p_trait == 6:
        fichier.write("\nI don’t pay attention to the risks in a situation. Never tell"
                      " me the odds.")
    if p_trait == 7:
        fichier.write("\nThe best way to get me to do something is to tell me I"
                      " can’t do it.")
    if p_trait == 8:
        fichier.write("\nI blow up at the slightest insult.")
    bond = random.randint(1, 6)
    if bond == 1:
        fichier.write("\nI’m trying to pay off an old debt I owe to a"
                      " generous benefactor.")
    if bond == 2:
        fichier.write("\nMy ill-gotten gains go to support my family.")
    if bond == 3:
        fichier.write("\nSomething important was taken from me, and I aim to"
                      " steal it back.")
    if bond == 4:
        fichier.write("\nI will become the greatest thief that ever lived.")
    if bond == 5:
        fichier.write("\nI’m guilty of a terrible crime. I hope I can redeem"
                      " myself for it.")
    if bond == 6:
        fichier.write("\nSomeone I loved died because of I mistake I made. That"
                      " will never happen again.")

    flaw = random.randint(1, 6)
    if flaw == 1:
        fichier.write("\nWhen I see something valuable, I can’t think about"
                      " anything but how to steal it.")
    if flaw == 2:
        fichier.write("\nWhen faced with a choice between money and my"
                      " friends, I usually choose the money.")
    if flaw == 3:
        fichier.write("\nIf there’s a plan, I’ll forget it. If I don’t forget it,"
                      " I’ll ignore it.")
    if flaw == 4:
        fichier.write("\nI have a “tell” that reveals when I’m lying.")
    if flaw == 5:
        fichier.write("\nI turn tail and run when things look bad.")
    if flaw == 6:
        fichier.write("\nAn innocent person is in prison for a crime that I"
                      " committed. I’m okay with that.")

    ideal = random.randint(1, 6)
    if ideal == 1:
        fichier.write("\n Your Ideal is : Honor. I don’t steal from others in the trade. (Lawful)")
    if ideal == 2:
        fichier.write("\n Your Ideal is : Freedom. Chains are meant to be broken, as are those"
                      " who would forge them. (Chaotic)")
    if ideal == 3:
        fichier.write("\n Your Ideal is : Charity. I steal from the wealthy so that I can help"
                      " people in need. (Good) ")
    if ideal == 4:
        fichier.write("\n Your Ideal is : Greed. I will do whatever it takes to become"
                      " wealthy. (Evil)")
    if ideal == 5:
        fichier.write("\n Your Ideal is : People. I’m loyal to my friends, not to any ideals, and"
                      " everyone else can take a trip down the Styx for all I care. (Neutral)")
    if ideal == 6:
        fichier.write("\n Your Ideal is : Redemption. There’s a spark of good in"
                      " everyone. (Good)")

    special = random.randint(1, 8)
    if special == 1:
        fichier.write("\n Your specialty is : Blackmailer")
    if special == 2:
        fichier.write("\n Your specialty is : Burglar")
    if special == 3:
        fichier.write("\n Your specialty is : Enforcer")
    if special == 4:
        fichier.write("\n Your specialty is : Fence")
    if special == 5:
        fichier.write("\n Your specialty is : Highway robber")
    if special == 6:
        fichier.write("\n Your specialty is : Hired killer")
    if special == 7:
        fichier.write("\n Your specialty is : Pickpocket")
    if special == 8:
        fichier.write("\n Your specialty is : Smuggler")

    fichier.write("\nSkill Proficiencies: Deception, Stealth")
    fichier.write("\nTool Proficiencies: One type of gaming set,"
                  "thieves’ tools,"
                  "\nEquipment: A crowbar, a set of dark common clothes including a hood")

# Folk Hero Background & bond

if back_ground == "Folk Hero":
    fichier.write("\nYou are a folk hero :")
    fichier.write("This defining event marked you as a hero of the people :")
    gold = 0
    pers_event = random.randint(1, 10)
    if pers_event == 1:
        fichier.write("\nI stood up to a tyrant’s agents.")
    if pers_event == 2:
        fichier.write("\nI saved people during a natural disaster.")
    if pers_event == 3:
        fichier.write("\nI stood alone against a terrible monster.")
    if pers_event == 4:
        fichier.write("\nI stole from a corrupt merchant to help the poor.")
    if pers_event == 5:
        fichier.write("\nI led a militia to fight off an invading army.")
    if pers_event == 6:
        fichier.write("\nI broke into a tyrant’s castle and stole weapons to"
                      " arm the people.")
    if pers_event == 7:
        fichier.write("\nI trained the peasantry to use farm implements as"
                      " weapons against a tyrant’s soldiers.")
    if pers_event == 8:
        fichier.write("\nA lord rescinded an unpopular decree after I led a"
                      " symbolic act of protest against it.")
    if pers_event == 9:
        fichier.write("\nA celestial, fey, or similar creature gave me a blessing or"
                      " revealed my secret origin.")
    if pers_event == 10:
        fichier.write("\nRecruited into a lord’s army, I rose to leadership and"
                      " was commended for my heroism.")
    fichier.write("\nSkill Proficiencies: Animal Handling, Survival"
                  "\nTool Proficiencies: One type of artisan’s tools, vehicles (land)"
                  "\nEquipment: A set of artisan’s tools (one of your choice),"
                  " a shovel, an iron pot, a set of common clothes")

    fichier.write("\nThese  are your personality trait, bond, flaw and speciality :")
    p_trait = random.randint(1, 8)
    if p_trait == 1:
        fichier.write("\nI judge people by their actions, not their words.")
    if p_trait == 2:
        fichier.write("\nIf someone is in trouble, I’m always ready to lend help.")
    if p_trait == 3:
        fichier.write("\nWhen I set my mind to something, I follow through no"
                      " matter what gets in my way.")
    if p_trait == 4:
        fichier.write("\nI have a strong sense of fair play and always try to find "
                      " the most equitable solution to arguments.")
    if p_trait == 5:
        fichier.write("\nI’m confident in my own abilities and do what I can to"
                      " instill confidence in others.")
    if p_trait == 6:
        fichier.write("\nThinking is for other people. I prefer action.")
    if p_trait == 7:
        fichier.write("\nI misuse long words in an attempt to sound smarter.")
    if p_trait == 8:
        fichier.write("\nI get bored easily. When am I going to get on"
                      " with my destiny?")

    bond = random.randint(1, 6)
    if bond == 1:
        fichier.write("\nI have a family, but I have no idea where they are. One"
                      " day, I hope to see them again.")
    if bond == 2:
        fichier.write("\nI worked the land, I love the land, and I will"
                      " protect the land.")
    if bond == 3:
        fichier.write("\nA proud noble once gave me a horrible beating, and I"
                      " will take my revenge on any bully I encounter.")
    if bond == 4:
        fichier.write("\nMy tools are symbols of my past life, and I carry them"
                      " so that I will never forget my roots.")
    if bond == 5:
        fichier.write("\nI protect those who cannot protect themselves.")
    if bond == 6:
        fichier.write("\nI wish my childhood sweetheart had come with me to"
                      " pursue my destiny.")

    flaw = random.randint(1, 6)
    if flaw == 1:
        fichier.write("\nThe tyrant who rules my land will stop at nothing to"
                      " see me killed.")
    if flaw == 2:
        fichier.write("\nI’m convinced of the significance of my destiny, and"
                      " blind to my shortcomings and the risk of failure.")
    if flaw == 3:
        fichier.write("\nThe people who knew me when I was young know my"
                      " shameful secret, so I can never go home again.")
    if flaw == 4:
        fichier.write("\nI have a weakness for the vices of the city,"
                      " especially hard drink.")
    if flaw == 5:
        fichier.write("\nSecretly, I believe that things would be better if I were a"
                      " tyrant lording over the land.")
    if flaw == 6:
        fichier.write("\nI have trouble trusting in my allies.")

    ideal = random.randint(1, 6)
    if ideal == 1:
        fichier.write("\n Your Ideal is : Respect. People deserve to be treated with dignity and"
                      " respect. (Good)")
    if ideal == 2:
        fichier.write("\n Your Ideal is : Fairness. No one should get preferential treatment"
                      " before the law, and no one is above the law. (Lawful)")
    if ideal == 3:
        fichier.write("\n Your Ideal is : Freedom. Tyrants must not be allowed to oppress the"
                      " people. (Chaotic)")
    if ideal == 4:
        fichier.write("\n Your Ideal is : Might. If I become strong, I can take what I want—what"
                      " I deserve. (Evil)")
    if ideal == 5:
        fichier.write("\n Your Ideal is : Sincerity. There’s no good in pretending to be"
                      " something I’m not. (Neutral)")
    if ideal == 6:
        fichier.write("\n Your Ideal is : Destiny. Nothing and no one can steer me away from"
                      " my higher calling. (Any)")

# Noble background & bond

if back_ground == "Noble":
    fichier.write("\nYou are a noble :")
    fichier.write("\nSkill Proficiencies: History, Persuasion"
                  "\nTool Proficiencies: One type of gaming set"
                  "\nLanguages: One of your choice"
                  "\nEquipment: A set of fine clothes, a signet ring, a scroll of pedigree")
    fichier.write("\nThese  are your personality trait, bond, flaw and speciality :")
    gold = 25
    p_trait = random.randint(1, 8)

    if p_trait == 1:
        fichier.write("\nMy eloquent flattery makes everyone I talk to feel like"
                      " the most wonderful and important person in the world.")
    if p_trait == 2:
        fichier.write("\nThe common folk love me for my kindness"
                      " and generosity.")
    if p_trait == 3:
        fichier.write("\nNo one could doubt by looking at my regal bearing that I"
                      " am a cut above the unwashed masses.")
    if p_trait == 4:
        fichier.write("\nI take great pains to always look my best and follow the"
                      " latest fashions.")
    if p_trait == 5:
        fichier.write("\nI don’t like to get my hands dirty, and I won’t be caught"
                      " dead in unsuitable accommodations.")
    if p_trait == 6:
        fichier.write("\nDespite my noble birth, I do not place myself above"
                      " other folk. We all have the same blood.")
    if p_trait == 7:
        fichier.write("\nMy favor, once lost, is lost forever.")
    if p_trait == 8:
        fichier.write("\nIf you do me an injury, I will crush you, ruin your name,"
                      " and salt your fields.")
    bond = random.randint(1, 6)
    if bond == 1:
        fichier.write("\nI will face any challenge to win the approval of my family.")
    if bond == 2:
        fichier.write("\nMy house’s alliance with another noble family"
                      " must be sustained at all costs.")
    if bond == 3:
        fichier.write("\nNothing is more important than the other members"
                      " of my family.")
    if bond == 4:
        fichier.write("\nI am in love with the heir of a family that my"
                      " family despises.")
    if bond == 5:
        fichier.write("\nMy loyalty to my sovereign is unwavering.")
    if bond == 6:
        fichier.write("\nThe common folk must see me as a hero of the people.")

    flaw = random.randint(1, 6)
    if flaw == 1:
        fichier.write("\nI secretly believe that everyone is beneath me.")
    if flaw == 2:
        fichier.write("\nI hide a truly scandalous secret that could ruin my"
                      " family forever.")
    if flaw == 3:
        fichier.write("\nI too often hear veiled insults and threats in every word"
                      " addressed to me, and I’m quick to anger.")
    if flaw == 4:
        fichier.write("\nI have an insatiable desire for carnal pleasures.")
    if flaw == 5:
        fichier.write("\nIn fact, the world does revolve around me.")
    if flaw == 6:
        fichier.write("\nBy my words and actions, I often bring shame"
                      " to my family.")

    ideal = random.randint(1, 6)
    if ideal == 1:
        fichier.write("\n Your Ideal is : Respect. Respect is due to me because of my position,"
                      " but all people regardless of station deserve to be treated"
                      " with dignity. (Good)")
    if ideal == 2:
        fichier.write("\n Your Ideal is : Responsibility. It is my duty to respect the authority of"
                      " those above me, just as those below me must respect"
                      " mine. (Lawful)")
    if ideal == 3:
        fichier.write("\n Your Ideal is : Independence. I must prove that I can handle myself"
                      " without the coddling of my family. (Chaotic)")
    if ideal == 4:
        fichier.write("\n Your Ideal is : Power. If I can attain more power, no one will tell me"
                      " what to do. (Evil)")
    if ideal == 5:
        fichier.write("\n Your Ideal is : Family. Blood runs thicker than water. (Any)")
    if ideal == 6:
        fichier.write("\n Your Ideal is : Noble Obligation. It is my duty to protect and care for"
                      " the people beneath me. (Good)")

# Sage background and bond

if back_ground == "Sage":
    fichier.write("\nYou are a sage :")
    fichier.write("\nSkill Proficiencies: Arcana, History"
                  "\nLanguages: Two of your choice"
                  "\nEquipment: A bottle of black ink, a quill, a small knife,")
    fichier.write("\na letter from a dead colleague posing a question you have"
                  " not yet been able to answer, a set of common clothes,")

    fichier.write("\n")
    fichier.write("\nThese  are your personality trait, bond, flaw and speciality :")
    gold = 10
    p_trait = random.randint(1, 8)

    if p_trait == 1:
        fichier.write("\nI use polysyllabic words that convey the impression of"
                      " great erudition.")
    if p_trait == 2:
        fichier.write("\nI’ve read every book in the world’s greatest libraries—or"
                      " I like to boast that I have.")
    if p_trait == 3:
        fichier.write("\nI’m used to helping out those who aren’t as smart"
                      " as I am, and I patiently explain anything and"
                      " everything to others.")
    if p_trait == 4:
        fichier.write("\nThere’s nothing I like more than a good mystery.")
    if p_trait == 5:
        fichier.write("\nI’m willing to listen to every side of an argument before I"
                      " make my own judgment.")
    if p_trait == 6:
        fichier.write("\nI . . . speak . . . slowly . . . when talking . . . to idiots, . . ."
                      " which . . . almost . . . everyone . . . is . . . compared . . ."
                      " to me.")
    if p_trait == 7:
        fichier.write("\nI am horribly, horribly awkward in social situations.")
    if p_trait == 8:
        fichier.write("\nI’m convinced that people are always trying to"
                      " steal my secrets.")
    bond = random.randint(1, 6)
    if bond == 1:
        fichier.write("\nIt is my duty to protect my students.")
    if bond == 2:
        fichier.write("\nI have an ancient text that holds terrible secrets that"
                      " must not fall into the wrong hands.")
    if bond == 3:
        fichier.write("\nI work to preserve a library, university, scriptorium,"
                      " or monastery.")
    if bond == 4:
        fichier.write("\nMy life’s work is a series of tomes related to a specific"
                      " field of lore.")
    if bond == 5:
        fichier.write("\nI’ve been searching my whole life for the answer to a"
                      " certain question.")
    if bond == 6:
        fichier.write("\nI sold my soul for knowledge. I hope to do great deeds"
                      " and win it back.")

    flaw = random.randint(1, 6)
    if flaw == 1:
        fichier.write("\nI am easily distracted by the promise of information.")
    if flaw == 2:
        fichier.write("\nMost people scream and run when they see a demon. I"
                      " stop and take notes on its anatomy.")
    if flaw == 3:
        fichier.write("\nUnlocking an ancient mystery is worth the price of a"
                      " civilization.")
    if flaw == 4:
        fichier.write("\nI overlook obvious solutions in favor of"
                      " complicated ones.")
    if flaw == 5:
        fichier.write("\nI speak without really thinking through my words,"
                      " invariably insulting others.")
    if flaw == 6:
        fichier.write("\nI can’t keep a secret to save my life, or anyone else’s.")

    ideal = random.randint(1, 6)
    if ideal == 1:
        fichier.write("\n Your Ideal is : Knowledge. The path to power and self-improvement is"
                      " through knowledge. (Neutral)")
    if ideal == 2:
        fichier.write("\n Your Ideal is : Beauty. What is beautiful points us beyond itself toward"
                      " what is true. (Good)")
    if ideal == 3:
        fichier.write("\n Your Ideal is : Logic. Emotions must not cloud our logical"
                      " thinking. (Lawful)")
    if ideal == 4:
        fichier.write("\n Your Ideal is : No Limits. Nothing should fetter the infinite possibility"
                      " inherent in all existence. (Chaotic)")
    if ideal == 5:
        fichier.write("\n Your Ideal is : Power. Knowledge is the path to power and"
                      " domination. (Evil)")
    if ideal == 6:
        fichier.write("\n Your Ideal is : Self-Improvement. The goal of a life of study is the"
                      " betterment of oneself. (Any)")

    special = random.randint(1, 8)
    if special == 1:
        fichier.write("\n Your specialty is : Alchemist")
    if special == 2:
        fichier.write("\n Your specialty is : Astronomer")
    if special == 3:
        fichier.write("\n Your specialty is : Discredited academic")
    if special == 4:
        fichier.write("\n Your specialty is : Librarian")
    if special == 5:
        fichier.write("\n Your specialty is : Professor")
    if special == 6:
        fichier.write("\n Your specialty is : Researcher")
    if special == 7:
        fichier.write("\n Your specialty is : Wizard’s apprentice")
    if special == 8:
        fichier.write("\n Your specialty is : Scribe")


# Soldier

if back_ground == "Soldier":
    fichier.write("\nYou are a soldier :")
    fichier.write("\nSkill Proficiencies: Athletics, Intimidation")
    fichier.write("\nTool Proficiencies: One type of gaming set, vehicles (land)")
    fichier.write("\nEquipment: An insignia of rank, a trophy taken from"
                  " a fallen enemy")
    fichier.write("\n(a dagger, broken blade, or piece of a"
                  " banner), a set of bone dice or deck of cards, a set of"
                  " common clothes")
    fichier.write("\n")
    gold = 10
    fichier.write("\nThese  are your personality trait, bond, flaw and speciality :")
    p_trait = random.randint(1, 8)

    if p_trait == 1:
        fichier.write("\nI’m always polite and respectful.")
    if p_trait == 2:
        fichier.write("\nI’m haunted by memories of war. I can’t get the images"
                      " of violence out of my mind.")
    if p_trait == 3:
        fichier.write("\nI’ve lost too many friends, and I’m slow to"
                      " make new ones.")
    if p_trait == 4:
        fichier.write("\nI’m full of inspiring and cautionary tales from"
                      " my military experience relevant to almost every"
                      " combat situation.")
    if p_trait == 5:
        fichier.write("\nI can stare down a hell hound without flinching.")
    if p_trait == 6:
        fichier.write("\nI enjoy being strong and like breaking things.")
    if p_trait == 7:
        fichier.write("\nI have a crude sense of humor.")
    if p_trait == 8:
        fichier.write("\nI face problems head-on. A simple, direct solution is the"
                      " best path to success.")

    bond = random.randint(1, 6)
    if bond == 1:
        fichier.write("\nI would still lay down my life for the people I"
                      " served with.")
    if bond == 2:
        fichier.write("\nSomeone saved my life on the battlefield. To this day, I"
                      " will never leave a friend behind.")
    if bond == 3:
        fichier.write("\nMy honor is my life.")
    if bond == 4:
        fichier.write("\nI’ll never forget the crushing defeat my company"
                      " suffered or the enemies who dealt it.")
    if bond == 5:
        fichier.write("\nThose who fight beside me are those worth dying for.")
    if bond == 6:
        fichier.write("\nI fight for those who cannot fight for themselves.")

    flaw = random.randint(1, 6)
    if flaw == 1:
        fichier.write("\nThe monstrous enemy we faced in battle still leaves me"
                      " quivering with fear.")
    if flaw == 2:
        fichier.write("\nI have little respect for anyone who is not a"
                      " proven warrior.")
    if flaw == 3:
        fichier.write("\nI made a terrible mistake in battle that cost many lives—"
                      " and I would do anything to keep that mistake secret.")
    if flaw == 4:
        fichier.write("\nMy hatred of my enemies is blind and unreasoning.")
    if flaw == 5:
        fichier.write("\nI obey the law, even if the law causes misery.")
    if flaw == 6:
        fichier.write("\nI’d rather eat my armor than admit when I’m wrong.")

    ideal = random.randint(1, 6)
    if ideal == 1:
        fichier.write("\n Your Ideal is : Greater Good. Our lot is to lay down our lives in defense"
                      " of others. (Good)")
    if ideal == 2:
        fichier.write("\n Your Ideal is : Responsibility. I do what I must and obey just"
                      " authority. (Lawful)")
    if ideal == 3:
        fichier.write("\n Your Ideal is : Independence. When people follow orders blindly, they"
                      " embrace a kind of tyranny. (Chaotic)")
    if ideal == 4:
        fichier.write("\n Your Ideal is : Might. In life as in war, the stronger force wins. (Evil)")
    if ideal == 5:
        fichier.write("\n Your Ideal is : Live and Let Live. Ideals aren’t worth killing over or"
                      " going to war for. (Neutral)")
    if ideal == 6:
        fichier.write("\n Your Ideal is : Nation. My city, nation, or people are all that"
                      " matter. (Any)")

    special = random.randint(1, 8)
    if special == 1:
        fichier.write("\n Your specialty is : Officer")
    if special == 2:
        fichier.write("\n Your specialty is : Scout")
    if special == 3:
        fichier.write("\n Your specialty is : Infantry")
    if special == 4:
        fichier.write("\n Your specialty is : Cavalry")
    if special == 5:
        fichier.write("\n Your specialty is : Healer")
    if special == 6:
        fichier.write("\n Your specialty is : Quartermaster")
    if special == 7:
        fichier.write("\n Your specialty is : Standard bearer")
    if special == 8:
        fichier.write("\n Your specialty is : Support staff (cook, blacksmith, or the like)")

# additional cantrip for an elf

if race == "Elf":
    elf_c = random.sample(wizard_cantrip, 1)
    fichier.write("\nAs an elf you know one additional cantrip : ")
    fichier.write(str(elf_c))
else:
    fichier.write("")

fichier.write("\n")
fichier.write("\n Gold and equipment :")
fichier.write("\n")

# define Equipment and Gold
if _klass == classes[0]:
    # cleric equipment
    fichier.write("You start with the following equipment, in addition to the "
                  "equipment granted by your background:"
                  "\n(a) a mace or (b) a warhammer (if proficient)"
                  "\n(a) scale mail, (b) leather armor, or (c) chain mail (if proficient)"
                  "\n(a) a light crossbow and 20 bolts or (b) any simple weapon"
                  "\n(a) a priest’s pack or (b) an explorer’s pack"
                  "\nA shield and a holy symbol")

elif _klass == classes[1]:
    # warrior equipment
    fichier.write("You start with the following equipment, in addition to the"
                  " equipment granted by your background:"
                  "\n(a) chain mail or (b) leather armor, longbow, and 20 arrows"
                  "\n(a) a martial weapon and a shield or (b) two martial weapons"
                  "\n(a) a light crossbow and 20 bolts or (b) two handaxes"
                  "\n(a) a dungeoneer’s pack or (b) an explorer’s pack")

elif _klass == classes[2]:
    # rogue equipment
    fichier.write("You start with the following equipment, in addition to the"
                  " equipment granted by your background:"
                  "\n(a) a rapier or (b) a shortsword"
                  "\n(a) a shortbow and quiver of 20 arrows or (b) a shortsword"
                  "\n(a) a burglar’s pack, (b) a dungeoneer’s pack, or (c) an explorer’s pack"
                  "\nLeather armor, two daggers, and thieves’ tools")

elif _klass == classes[3]:
    # wizard equipment
    fichier.write("You start with the following equipment, in addition to the"
                  "equipment granted by your background:"
                  "\n(a) a quarterstaff or (b) a dagger"
                  "\n(a) a component pouch or (b) an arcane focus"
                  "\n(a) a scholar’s pack or (b) an explorer’s pack"
                  "A spellbook")

else:
    fichier.write("If you want to keep this character, you will also need to create its equipment. ")
# if you add a new class keep the same pattern beginning by elif (and attention to the indent)
# and don't forget to add this new class in the "classes" group line 11 !


fichier.write("\nand ")
fichier.write(str(gold))
fichier.write(" gold pieces.")

# Let's add to blank lines if you re-run the program without deleting the character on the char-sheet.txt
fichier.write("\n")
fichier.write("\n")

# End of the program : close the file
fichier.close()
