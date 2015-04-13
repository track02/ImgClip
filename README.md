# ImgClip
Image clipper for quickly cropping multiple areas from an image


#27/03/15
#Refresh rectangle, let user see what will be selected DONE

#28-29/03/15
#Consider alternate methods to update image rather than reading from file
        # Create a mat that holds a reference copy DONE
        # Pull from reference instead of file DONE

#30/03/15
#Crop rectangle
        # Only works if selecting from top left to bottom right
        # Look into conditional to check point position and adjust 


#31/03/15
# Save file DONE
        

#1/04/15 & 02/04/15
# Add in handling for large images - exceeding user resolution
# Starting with a fixed window size 800x800


#7/04/15

# Fixed poor refresh rate - poll once and check received value instead of repeat polling


#8/4/15
# Fixed drawing ROI from any point, check x/y values and swap or adjust by difference as needed

#Need to look in to updating reference as image position changes


#13/4/15

# Fixed offsetting selection area / preview with display

# Look into dragging image using mouse 
# Look into zooming in / zooming out for easier selection + traversa
