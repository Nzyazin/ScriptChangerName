import os
import random

path = r"C:\Users\zyazi\Downloads\Attachments\\"
listOfFiles = os.listdir(path)
countOfFile = len(listOfFiles)
os.chdir(path)

for i in range(0, countOfFile):
    value = random.uniform(0, 100)
    os.rename(path+listOfFiles[i], str(i + 1) + "#" + str(int(value)) + ".jpg")