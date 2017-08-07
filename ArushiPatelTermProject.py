#Arushi Patel (aruship)
from tkinter import *
import random

######################################
#images taken from wikipedia,pixabay,
#trans americas, clipartpanda,pngimg,
#findicons, microsoft word
######################################

####################################
# init
####################################
def init(data):
    data.score =0
    data.mode = "splashScreen"
    data.timerDelay = 100
    data.height = 800
    data.width = 800
    data.speed = 10
    data.speedAI = 12
    data.speedAI2 = 12
    data.switchOnProgress = False
    data.r = 25
    data.cx= 280
    data.cy=750
    data.onLeft1, data.onLeft2 = True, True
    data.win= False
    data.coconuts = []
    data.powerUps = []
    data.coconuts1 = []
    data.coconuts2 = []
    data.coconutsAI1 =[]
    data.coconutsAI2 = []
    data.invincible = []
    data.pauseDrops = False
    data.pause1Drop = False
    data.pause2Drop = False
    init1(data)

def init1(data):
    data.beInvincible = False
    data.Invincible1 = False
    data.Invincible2 = False
    data.scaryBug = []
    data.time = 0
    data.coconutFall = False
    data.sides = ["r", "l"]
    data.level = 1
    data.splashScreenTime = 0
    data.splashScreenDrops = []
    data.background= PhotoImage(file="tree.gif")
    data.deadScreen = PhotoImage(file = "deadBug.gif")
    data.ladyBug = PhotoImage(file = "lady.gif")
    data.winScreen= PhotoImage(file = "treeTop1.gif")
    data.winBug = PhotoImage(file = "littleBug.gif")
    data.halfBackground = PhotoImage(file = "halfTree.gif")
    data.umbrella = PhotoImage(file = "umbrella2.gif")
    data.spider = PhotoImage(file = "spider.gif")
    data.hourGlass = PhotoImage(file = "hourGlass.gif")
    data.splashScreen = PhotoImage(file = "splash.gif")
    init2(data)

def init2(data):
    data.tbg= PhotoImage(file = "tbg2.gif")
    data.click = PhotoImage(file = "click.gif")
    data.notClick = PhotoImage(file = "notClick.gif")
    data.player1X = 150
    data.player1Y = 750
    data.player2X = 550
    data.player2Y = 750
    data.winner = None
    data.speed = 12
    data.speed2 = 12
    data.editorTime = 0
    data.editorDrops = []
    data.margin = 100
    data.enter = False
    data.powerUpsEditor = None
    data.yourSpeed = None
    data.rainSpeed = None
    data.slow= data.notClick
    data.medium = data.notClick
    data.fast = data.notClick
    data.drizzle = data.notClick
    data.rain =data.notClick
    data.thunderstorm = data.notClick
    init3(data)

def init3(data):
    data.yes = data.notClick
    data.no = data.notClick
    data.enter = data.notClick
    data.levelEditorLives =2
    data.rSpeed = None
    data.start = None
    data.start1 = None
    data.start2 = None
    data.difficulty = None
    data.mode1 = data.notClick
    data.mode2 = data.notClick
    data.mode3 = data.notClick
    data.mode4 = data.notClick
    data.mode5 = data.notClick
    data.mode6 = data.notClick
    data.home = PhotoImage(file = "home.gif")
    data.helpScreen = PhotoImage(file = "help1.gif")
    data.title = PhotoImage(file = "title.gif")
    data.scoreList = []
    data.spotList = [270,364,458,552, 646, 740]
    data.savedScores = readFile("score.txt")
    if data.mode == "levelCreated":
        setEverything(data)
    initsplashScreenNumbers(data)

def initsplashScreenNumbers(data):
    data.splashButtonY = 425
    data.p1ButtonX= 225
    data.p2ButtonX = 290
    data.edButton = 355
    data.diffButton = 425
    data.helpButton = 490
    data.sboardButton = 555
    data.hitPenalty = 75
    data.splashText = data.height/2-20
    data.lives = 2
    data.levelMax = 8
    data.lane = 94
    data.Player1Min= 270
    data.Player1Max = 740
    data.homeX =50
    data.homeY = 650
    initScoreBoardHelp(data)
    init1Player(data)

def initScoreBoardHelp(data):
    data.tbgY=5*data.height/12
    data.txtTScore = 150
    data.S_P = 220
    data.numScores = 5
    data.scorePos = data.height/10
    data.scoreShift = 270
    data.helpY = data.height/2-20
    data.name = ""
    data.printName = ""
    data.hit = False
    initAI(data)

def init1Player(data):
    data.buffer = 40

def initAI(data):
    data.AITY = 225
    data.easyX = 200
    data.easyY = 300
    data.medX =400
    data.hardX = 600
    data.enterY = 450
    data.difS = 4
    data.difM = 6
    data.difH = 8
    data.last = 500
    data.enterX = 575
    data.PUT = 450
    data.RST = 350
    data.YST = 250
####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "splashScreen"): splashScreenMousePressed(event, data)
    elif (data.mode == "1Player"): playerMousePressed(event, data)
    elif (data.mode == "2Player"): twoPlayerMousePressed(event, data)
    elif (data.mode == "editor"): editorMousePressed(event,data)
    elif (data.mode == "levelCreated"): levelCreatedMousePressed(event,data)
    elif (data.mode == "AI"): AIMousePressed(event, data)
    elif (data.mode == "difficulty"): difficultyMousePressed(event, data)
    elif (data.mode == "scoreboard"): scoreboardMousePressed(event, data)
    elif (data.mode == "help"): helpMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "splashScreen"): splashKeyPressed(event, data)
    elif (data.mode == "1Player"):playerKeyPressed(event, data)
    elif (data.mode == "2Player"):twoPlayerKeyPressed(event, data)
    elif (data.mode == "editor"): editorKeyPressed(event, data)
    elif (data.mode == "levelCreated"): levelCreatedKeyPressed(event,data)
    elif (data.mode == "AI"): AIKeyPressed(event, data)
    elif (data.mode == "difficulty"): difficultyKeyPressed(event, data)
    elif (data.mode == "scoreboard"): scoreboardKeyPressed(event, data)
    elif (data.mode == "help"): helpKeyPressed(event, data)
    
