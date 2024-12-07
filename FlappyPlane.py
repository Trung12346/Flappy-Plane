import pygame
import sys
import random
import threading
import time
import webbrowser

pygame.init()
root = pygame.display.set_mode((600, 680))
pygame.display.set_caption("Flappy Plane")
pygame.display.set_icon(pygame.image.load("Pics/plane icon.png"))

sky_background_x_1 = 0
sky_background_x_2 = 440
sky_background_x_3 = 880
house_1_background_x_1 = 0
house_1_background_x_2 = 440
house_1_background_x_3 = 880
house_2_background_x_1 = 0
house_2_background_x_2 = 440
house_2_background_x_3 = 880
sky_sub = 0.5
house_1_sub = 1.5
house_2_sub = 2.5
gravity = 0.5
plane_object_movement = 0
game = False
score = 0
temp_score = 0
temp = -1
temp_2 = True
scan = 0
sub_scan = 0
best_score = "0"
text_1 = pygame.font.Font("Fonts/04B_19.ttf", 20)
text_2 = pygame.font.Font("Fonts/04B_19.ttf", 40)
text_3 = pygame.font.Font("Fonts/04B_19.ttf", 120)

HEX = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "10", "11", "12", "13",
"14", "15", "16", "17", "18", "19", "1A", "1B", "1C", "1D", "1E", "1F", "20", "21", "22", "23", "24", "25", "26", "27",
"28", "29", "2A", "2B", "2C", "2D", "2E", "2F", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "3A", "3B",
"3C", "3D", "3E", "3F", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "4A", "4B", "4C", "4D", "4E", "4F",
"50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "5A", "5B", "5C", "5D", "5E", "5F", "60", "61", "62", "63", 
"64", "65", "66", "67", "68", "69", "6A", "6B", "6C", "6D", "6E", "6F", "70", "71", "72", "73", "74", "75", "76", "77", 
"78", "79", "7A", "7B", "7C", "7D", "7E", "7F", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "8A", "8B", 
"8C", "8D", "8E", "8F", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "9A", "9B", "9C", "9D", "9E", "9F",
"A0", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "AA", "AB", "AC", "AD", "AE", "AF", "B0", "B1", "B2", "B3",
"B4", "B5", "B6", "B7", "B8", "B9", "BA", "BB", "BC", "BD", "BE", "BF", "C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7", 
"C8"]

DEC = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
"20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39",
"40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", 
"60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79",
"80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99",
"100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119",
"120", "121", "122", "123", "124", "125", "126", "127", "128", "129", "130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
"140", "141", "142", "143", "144", "145", "146", "147", "148", "149", "150", "151", "152", "153", "154", "155", "156", "157", "158", "159", 
"160", "161", "162", "163", "164", "165", "166", "167", "168", "169", "170", "171", "172", "173", "174", "175", "176", "177", "178", "179", 
"180", "181", "182", "183", "184", "185", "186", "187", "188", "189", "190", "191", "192", "193", "194", "195", "196", "197", "198", "199", 
"200"]

def imageLoad(path):
    return pygame.image.load(path)

sky_background = imageLoad("Pics/background.png").convert()
house_1_background = imageLoad("Pics/line2.png").convert_alpha()
house_2_background = imageLoad("Pics/line1.png").convert_alpha()
plane_object = imageLoad("Pics/plane.png").convert_alpha()
tower_object = imageLoad("Pics/tower.png").convert_alpha()
top_tower_object = imageLoad("Pics/tower_flip.png").convert_alpha()
play_object = imageLoad("Pics/play.png").convert_alpha()
play_image = imageLoad("Pics/play.png").convert_alpha()
facebook_icon = imageLoad("Pics/iconfb.png").convert_alpha()

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self):
        global game
        root.blit(self.image, (self.rect.x, self.rect.y))

        pos = pygame.mouse.get_pos()   

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                game = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

