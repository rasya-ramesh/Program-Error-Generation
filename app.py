from flask import Flask, request, json, jsonify, redirect, url_for, render_template, send_file
from flask_cors import CORS, cross_origin
import sqlite3
import os
import copy
from werkzeug.utils import secure_filename


app = Flask(__name__, template_folder = 'templates', static_url_path='/static')
session = {}
# app.config['UPLOAD_FOLDER'] = '../programs/teacher_programs/input_programs/'
# app.config['SECRET_KEY'] = "IkKJ5U885e2QUwG9BUfCv8Tj"
# SECRET_KEY = "IkKJ5U885e2QUwG9BUfCv8Tj"
# SESSION_TYPE = 'filesystem'
# app.config.from_object(__name__)
# Session(app)
CORS(app, support_credentials=True)
perc=0
#
# @app.after_request
# def creds(response):
#     response.headers['Access-Control-Allow-Origin'] = 'true'
#     return response
# app.config["SECRET_KEY"] = 'IkKJ5U885e2QUwG9BUfCv8Tj'
# CORS(app, support_credentials=True)
conn = sqlite3.connect('pgmErrorGeneration.db', check_same_thread=False)
conn.execute("PRAGMA foreign_keys = ON")
c = conn.cursor()

@app.route('/')
@cross_origin(supports_credentials=True)
def start():
    print("here")
    global session
    print(session.get("USERNAME"))
    if not session.get("USERNAME") is None:
        user = session.get("USERNAME")
        return render_template("index.html", user=user)
        # return jsonify(status = "Login Successful"), 200
    else:
        print("No username found in session")
        return render_template("login.html")

@app.route('/render_set_paper')
@cross_origin(supports_credentials=True)
def render_set_paper():
    return render_template("setquestions.html")

@app.route('/render_login')
@cross_origin(supports_credentials=True)
def render_login():
    return render_template("login.html")

@app.route('/render_index')
@cross_origin(supports_credentials=True)
def render_index():
    print("render_index")
    return render_template("index.html")

@app.route('/render_stats')
@cross_origin(supports_credentials=True)
def render_stats():
    return render_template("my_stats.html")

@app.route('/render_feedback')
@cross_origin(supports_credentials=True)
def render_feedback():
    return render_template("feedback.html")

@app.route('/render_contact')
@cross_origin(supports_credentials=True)
def render_contact():
    return render_template("contactus.html")

@app.route('/downloadfile/<path:filename>', methods = ['GET', 'POST'])
@cross_origin(supports_credentials=True)
def downloadfile(filename):
    return send_file(filename)

@app.route('/download', methods = ['GET', 'POST'])
@cross_origin(supports_credentials=True)
def download():
    print("download has been invoked")
    if request.method == 'GET':
        path = "papers/"
        links = []
        for file in os.listdir(path):
            links.append("/papers/" + file)

        return jsonify({'links':links}),200
    else:
        return jsonify({}),405

@app.route('/upload', methods = ['GET', 'POST'])
@cross_origin(supports_credentials=True)
def upload():
    if request.method == 'POST':
        print(request.files)
        os.system("rm programs/python/teacher_programs/input_programs/*")
        os.system("rm programs/c/teacher_programs/input_programs/*")
        for file in request.files:
            f = request.files[file]

            if ".py" in f.filename:
                path = 'programs/python/teacher_programs/input_programs/'
            elif '.c' in f.filename:
                path = 'programs/c/teacher_programs/input_programs/'
            f.save(os.path.join(path, secure_filename(f.filename)))
        cat = "teacher_programs"
        list_of_files = list(os.listdir("programs/python/teacher_programs/input_programs/"))
        list_of_files.extend(list(os.listdir("programs/c/teacher_programs/input_programs/")))
        for file in list_of_files:
            inp_file = file
            if ".py" in file:
                lang = 'python'
                inp_grammer = "grammars/python_grammar.txt"
            else:
                lang = 'c'
                inp_grammer = "grammars/grammar_tent.txt"
            perc = 30
            perc_str=str(perc)
            print("perc is" + perc_str)
            command = 'python3 interpretgrammar.py -g ' + inp_grammer + ' -l ' + lang + ' -p '+ perc_str + ' -i ' +inp_file + ' -t ' + cat
            print("COMMAND: " + command)
            os.system(command)

        path_to_write = "papers/"
        os.system("rm papers/*")
        for i in range(0,int(request.form['quantity'])):
            qp = "Question Paper Set " + str(i+1) + "\n\n"
            count = 1
            for file in list_of_files:
                qp += "Question " + str(count) +":\n"
                count += 1
                if ".py" in file:
                    path =  "programs/python/teacher_programs/output_programs/"
                    fname = file[:-3]
                    extension = ".py"
                elif ".c" in file:
                    path =  "programs/c/teacher_programs/output_programs/"
                    fname = file[:-2]
                    extension = ".c"
                print(fname)
                f = open(path + fname + "_" + str(i) + extension, "r")
                qp += f.read()
                qp += "\n\n"
                f.close()
            f = open(path_to_write + "/set_"+str(i+1) +".txt", "w", encoding = "utf-8")
            f.write(qp)
            f.close()

        # for file in os.listdir(path_to_write):
        #     pdf = FPDF()    
        #     pdf.add_page() 
        #     # pdf.set_font("Arial", size = 15) 
        #     f = open(file, "r", encoding = "utf-8") 
        #     file = file[:-4]
        #     # insert the texts in pdf 
        #     for x in f: 
        #         pdf.cell(200, 10, txt = x, ln = 1) 
        #     # save the pdf with name .pdf 
        #     pdf.output("papers/" + file + ".pdf") 

        # os.system("rm papers/*.txt")
        return render_template("downloadpapers.html")
    else:
        return jsonify({}),405

