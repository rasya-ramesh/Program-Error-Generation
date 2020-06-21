import os
from os import path
import glob
curdir ="programs/"
count = 0;

# to remove .DS_Store
for p in os.listdir("."):
    if ".DS_Store" in p or "parsetab" in p or "ply_program.py" in p or "error_msgs.txt" in p:
        print(p)
        count += 1
        os.system("rm "+p)

for p in os.listdir("."):
    if ".DS_Store" in p or "parsetab" in p or "ply_program.py" in p or "error_msgs.txt" in p:
        count += 1
        os.system("rm ."+p)

for p in os.listdir("./templates"):
    if ".DS_Store" in p or "parsetab" in p or "ply_program.py" in p or "error_msgs.txt" in p:
        count += 1
        os.system("rm ./templates/"+p)

for p in os.listdir("./static"):
    if ".DS_Store" in p or "parsetab" in p or "ply_program.py" in p or "error_msgs.txt" in p:
        count += 1
        os.system("rm ./static/"+p)

for p in os.listdir("./static/images"):
    if ".DS_Store" in p or "parsetab" in p or "ply_program.py" in p or "error_msgs.txt" in p:
        count += 1
        os.system("rm ./static/images/"+p)

for p in os.listdir("./static/scripts"):
    if ".DS_Store" in p or "parsetab" in p or "ply_program.py" in p or "error_msgs.txt" in p:
        count += 1
        os.system("rm ./static/scripts/"+p)

for p in os.listdir("./static/css"):
    if ".DS_Store" in p or "parsetab" in p or "ply_program.py" in p or "error_msgs.txt" in p:
        count += 1
        os.system("rm ./static/css/"+p)



for language in os.listdir(curdir):
    curdir ="programs/"
    curdir+=language
    # print(curdir)

    if path.isdir(curdir):
      for category in os.listdir(curdir):
        tempdir = curdir+"/"+category
        # print(tempdir)

        if path.isdir(tempdir):
            try:
                for file in os.listdir(tempdir+"/output_programs/"):
                    filepath = tempdir+"/output_programs/"+file
                    if path.isdir(filepath):
                        for error in os.listdir(filepath):
                            os.system("rm "+filepath+"/"+error)
                            count+=1
                    else :
                        os.system("rm "+filepath)
                        count+=1
            except:
                pass


            # print("\t\t\t"+filepath)
print("removed "+str(count)+ " files.")
