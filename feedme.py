import pygame
import logging
from time import sleep
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s",filename="feedme.log",filemode="a+",level=logging.INFO)
logging.info("Initializing pygame.")
pygame.init()
pygame.font.init()
VERSION = "0.1.1-alpha"
logging.info("Initializing game screen")
screen = pygame.display.set_mode((1280,720))
WIDTH, HEIGHT = pygame.display.get_surface().get_size()
pygame.display.set_caption("Feed The Kelsey")
icon = pygame.image.load("feed.ico")
pygame.display.set_icon(icon)
font = pygame.font.SysFont("Consolas",48)
sfont = pygame.font.SysFont("Consolas",24)
tfont = pygame.font.SysFont("Consolas",12)
text_surface = font.render("==Enderbyte Programs==",1,(255,255,255))
instat = sfont.render("Feed the Kelsey",1,(255,255,255))
screen.blit(instat,(400,400))
screen.blit(text_surface,(400,300))
pygame.display.flip()
sleep(1)
instat = sfont.render("Preparing Libraries",1,(255,255,255))
screen.blit(instat,(400,400))
screen.blit(text_surface,(400,300))
pygame.display.flip()
logging.info("Initializing libraries")
from tkinter import Tk
from tkinter import messagebox
from tkinter import filedialog
import os
import sys
import json
from send2trash import send2trash
screen.fill(pygame.Color("black"))

instat = sfont.render("Loading assets",1,(255,255,255))
screen.blit(instat,(400,400))
screen.blit(text_surface,(400,300))
pygame.display.flip()


PATH = os.getcwd()
ASSETS = PATH+"/assets"
TEXTURES = ASSETS+"/textures"
SOUNDS = ASSETS + "/sounds"
SAVES = PATH + "/saves"
APPDATA = PATH + "/config"
CONFIGP = APPDATA + "/config.json"
ANGRY = False
INGAME = False
assets = [PATH+"/feed.ico",TEXTURES+"/title.jpg",TEXTURES+"/sleepy.jpg",TEXTURES+"/appeased.jpg",SOUNDS+"/menu.ogg",SOUNDS+"/config.ogg",SOUNDS+"/normal.ogg"]
if not os.path.isfile("feedme.exe") and not os.path.isfile("feedme.py"):
    Tk().withdraw()
    messagebox.showerror("Error","Game is not running in correct directory")
    sys.exit(1)
class Button():
        def __init__(self, color, x,y,width,height, text=''):
            self.color = color
            self.ogcol = color
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.text = text
            self.juston = False
            self.on = False

        def draw(self,win,outline=None):
            #Call this method to draw the button on the screen
            if outline:
                pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
                
            pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
            
            if self.text != '':
                font = pygame.font.SysFont('Consolas', 24)
                text = font.render(self.text, 1, (0,0,0))
                win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

        def isOver(self, pos):
            
            #Pos is the mouse position or a tuple of (x,y) coordinates
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
                    self.color = (128,128,128)
                    self.on = True
                    
                else:
                    self.color = self.ogcol
                    self.on = False
                    
            else:
                self.color = self.ogcol
                self.on = False
                
            if not self.on and self.juston:
                pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
            self.juston = self.on
            
            for event in ev:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pos[0] > self.x and pos[0] < self.x + self.width:
                        if pos[1] > self.y and pos[1] < self.y + self.height:
                            return True

logging.info("Initializing assets")
for item in assets:
    if not os.path.isfile(item):
        logging.error(f"ASSET {item} NOT FOUND")
        screen.fill(pygame.Color("black"))
        pitem = item.replace(PATH,"")
        instat = sfont.render(f"Error: Asset {pitem} could not be found.",1,(255,0,0))
        screen.blit(instat,(0,400))
        screen.blit(text_surface,(400,300))
        pygame.display.flip()
        Tk().withdraw()
        messagebox.showerror("Error","Failed to load: missing asset")
        sys.exit(1)
bg = pygame.image.load(TEXTURES + "/title.jpg")
tex_sleepy = pygame.image.load(TEXTURES + "/sleepy.jpg")
text_appeased = pygame.image.load(TEXTURES + "/appeased.jpg")
dapd = {
    "mute" : False
}

if os.path.isfile(CONFIGP):
    with open(CONFIGP) as f:
        APPDATA = json.load(f)
else:

    logging.warning("Could not find appdata file")
    with open(CONFIGP,"w+") as f:
        f.write(json.dumps(dapd))

def updateappdata():
    with open(CONFIGP,"w+") as f:
        f.write(json.dumps(APPDATA))
fullscreen = False
if APPDATA["fullscreen"]:
    screen = pygame.display.set_mode((1280,720),pygame.FULLSCREEN)
    fullscreen = True

logging.info("Initializing sound")
screen.fill(pygame.Color("black"))
instat = sfont.render("Loading sound",1,(255,255,255))
screen.blit(instat,(400,400))
screen.blit(text_surface,(400,300))
pygame.display.flip()
pygame.mixer.init()
pygame.mixer.music.load(SOUNDS+"/menu.ogg")
pygame.mixer.music.play(loops=-1)
if APPDATA["mute"]:
    pygame.mixer.music.pause()
running = True
clock = pygame.time.Clock()
screen.fill(pygame.Color("black"))



exitbutton = Button((255,0,0),WIDTH/2-100,HEIGHT-100,100,50,"Exit")
configbutton = Button((0,128,255),WIDTH/2-100,HEIGHT-200,100,50,"Config")
cfg_mute = Button((128,255,128),WIDTH/4,100,100,50,"Mute")
cfg_unmute = Button((255,128,0),WIDTH/2+WIDTH/4,100,100,50,"Unmute")
cfg_tf = Button((255,255,255),WIDTH/4,200,300,50,"Toggle Fullscreen")
startgame_button = Button((64,255,64),WIDTH/2-125,HEIGHT/2-50,150,50,"Start Game")
cfg_back = Button((255,255,255),100,HEIGHT-100,100,50,"Back")
cf_button = Button((128,255,128),WIDTH-150,0,150,50,"Get money")