@app.route('/perc_errors', methods = ['POST'])
@cross_origin(supports_credentials=True)
def perc_errors():
    if(request.method=='POST'):
        print("inside")
        received = json.loads(request.data)
        global perc

        perc=received


@app.route('/get_error_msgs', methods = ['POST'])
@cross_origin(supports_credentials=True)
def get_error_msgs():
    if(request.method=='POST'):
        received = json.loads(request.data)
        lang = received[0]
        cat = received[1]
        pgm = received[2]
        file = received[3]
        submission = received[4]

        temp_soln = open("temp_soln.txt",'w')
        temp_soln.write(submission)
        temp_soln.close()
        if lang=="python":
            file = file[:-3].strip()
            extension=".py"

        if lang=="c":
            file = file[:-2].strip()
            extension=".c"

        print(file)
        path = 'programs/' + lang + "/" + cat + "/output_programs/errors/" + file + "_error" + extension

        if lang == "python":
            os.system("python3 " + path +" 2> error_msgs.txt")

        if lang == "c":
            os.system("gcc "+ path + " 2> error_msgs.txt")

        errors_ptr = open(path, "r")
        errors = errors_ptr.read()
        errors_ptr.close()

        format_errs = open("format_errs.txt",'w')
        format_errs.close()
        os.system('python3 check_corrections.py -i temp_soln.txt -e '+path+ ' -o format_errs.txt')

        format_errs = open("format_errs.txt",'r')
        errors =  format_errs.read()
        format_errs.close()
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
        error_pgm = received[3]
        f_type = received[4]
        code = ""
        if f_type == "solution" and not (error_pgm is None):
            folder = "input_programs"
            pgm_name = pgm
            error_pgm = error_pgm.split(".")
            extension = error_pgm[1]
            error_pgm = error_pgm[0]
            error_path = 'programs/' + lang + "/" + cat + "/" + "output_programs" + "/" + error_pgm + "_errors_marked." + extension
            ptr = open(error_path, "r")
            code += ptr.read()
            code += " thisisauniquecombinationofcharactersnoonesgonnause "
            ptr.close()

        elif f_type == "solution":
            folder = "input_programs"
            pgm_name = pgm

        else:
            folder = "output_programs"
            pgm_name = error_pgm

        path = 'programs/' + lang + "/" + cat + "/" + folder + "/" + pgm_name

        code_ptr = open(path, "r")
        code+=code_ptr.read()
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
        path = 'programs/' + lang
        dirs = os.listdir(path)
        # try:
        #     dirs.remove('.DS_Store')
        # except:
        #     pass
        # try:
        #     dirs.remove('errors')
        # except:
        #     pass
        dirs_list = copy.deepcopy(dirs)
        for file in dirs_list:
            if "error" in file or ".DS_Store" in file or "teacher" in file:
                dirs.remove(file)
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
        path = 'programs/' + lang + '/' + cat + '/input_programs'
        files = os.listdir(path)
        # try:
        #     files.remove('.DS_Store')
        # except:
        #     pass
        # try:
        #     files.remove('errors')
        # except:
        #     pass
        files_list = copy.deepcopy(files)
        for file in files_list:
            if "error" in file or ".DS_Store" in file:
                files.remove(file)

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

        perc_str=str(perc)
        print("perc is" + perc_str)
        path = 'programs/' + lang + '/' + cat + '/output_programs'
        os.system("rm " + path + "/" +"*")
        command = 'python3 interpretgrammar.py -g ' + inp_grammer + ' -l ' + lang + ' -p '+ perc_str + ' -i ' +inp_file + ' -t ' + cat
        print("COMMAND: " + command)
        os.system(command)
        files = os.listdir(path)
        # try:
        #     files.remove('.DS_Store')
        # except:
        #     pass
        # try:
        #     files.remove('errors')
        # except:
        #     pass
        files_list = copy.deepcopy(files)
        for file in files_list:
            if "error" in file or ".DS_Store" in file:
                files.remove(file)


        return jsonify({'files':files}),200
    else:
        return jsonify({}),405