def timerFired(data):
    if (data.mode == "splashScreen"): splashScreenTimerFired(data)
    elif (data.mode == "1Player"):playerTimerFired(data)
    elif (data.mode == "2Player"):twoPlayerTimerFired(data)
    elif (data.mode == "editor"): editorTimerFired(data)
    elif (data.mode == "levelCreated"): levelCreatedTimerFired(data)
    elif (data.mode == "AI"): AITimerFired(data)
    elif (data.mode == "difficulty"): difficultyTimerFired(data)
    elif (data.mode == "scoreboard"): scoreboardTimerFired(data)
    elif (data.mode == "help"): helpTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "splashScreen"): splashScreenRedrawAll(canvas, data)
    elif (data.mode == "1Player"):playerRedrawAll(canvas, data)
    elif (data.mode == "2Player"):twoPlayerRedrawAll(canvas, data)
    elif (data.mode == "editor"): editorRedrawAll(canvas, data)
    elif (data.mode == "levelCreated"): levelCreatedRedrawAll(canvas,data)
    elif (data.mode == "AI"): AIRedrawAll(canvas, data)
    elif (data.mode == "difficulty"): difficultyRedrawAll(canvas, data)
    elif (data.mode == "scoreboard"): scoreboardRedrawAll(canvas, data)
    elif (data.mode == "help"): helpRedrawAll(canvas, data)

####################################
# splashScreen mode
####################################
def splashScreenMousePressed(event, data):
    #checks for selection of mode
    if data.splashButtonY-2*data.r <= event.x <=data.splashButtonY+2*data.r:
        if data.p1ButtonX-data.r<=event.y<=data.p1ButtonX+data.r:
            data.mode = "1Player"
        if data.p2ButtonX-data.r<=event.y<=data.p2ButtonX+data.r:
            data.mode = "2Player"
        if data.edButton-data.r<=event.y<=data.edButton+data.r:
            data.mode = "editor"
        if data.diffButton-data.r<=event.y<=data.diffButton+data.r:
            data.mode = "difficulty"
        if data.helpButton-data.r<=event.y<=data.helpButton+data.r:
            data.mode = "help"
        if data.sboardButton-data.r<=event.y<=data.sboardButton+data.r:
            data.mode = "scoreboard"

def splashKeyPressed(event, data):
    pass


def splashScreenTimerFired(data):
    data.splashScreenTime += 1
    if data.splashScreenTime %2 ==1:
        rainDropSplash(data)
    for drop in data.splashScreenDrops:
            drop.onTimerFired(data)

def splashScreenButtons(canvas, data):
    canvas.create_image(data.splashButtonY,data.p1ButtonX,image = data.mode1)
    canvas.create_image(data.splashButtonY,data.p2ButtonX,image = data.mode2)
    canvas.create_image(data.splashButtonY,data.edButton,image = data.mode3)
    canvas.create_image(data.splashButtonY,data.diffButton,image = data.mode4)
    canvas.create_image(data.splashButtonY,data.helpButton,image = data.mode5)
    canvas.create_image(data.splashButtonY,data.sboardButton,image =data.mode6)
        
def rainDropSplash(data):
    xPosition = random.randint(0,800)
    data.splashScreenDrops.append(Coconuts(xPosition,0))

def splashScreenRedrawAll(canvas, data):
    canvas.create_image(data.width/2, data.splashText-10, image=data.title)
    for drop in data.splashScreenDrops: drop.draw(canvas)
    canvas.create_text(data.width/2, data.splashText, text="""
       1.) Single Player Level Mode


       2.) Two-Player Mode

       
       3.) Level Creator Practice Mode

       
       4.) Play Against the Computer

       
       5.) Help and Instructions

       
       6.) Scoreboard

       
       """, font="Arial 14 bold", fill = "yellow")
    splashScreenButtons(canvas, data)

####################################
# taken from class notes
####################################

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

####################################
# 1Player mode
####################################


