from flask import Flask, request, json, jsonify
from flask_cors import CORS, cross_origin
import os


app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/get_categories', methods = ['POST'])
@cross_origin(supports_credentials=True)
def get_categories():
    if(request.method=='POST'):
        if(request.is_json):
            lang = request.json['lang']
        else:
            received = json.loads(request.data)
            lang = received[0]
        path = '../programs/' + lang
        dirs = os.listdir(path)
        try:
            dirs.remove('.DS_Store')
        except:
            pass
        return jsonify({'directories':dirs}),200
    else:
        return jsonify({}),405


@app.route('/get_programs', methods = ['POST'])
@cross_origin(supports_credentials=True)
def get_programs():
    if(request.method=='POST'):
        if(request.is_json):
            lang = request.json['lang']
            cat = request.json['cat']
        else:
            received = json.loads(request.data)
            lang = received[0]
            cat = received[1]
        path = '../programs/' + lang + '/' + cat + '/input_programs'
        files = os.listdir(path)
        try:
            files.remove('.DS_Store')
        except:
            pass
        return jsonify({'files':files}),200
    else:
        return jsonify({}),405

@app.route('/get_code', methods =['GET','POST','DELETE','PUT'])
@cross_origin(supports_credentials=True)
def fetch_code():
    if(request.method=='POST'):
        received = json.loads(request.data)
        lang = received[0]
        cat = received[1]
        inp_file = received[2]

        #for python programs
        if lang == 'python':
            inp_grammer = "grammars/new_python_grammar.txt"

        #for C programs
        elif lang == "c":
            inp_grammer = "grammars/grammar_tent.txt"

        path = '../programs/' + lang + "/" + cat + "/output_programs/"
        command = 'python3 interpretgrammar.py -g ' + inp_grammer + ' -l ' + lang + ' -i ' + inp_file + ' -t ' + cat
        print("COMMAND: " + command)
        os.system(command)
        os.system('python3 ply_program.py')
        files = os.listdir(path)
        try:
            files.remove('.DS_Store')
        except:
            pass
        print(path)
        print(files)
        print(path + files[0])
        error_pgm_ptr = open(path + files[0], "r")
        error_pgm = error_pgm_ptr.read()
        error_pgm_ptr.close()

        os.system("rm " + path +"*")
        return error_pgm,200

    else:
        return jsonify({}),405




if __name__ == '__main__':
    app.run( debug=True,
             host='0.0.0.0',
             port=80
             )
    # app.run(debug=True)
