import os
from os import path
curdir ="programs/"
count = 0;
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