#Coconuts (from Mario game) represent the water drops
class Coconuts(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.r = 9
        self.fill = "deep sky blue"
        self.speed = 30
        self.outline= "blue"

    def draw(self, canvas):
        canvas.create_polygon(self.x,self.y- 2*self.r,
                              self.x-self.r, self.y,
                              self.x, self.y + self.r,
                              self.x+self.r, self.y, fill = self.fill,
                              outline = self.outline, width = 3)

    def onTimerFired(self, data):
        # downward falling motion
        self.y += self.speed
    
def hit(data):
    #checks for hitting rain
    for coconut in data.coconuts:
        if data.mode == "1Player" or data.mode == "levelCreated":
            if coconut.y>=data.cy-data.r and coconut.y<=data.cy+data.r:
                if coconut.x>=data.cx-data.r and coconut.x<=data.cx+data.r:
                    data.cy+=data.hitPenalty
                    if data.mode == "levelCreated":
                        data.lives-=1
                    elif data.hit ==False and data.level<data.levelMax:
                        data.score -=data.level
                    data.coconuts.remove(coconut)
                    if data.mode == "levelCreated":
                        data.levelEditorLives-=1

                    
def hit2Player(data):
    if data.mode == "2Player":
        if data.Invincible1 == False:
            #only when powerup isn't active
            for coconut in data.coconuts1:
                if coconut.y>=data.player1Y-data.r \
                and coconut.y<=data.player1Y+data.r:
                    if coconut.x>=data.player1X-data.r and \
                       coconut.x<=data.player1X+data.r:
                        data.player1Y+=data.hitPenalty 
                        data.coconuts1.remove(coconut)
        if data.Invincible2 == False:
            #only when powerup isn't active
            for coconut in data.coconuts2:
                if coconut.y>=data.player2Y-data.r and \
                   coconut.y<=data.player2Y+data.r:
                    if coconut.x>=data.player2X-data.r and \
                       coconut.x<=data.player2X+data.r:
                        data.player2Y+=data.hitPenalty 
                        data.coconuts2.remove(coconut)


class PowerUps(Coconuts):
    def __init__(self,x,y):
        super().__init__(x, y)

    def draw(self, canvas, data):
         canvas.create_image(self.x, self.y, image=data.hourGlass)
         
def hitPause(data):
    # checks if hits hour-glass & pauses with flag
    for powerUp in data.powerUps:
        if data.mode == "1Player" or data.mode == "levelCreated":
            if powerUp.y>=data.cy-data.r and powerUp.y<=data.cy+data.r:
                if powerUp.x>=data.cx-data.r and powerUp.x<=data.cx+data.r:
                    data.pauseDrops = True
                    data.start = data.cy
                    data.powerUps.remove(powerUp)
        elif data.mode == "2Player" or data.mode == "AI":
            if powerUp.y>=data.player1Y-data.r and \
               powerUp.y<=data.player1Y+data.r:
                if powerUp.x>=data.player1X-data.r and \
                   powerUp.x<=data.player1X+data.r:
                    data.pause1Drop = True
                    data.start1 = data.player1Y
                    data.powerUps.remove(powerUp)
            if powerUp.y>=data.player2Y-data.r and \
               powerUp.y<=data.player2Y+data.r:
                if powerUp.x>=data.player2X-data.r and \
                   powerUp.x<=data.player2X+data.r:
                    data.pause2Drop = True
                    data.start2 = data.player2Y
                    data.powerUps.remove(powerUp)
                    

class Invincible(PowerUps):
    def __init__(self,x,y):
        super().__init__(x, y)
    
    def draw(self, canvas, data):
         canvas.create_image(self.x, self.y, image=data.umbrella)

def hitInvincible(data):
    #checks if hits umbrella powerup
    for powerUp in data.invincible:
        if data.mode == "1Player" or data.mode == "levelCreated":
            if powerUp.y>=data.cy-data.r and powerUp.y<=data.cy+data.r:
                if powerUp.x>=data.cx-data.r and powerUp.x<=data.cx+data.r:
                    data.beInvincible = True
                    data.start = data.cy
                    data.invincible.remove(powerUp)
        if data.mode == "2Player" or data.mode == "AI":
            #for player1
            if powerUp.y>=data.player1Y-data.r and \
               powerUp.y<=data.player1Y+data.r:
                if powerUp.x>=data.player1X-data.r and \
                   powerUp.x<=data.player1X+data.r:
                    data.Invincible1=True
                    data.start1 = data.player1Y
                    data.invincible.remove(powerUp)
            # for player 2
            if powerUp.y>=data.player2Y-data.r and \
               powerUp.y<=data.player2Y+data.r:
                if powerUp.x>=data.player2X-data.r and \
                   powerUp.x<=data.player2X+data.r:
                    data.Invincible2=True
                    data.start2 = data.player2Y
                    data.invincible.remove(powerUp)
         
class ScaryBug(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 25

    def draw(self, canvas, data):
        canvas.create_image(self.x, self.y, image=data.spider)

    def onTimerFired(self, data):
        if data.mode =="2Player" or data.mode == "AI":
            self.speed = 35
        self.y -= self.speed
        if data.mode == "1Player" or data.mode == "levelCreated" and\
           data.time %8 ==0:
            #makes spider dynamically move
            side = random.choice(data.sides)
            if side == "l":
                if self.x -data.lane >=data.Player1Min:self.x-=data.lane
                else: self.x+=data.lane
            elif side == "r":
                if self.x+data.lane<= data.Player1Max:self.x +=data.lane
                else: self.x -=data.lane
                    
            
         
def hitScaryBug(data):
    # checks for automatic death by spider
    for bug in data.scaryBug:
        if data.mode == "1Player" or data.mode == "levelCreated":
            if bug.y>=data.cy-1.5*data.r and bug.y<=data.cy+1.5*data.r:
                if bug.x>=data.cx-1.5*data.r and bug.x<=data.cx+1.5*data.r:
                    data.hit = True
                    data.lives = 0
                    data.levelEditorLives = 0
        if data.mode == "2Player" or data.mode == "AI":
            if bug.y>=data.player1Y-data.r and bug.y<=data.player1Y+data.r:
                if bug.x>=data.player1X-data.r and bug.x<=data.player1X+data.r:
                    data.winner= "player2"
            if bug.y>=data.player2Y-data.r and bug.y<=data.player2Y+data.r:
                if bug.x>=data.player2X-data.r and bug.x<=data.player2X+data.r:
                    data.winner= "player1"

def drawPowerups(canvas, data):
    for bug in data.scaryBug:
        bug.draw(canvas, data)
    for powerUp in data.powerUps:
        powerUp.draw(canvas, data)
    for powerUp in data.invincible:
        powerUp.draw(canvas, data)

def drawHome(canvas, data):
    #home button in every screen
    canvas.create_image(data.homeX,data.homeY, image= data.home)

def checkHome(event, data):
    if data.homeY-data.r<= event.y <= data.homeY +data.r:
        if data.homeX-data.r<= event.x<=data.homeX+ data.r:
            init(data)
        
def coconutShot(data):
    if data.level >0 and data.pauseDrops == False:
        if data.time%int(data.levelMax/data.level) == 0 or data.time%6==0:
            #increases drops as level increases
            xPosition1 = random.randint(0,data.Player1Min-data.buffer)
            xPosition2 = random.randint(data.Player1Max+data.buffer,
                                        data.width +data.buffer)
            data.coconuts.append(Coconuts(xPosition1,0))
            data.coconuts.append(Coconuts(xPosition2,0))
            xPosition4 = random.randint(data.Player1Min-data.buffer,
                                        data.Player1Max+data.buffer)
            data.coconuts.append(Coconuts(xPosition4,0))
        if data.time %5 ==0:
            xPosition3 = random.randint(0, data.Player1Min-data.buffer)
            data.coconuts.append(Coconuts(xPosition3,0))
        if data.time % int(24/data.level) ==0:
            side = random.choice(data.sides)
            if side == "l": 
                data.coconuts.append(Coconuts(data.Player1Min,0))
            elif side =="r":
                data.coconuts.append(Coconuts(data.Player1Max,0))
        powerUpCoconutShot(data)
        
def powerUpCoconutShot(data):
    #adds powerUps
    #magic #s toallow for powerups to be added at different times
        if data.time % 60 == 0 and data.time%120 !=0:
            Position = random.choice(data.spotList)
            data.powerUps.append(PowerUps(Position,0))
        if data.time%50 == 0:
            Position = random.choice(data.spotList)
            data.invincible.append(Invincible(Position,0))
        if data.time %100==0:
            Position = random.choice(data.spotList)
            data.scaryBug.append(ScaryBug(Position,750))

def playerKeyPressed(event,data):
    if data.level<data.levelMax and event.keysym == "r": init(data)
    if (event.keysym == "Left") and data.cx>=data.Player1Min+(data.lane/2):
        data.cx -=(data.lane)/2
    elif(event.keysym == "Right") and data.cx<=data.Player1Max:
        data.cx +=(data.lane)/2
    if data.level >= data.levelMax:
        #enter name for scoreboard
        if len(event.keysym) ==1:
            if len(data.name) <15:
                data.name += event.keysym
        if event.keysym=="BackSpace":
            data.name = data.name[0:-1]
        if event.keysym == "Return":
            data.scoreList += ((data.score, data.name))
            #saves file
            writeFile("score.txt",
                      data.savedScores+str(data.score)+","+data.name+"\n")
            data.mode ="scoreboard"
        

def playerMousePressed(event, data): checkHome(event, data)

def playerTimerFired(data):
    #actually pauses, and moves drops/player
    if data.hit== False and data.level<data.levelMax:
        data.cy-=data.speed
        if data.time%5 ==0: data.score +=data.level
        if data.cy < 15: #basically made it to the top
            data.level +=1
            data.cy = data.Player1Max + 10
            data.speed +=2
        if data.cy>40: #so drops you can't see don't hit you
            data.time +=1
            if data.pauseDrops !=True: coconutShot(data)
        for powerUp in data.powerUps: powerUp.onTimerFired(data)
        hitPause(data)
        for powerUp in data.invincible: powerUp.onTimerFired(data)
        hitInvincible(data)
        for bug in data.scaryBug: bug.onTimerFired(data)
        hitScaryBug(data)
        for coconut in data.coconuts:
            # only want drops to move if not paused
            if data.pauseDrops == False: coconut.onTimerFired(data)
        if data.beInvincible == False:hit(data)
        if data.start != None:
            if abs(data.start-data.cy) >= 120:
                #to limit time for powerups to be active
                data.pauseDrops, data.beInvincible = False, False

def playerRedrawAll(canvas, data):
    # magic #s mainly for screen placement
    canvas.create_image(data.width/2, data.height/2, image=data.background)
    canvas.create_line(0,20, data.width, 20)
    for coconut in data.coconuts: coconut.draw(canvas)
    drawPowerups(canvas, data)
    canvas.create_image(data.cx, data.cy, image=data.ladyBug)
    canvas.create_text(data.width/6,50, text ="Level: %d" %data.level,
                       font = "Arial 18 bold", fill = "yellow")
    canvas.create_text(data.width/6,80, text ="Score: %d" %data.score,
                       font = "Arial 18 bold", fill = "yellow")
    canvas.create_text(2*data.width/3,660,
                       text ="""The greater the level, the more points get
                    added to your score!""",
                       font = "Arial 15 bold", fill = "yellow")
    if data.hit== True:
        canvas.create_rectangle(0,0,data.width, data.height, fill = "black")
        canvas.create_image(data.width/2, data.height/2, image=data.deadScreen)
        canvas.create_text(data.width/2,data.height/4,
                           text = "You Lose! Better Luck Next Time!",
                           font = "Helvetica 23 bold", fill = "yellow")
        canvas.create_text(data.width/2,280, text ="Score: %d" %data.score,
                       font = "Arial 13 bold", fill = "yellow")
    if data.level >= 8: madeIt(canvas, data)
    drawHome(canvas, data)

def madeIt(canvas, data):# magic #s mainly for screen placement
    canvas.create_rectangle(0,0, data.width, data.height, fill = "black")
    canvas.create_image(data.width/2, data.height/2, image=data.winScreen)
    canvas.create_image(300, 320, image=data.winBug)
    canvas.create_text(data.width/2,70, text = "You Made it!",
                       font = "Arial 23 bold", fill = "yellow")
    canvas.create_text(data.width/2,100, text ="Score: %d" %data.score,
                   font = "Arial 15 bold", fill = "yellow")
    canvas.create_text(data.width/2,375, text ="Congrats! Enter your Name!",
                   font = "Arial 15 bold", fill = "yellow")
    canvas.create_rectangle(data.width/2 - 50, 400, data.width/2+50, 450,
                            fill = "white")
    canvas.create_text(data.width/2, 425, text = data.name)
    
        
####################################
# 2Player mode
####################################        
def drop2Player(data):
    #adds drops when not paused
    #magic #s are position of where drops are starting
    if data.winner ==None and data.pauseDrops == False:
        if data.time%15==0:
            xPosition1 = random.randint(0,385)
            if abs(xPosition1 - 100)>25 and abs(xPosition1 - 360)>25:
                #so random drops don't interfere with the lane ones
                if data.pause1Drop != True:
                    data.coconuts1.append(Coconuts(xPosition1,0))
                if data.pause2Drop != True:
                    data.coconuts2.append(Coconuts(xPosition1 +410,0))
        if data.time % 12 ==0:
            side = random.choice(data.sides)
            if side == "l":
                if data.pause1Drop != True:
                    data.coconuts1.append(Coconuts(140,0))
                if data.pause2Drop != True:
                    data.coconuts2.append(Coconuts(540,0))
            elif side =="r":
                if data.pause1Drop !=True:data.coconuts1.append(Coconuts(344,0))
                if data.pause2Drop!=True:data.coconuts2.append(Coconuts(755,0))
        powerupDrop2Player(data)

def powerupDrop2Player(data):
    #adds powerups on both screens (in the same position)
        if data.time % 45 == 0 and data.time%90 !=0:
            #randomize placement
            side = random.choice(data.sides)
            if side == "l":
                if data.pause1Drop!=True:data.powerUps.append(PowerUps(140,0))
                if data.pause2Drop!=True:data.powerUps.append(PowerUps(540,0))
            elif side =="r":
                if data.pause1Drop!=True:data.powerUps.append(PowerUps(344,0))
                if data.pause2Drop!=True:data.powerUps.append(PowerUps(755,0))
        if data.time%60 == 0:
            side = random.choice(data.sides)
            if side == "l": 
                if data.pause1Drop!=True:data.invincible.append(Invincible(140,0))
                if data.pause2Drop!=True:data.invincible.append(Invincible(540,0))
            elif side =="r":
                if data.pause1Drop!=True:data.invincible.append(Invincible(344,0))
                if data.pause2Drop!=True:data.invincible.append(Invincible(755,0))
        if data.time %90==0:
            side = random.choice(data.sides)
            if side == "l": 
                data.scaryBug.append(ScaryBug(140,750))
                data.scaryBug.append(ScaryBug(540,750))
            elif side =="r":
                data.scaryBug.append(ScaryBug(344,750))
                data.scaryBug.append(ScaryBug(755,750))
                
def twoPlayerKeyPressed(event,data):
    # controllers for both bugs
    if event.keysym == "r": init(data)
    if data.winner==None:
        if (event.keysym == "a") and data.onLeft1==False:
            data.onLeft1 = True
            data.player1X = 150
        if(event.keysym == "d") and data.onLeft1== True:
            data.onLeft1 = False
            data.player1X = 330
        if (event.keysym == "Left") and data.onLeft2==False:
            data.onLeft2 = True
            data.player2X = 550
        if(event.keysym == "Right") and data.onLeft2 == True:
            data.onLeft2 = False
            data.player2X = 750

def twoPlayerMousePressed(event, data):
    checkHome(event, data)
    
def twoPlayerTimerFired(data):
    if data.winner == None:
        data.player1Y-=data.speed
        #<15 signifies that lady bug reached the top
        if data.player1Y < 15 and data.player2Y >15:
            data.winner= "player1"
        if data.player1Y>40:
            data.time +=1
            drop2Player(data)
        data.player2Y-=data.speed
        if data.player2Y < 15 and data.player1Y> 15:
            data.winner= "player2"
        if data.player2Y>40:
            data.time +=1
            drop2Player(data)
        if data.player1Y < 15 and data.player2Y <15:
            data.winner = "tie"
        for powerUp in data.powerUps: powerUp.onTimerFired(data)
        hitPause(data)
        for powerUp in data.invincible:powerUp.onTimerFired(data)
        hitInvincible(data)
        for bug in data.scaryBug:bug.onTimerFired(data)
        hitScaryBug(data)
        powerupTimerFired(data)

def powerupTimerFired(data):
        for coconut in data.coconuts1:
            if data.pause1Drop == False:
                coconut.onTimerFired(data)
        hit2Player(data)
        for coconut in data.coconuts2:
            if data.pause2Drop == False:
                coconut.onTimerFired(data)      
        if data.start1 != None:
            # to make powerups only active for set amount of time
            if abs(data.start1-data.player1Y) >= 120:
                data.pause1Drop = False
                data.Invincible1 = False
        if data.start2 != None:
            if abs(data.start2-data.player2Y) >= 120:
                data.pause2Drop = False
                data.Invincible2 = False
        

def twoPlayerRedrawAll(canvas, data):
    #magic #s for placement on screen
    canvas.create_image(data.width/4, data.height/2, image=data.halfBackground)
    canvas.create_image(3*data.width/4, data.height/2,image=data.halfBackground)
    canvas.create_line(data.width/2, 0, data.width/2, data.height, width = 10)
    canvas.create_line(0,20, data.width, 20)
    for coconut in data.coconuts1: coconut.draw(canvas)
    for coconut in data.coconuts2: coconut.draw(canvas)
    drawPowerups(canvas, data)
    canvas.create_image(data.player1X, data.player1Y, image=data.ladyBug)
    canvas.create_image(data.player2X, data.player2Y, image=data.ladyBug)
    canvas.create_text(50,40, text = "Player 1",font = "Arial 15 bold",
                       fill = "yellow")
    canvas.create_text(450,40, text = "Player 2",font = "Arial 15 bold",
                       fill = "yellow")
    winner(canvas, data)
    drawHome(canvas, data)

def winner(canvas, data):
    if data.winner== "player1":
        canvas.create_rectangle(0,0, data.width, data.height, fill = "black")
        canvas.create_image(data.width/2, data.height/2, image=data.winScreen)
        canvas.create_image(300, 320, image=data.winBug)
        canvas.create_text(data.width/2,100, text = "You Made it! Player 1",
                           font = "Arial 23 bold", fill = "yellow")
    elif data.winner== "player2":
        canvas.create_rectangle(0,0, data.width, data.height, fill = "black")
        canvas.create_image(data.width/2, data.height/2, image=data.winScreen)
        canvas.create_image(300, 320, image=data.winBug)
        canvas.create_text(data.width/2,100, text = "You Made it! Player 2",
                           font = "Arial 23 bold", fill = "yellow")
    elif data.winner== "tie":
        canvas.create_rectangle(0,0, data.width, data.height, fill = "black")
        canvas.create_image(data.width/2, data.height/2, image=data.winScreen)
        canvas.create_image(300, 320, image=data.winBug)
        canvas.create_text(data.width/2,100, text = "Tie! You Both Made it!",
                           font = "Arial 23 bold", fill = "yellow")

####################################
# editor mode
####################################

def editorKeyPressed(event,data):
    if event.keysym == "r": init(data)

def editorMousePressed(event, data):
    #check for click on button for your speed
    checkHome(event, data)
    if data.easyY-data.r<= event.y <= data.easyY +data.r:
        if data.easyX-2*data.r<= event.x<=data.easyX+2*data.r:
            data.yourSpeed = "slow"
            data.slow =  data.click
            data.medium, data.fast = data.notClick, data.notClick
        if data.medX-2*data.r<= event.x<=data.medX+2*data.r:
            data.yourSpeed = "medium"
            data.medium = data.click
            data.slow, data.fast = data.notClick, data.notClick
        if data.hardX-2*data.r<= event.x<=data.hardX+2*data.r:
            data.yourSpeed = "fast"
            data.fast = data.click
            data.slow, data.medium = data.notClick, data.notClick
    checkMiddle(event, data)
    checkLast(event, data)

def checkMiddle(event, data):
    #check for click on button for rain speed
    if data.medX-data.r<= event.y <= data.medX + data.r:
        if data.easyX-2*data.r<= event.x<=data.easyX+2*data.r:
            data.rainSpeed = "drizzle"
            data.drizzle = data.click
            data.rain, data.thunderstorm = data.notClick, data.notClick
        if data.medX-2*data.r<= event.x<=data.medX+2*data.r:
            data.rainSpeed = "rain"
            data.rain = data.click
            data.drizzle, data.thunderstorm = data.notClick, data.notClick
        if data.hardX-2*data.r<= event.x<=data.hardX+2*data.r:
            data.rainSpeed = "thunderstorm"
            data.thunderstorm = data.click
            data.drizzle, data.rain = data.notClick, data.notClick

def checkLast(event, data):
    #check for click on button for powerups
    if data.last-data.r<=event.y<= data.last+data.r:
        if data.easyY-2*data.r<= event.x<=data.easyY+2*data.r:
            data.powerUpsEditor = True
            data.yes, data.no = data.click, data.notClick
        if data.last-2*data.r<= event.x<=data.last+2*data.r:
            data.powerUpsEditor = False
            data.no, data.yes = data.click, data.notClick
    if data.enter == data.click:
        if data.enterX-data.r<=event.y<=data.enterX+data.r:
            if data.medX-2*data.r<= event.x<=data.medX+2*data.r:
                data.mode="levelCreated"
                
            

def drawButtons(canvas, data):
    #makes each button
    data.font, data.fill = "Helvetica 13 bold", "yellow"
    canvas.create_text(data.medX,data.YST, text= "Your Speed:",
                       font = data.font,fill =data.fill)
    canvas.create_image(data.easyX,data.easyY, image = data.slow)
    canvas.create_text(data.easyX,data.easyY, text="Slow", font = data.font)
    canvas.create_image(data.medX,data.easyY, image = data.medium)
    canvas.create_text(data.medX,data.easyY, text="Medium", font = data.font)
    canvas.create_image(data.hardX,data.easyY, image = data.fast)
    canvas.create_text(data.hardX,data.easyY, text="Fast",font = data.font)
    canvas.create_image(data.easyX,data.medX, image = data.drizzle)
    canvas.create_text(data.medX,data.RST, text= "Rain Speed:",
                       font = data.font,fill =data.fill)
    canvas.create_text(data.easyX,data.medX, text="Drizzle",font = data.font)
    canvas.create_image(data.medX,data.medX, image = data.rain)
    canvas.create_text(data.medX,data.medX, text="Rain",font = data.font)
    canvas.create_image(data.hardX,data.medX, image = data.thunderstorm)
    canvas.create_text(data.hardX,data.medX, text="Heavy",font = data.font)
    canvas.create_text(data.medX,data.PUT, text= "PowerUps?",
                       font = data.font,fill =data.fill)
    canvas.create_image(data.easyY,data.last, image = data.yes)
    canvas.create_text(data.easyY,data.last, text="Yes",font = data.font)
    canvas.create_image(data.last,data.last, image = data.no)
    canvas.create_text(data.last,data.last, text="No",font = data.font)
    changeEnter(canvas, data)

def changeEnter(canvas, data):
    #makes it so the enter button respond to click
    if data.powerUpsEditor != None and data.yourSpeed != None and \
       data.rainSpeed != None: data.enter = data.click
    canvas.create_image(data.medX,data.enterX, image = data.enter)
    canvas.create_text(data.medX,data.enterX, text="Enter",font = data.font)

def editorTimerFired(data):
    data.editorTime += 1
    if data.editorTime %2 ==0:
        rainDrop(data)
    for drop in data.editorDrops:
            drop.onTimerFired(data)

def rainDrop(data):
    #background drops
    xPosition = random.randint(0,data.width)
    data.editorDrops.append(Coconuts(xPosition,0))

def editorRedrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image=data.background)
    canvas.create_image(data.width/2, data.height/2, image=data.tbg)
    for drop in data.editorDrops:
        drop.draw(canvas)
    canvas.create_text(data.width/2, data.S_P -10, text = "Edit Your Level!",
                       font="Arial 23 bold", fill = "yellow")
    drawButtons(canvas, data)
    drawHome(canvas, data)
####################################
# levelCreated mode
####################################
def setEverything(data):
    #customizing game
    if data.yourSpeed == "slow": data.speed = 6
    elif data.yourSpeed == "medium": data.speed = 10
    elif data.yourSpeed == "fast": data.speed = 14
    if data.rainSpeed == "thunderstorm": data.rSpeed = 7
    elif data.rainSpeed == "rain": data.rSpeed = 10
    elif data.rainSpeed == "drizzle": data.rSpeed = 13
        

def levelCoconutShot(data):
    #adding drops
    if data.levelEditorLives >0:
        if data.time%int(0.35*data.rSpeed) == 0:
            xPosition1 = random.randint(0,data.Player1Min-data.buffer)
            xPosition2 = random.randint(770, 870)
            xPosition3 = random.randint(220,770)
            data.coconuts.append(Coconuts(xPosition3,0))
            data.coconuts.append(Coconuts(xPosition1,0))
            data.coconuts.append(Coconuts(xPosition2,0))
        if data.time % int(0.55*data.rSpeed) ==0:
            xPosition3 = random.randint(0, 220)
            xPosition5 = random.randint(220,770)
            data.coconuts.append(Coconuts(xPosition3,0))
            data.coconuts.append(Coconuts(xPosition5,0))
        if data.time % int(data.rSpeed) ==0:
            side = random.choice(data.sides)
            if side == "l": 
                data.coconuts.append(Coconuts(3*data.width/8-20,0))
            elif side =="r":
                data.coconuts.append(Coconuts(7*data.width/8+40,0))
            xPosition4= random.randint(220,770)
            data.coconuts.append(Coconuts(xPosition4,0))
            
        levelPowerUp(data)

def levelPowerUp(data):
    # adding power-ups only if clicked yes
    if data.powerUpsEditor == True:
        if data.time % 20 == 0 and data.time%40 !=0:
            Position = random.choice(data.spotList)
            data.powerUps.append(PowerUps(Position,0))
        if data.time%30 == 0:
            Position = random.choice(data.spotList)
            data.invincible.append(Invincible(Position,0))
        if data.time %35==0:
            Position = random.choice(data.spotList)
            data.scaryBug.append(ScaryBug(Position,750))

def levelCreatedKeyPressed(event,data):
    if event.keysym == "r": init(data)
    if data.levelEditorLives>0:
        if (event.keysym == "Left") and data.cx>=317:
            data.cx -=(data.lane/2)
        elif(event.keysym == "Right") and data.cx<=740:
            data.cx +=(data.lane/2)

def levelCreatedMousePressed(event, data):
    checkHome(event, data)

def levelCreatedTimerFired(data):
    setEverything(data)
    if data.levelEditorLives>0:
        data.cy-=data.speed
        if data.cy < 15:
            data.level +=1
        if data.cy>40:
            data.time +=1
            if data.pauseDrops !=True: levelCoconutShot(data)
        if data.powerUpsEditor == False:
            for coconut in data.coconuts: coconut.onTimerFired(data)
            hit(data)
        if data.powerUpsEditor == True:
            for powerUp in data.powerUps: powerUp.onTimerFired(data)
            hitPause(data)
            for powerUp in data.invincible: powerUp.onTimerFired(data)
            hitInvincible(data)
            for bug in data.scaryBug: bug.onTimerFired(data)
            hitScaryBug(data)
            for coconut in data.coconuts:
                if data.pauseDrops == False:coconut.onTimerFired(data)
            if data.beInvincible == False: hit(data)
            if data.start != None:
                            #to make powerups only active for set amount of time
                if abs(data.start-data.cy) >= 120:
                    data.pauseDrops, data.beInvincible = False, False


def levelCreatedRedrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image=data.background)
    canvas.create_line(0,20, data.width, 20)
    for coconut in data.coconuts: coconut.draw(canvas)
    if data.powerUpsEditor == True: drawPowerups(canvas, data)
    canvas.create_image(data.cx, data.cy, image=data.ladyBug)
    canvas.create_text(data.width/6,100,
                       text ="Total Lives: %d" %data.levelEditorLives,
                       font = "Arial 20 bold", fill = "yellow")
    canvas.create_text(data.width/2,660,
                       text ="""You lose a life for hitting a drop
         & don't get eaten!""",
                       font = "Arial 15 bold", fill = "yellow")
    if data.levelEditorLives <=0:
        canvas.create_rectangle(0,0, data.width, data.height, fill = "black")
        canvas.create_image(data.width/2, data.height/2, image=data.deadScreen)
        canvas.create_text(data.width/2,data.height/4,
                           text = "You Lose! Better Luck Next Time!",
                           font = "Helvetica 23 bold", fill = "yellow")    
    if data.level > 1: winEditor(canvas, data)
    drawHome(canvas, data)

