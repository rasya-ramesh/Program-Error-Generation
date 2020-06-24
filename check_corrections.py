#python check_corrections.py -i temp_soln.txt -s temp_correct.txt -e errors.txt -o output_file.txt

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", required=True, help="user corrected code")
parser.add_argument("-s", required=True, help="solution code")
parser.add_argument("-e", required=True, help="Linewise error messages file")
parser.add_argument("-o", required=True, help="Output file for formatted errors")

args = parser.parse_args()
code_file = args.i
solution_file = args.s
errors_file = args.e
out_file = args.o
cf = open(code_file,'r')
code = cf.readlines()
cf.close()
ef = open(errors_file,'r')
errors = ef.readlines()
ef.close()
sf = open(solution_file,'r')
solution = sf.readlines()
sf.close()

output = []
codelines = []
solutionlines = []
for line in code:
    codelines.append(line[:-1])
for line in solution:
    solutionlines.append(line[:-1])

def check_added(e,lineno, symbol):
    # print(symbol)
    element = ""
    curline = codelines[lineno-1]
    solutionline = solutionlines[lineno -1]
    print(solutionline, curline)

    if solutionline.count(symbol) == curline.count(symbol):    #if symbol in curline :
        element  = "<span class='corrected' >"+e[:-1]+"</span>\n"
    else:
        element  = "<span class='not_corrected' >"+e[:-1]+"</span>\n"

    return element


def check_missing(e,lineno, symbol):
    element = ""
    #print(symbol)
    if (lineno-1)< len(codelines):
        curline = codelines[lineno-1]
        solutionline = solutionlines[lineno -1]
        print(solutionline, curline)
        if solutionline.count(symbol) == curline.count(symbol) : #if symbol in curline :
            element  = "<span class='corrected' >"+e[:-1]+"</span>\n"
        else:
            element  = "<span class='not_corrected' >"+e[:-1]+"</span>\n"
        return element
    else:
        return e[:-1]


for e in errors:
    error = e.split(" ")
    if len(e)>11:
            lineno = int(error[2])
            print(error)
            if "Unknown" in e:
                # print(error[6])
                element = check_added(e,lineno,error[6])
            elif "missing" in e:
                # print(error[5])
                element = check_missing(e,lineno,error[5])
            output.append(element)


print("-"*20+"DONEZO")
print(output)
print("-"*20+"DONEZO")

outputfile = open(out_file, 'w')
for i in output:
    outputfile.writelines(i+"\n")
outputfile.close()