class ButtonFacebook():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self):
        global game
        root.blit(self.image, (self.rect.x, self.rect.y))

        pos = pygame.mouse.get_pos()   

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                webbrowser.open_new_tab("https://www.facebook.com/smlgamingVN/")

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

play_button = Button(300, 500, play_image)
facebook_contact_button = ButtonFacebook(550, 590, facebook_icon)

plane_object_rect = plane_object.get_rect(center = (120, 340))

def gravityIncs():
    gravity = 0
    while gravity <= 0.5:
        time.sleep(0.3)
        gravity += 0.05

def saveBest(current_score):
    with open("Player Data/score.txt", "r") as f_r:
        best_score = f_r.read()

    best_score = best_score.replace("265V699dsfFCh077g'", "").replace("'256577GHcjF7777B7721436'gghAWr7'36'65ggh2T5'4656sd46zg66fgfhFwa66'2zsdgwys2'34sZf4'10010001'53fdsA4ffdzA6", "")
    global scan
    global sub_scan  
    
    scan = 0
    sub_scan = 0
    while scan < 200:
        if best_score == HEX[scan]:
            best_score_dec = DEC[scan]
            if current_score > int(best_score_dec):
                best_score_dec = current_score           
                while sub_scan < 200:
                    if best_score_dec == int(DEC[sub_scan]):
                        best_score_hex = HEX[sub_scan]
                        best_score_hex = "265V699dsfFCh077g'" + best_score_hex + "'256577GHcjF7777B7721436'gghAWr7'36'65ggh2T5'4656sd46zg66fgfhFwa66'2zsdgwys2'34sZf4'10010001'53fdsA4ffdzA6"
                        with open("Player Data/score.txt", "w") as f_w:
                            f_w.write(best_score_hex)
                    sub_scan += 1
        scan += 1
        
def getBestScore():
    x = 0
    with open("Player Data/score.txt", "r") as f_r:
        best_score = f_r.read()
    best_score = best_score.replace("265V699dsfFCh077g'", "").replace("'256577GHcjF7777B7721436'gghAWr7'36'65ggh2T5'4656sd46zg66fgfhFwa66'2zsdgwys2'34sZf4'10010001'53fdsA4ffdzA6", "")

    for x in range(0, 201, 1):
        if best_score == HEX[x]:
            best_score_current = DEC[x]
            return best_score_current

def createTower_lower(height):
    new_tower_lower = tower_object.get_rect(topleft = (600, height))
    return new_tower_lower

def createTower_upper(height):
    new_tower_upper = top_tower_object.get_rect(bottomleft = (600, height))
    return new_tower_upper

def moveTower(towers):
    for tower in towers:
        tower.centerx -= 10
    return towers

def drawTower(object, towers):
    for tower in towers:
        root.blit(object, tower)

def collision(towers):
    for tower in towers:
        if plane_object_rect.colliderect(tower):
            global game
            game = False
    if plane_object_rect.top <= 0 or plane_object_rect.bottom >= 680:
        game = False

def rotateObj(surface):
    modified_plane = pygame.transform.rotozoom(surface, -plane_object_movement/1.5, 1)
    return modified_plane

def pointCounter(towers):
    global score
    try:
        if towers[temp].right == 10:       
            score += 1
    except:
        pass

def pointUpd():
    global score_display_rect
    global score_display
    score_display = text_2.render(str(score), True, (0, 0, 0))
    score_display_rect = score_display.get_rect(center = (300, 200))

tower_object_list_lower = []
tower_object_list_upper = []