def winEditor(canvas, data):
    #screen for when you win
    canvas.create_rectangle(0,0, data.width, data.height, fill = "black")
    canvas.create_image(data.width/2, data.height/2, image=data.winScreen)
    canvas.create_image(300, 320, image=data.winBug)
    canvas.create_text(data.width/2,100, text = "You Made it!",
                       font = "Arial 23 bold", fill = "yellow")

####################################
# AI Difficulty Mode
####################################
def difficultyKeyPressed(event,data):
    if event.keysym == "r": init(data)

def drawDifficulties(canvas, data):
    canvas.create_text(data.medX,data.AITY, text= "Computer Difficulty:",
                       font="Arial 23 bold", fill = "yellow") 
    canvas.create_image(data.easyX, data.easyY, image=data.slow)
    canvas.create_text(data.easyX,data.easyY, text="Easy")
    canvas.create_image(data.medX, data.easyY, image=data.medium)
    canvas.create_text(data.medX,data.easyY, text="Medium")
    canvas.create_image(data.hardX, data.easyY, image=data.fast)
    canvas.create_text(data.hardX,data.easyY, text="Hard")
    if data.difficulty !=None:
        data.enter = data.click
    canvas.create_image(data.medX, data.enterY, image=data.enter)
    canvas.create_text(data.medX,data.enterY, text="Enter")