@app.route('/store_data', methods =['GET','POST','DELETE','PUT'])
@cross_origin(supports_credentials=True)
def store_data():
    from datetime import datetime
    if(request.method=='POST'):
        if(request.is_json):
            lang = request.json['language']
            cat = request.json['category']
            pgm = request.json['program']
            score = request.json['score']
        else:
            received = json.loads(request.data)
            lang = received['language']
            cat = received['category']
            pgm = received['program']
            score = received['score']

        score = score[7:]
        uname = session['USERNAME']
        date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        c.execute("INSERT into submissions VALUES(?,?,?,?,?,?)",(date, uname, lang, cat, pgm, score))
        conn.commit()
        test = list(c.execute("SELECT * FROM submissions"))
        print(test)
        return jsonify(status="Successful"), 201
    else:
        return jsonify({}),405

@app.route('/get_submissions', methods =['GET','POST','DELETE','PUT'])
@cross_origin(supports_credentials=True)
def get_submissions():
    from datetime import datetime
    if(request.method=='GET'):
        global session
        uname = session['USERNAME']

        tuples = list(c.execute("SELECT * FROM submissions WHERE username = '%s'"%uname))
        return_dict = {}
        i = 0
        for t in tuples:
            temp = {}
            temp["datetime"] = t[0]
            temp["username"] = t[1]
            temp["language"] = t[2]
            temp["category"] = t[3]
            temp["program"] = t[4]
            temp["score"] = t[5]
            return_dict[str(i)] = temp
            i+=1

        return jsonify(return_dict), 201
    else:
        return jsonify({}),405

@app.route('/signup', methods =['GET','POST','DELETE','PUT'])
@cross_origin(supports_credentials=True)
def add_user():
    if(request.method=='POST'):
        if(request.is_json):
            uname = request.json['username']
            pwd = request.json['password']
        else:
            received = json.loads(request.data)
            uname = received['username']
            pwd = received['password']
        if(not(uname) or not(pwd)):
            if(request.is_json):
                return jsonify({}),400
            else:
                return jsonify(status="Fields empty"),400

        u_names = list(c.execute("SELECT username FROM users"))
        u_names = [u_names[i][0] for i in range(0,len(u_names))]
        print(u_names)
        if(uname in u_names):
            if(request.is_json):
                # raise AssertionError('Username Already in Use')
                return jsonify({}), 400

            return jsonify(status="Username Already in Use"),400

        user = {
            'username': uname,
            'password': pwd
        }

        c.execute("INSERT into users VALUES(?,?)", (uname, pwd))
        conn.commit()
        if(request.is_json):
            return jsonify({}), 201
        return jsonify(status="Successful"), 201
    else:
        return jsonify({}),405

@app.route("/signin", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def sign_in():

    if request.method == "POST":
        if(request.is_json):
            username = request.json['username']
            password = request.json['password']
        else:
            received = json.loads(request.data)
            username = received['username']
            password = received['password']

        if(not(username) or not(password)):
            if(request.is_json):
                return jsonify({}),400
            else:
                return jsonify(status="\nFields empty"),400

        users_tuples = list(c.execute("SELECT * FROM users"))
        passwords = [users_tuples[i][1] for i in range(0,len(users_tuples))]
        users = [users_tuples[i][0] for i in range(0,len(users_tuples))]


        if not username in users:
            return jsonify(status="\nUsername Not Found"),400
        else:
            user = username

        for u in users_tuples:
            uname = u[0]
            pwd = u[1]
            if uname == username:
                if not password == pwd:
                    return jsonify(status="\nWrong Password"),400
                else:
                    global session
                    session["USERNAME"] = username
                    print("session username set")
                    print(session)
                    return redirect(url_for("profile"))
                    # return jsonify(status = "\nLogin Successful"), 200
        return jsonify(status = "Unknown Error"),400
    else:
        return jsonify({}),405

@app.route("/profile")
@cross_origin(supports_credentials=True)
def profile():
    global session
    print(session.get("USERNAME"))
    if not session.get("USERNAME") is None:
        user = session.get("USERNAME")
        print('here i am')
        return redirect(url_for("render_index"))
        # return jsonify(status = "Login Successful"), 200
    else:
        print("No username found in session")
        return redirect(url_for("sign_in"))

if __name__ == '__main__':
    app.secret_key = "IkKJ5U885e2QUwG9BUfCv8Tj"
    app.run( debug=True,
             host='0.0.0.0',
             port=80
             )
    # app.run(debug=True)