SPAWNTOWER = pygame.USEREVENT
pygame.time.set_timer(SPAWNTOWER, 3000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SPAWNTOWER:
            if game:
                tower_object_list_lower.append(createTower_lower(lower_tower_height))
                tower_object_list_upper.append(createTower_upper(upper_tower_height))
                temp += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                plane_object_movement = 0
                plane_object_movement -= 12

    score_display_highest = text_1.render("Best Score: " + str(getBestScore()), True, (0, 0, 0))
    
    if sky_background_x_1 <= -440:
        sky_background_x_1 = 0
        sky_background_x_2 = 440
        sky_background_x_3 = 880
    if house_1_background_x_1 <= -440:
        house_1_background_x_1 = 0
        house_1_background_x_2 = 440
        house_1_background_x_3 = 880
    if house_2_background_x_1 <= -440:
        house_2_background_x_1 = 0
        house_2_background_x_2 = 440
        house_2_background_x_3 = 880

    house_1_background_rect_1 = house_1_background.get_rect(bottomleft = (house_1_background_x_1, 680))
    house_1_background_rect_2 = house_1_background.get_rect(bottomleft = (house_1_background_x_2, 680))
    house_1_background_rect_3 = house_1_background.get_rect(bottomleft = (house_1_background_x_3, 680))
    house_2_background_rect_1 = house_2_background.get_rect(bottomleft = (house_2_background_x_1, 680))
    house_2_background_rect_2 = house_2_background.get_rect(bottomleft = (house_2_background_x_2, 680))
    house_2_background_rect_3 = house_2_background.get_rect(bottomleft = (house_2_background_x_3, 680))
    score_display_highest_rect = score_display_highest.get_rect(center = (480, 20))       

    root.blit(sky_background, (sky_background_x_1, 0))
    root.blit(sky_background, (sky_background_x_2, 0))
    root.blit(sky_background, (sky_background_x_3, 0))
    root.blit(house_1_background, house_1_background_rect_1)
    root.blit(house_1_background, house_1_background_rect_2)
    root.blit(house_1_background, house_1_background_rect_3)
    root.blit(house_2_background, house_2_background_rect_1)
    root.blit(house_2_background, house_2_background_rect_2)
    root.blit(house_2_background, house_2_background_rect_3)
    root.blit(score_display_highest, score_display_highest_rect)

    sky_background_x_1 -= sky_sub
    sky_background_x_2 -= sky_sub
    sky_background_x_3 -= sky_sub
    house_1_background_x_1 -= house_1_sub
    house_1_background_x_2 -= house_1_sub
    house_1_background_x_3 -= house_1_sub
    house_2_background_x_1 -= house_2_sub
    house_2_background_x_2 -= house_2_sub
    house_2_background_x_3 -= house_2_sub
    
    if game == False:
        plane_object_movement = 0
        if temp_2:
            temp_score = score
        temp_2 = False

        plane_object_rect.center = (120, 340)
        tower_object_list_lower.clear()
        tower_object_list_upper.clear()

        temp = -1
        score = 0

        score_display_best = text_3.render(str(temp_score), True, (0, 0, 0))
        score_display_best_rect = score_display_best.get_rect(center = (300, 300))
        root.blit(score_display_best, score_display_best_rect)

        play_button.draw()
        facebook_contact_button.draw()

        save = threading.Thread(target = saveBest, args = (temp_score,)).start()


    if game:
        increase = threading.Thread(target = gravityIncs).start()
        temp_2 = True
        temp_score = 0

        tower_height_float = random.randint(250, 400)
        lower_tower_height = tower_height_float + 125
        upper_tower_height = tower_height_float - 125

        tower_object_list_lower = moveTower(tower_object_list_lower)
        tower_object_list_upper = moveTower(tower_object_list_upper)

        plane_object_movement += gravity
        plane_object_rect.centery += plane_object_movement
        plane_object_rotated = rotateObj(plane_object)

        drawTower(tower_object, tower_object_list_lower)
        drawTower(top_tower_object, tower_object_list_upper)
        root.blit(plane_object_rotated, plane_object_rect)
        collision(tower_object_list_lower)
        collision(tower_object_list_upper)
        pointCounter(tower_object_list_lower)
        pointUpd()
        root.blit(score_display, score_display_rect)

    pygame.display.update()
    pygame.time.Clock().tick(60)