def difficultyMousePressed(event, data):
    #sets up buttons to customize
    checkHome(event, data)
    if data.easyY-data.r<= event.y <= data.easyY +data.r:
        if data.easyX-2*data.r<= event.x<=data.easyX+2*data.r:
            data.difficulty = data.difS
            data.slow = data.click
            data.medium, data.fast = data.notClick, data.notClick
        if data.medX-2*data.r<= event.x<=data.medX+2*data.r:
            data.difficulty = data.difM
            data.medium = data.click
            data.slow, data.fast = data.notClick, data.notClick
        if data.hardX-2*data.r<= event.x<=data.hardX+2*data.r:
            data.difficulty = data.difH
            data.fast = data.click
            data.slow, data.medium = data.notClick, data.notClick
    if data.enter == data.click:
        if data.enterY-data.r<=event.y<=data.enterY+data.r:
            if data.medX-2*data.r<= event.x<=data.medX+2*data.r:
                data.mode="AI"

def difficultyTimerFired(data):
    # makes normal background rain
    data.editorTime += 1
    if data.editorTime %2 ==0:
        rainDrop(data)
    for drop in data.editorDrops:
            drop.onTimerFired(data)

def rainDrop(data):
    xPosition = random.randint(0,data.width)
    data.editorDrops.append(Coconuts(xPosition,0))

def difficultyRedrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image=data.background)
    canvas.create_image(data.width/2, data.height/2, image=data.tbg)
    for drop in data.editorDrops:
        drop.draw(canvas)
    drawDifficulties(canvas, data)
    drawHome(canvas, data)

####################################
# AI mode
####################################
def hitAI1(data, distance):
    for coconut in data.coconutsAI1:
        # so AI switches by itself
        if (data.player1Y-data.r - coconut.y<=distance) and \
           data.switchOnProgress == False:
            if coconut.x>=data.player1X-data.r and \
            coconut.x<=data.player1X+data.r or AISwitchBug(data,distance)==True:
                testInt = random.randint(0,9)
                # to have different levels of difficulty
                if testInt<= data.difficulty:
                    data.switchOnProgress= True
                    if data.player1X == 150:
                        data.player1X = 340
                    else:
                        data.player1X = 150
                    data.switchOnProgress= False
        if coconut.y>=data.player1Y-data.r and coconut.y<=data.player1Y+data.r:
            if coconut.x>=data.player1X-data.r and \
               coconut.x<=data.player1X+data.r:
                data.player1Y+=50
                data.coconutsAI1.remove(coconut)

def AISwitchBug(data, distance):
    #AI to move for spider
    for scaryBug in data.scaryBug:
        if (data.player1Y-data.r - scaryBug.y<=distance) and \
           data.switchOnProgress == False:
            if scaryBug.x>=data.player1X-data.r and \
               scaryBug.x<=data.player1X+data.r:
                return True

