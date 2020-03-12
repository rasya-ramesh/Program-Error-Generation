from flask import Flask, request, json, jsonify
from flask_cors import CORS, cross_origin
import os


app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/', methods =['GET','POST','DELETE','PUT'])
@cross_origin(supports_credentials=True)
def fetch_code():
    if(request.method=='POST'):
        if(request.is_json):
        	lang = request.json['lang']
        	pgm = request.json['pgm']
        else:
            received = json.loads(request.data)
            lang = received[0]
            pgm = received[1]
        
        if(not(lang) or not(pgm)):
            if(request.is_json):
                return jsonify({}),400
            else:
                return jsonify(status="Fields empty"),400

        #for python programs
        if lang == 'python':
            inp_grammer = "grammars/python_grammar.txt"
            folder = "../programs/python"
            if pgm == "functions":
                inp_file = "double.py"
            elif pgm == "if_else":
                inp_file = "ifelse1.py"

        #for C programs
        elif lang == "c":
            inp_grammer = "grammars/grammar_C.txt"
            folder = "../programs/c"
            if pgm == "functions":
                inp_file = "floatsum.c"
            elif pgm == "if_else":
                inp_file = "check_odd.c"
                print("here")

        path = folder + "/" + pgm + "/output_programs/"
        command = 'python3 interpretgrammar.py -g ' + inp_grammer + ' -l ' + lang + ' -i ' + inp_file + ' -t ' + pgm
        print("COMMAND: " + command)
        os.system(command)
        os.system('python3 ply_program.py')
        files = os.listdir(path)
        print(path)
        print(files)
        print(path + files[0])
        error_pgm = open(path + files[0], "r").read()
        # return jsonify({}), 200
        print(type(error_pgm))
        # return error_pgm
        return error_pgm,200
        
    else:
        return jsonify({}),405



if __name__ == '__main__':
    app.run( debug=True,
             host='0.0.0.0',
             port=80
             )
    # app.run(debug=True)