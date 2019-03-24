from flask import Flask, render_template, request, redirect, session
import random	                
app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def index():
    if 'num' not in session:
        session['num']= random.randint(1, 100)
        print(session['num'])
    if 'message' not in session:
        session["message"]=""    
    return render_template("index.html", result=session["message"])

@app.route('/result', methods=["POST"])
def results():  
    if int(request.form['guess']) == session['num']:
        session["message"] = "Correct!"
        return redirect('/')
    if int(request.form['guess']) > session['num']:
        session["message"] = "Too High"
        return redirect('/')
    if int(request.form['guess']) < session['num']:
        session["message"] = "Too Low"
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

