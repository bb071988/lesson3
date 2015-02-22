import sys

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)],
        print ""

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print "Be with you in a moment"
        print "Twoning, sproing, splang"
        
class Drummer(Musician):
    def __init__(self):
        super(Drummer,self).__init__(["crash","boom","bam"])
        
    def count_off(self):
        for x in range(1,5):
            print 'Tick ' +  str(x)
            print ""
            x +=1
            
    def cumbust(self):
        print("I think I am cumbusting")
        
class Band(object):
    def __init__(self):
        self.member = None
        self.bandmates = []
        
    def fire(self,member):
        self.bandmates.remove(member)
        
    def hire(self,member):
        self.bandmates.append(member)
        
    def print_band(self):
        print self.bandmates
    
    def play_solos(self):
        for bandmate in self.bandmates:
            print bandmate + ' will now solo '
            bandmate.solo(3)
        
        

demo = None        
        
if __name__ == '__main__':

    try:
        demo = sys.argv[1]  
    except:
        pass

    if demo == 'Drummer':
        moon = Drummer()
        print "demo solo -- " , moon.solo(6)
        moon.count_off() # where does the None before the countoff come from?
        moon.cumbust()
        
    elif demo == 'Band':
        print 'Bandmmates include: '
        wonders =  Band()
        will = Bassist
        wonders.hire('will')
        snake = Guitarist
        wonders.hire('snake')
        slash = Drummer
        wonders.hire('slash')
        wonders.play_solos()
        wonders.print_band()
        print "Band fires Snake"
        wonders.fire("snake")
        wonders.print_band()
        
        
    else:
        print("Unknown argument")
        
        
        # Since Drummer is a subclass of Musician it inherits the solo method - no additional code required.
        
        
        
        