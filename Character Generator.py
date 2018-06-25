def mainprompt():
    import random
    import os
    Again = 'y'
    while Again == 'y':
        # Name
        print()
        Name = input(" What is your possible OC's name? ")
        os.system('CLS')
        print()
        # Gender
        Gender = input(' Is your OC Male? (y/n) ')
        os.system('CLS')
        print()
        if Gender == 'n':
            Gender = input(' Is your OC Female? (y/n) ')
            os.system('CLS')
            print()
            if Gender == 'n':
                Gender = 'Neutral'
            elif Gender == 'y':
                Gender = 'Female'
        elif Gender == 'y':
            Gender = 'Male'

        # Sexual Orientation
        Sexuality = input(" What is the OC's sexual preference? ")
        os.system('CLS')
        print()

        # Species
        Species = input(' Do you want your OC to be human? (y/n) ')
        os.system('CLS')
        if Species == 'n' and Gender == 'Female':
            Species = ('Vampire', 'Werewolf', 'Mermaid', 'Ghost', 'Ghoul', 'Dragon', 'Genie', 'Witch', 'Angel', 'Demon', 'Dark Elf', 'Fairy', 'Elf', 'Nymph', 'Neko', 'Kitsune', 'Elemental', 'Leprechan')
            Species = random.choice(Species)
        elif Species == 'n' and Gender == 'Male':
            Species = ('Vampire', 'Werewolf', 'Merman', 'Ghost', 'Ghoul', 'Dragon', 'Genie', 'Warlock', 'Angel', 'Demon', 'Dark Elf', 'Fairy', 'Elf', 'Satyr', 'Neko', 'Kitsune', 'Elemental', 'Leprechan') 
            Species = random.choice(Species)
        elif Species == 'n' and Gender == 'Neutral':
            Species = ('Vampire', 'Werewolf', 'Merfolk', 'Ghost', 'Ghoul', 'Dragon', 'Genie', 'Wizard', 'Angel', 'Demon', 'Dark Elf', 'Fairy', 'Elf', 'Nymph', 'Satyr', 'Neko', 'Kitsune', 'Elemental', 'Leprechan')
            Species = random.choice(Species)
        else:
            Species = 'Human'
        # Age
        Age = random.randint(10,50)
    
        # Birthday
        Month = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
        Month = random.choice(Month)
        if Month == 'February':
            day = random.randint(1,28)
        else:
            day = random.randint(1,30)    
        # Ethnicity
        Ethnicity = ('Native', 'Latino', 'Caucasian', 'African', 'Middle Eastern', 'Asian')
        
        Ethnicity = random.choice(Ethnicity)

        # Personality Type
        Personality = ('Introvert', 'Extrovert')
        Personality = random.choice(Personality)
        
        # Religion
        Religion = ('Theist','Atheist', 'Agnostic', 'Gnostic', 'Deist')
        Religion = random.choice(Religion)
        
        # Hair Color
        Hair = ('Blond', 'Red', 'Brown', 'Black', 'Gray', 'White')
        Texture = ' '
        Hair = random.choice(Hair)
        if Hair == 'Blond':
            Texture = ('- Ash', '- Bronze', '- Flaxen', '- Ginger', '- Golden', '- Honey', '- Platinum', '- Tawny', '- Wheaten')
            Texture = random.choice(Texture)
        elif Hair == 'Red':
            Texture = ('- Auburn', '- Copper', '- Flaming', '- Strawberry Blond')
            Texture = random.choice(Texture)
        elif Hair == 'Brown':
            Texture = ('- Ginger', '- Sandy', '- Chestnut', '- Russet', '- Sable', '- Sorrel')
            Texture = random.choice(Texture)
        elif Hair == 'Black':
            Texture = ('- Jet', '- Sooty')
            Texture = random.choice(Texture)
        elif Hair == 'Gray':
            Texture = ('- Ash', '- Iron', '- Salt and Pepper', '- Silver', '- Steel')
            Texture = random.choice(Texture)
        elif Hair == 'White':
            Texture = ('- Pearl', '- Snow')
            Texture = random.choice(Texture)

        # Eye Color 
        Eye = ('Black', 'Blue', 'Brown', 'Gray', 'Green', 'Hazel', 'Violet', 'Red')
        EyeTexture = ' '
        Eye = random.choice(Eye)
        if Eye == 'Black':
            EyeTexture = ('- Anthracite', '- Coal', '- Ebony', '- Jet', '- Midnight', '- Obsidian', '- Pitch', '- Sloe-eyed', '- Smoky', '- Soot', '- Velvety')
            EyeTexture = random.choice(EyeTexture)
        elif Eye == 'Blue':
            EyeTexture = ('- Aquamarine', '- Arctic', '- Baby', '- China', '- Cornflower', '- Crystal', '- Denim', '- Electric', '- Forget-Me-Not', '- Gunmetal', '- Ice', '- Indigo', '- Lasor-beam', '- Sapphire', '- Sky', '- Steel')
            EyeTexture = random.choice(EyeTexture)
        elif Eye == 'Brown':
            EyeTexture = ('- Amber', '- Brandy', '- Champagne', '- Chestnut', '- Chocolate', '- Cognac', '- Doe-Eyed', '- Golden', '- Nut', '- Russet', '- Soft', '- Tawny', '- Topaz', '- Velvety', '- Walnut', '- Whiskey')
            EyeTexture = random.choice(EyeTexture)
        elif Eye == 'Gray':
            EyeTexture = ('- Charcoal', '- Cloud', '- Graphite', '- Gunmetal', '- Silver', '- Slate', '- Smoky', '- Steel', '- Storm')
            EyeTexture = random.choice(EyeTexture)
        elif Eye == 'Green':
            EyeTexture = ('- Bottle', "- Cat's Eye", '- Chartreuse', '- Emerald', '- Forest', '- Gress', '- Jade', '- Leaf', '- Sea')
            EyeTexture = random.choice(EyeTexture)
        elif Eye == 'Violet':
            EyeTexture = ('- Amethyst', '- Hyacinth', '- Ultramarine')
            EyeTexture = random.choice(EyeTexture)
        else:
            EyeTexture = " "
    
        # Results
        print()
        print()
        print(" Congratulations!",Name,"is born!")
        print("________________________________ ")
        print()
        print(" Name:",Name)
        print()
        print(" Age:",Age)
        print()
        print(" Gender:",Gender)
        print()
        print(" Sexuality:",Sexuality)
        print()
        print(" Birthday:",Month,day)
        print()
        print(" Ethnicity:",Ethnicity)
        print()
        print(" Species:",Species)
        print()
        print(" Hair Color:",Hair,Texture)
        print()
        print(" Eye Color:",Eye,EyeTexture)
        print()
        print(' Religion:', Religion)
        print()
        print(' Personality:',Personality)
        print()
        print()
        Again = input(' Do you want to generate another OC? (y/n) ')
        if Again == 'y':
            os.system('CLS')
        if Again == 'n':
            exit()
mainprompt()
