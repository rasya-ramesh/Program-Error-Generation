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

for p in os.listdir("./grammar_to_ply"):
    if ".DS_Store" in p or "parsetab" in p or "ply_program.py" in p or "error_msgs.txt" in p:
        count += 1
        os.system("rm ./grammar_to_ply/"+p)

for p in os.listdir("./UI"):
    if ".DS_Store" in p or "parsetab" in p or "ply_program.py" in p or "error_msgs.txt" in p:
        count += 1
        os.system("rm ./UI/"+p)

for p in os.listdir("./UI/tool"):
    if ".DS_Store" in p or "parsetab" in p or "ply_program.py" in p or "error_msgs.txt" in p:
        count += 1
        os.system("rm ./UI/tool/"+p)

for language in os.listdir(curdir):
    curdir ="programs/"
    curdir+=language
    # print(curdir)

    if path.isdir(curdir):
      for category in os.listdir(curdir):
        tempdir = curdir+"/"+category
        # print(tempdir)

        if path.isdir(tempdir):
          for file in os.listdir(tempdir+"/output_programs/"):
            filepath = tempdir+"/output_programs/"+file

            if path.isdir(filepath):
                for error in os.listdir(filepath):
                    os.system("rm "+filepath+"/"+error)
                    count+=1
            else :
                os.system("rm "+filepath)
                count+=1


            # print("\t\t\t"+filepath)
print("removed "+str(count)+ " files.")
