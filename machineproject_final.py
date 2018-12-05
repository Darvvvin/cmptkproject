import pygame
import re
from random import randint

#initialization
pygame.init()
win = pygame.display.set_mode((960, 720))
pygame.display.set_caption("Collect! Multiply! Divide!")
clock = pygame.time.Clock()
COLOR_INACTIVE = pygame.Color("black")
COLOR_ACTIVE = pygame.Color("yellow")
FONT = pygame.font.Font("ARCADEPI.ttf", 72)
FONT2 = pygame.font.Font("ARCADEPI.ttf", 92)

#counters
coun = 6000
mill = 0
sec = 0
minu = 0
startcount = 0
correct = 0
loss = 0
totalcoun = 0
totalmin = 0
totalsec = 0
printonce = 0

#conversion
totalcoun = coun
mill = coun
while mill > 99:
    mill = mill - 100
sec = int (coun/100)
while sec > 59:
    sec = sec - 60
minu = int (coun / 6000)
#chocolate array setup
TILESIZE = 80

#art stuff
bg = pygame.image.load('sprites/bgnew3.jpg')
bg1 = pygame.image.load('sprites/bg3.jpg')
play = pygame.image.load('sprites/playspr2.png')
play_new = pygame.image.load('sprites/playspr2_new.png')

array = pygame.image.load('sprites/koya.png')
array = pygame.transform.scale(array, (350,350))

piece = pygame.image.load('sprites/piece.png')
piece = pygame.transform.scale(piece, (80,80))

mouse = pygame.mouse.get_pos()

pygame.display.set_icon(array)

#button
box_surface = pygame.Surface.get_rect(play)
click = pygame.draw.rect(bg, (255,255,255),(352,530,242,126), 0)

#/art stuff

#global
#/global

#functions----------------------------------------------
def loadNext():
    gameplay()

#timer
def timecount():
    global coun
    global mill
    global sec
    global minu
    global startcount
    global totalmin
    global totalsec
    global printonce
    if coun < 1:
        if printonce < 1 :
        
            totalsec = int (totalcoun/100)
            while totalsec > 59:
                totalsec = totalsec - 60
            totalmin = int (totalcoun / 6000)
            printonce += 1
            print("You got ", correct, "answers in", totalmin, "minutes, and ",totalsec, "seconds")

    if coun > 0 :
        #DECREMENT BY 3
        coun -= 3
        mill = coun
        while mill > 99:
            mill = mill - 100
            sec = int (coun/100)
        while sec > 59:
            sec = sec - 60
            minu = int (coun / 6000)
        if coun < 6000:
            minu = 0
        if coun < 100:
            sec = 0
        if coun < 0:
            mill = 0
        

#gives 8 seconds per correct answer
def rewardtime():
    global coun
    global totalcoun
    global correct
    
    coun += 100
    #also adds to total count and correct answer
    totalcoun += 800
    correct += 1
    #convertion for the minutes and seconds of total time
    totalsec = int (totalcoun/100)
    while totalsec > 59:
        totalsec = totalsec - 60
    totalmin = int (totalcoun / 6000)
    
def redrawGameWindow():
    win.blit(bg,(0,0))
    pygame.display.update()

def fade(width, height):
    fade = pygame.Surface((width,height))
    fade.fill((0,0,0))
    for alpha in range(0,300,2):
        fade.set_alpha(alpha)
        win.blit(bg,(0,0))
        win.blit(play, (352,530))
        win.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(0)

def gameplay():
    global random_num
    global random_num2
    global answ
    global correct

#    if correct > 12:
#        random_num = randint(10,20)
#        random_num2 = randint(10,20)
#    elif correct > 9:
#        random_num = randint(8,17)
#        random_num2 = randint(8,17)
#   elif correct > 6:
#        random_num = randint(6,14)
#        random_num2 = randint(6,14)
#    elif correct > 3:
#        random_num = randint(4,11)
#        random_num2 = randint(4,11)
#    else:
#        random_num = randint(1,8)
#        random_num2 = randint(1,4)
#
    random_num = randint(1,8)
    random_num2 = randint(1,4)

    answ = random_num*random_num2
    
    GRIDWIDTH = random_num/TILESIZE
    GRIDHEIGHT = random_num2/TILESIZE
    
    draw_grid()

    print(random_num)
    print(random_num2)
    print("The answer is",answ)
     
def level_11():  
    print("Level 1 has Started")
 
    gameExit = False
    gameOver = False
    
    gameplay()
    
    if __name__ == '__main__':
        main()
        pygame.quit()
        
    gameplay()
    
    while not gameExit:
        while coun > 0 :

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    gameExit = True

def redrawArray():
    for x in range(160,160+80*random_num,TILESIZE):
        for y in range(80,80+80*random_num2,TILESIZE):
            win.blit(piece,(x,y))

