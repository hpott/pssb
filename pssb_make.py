import os
n="\n"

id=raw_input("id: ")
name=raw_input("name: ")
url=raw_input("url: ")
cat=raw_input("catergory: ")

browser=raw_input("browser(leave blank for default):  ")
if browser == "":
    browser="firefox"
imgfile=raw_input("Icon file: ")

with open(id+".pssb","w+") as datafile:
    datafile.write(id+n+name+n+url+n+cat+n+browser+n+imgfile)
print('Building ssb file')
data=id+".pssb"
os.system("mkdir "+id)
os.system("mv "+data+" "+id)
os.system("mv "+imgfile+" "+id)
os.system("tar -cvf "+id+".ssb "+id+"/")
print("Cleaning up")
os.system("rm "+id+"/*")
os.system("rmdir "+id)
