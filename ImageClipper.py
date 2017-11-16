import cv2
import numpy as np
import copy

# Crop ROI coordinates
x1, y1 = 0, 0
x2, y2 = 0, 0

# img is the image read in from external file
img = cv2.imread("testing.png")

# Track if mouse is held down
down = False

# Window Size - To read in from config
resolutionx = 800
resolutiony = 600

# Image size
sy, sx = img.shape[:2]

# Display coordinates
dx1, dy1 = 0, 0
dy2, dx2 = sy, sx

if (dx2 >= resolutionx):
    dx2 = resolutionx
if (dy2 >= resolutiony):
    dy2 = resolutiony

# Increment display view by
inc = 10

# preview shows highlighted area
preview = None

# Copy of display image - dont want drawn rectangles to be permanent
ref = copy.copy(img)  # pointer to original image


# mouse callback function
def draw_rect(event, x, y, flags, param):
    global x2, x1, y2, y1, down, preview, img

    if event == cv2.EVENT_MOUSEMOVE and down == True:
        img = copy.copy(ref)  # point display back to original
        x2, y2 = x, y
        # Offset - keep up with what is being displayed
        cv2.rectangle(img, (x1 + dx1, y1 + dy1), (x2 + dx1, y2 + dy1), (0, 255, 0), 2)

    if event == cv2.EVENT_LBUTTONDOWN:
        x1, y1 = x, y
        down = True

    if event == cv2.EVENT_LBUTTONUP:
        img = copy.copy(ref)  # point display back to original
        x2 = x
        y2 = y

        # Check points, in case rectangle has been drawn bottom to top
        if (x2 < x1 and y2 < y1):
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        # And again for top right to bottom left
        elif (x1 > x2 and y1 < y2):
            diff = x1 - x2
            x1, x2 = x1 - diff, x2 + diff

        # And last for bottom left to top right
        if (y1 > y2 and x1 < x2):
            diff = y1 - y2
            y1, y2 = y1 - diff, y2 + diff

        preview = ref[y1 + dy1:y2 + dy1, x1 + dx1:x2 + dx1]
        cv2.rectangle(img, (x1 + dx1, y1 + dy1), (x2 + dx1, y2 + dy1), (0, 255, 0), 2)  # draw end rect
        cv2.destroyWindow('preview')
        down = False


cv2.namedWindow('display')
cv2.namedWindow('preview')
cv2.resizeWindow('display', resolutionx, resolutiony)
cv2.setMouseCallback('display', draw_rect)

# Display loop / key handler
while (True):

    cv2.imshow('display', img[dy1:dy2, dx1:dx2])

    key = cv2.waitKey(20)
    print(preview)

    if (preview is not None ):
        cv2.imshow('preview', preview)

    if (key & 0xFF == 119): ##w key press
        # Move Up - decrease y
        if ((dy1 - inc) <= 0):
            dy2 -= dy1
            dy1 = 0
        else:
            dy1 -= inc
            dy2 -= inc
        print(dy1, dy2)

    if (key & 0xFF == 115): #s key press
        # MOVE DOWN - increase y
        if ((dy2 + inc) >= sy):
            dy1 += sy - dy2
            dy2 = sy
        else:
            dy2 += inc
            dy1 += inc
        print(dy1, dy2)

    if (key & 0xFF == 97): #a key press
        # MOVE LEFT - decrease x
        if ((dx1 - inc) <= 0):
            dx2 -= dx1
            dx1 = 0
        else:
            dx1 -= inc
            dx2 -= inc
        print(dx1, dx2)

    if (key & 0xFF == 100): #d keypress
        # MOVE RIGHT
        if ((dx2 + inc) >= sx):
            dx1 += sx - dx2
            dx2 = sx
        else:
            dx2 += inc
            dx1 += inc
        print(dx1, dx2)

    if (key & 0xFF == 27): #esc key press
        break

    if (key & 0xFF == 120): #x key press
        cv2.imwrite('MyImg.png', preview)


cv2.destroyAllWindows()

# 27/03/15
# Refresh rectangle, let user see what will be selected DONE

# 28-29/03/15
# Consider alternate methods to update image rather than reading from file
# Create a mat that holds a reference copy DONE
# Pull from reference instead of file DONE

# 30/03/15
# Crop rectangle
# Only works if selecting from top left to bottom right
# Look into conditional to check point position and adjust


# 31/03/15
# Save file DONE


# 1/04/15 & 02/04/15
# Add in handling for large images - exceeding user resolution
# Starting with a fixed window size 800x800


# 7/04/15

# Fixed poor refresh rate - poll once and check received value instead of repeat polling


# 8/4/15
# Fixed drawing ROI from any point, check x/y values and swap or adjust by difference as needed

# Need to look in to updating reference as image position changes


# 13/4/15

# Fixed offsetting selection area / preview with display

# Look into dragging image using mouse 
# Look into zooming in / zooming out for easier selection + traversal
