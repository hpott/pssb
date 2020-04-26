import sys
import os

#This is an incrdibly dumb way to get arguments, but it works
argf=sys.argv[1]

truefile=os.path.isfile(argf)

#Detects if specified file exists
if truefile == False:
    print("File not valid. Try again")
    quit()

#Unpacks the .ssb file
os.system("tar -xvf "+argf)

#This is a mess but it works somehow
dirf=argf
argf = dirf[:-4]
for line in argf.split('\n'):
    continue

dirf = dirf[:-4]
dirf=dirf+".pssb"
os.system("cp "+argf+"/* ./")

#Get values from file
#I am too tired to do this propely but this works
with open(dirf, 'r') as pssb:
    sigline = 1
    for line in range(sigline - 1):
        pssb.readline()
    data=pssb.readline().replace('\n', '')
id=data
with open(dirf, 'r') as pssb:
    sigline = 2
    for line in range(sigline - 1):
        pssb.readline()
    data=pssb.readline().replace('\n', '')
name=data
with open(dirf, 'r') as pssb:
    sigline = 3
    for line in range(sigline - 1):
        pssb.readline()
    data=pssb.readline().replace('\n', '')
link=data
with open(dirf, 'r') as pssb:
    sigline = 4
    for line in range(sigline - 1):
        pssb.readline()
    data=pssb.readline().replace('\n', '')
cat=data
with open(dirf, 'r') as pssb:
    sigline = 5
    for line in range(sigline - 1):
        pssb.readline()
    data=pssb.readline().replace('\n', '')
browser=data
with open(dirf, 'r') as pssb:
    sigline = 6
    for line in range(sigline - 1):
        pssb.readline()
    data=pssb.readline().replace('\n', '')
iconpath=data

#Install ssb
print ("Follow the dialog prompts to install"+id+"...")
os.system("ice -b "+browser+" -c "+cat+" -i "+iconpath+" -I True  -n"+name+" -u "+link)
#Removes junk
print("Cleaning Up")
os.system("rm "+argf+"/*")
os.system("rmdir "+argf)
os.system("rm "+argf+".png "+dirf   )

print ("Completed")
