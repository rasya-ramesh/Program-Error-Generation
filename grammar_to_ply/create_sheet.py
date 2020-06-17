import os
from os import path
import glob
import csv
import sys

#python create_sheet.py -f   ---> -f for forst run. After that just append.
#generating repository in the form of a csv file.
error_num = 4
curdir ="../programs/"
count = 0;

list_of_progs = []
percentage = "40"

if len(sys.argv)>1:
    log_file = open("logfile.txt","w")
    with open('../ErrorsRepository.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Language", "Category","Program_Name","Percentage_errors", "Input_file", "Error_1", "Error_2", "Error_3", "Error_4"])
        for language in os.listdir(curdir):
                curdir ="../programs/"
                curdir+=language
                # print(curdir)
                print("======="+language+"=======")
                if path.isdir(curdir):
                  for category in os.listdir(curdir):
                    tempdir = curdir+"/"+category
                    # print(tempdir)

                    if path.isdir(tempdir):

                      for file in os.listdir(tempdir+"/input_programs/"):

                        thisrow =[language, category,file,percentage]

                        filepath = tempdir+"/input_programs/"+file
                        if (".DS_Store" in filepath):
                            break
                        correct_file = open(filepath , "r")
                        correct_prog = correct_file.read()
                        thisrow.append(correct_prog)
                        correct_file.close


                        if language == "python":
                            command = "python3 interpretgrammar.py -g grammars/python_grammar.txt -l python -i " + file +" -t " +category + " -p " + percentage
                        else :
                            command = "python3 interpretgrammar.py -g grammars/grammar_tent.txt -l c -i " + file +" -t "+category+" -p "+percentage
                        os.system(command)

                        serial = 0
                        for i in range(0,error_num):
                            this_error = file.split('.')[0] + "_"+ str(i) +"."
                            #print("OOOOOOOOOOOOOOOOOOOOOOOOOOOO----------- " + this_error +"-----------OOOOOOOOOOOOOOOOOOOOOOOOOOOO" )
                            for err_output in os.listdir(tempdir+"/output_programs/"):
                                cur_err = tempdir+"/output_programs/"+err_output
                                if (this_error in err_output) and (path.isdir(cur_err) == False ) :
                                    error_file =  open(cur_err , "r")
                                    error_prog = error_file.read()
                                    thisrow.append(error_prog)
                                    error_file.close()
                                    break


                        #write into CSV
                        if len(thisrow)  == 9:
                            log_file.writelines(filepath +" " + str(percentage) +" \n")
                        else:
                            log_file.writelines(filepath +" FAILED \n")
                        writer.writerow(thisrow)
    log_file.close()

else:
  log_file = open("logfile.txt","a")
  with open('../ErrorsRepository.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow([])
    for language in os.listdir(curdir):
            curdir ="../programs/"
            curdir+=language
            # print(curdir)
            print("======="+language+"=======")
            if path.isdir(curdir):
              for category in os.listdir(curdir):
                tempdir = curdir+"/"+category
                # print(tempdir)

                if path.isdir(tempdir):

                  for file in os.listdir(tempdir+"/input_programs/"):

                    thisrow =[language, category,file,percentage]

                    filepath = tempdir+"/input_programs/"+file
                    if (".DS_Store" in filepath):
                        break
                    correct_file = open(filepath , "r")
                    correct_prog = correct_file.read()
                    thisrow.append(correct_prog)
                    correct_file.close


                    if language == "python":
                        command = "python3 interpretgrammar.py -g grammars/python_grammar.txt -l python -i " + file +" -t " +category + " -p " + percentage
                    else :
                        command = "python3 interpretgrammar.py -g grammars/grammar_tent.txt -l c -i " + file +" -t "+category+" -p "+percentage
                    os.system(command)

                    serial = 0
                    for i in range(0,error_num):
                        this_error = file.split('.')[0] + "_"+ str(i) +"."
                        #print("OOOOOOOOOOOOOOOOOOOOOOOOOOOO----------- " + this_error +"-----------OOOOOOOOOOOOOOOOOOOOOOOOOOOO" )
                        for err_output in os.listdir(tempdir+"/output_programs/"):
                            cur_err = tempdir+"/output_programs/"+err_output
                            if (this_error in err_output) and (path.isdir(cur_err) == False ) :
                                error_file =  open(cur_err , "r")
                                error_prog = error_file.read()
                                thisrow.append(error_prog)
                                error_file.close()
                                break


                    #write into CSV
                    if len(thisrow)  == 9:
                        log_file.writelines(filepath +" " + str(percentage) +" \n")
                    else:
                        log_file.writelines(filepath +" FAILED \n")
                    writer.writerow(thisrow)
log_file.close()

            #list_of_progs.append(str(filepath))

# print(list_of_progs)
#
# for program in list_of_progs[:3]:
#
#     command = "python3 ../interpretgrammar.py -g ../grammars/new_python_grammar.txt -l python -i " + program +" -t toy_programs -p 40"
#     os.system(command)
#     print(program + "  done")
#

#python3 interpretgrammar.py -g grammars/new_python_grammar.txt -l python -i factorial.py  -t toy_programs
