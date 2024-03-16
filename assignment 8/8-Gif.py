import os
import imageio
IMAGES = []

file_list = sorted(os.listdir("assignment 8/pics"))

for file_name in file_list:
    file_path = "assignment 8/pics/" + file_name
    image = imageio.imread(file_path)
    IMAGES.append(image)
    
imageio.mimsave("assignment 8/my_output.gif" , IMAGES)