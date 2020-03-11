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

        if lang == 'python':
            inp_grammer = "grammars/python_grammar.txt"
            folder = "../programs/python"
        elif lang == 'c':
            inp_grammer = "grammars/c_grammar.txt"
            folder = "../programs/C"

        if pgm == 'functions':
            inp_file = "double.py"

        elif pgm == 'if_else':
            inp_file = "ifelse1.py"

        os.system('python3 interpretgrammar.py -g' + inp_grammer + ' -l python -i ' + inp_file + ' -t ' + pgm)
        os.system('python3 output.py')
        error_pgm = open("../programs/" + lang + "/" + pgm + "/output_programs/ifelse1_1add.py", "r").read()
        # return jsonify({}), 200
        print(type(error_pgm))
        # return error_pgm
        return error_pgm,200
        
    else:
        return jsonify({}),405



if __name__ == '__main__':
    app.run( debug=False,
             host='0.0.0.0',
             port=80
             )
    # app.run(debug=True)