def hitAI2(data, distance):
    # check if human controlled player hits drops
    for coconut in data.coconutsAI2:
        if coconut.y>=data.player2Y-data.r and coconut.y<=data.player2Y+data.r:
            if coconut.x>=data.player2X-data.r and \
               coconut.x<=data.player2X+data.r:
                data.player2Y+=50 
                data.coconutsAI2.remove(coconut)
                    
def coconutShotAI(data):
    if data.winner ==None:
        # randomize position of drops off of tree
        if data.time%15==0:
            xPosition1 = random.randint(0,385)
            if abs(xPosition1 - 100)>40 and abs(xPosition1 - 360)>40:
                if data.pause1Drop != True:
                    data.coconutsAI1.append(Coconuts(xPosition1,0))
                if data.pause2Drop != True:
                    data.coconutsAI2.append(Coconuts(xPosition1 +410,0))
        if data.time%8 ==0:
            xPosition2 = random.randint(0,80)
            xPosition3 = random.randint(364, 385)
            if data.pause1Drop != True:
                data.coconutsAI1.append(Coconuts(xPosition2,0))
                data.coconutsAI1.append(Coconuts(xPosition3,0)) 
            if data.pause2Drop != True:
                data.coconutsAI2.append(Coconuts(xPosition2+410,0))
                data.coconutsAI2.append(Coconuts(xPosition3+410,0))
        addExtraCoconut(data)
        addPowerUpsAI(data)

def addExtraCoconut(data):
    #adds drops to edges of trees
    if data.time % (18) ==0:
        side = random.choice(data.sides)
        if side == "l":
            if data.pause1Drop != True:
                data.coconutsAI1.append(Coconuts(140,0))
            if data.pause2Drop != True:
                data.coconutsAI2.append(Coconuts(540,0))
        elif side =="r":
            if data.pause1Drop != True:
                data.coconutsAI1.append(Coconuts(344,0))
            if data.pause2Drop != True:
                data.coconutsAI2.append(Coconuts(755,0))
    if data.time % 37 == 0:
        side = random.choice(data.sides)
        if side == "l":
            if data.pause1Drop != True:
                data.powerUps.append(PowerUps(140,0))
            if data.pause2Drop != True:
                data.powerUps.append(PowerUps(550,0))
        elif side =="r":
            if data.pause1Drop != True:
                data.powerUps.append(PowerUps(344,0))
            if data.pause2Drop != True:
                data.powerUps.append(PowerUps(755,0))
                    
def addPowerUpsAI(data):
    #randomly add powerups on tree
    if data.time%33 == 0:
        side = random.choice(data.sides)
        if side == "l":
            if data.pause1Drop != True:
                data.invincible.append(Invincible(140,0))
            if data.pause2Drop != True:
                data.invincible.append(Invincible(550,0))
        elif side =="r":
            if data.pause1Drop != True:
                data.invincible.append(Invincible(344,0))
            if data.pause2Drop != True:
                data.invincible.append(Invincible(755,0))
    if data.time %66==0:
        side = random.choice(data.sides) 
        if side == "l":
            data.scaryBug.append(ScaryBug(140,750))
            data.scaryBug.append(ScaryBug(550,750))
        elif side =="r":
            data.scaryBug.append(ScaryBug(344,750))
            data.scaryBug.append(ScaryBug(750,750))

                
