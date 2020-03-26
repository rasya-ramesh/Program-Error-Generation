from flask import Flask, request, json, jsonify
from flask_cors import CORS, cross_origin
import os


app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/get_error_msgs', methods = ['POST'])
@cross_origin(supports_credentials=True)
def get_error_msgs():
    if(request.method=='POST'):
        received = json.loads(request.data)
        lang = received[0]
        cat = received[1]
        pgm = received[2]
        file = received[3]
        if lang=="python":
            file = file[:-3].strip()
            extension=".py"

        if lang=="c":
            file = file[:-2].strip()
            extension=".c"

        print(file)
        path = '../programs/' + lang + "/" + cat + "/output_programs/errors/" + file + "_error" + extension

        if lang == "python":
            os.system("python3 " + path +" 2> error_msgs.txt")

        if lang == "c":
            os.system("gcc "+ path + " 2> error_msgs.txt")
        
        errors_ptr = open(path, "r")
        errors = errors_ptr.read()
        errors_ptr.close()
        return errors,200
    else:
        return jsonify({}),405

@app.route('/get_file', methods = ['POST'])
@cross_origin(supports_credentials=True)
def get_file():
    if(request.method=='POST'):
        import re
        received = json.loads(request.data)
        lang = received[0]
        cat = received[1]
        pgm = received[2]
        f_type = received[3]

        if f_type == "solution":
            folder = "input_programs"
            pgm_name = pgm

        else:
            folder = "output_programs"
            pgm_name = f_type

        path = '../programs/' + lang + "/" + cat + "/" + folder + "/" + pgm_name
        
        code_ptr = open(path, "r")
        code = code_ptr.read()
        code_ptr.close()
        code = re.sub(r'n\+', '\n', code)
        print(code)
        return code,200
    else:
        return jsonify({}),405

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
            dirs.remove('errors')
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
            files.remove('errors')
        except:
            pass
        return jsonify({'files':files}),200
    else:
        return jsonify({}),405

@app.route('/get_outputs', methods = ['POST'])
@cross_origin(supports_credentials=True)
def get_outputs():
    if(request.method=='POST'):
        received = json.loads(request.data)
        lang = received[0]
        cat = received[1]
        inp_file = received[2]
        #for python programs
        if lang == 'python':
            inp_grammer = "grammars/python_grammar.txt"

        #for C programs
        elif lang == "c":
            inp_grammer = "grammars/grammar_tent.txt"

        path = '../programs/' + lang + '/' + cat + '/output_programs'
        os.system("rm " + path + "/" +"*")
        command = 'python3 interpretgrammar.py -g ' + inp_grammer + ' -l ' + lang + ' -i ' + inp_file + ' -t ' + cat
        print("COMMAND: " + command)
        os.system(command)
        os.system('python3 ply_program.py')
        files = os.listdir(path)
        try:
            files.remove('.DS_Store')
            files.remove('errors')
        except:
            pass
        return jsonify({'files':files}),200
    else:
        return jsonify({}),405






if __name__ == '__main__':
    app.run( debug=True,
             host='0.0.0.0',
             port=80
             )
    # app.run(debug=True)
