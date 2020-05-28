

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", required=True, help="user corrected code")
parser.add_argument("-e", required=True, help="Linewise error messages file")

args = parser.parse_args()
code_file = args.i
errors_file = args.e
cf = open(code_file,'r')
code = cf.readlines()
cf.close()
ef = open(errors_file,'r')
errors = ef.readlines()
ef.close()

output = []
codelines = []
for line in code:
    codelines.append(line[:-1])

def check_added(e,lineno, symbol):
    element = ""
    curline = codelines[lineno-1]
    if symbol in curline:
        element  = "<span class='not_corrected' >"+e[:-1]+"</span>\n"
    else:
        element  = "<span class='corrected' >"+e[:-1]+"</span>\n"


    print("")
    return element


def check_missing(e,lineno, symbol):
    element = ""
    curline = codelines[lineno-1]
    if symbol in curline :
        element  = "<span class='corrected' >"+e[:-1]+"</span>\n"
    else:
        element  = "<span class='not_corrected' >"+e[:-1]+"</span>\n"
    return element


for e in errors:
    error = e.split(" ")
    if len(e)>11:
            lineno = int(error[2])
            if "Unknown" in e:
                # print(error[6])
                element = check_added(e,lineno,error[6])
            elif "missing" in e:
                # print(error[5])
                element = check_missing(e,lineno,error[5])
            output.append(element)

for i in output:
    print(i)
