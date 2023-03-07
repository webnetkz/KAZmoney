#######################################
#
#    Script to auto generate images
#      for piece recognition
#
#                 by
#
#          Code Monkey King
#
#######################################

# Set this FEN on the chess board in the browser:
# "k1q1r1b1/1n1p4/8/8/8/1N1P4/K1Q1R1B1/8 w - - 0 1"
# "k1q1r1b1/1n1p4/8/8/8/1N1P4/K1Q1R1B1/8 w KQkq - 0 1"
# to make sure the script would work properly

# packages
import cv2
import pyautogui as pg
from find_board import get_start_position


position_board = get_start_position()
print(position_board)



# constants (modify if needed)
BOARD_SIZE = position_board[2]-4
DARK_SQUARE_THRESHOLD = 210
CELL_SIZE = int(BOARD_SIZE / 8)
BOARD_TOP_COORD = position_board[1]+3
BOARD_LEFT_COORD = position_board[0]+2
# BOARD_SIZE = 832
# BOARD_TOP_COORD = 172
# BOARD_LEFT_COORD = 512


print(BOARD_SIZE)
print(BOARD_TOP_COORD)
print(BOARD_LEFT_COORD)


# map pieces
piece_names = {
    '0': 'black_king',
    '1': 'black_queen',
    '2': 'black_rook',
    '3': 'black_bishop',
    '4': 'black_knight',
    '5': 'black_pawn',
    '6': 'white_knight',
    '7': 'white_pawn',
    '8': 'white_king',
    '9': 'white_queen',
    '10': 'white_rook',
    '11': 'white_bishop'
}

# board top left corner coords (change if needed)
y = BOARD_TOP_COORD
x = BOARD_LEFT_COORD

# take a screenshot and store it locally
pg.screenshot('screenshot.png')

# load local screenshot
screenshot = cv2.imread('screenshot.png')

cv2.circle(screenshot, (BOARD_LEFT_COORD, BOARD_TOP_COORD), (1), (255, 0, 0), thickness=1)
cv2.circle(screenshot, (BOARD_LEFT_COORD+BOARD_SIZE, BOARD_TOP_COORD), (1), (255, 0, 0), thickness=1)

#cv2.imshow("x", screenshot)
#cv2.waitKey(0)


# convert screenshot to grayscale
screenshot_grayscale = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

# piece code
piece_code = 0

# loop over board rows
for row in range(8):
    # loop over board columns
    for col in range(8):
        # pick up certain rows
        if row in [0, 1, 5, 6]:
            # match only light squares
            if screenshot_grayscale[y][x] > DARK_SQUARE_THRESHOLD:
                print(screenshot_grayscale[y][x])
                cv2.imshow("x", screenshot_grayscale[y:y+3, x:x+3])
                #cv2.waitKey(0)
                # skip empty cells
                if row == 1 and col < 4: continue
                if row == 5 and col < 4: continue
                
                # crop piece image
                piece_image = screenshot[y:y + CELL_SIZE, x: x + CELL_SIZE]
                
                # uncomment to display extracted images
                cv2.imshow('scr', piece_image)
                #cv2.waitKey(0)
                
                # store extracted image
                cv2.imwrite('./pieces/' + piece_names[str(piece_code)] + '.png', piece_image)
                
                # increment piece code
                piece_code += 1
        
        # increment x coord by cell size
        x += CELL_SIZE
    
    # restore x coord, increment y coordinate by cell size
    x = BOARD_LEFT_COORD
    y += CELL_SIZE

# clean up windows
cv2.destroyAllWindows()

