from datetime import date, datetime
from flask import Flask, render_template, redirect, request, session
import random

from flask.helpers import total_seconds

app = Flask(__name__)
app.secret_key = "838r9or9"

@app.route('/')
def index():
    if "total" not in session:
        session['total'] = 0
    if "log" not in session:
        session['log'] = ""
    
    return render_template('/index.html')

@app.route('/process', methods = ['POST'])
def submit_btn():
    date_time = datetime.now()
    hour = 0
    minute = 0
    year = date_time.year
    month = date_time.month
    day = date_time.day

    if date_time.hour > 12:
        hour = (str)(date_time.hour - 12)
        minute = (str)(date_time.minute) + " pm"
    else:
        hour = (str)(date_time.hour)
        minute = (str)(date_time.minute) + " am"

    if "farm" in request.form:
        session['farm'] = random.randint(10,20)
        session['total'] += session['farm']
        session['log'] += f"<li>Earned {session['farm']} golds from the {request.form['farm']} on {month}-{day}-{year} at {hour}:{minute}</li>"
    elif "cave" in request.form:
        session['cave'] = random.randint(5,10)
        session['total'] += session['cave']
        session['log'] += f"<li>Earned {session['cave']} golds from the {request.form['cave']} on {month}-{day}-{year} at {hour}:{minute}</li>"
    elif "house" in request.form:
        session['house'] = random.randint(2,5)
        session['total'] += session['house']
        session['log'] += f"<li>Earned {session['house']} golds from the {request.form['house']} on {month}-{day}-{year} at {hour}:{minute}</li>"
    elif "casino" in request.form:
        session['casino'] = random.randint(-50,50)
        session['total'] += session['casino']
        session['log'] += f"<li>Earned {session['casino']} golds from the {request.form['casino']} on {month}-{day}-{year} at {hour}:{minute}</li>"
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)