def draw_grid():
    for x in range(160,880,TILESIZE):
        pygame.draw.line(bg1, (255,255,255), (x,80),(x,400))

    for y in range(80,480,TILESIZE):
        pygame.draw.line(bg1, (255,255,255), (160,y),(800,y))
    
#/functions--------------------------------------------
#inputBox----------------------------------------------
#***********************************************
# Title: Input Box in Pygame
# Author: skrx
# Date: September 24, 2017
# Code version: 3
# Availability: StackOverflow https://stackoverflow.com/questions/46390231/how-to-create-a-text-input-box-with-pygame 
#***********************************************
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        global correct
        global loss
        global accuracy
        global startcount
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                #timer counts when you press the box
                if startcount == 0:
                    startcount += 1
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
#----------------------------GAMEPLAY PROGRESSION-----------------------------#
                    if self.text == str(answ):
                        print("That is correct! Next question.")
                        print("-------------------")
                        correct += 1
                        print(correct,"correct")
                        print(loss,"wrong")
                        print("Accuracy:",1 if correct == 0 else round((1-(loss/correct))*100),"%",)
                        print("-------------------")
                        loadNext()
                        rewardtime()
                    else:
                        print("That is incorrect.")
                        loss += 1
#----------------------------GAMEPLAY PROGRESSION-----------------------------#
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if re.match('^[0-9]*$',str(self.text)) and len(str(self.text)) < 3:
                        self.text += event.unicode
#-----------------------------------------------------------------------------#
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, (255,255,255))
                pygame.display.flip()

    def update(self):
        width = max(217, self.txt_surface.get_width())

    def draw(self, win):
        #position text properly
        win.blit(self.txt_surface, (self.rect.x+80 if len(str(self.text)) == 1 else self.rect.x+55 if len(str(self.text)) == 2 else self.rect.x+28, self.rect.y+65))
        # Blit the rect.
        pygame.draw.rect(win, self.color, self.rect, 5)



def main():
    pygame.init()
    clock = pygame.time.Clock()
    input_box = InputBox(705, 440, 215, 200)
    input_boxes = [input_box]
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)
                
        for box in input_boxes:
            box.update()

            if startcount == 1:
            
                timecount()
                
        win.blit(bg1, (0,0))            
        redrawArray()
#--------NUMBERS---------------------------------------------------        
        num = FONT2.render(str(random_num), True, (255,255,255))
        win.blit(num,(116 if len(str(random_num)) < 2 else 80,500))
#---------------!!!!NOTABLE!!!!PUT IN DOCUMENTATION!!!!!-----------
        condition = True
        num2 = FONT2.render(str(random_num2), True, (255,255,255))
        win.blit(num2,(449 if len(str(random_num2)) < 2 else 413,500))
#------------------TIMER DISPLAY-----------------------------------
        if coun > 5999:
            MINUT = FONT2.render(str(minu), True, (255,255,255))
            win.blit(MINUT,(600,30))
        if coun > 5999 :
            seco = FONT2.render(str(sec), True, (255,255,255))
            win.blit(seco,(790,30))
        if coun < 6000:
            seco = FONT2.render(str(sec), True, (255,255,255))
            win.blit(seco,(600,30))
            
        if coun > 3000 and coun < 5999 :
            seco = FONT2.render(str(sec), True, (255,255,255))
            win.blit(seco,(600,30))
        elif coun < 3000:
            seco = FONT2.render(str(sec), True, (255,0,0))
            win.blit(seco,(600,30))
        if coun < 6000 and coun > 3000:
            milli = FONT2.render(str(mill), True, (255,255,255))
            win.blit(milli,(790,30))
        if coun < 3000:
            milli = FONT2.render(str(mill), True, (255,0,0))
            win.blit(milli,(790,30))
                 
#--------NUMBERS---------------------------------------------------         
        for box in input_boxes:
            box.draw(win)

        pygame.display.update()
        clock.tick(30)
        
    pygame.display.update()
        
#/inputBox---------------------------------------------------------    
#game
redrawGameWindow()
run = True
level_1 = False
while run:
#Quit -------------------------------------------------------------
    pygame.time.delay(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#Play -------------------------------------------------------------
    if level_1 == False:
        if click.collidepoint(pygame.mouse.get_pos()):
            win.blit(play_new,[352,530])
            pygame.display.update()
                   
            if pygame.mouse.get_pressed()[0]:
                print("Starting Level 1...")
                fade(960,720)
                level_1 = True               

        else: win.blit(play, (352,530))

    if level_1:
        level_11()        
        
    clock.tick(30)
    pygame.display.update()
#exit ---------------------------------------------------
pygame.quit()