def AIKeyPressed(event,data):
    if event.keysym == "r": init(data)
    if data.winner==None:
        if (event.keysym == "Left") and data.onLeft1==False:
            data.onLeft1 = True
            data.player2X = 550
        elif(event.keysym == "Right") and data.onLeft1== True:
            data.onLeft1 = False
            data.player2X = 750

def AIMousePressed(event, data): checkHome(event, data)
def AITimerFired(data):
    if data.winner == None:
        #want to check hit twice (before & after elements move)
        if data.Invincible1 == False:hitAI1(data, 31)
        if data.Invincible2 == True: pass
        elif data.Invincible2 == False:hitAI2(data, 31)
        for coconut in data.coconutsAI1:
            if data.pause1Drop == False:coconut.onTimerFired(data)
        for coconut in data.coconutsAI2:
            if data.pause2Drop == False:coconut.onTimerFired(data)
        # second check
        if data.Invincible1 == False:hitAI1(data,13)
        if data.Invincible2 == True:pass
        elif data.Invincible2 == False:hitAI2(data,13)
        data.player1Y-=data.speedAI
        #establishing winer
        if data.player1Y < 15 and data.player2Y >15: data.winner= "player1"
        if data.player1Y>40:
            data.time +=1
            coconutShotAI(data)
        data.player2Y-=data.speedAI
        if data.player2Y < 15 and data.player1Y> 15: data.winner= "player2" 
        if data.player2Y>40:
            data.time +=1
            coconutShotAI(data)
        if data.player1Y < 15 and data.player2Y <15: data.winner = "tie"
        for powerUp in data.powerUps: powerUp.onTimerFired(data)
        hitPause(data)
        powerUpAITimerFired(data)

def powerUpAITimerFired(data):
    #moves both sides symmetrically 
    for powerUp in data.invincible:
        powerUp.onTimerFired(data)
    hitInvincible(data)
    for bug in data.scaryBug:
        bug.onTimerFired(data)
    hitScaryBug(data)
    if data.start1 != None:
        if abs(data.start1-data.player1Y) >= 120:
            data.pause1Drop = False
            data.Invincible1 = False
    if data.start2 != None:
        if abs(data.start2-data.player2Y) >= 120:
            data.pause2Drop = False
            data.Invincible2 = False
            


def AIRedrawAll(canvas, data):
    canvas.create_image(data.width/4, data.height/2, image=data.halfBackground)
    canvas.create_image(3*data.width/4, data.height/2,image=data.halfBackground)
    canvas.create_line(data.width/2, 0, data.width/2, data.height, width = 10)
    canvas.create_line(0,20, data.width, 20)
    for coconut in data.coconutsAI1:
        coconut.draw(canvas)
    for coconut in data.coconutsAI2:
        coconut.draw(canvas)
    canvas.create_text(50,40, text = "Computer",font = "Arial 15 bold",
                       fill = "yellow")
    canvas.create_text(450,40, text = "Player 1",font = "Arial 15 bold",
                       fill = "yellow")
    drawPowerups(canvas, data)
    canvas.create_image(data.player1X, data.player1Y, image=data.ladyBug)
    canvas.create_image(data.player2X, data.player2Y, image=data.ladyBug)
    AIWinner(canvas, data)
    drawHome(canvas, data)

def AIWinner(canvas, data):
    if data.winner== "player1":
        canvas.create_rectangle(0,0, data.width, data.height, fill = "black")
        canvas.create_image(data.width/2, data.height/2, image=data.winScreen)
        canvas.create_image(300, 320, image=data.winBug)
        canvas.create_text(data.width/2,100, text = "The Computer Won :(",
                           font = "Arial 23 bold", fill = "yellow")
    elif data.winner== "player2":
        canvas.create_rectangle(0,0, data.width, data.height, fill = "black")
        canvas.create_image(data.width/2, data.height/2, image=data.winScreen)
        canvas.create_image(300, 320, image=data.winBug)
        canvas.create_text(data.width/2,100, text = "You Made it! You Won!",
                           font = "Arial 23 bold", fill = "yellow")
    elif data.winner== "tie":
        canvas.create_rectangle(0,0, data.width, data.height, fill = "black")
        canvas.create_image(data.width/2, data.height/2, image=data.winScreen)
        canvas.create_image(300, 320, image=data.winBug)
        canvas.create_text(data.width/2,100, text = "Tie! You Both Made it!",
                           font = "Arial 23 bold", fill = "yellow")
####################################
# ScoreBoard mode
####################################

def scoreboardKeyPressed(event, data):
    if event.keysym == "r": init(data)

def scoreboardMousePressed(event, data): checkHome(event, data)

def scoreboardTimerFired(data):
    difficultyTimerFired(data)

def scoreboardRedrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image=data.background)
    canvas.create_image(data.width/2, data.tbgY, image=data.tbg)
    for drop in data.editorDrops:
        drop.draw(canvas)
    canvas.create_text(data.width/2, data.txtTScore, text="Top Scores!",
                       font = "Arial 30 bold", fill = "yellow")
    canvas.create_text(data.width/2, data.S_P, text="Score_Player",
                       font = "Arial 20 bold", fill = "yellow")
    drawHome(canvas, data)
    #reads file
    data.savedScores
    data.savedScores=readFile("score.txt")
    score=data.savedScores.splitlines()
    scores=[]
    for line in score:
        scores.append(line.split(","))
    #sorts scores to find top 5
    scores = sorted(scores, key = lambda x: int(x[0]))
    top5 = scores[-data.numScores:]
    top5.reverse()
    for i in range(len(top5)):
        canvas.create_text(data.width/2, data.scoreShift+(i*50),
                           text = top5[i],
                           font = "Arial 18 bold", fill = "yellow")

####################################
# help mode
####################################

def helpKeyPressed(event, data):
    if event.keysym == "r": init(data)

def helpMousePressed(event, data): checkHome(event, data)

def helpTimerFired(data):
    difficultyTimerFired(data)

def helpRedrawAll(canvas, data):
    canvas.create_image(data.width/2, data.helpY, image=data.helpScreen)
    for drop in data.editorDrops:
        drop.draw(canvas)
    drawHome(canvas, data)

#######################################
# use the run function as-is from notes
#######################################

def run(width=15000, height=25000):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    # create the root and the canvas
    root = Tk()
    init(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1000, 1000)