MENU = True
CONFIG = False
STATE = "appeased"
MONEY = 0

angerlevels = ["sleepy","hyperactive","happy","appeased","displeased","annoyed","angry","furious"]
pygame.display.flip()
while running:
    screen.fill((255,255,255))
    mval = sfont.render(f"You have {MONEY} money",1,(0,0,0))
    if STATE == "appeased":
        kelstext = font.render(f"The Kelsey is {STATE}",1,(0,0,0))
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            logging.info("Quitting...")
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and CONFIG:
                logging.info("Returning to menu from config")
                MENU = True
                CONFIG = False
                screen.blit(bg,(0,0))
                if not APPDATA["mute"]:
                    pygame.mixer.music.load(SOUNDS+"/menu.ogg")
                    pygame.mixer.music.play(loops=-1)
            keysdown = pygame.key.get_pressed()
            if keysdown[pygame.K_m] and keysdown[pygame.K_LCTRL] and INGAME:
                logging.info("returning to menu from game")
                MENU = True
                INGAME = False
                screen.blit(bg,(0,0))
                if not APPDATA["mute"]:
                    pygame.mixer.music.load(SOUNDS+"/menu.ogg")
                    pygame.mixer.music.play(loops=-1)
    
    
    if MENU:
        
        screen.blit(bg,(0,0))
        exitbutton.draw(screen)
        if exitbutton.isOver(pygame.mouse.get_pos()) == True:
            running = False
            
        configbutton.draw(screen)
        if configbutton.isOver(pygame.mouse.get_pos()):
            logging.info("Starting CFG")
            MENU = False
            CONFIG = True
            if not APPDATA["mute"]:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(SOUNDS+"/config.ogg")
                pygame.mixer.music.play(loops=-1)
        startgame_button.draw(screen)
        if startgame_button.isOver(pygame.mouse.get_pos()):
            INGAME = True
            MENU = False
            screen.fill((255,255,255))
            if not APPDATA["mute"]:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(SOUNDS+"/normal.ogg")
                pygame.mixer.music.play(loops=-1)
        titletext = font.render("Feed the Kelsey",1,(255,255,255))
        tt_rect = titletext.get_rect(center=(WIDTH/2,50))
        screen.blit(titletext,tt_rect)

        cr_text = tfont.render("(c) 2022 Enderbyte Programs",1,(255,255,255))
        screen.blit(cr_text,(0,HEIGHT-20))
        vr_text = tfont.render(f"v{VERSION}",1,(255,255,255))
        screen.blit(vr_text,(WIDTH-100,HEIGHT-20))

    if CONFIG:
        screen.fill((64,64,64))
        ctitletext = font.render("Configuration",1,(255,255,255))
        ctt_rect = ctitletext.get_rect(center=(WIDTH/2,50))
        cesctext = sfont.render("Press escape to return to the title screen. All changes are saved",1,(255,255,255))
        cst_rect = cesctext.get_rect(center=(WIDTH/2,HEIGHT-50))
        screen.blit(ctitletext,ctt_rect)
        screen.blit(cesctext,cst_rect)
        cfg_mute.draw(screen)
        if cfg_mute.isOver(pygame.mouse.get_pos()):
            APPDATA["mute"] = True
            pygame.mixer.music.fadeout(1000)
            updateappdata()
        cfg_unmute.draw(screen)
        if cfg_unmute.isOver(pygame.mouse.get_pos()):
            APPDATA["mute"] = False
            pygame.mixer.music.play(loops=-1)
            updateappdata()
        cfg_tf.draw(screen)
        if cfg_tf.isOver(pygame.mouse.get_pos()) and not fullscreen:
            APPDATA["fullscreen"] = True
            fullscreen = True
            screen = pygame.display.set_mode((1280,720),pygame.FULLSCREEN)
            updateappdata()
            sleep(0.5) #Debounce button
        elif cfg_tf.isOver(pygame.mouse.get_pos()) and APPDATA["fullscreen"]:
            APPDATA["fullscreen"] = False
            fullscreen = False
            screen = pygame.display.set_mode((1280,720))
            updateappdata()
            sleep(0.5)
        cfg_back.draw(screen)
        if cfg_back.isOver(pygame.mouse.get_pos()):
            MENU = True
            CONFIG = False
            screen.blit(bg,(0,0))
            if not APPDATA["mute"]:
                pygame.mixer.music.load(SOUNDS+"/menu.ogg")
                pygame.mixer.music.play(loops=-1)
    if INGAME:
        
        if STATE == "appeased":
            screen.blit(text_appeased,(0,0))
        screen.blit(kelstext,(310,10))
        screen.blit(mval,(0,HEIGHT-50))
        cf_button.draw(screen)
        if cf_button.isOver(pygame.mouse.get_pos()):
            pkrt = Tk()
            pkrt.withdraw()
            pkrt.wm_attributes("-topmost",True)
            m = filedialog.askopenfilename(title="Choose which file to shred",filetypes=[("file","*.*")])
            del pkrt
            if m != "":
                
                try:
                    with open(m,"rb") as f:
                        a = f.read()
                        
                        MONEY += len(a)
                except Exception as e:
                    logging.error(f"Failed to open file error {e}")
                else:
                    send2trash(str(m.replace("/","\\")))
            

    pygame.display.update()

pygame.mixer.quit()
pygame.quit()
logging.info("Quit")
