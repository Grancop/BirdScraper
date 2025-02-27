import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#INSTRUCTIONS:
#STEP 1: Download python. type 'python' into the terminal and you'll be brought to the page you need. 

#STEP 2: Set the python interpreter. ctrl+shift+P and type in 'Python: Select Interpreter'. Select the path that you 
# downloaded python to (Should be marked with 'Recommended' on the right)

#STEP 3: Download requests and beautifulsoup. Type these commands into the terminal:
# python -m pip install requests 
# python -m pip install beautifulsoup4

#STEP 4: Set the 'website_url' variable at the bottom of your code to whatever you want. Pretty self explanitory.

#The folder will be created in the same location as this file. You you ever want to swap folders you can do so by
# changing the 'folder' varible just below. Note that if you already have a folder with some bird pics you'll have to move it 
# to the folder that this file is in, otherwise the program will just make a new folder. It won't search randomly through your files.

#REPLACE WITH NEW FOLDER NAME TO MAKE A NEW FOLDER
def download_images(url, folder="bird_images"):
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    
    img_tags = soup.find_all("img")
    if not img_tags:
        print("No images found.")
        return

    for img in img_tags:
        img_url = img.get("src")
        if not img_url:
            continue
        
        img_url = urljoin(url, img_url)

        try:
            img_data = requests.get(img_url).content
            img_name = os.path.join(folder, os.path.basename(img_url.split("?")[0]))

            with open(img_name, "wb") as img_file:
                img_file.write(img_data)
            print(f"Downloaded: {img_name}")
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")

#REPLACE WITH DESIRED URL
website_url = "https://en.wikipedia.org/wiki/Bird" 
download_images(website_url)
