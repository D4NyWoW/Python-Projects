from PIL import Image, ImageFilter
import sys, os

# img = Image.open('./images/pikachu.jpg')
#filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.convert('L') # convert images to different format like black and white
# filtered_img = img.rotate(90)
# filtered_img = img.resize((300, 300)) # the resize accept a tuple

# box = (100, 100, 400, 400)
# filtered_img = img.crop(box)
# filtered_img.save("blur.png", 'png') # png support that filters

# img1 = Image.open('./astro.jpg')
# img1.thumbnail((400, 200)) # keep the aspect ratio
# img1.save('thumbnail.jpg')

# Convert JPG to PNG

# grab to first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# check if new/ exists, if not create it
if not os.path.exists(output_folder): # this is going to check if the third argument does exist
    os.makedirs(output_folder)

for filename in os.listdir(image_folder): # this is going to be the items in the directory
    img3 = Image.open(f'{image_folder}{filename}') 
    clean_name = os.path.splitext(filename)[0] # we need to remove .jpg so we can save that as .png
    #print(clean_name) # give a tuple about the name and the extension -> jpg in that case
    img3.save(f'{output_folder}{clean_name}.png', 'png')
    print('good work !')

# loop through images -> convert images to png -> save to the new folder