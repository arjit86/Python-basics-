import os 
oldname = "rename.txt"
newname = "renamed_by_python.txt"
with open(oldname) as f : 
    content = f.read()

with open(newname,"w") as f :
    f.write(content)

os.remove(oldname)
#rename any kind of file 