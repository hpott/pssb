import os
n="\n"
favicon=False
id=raw_input("id: ")
name=raw_input("name: ")
url=raw_input("url: ")
cat=raw_input("catergory: ")

browser=raw_input("browser(leave blank for default):  ")
if browser == "":
    browser="firefox"
imgfile=raw_input("Icon file(leave blank to use site favicon): ")

if imgfile == "":
    print("Favicon will be generated when user installs")
    favicon=True

with open(id+".pssb","w+") as datafile:
    datafile.write(id+n+name+n+url+n+cat+n+browser+n+imgfile)
print('Building ssb file')
data=id+".pssb"
os.system("mkdir "+id)
os.system("mv "+data+" "+id)
if favicon==False:
    os.system("mv "+imgfile+" "+id)

os.system("tar -cvf "+id+".ssb "+id+"/")
print("Cleaning up")
os.system("rm "+id+"/*")
os.system("rmdir "+id)
