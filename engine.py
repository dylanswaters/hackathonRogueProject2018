import tcod
import csv
import sys
from theMap import *
from Item import *
from Monster import *
from Event import *

color_dark_wall = tcod.Color(0, 0, 100)
color_dark_ground = tcod.Color(50, 50, 150)

GAME_HEIGHT = 50
GAME_WIDTH = 50

itemList = []
# csv item reader
with open('items.csv','r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        itemList.append(row)
# print(itemList)

playerList = []
# csv item reader
with open('players.csv','r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        playerList.append(row)
# print(playerList)

def render_all(mapToUse, con):
    global color_light_wall
    global color_light_ground

    for y in range(GAME_HEIGHT):
        for x in range(GAME_WIDTH):
            tcod.console_put_char(con, x, y, " ", tcod.BKGND_NONE)

    for y in range(GAME_HEIGHT):
        for x in range(GAME_WIDTH):
            if(mapToUse.map[x][y].charToken != ""):
                tcod.console_put_char(con, x, y, mapToUse.map[x][y].charToken, tcod.BKGND_NONE)
                # else:
                #      tcod.console_put_char(con, x, y, "#", tcod.BKGND_NONE)
    for roomIndex in mapToUse.roomList:
        # print("room " + roomIndex.roomName + " player list:")
        # print(roomIndex.playerList)
        # print()
        placeX = roomIndex.x1
        placeY = roomIndex.y1
        for i in range(0, len(roomIndex.playerList)):
            # print(roomIndex.playerList[i].name[0])
            # print(placeX+1, placeY+1)
            tcod.console_put_char(con, placeX+1, placeY+1, roomIndex.playerList[i].name[0], tcod.BKGND_NONE)
            if(placeX < roomIndex.x2-2):
                placeX += 1
            else:
                placeX = roomIndex.x1
                if(placeY < roomIndex.y2-1):
                    placeY += 1
                else:
                    placeY = roomIndex.y1

    # blit the contents of "con" to the root console
    tcod.console_blit(con, 0, 0, GAME_WIDTH, GAME_HEIGHT, 0, 0, 0)

def handle_keys(currPlayer, mapToUse):
    global fov_recompute

    #key = tcod.console_check_for_keypress()  #real-time
    key = tcod.console_wait_for_keypress(True)  #turn-based

    if key.vk == tcod.KEY_ESCAPE:
        sys.exit()

    # if key.vk == tcod.KEY_ENTER and key.lalt:
    #     #Alt+Enter: toggle fullscreen
    #     tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

    #movement keys
    if tcod.console_is_key_pressed(tcod.KEY_UP):
        mapToUse.movePlayer(currPlayer, 0)
        fov_recompute = True

    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
        mapToUse.movePlayer(currPlayer, 2)
        fov_recompute = True

    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
        mapToUse.movePlayer(currPlayer, 3)
        fov_recompute = True

    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        mapToUse.movePlayer(currPlayer, 1)
        fov_recompute = True

def main():
    # player_x = int(screen_width / 2)
    # player_y = int(screen_height / 2)

    tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)

    tcod.console_init_root(GAME_WIDTH, GAME_HEIGHT, 'tcod tutorial revised', False)
    con = tcod.console_new(GAME_WIDTH, GAME_HEIGHT)

    key = tcod.Key()
    mouse = tcod.Mouse()

    gameMap = Map(GAME_WIDTH, GAME_HEIGHT, 9)
    gameMap.make_map()
    # for i in range(0, len(gameMap.roomList)):
    #     print(gameMap.roomList[i])

    newItem = item(itemList[0])
    gameMap.insert_item(newItem, gameMap.roomList[1])
    # print(gameMap.roomList[0].itemList)

    playersToTakeTurn = []
    # for i in range(0, len(gameMap.roomList)):
    #     print(gameMap.roomList[i].playerList)
    p1 = player(playerList[0])
    gameMap.insert_player(p1, 0)
    playersToTakeTurn.append(p1)
    p2 = player(playerList[1])
    gameMap.insert_player(p2, 0)
    playersToTakeTurn.append(p2)
    p3 = player(playerList[2])
    gameMap.insert_player(p3, 0)
    playersToTakeTurn.append(p3)
    p4 = player(playerList[3])
    gameMap.insert_player(p4, 0)
    playersToTakeTurn.append(p4)
    p5 = player(playerList[4])
    gameMap.insert_player(p5, 0)
    playersToTakeTurn.append(p5)
    p6 = player(playerList[5])
    gameMap.insert_player(p6, 0)
    playersToTakeTurn.append(p6)
    p7 = player(playerList[6])
    gameMap.insert_player(p7, 0)
    playersToTakeTurn.append(p7)
    # for i in range(0, len(gameMap.roomList)):
    #     print(gameMap.roomList[i].playerList)

    while not tcod.console_is_window_closed():
        # tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)

        tcod.console_set_default_foreground(0, tcod.white)
        render_all(gameMap, con)

        tcod.console_flush()

        # key = tcod.console_check_for_keypress()

        for i in range(0, len(gameMap.roomList)):
            print("room: ", i, " has ", len(gameMap.roomList[i].playerList), " players")
            for j in range(0, len(gameMap.roomList[i].playerList)):
                print(gameMap.roomList[i].playerList[j].name)

        # print(playersToTakeTurn)
        for p in playersToTakeTurn:
            print(p.name)
            handle_keys(p, gameMap)
            # render_all(gameMap, con)


if __name__ == '__main__':
    main()
