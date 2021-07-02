import os
from os import path
from shutil import copyfile

def main(folder_name):
   # Check if project already exist:
   if path.exists(folder_name) == False :
      # create folders/projects
      cmd="scrapy startproject " + folder_name 
      os.system(cmd)
      current_dir = os.getcwd()
      # coppy spider scripts from Spider_scripts folder
      copyfile(current_dir + "/Spider_scripts/" + folder_name + "_scraper.py", 
      current_dir + "/" + folder_name + "/" + folder_name + "/spiders/" + folder_name + "_scrapper.py")

   else :
      print("Folders for " + folder_name + " exist. You are ready to crawl. If it's not working, check setup.py files")




if __name__== "__main__":
   main('aruodas')
   main('capitallt')