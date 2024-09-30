from flask import Flask, render_template, request, redirect, url_for, session
import accessdb

app = Flask(__name__)
app.secret_key = 'your_secret_key'
NAME_IDX=0
PWD_IDX=1
ADMIN_IDX=2
FLAG = "NCtfU{Oh_nO_y0U_KN0W_$q1_inJEcTI0nl5l5}"
# con = sqlite3.connect('users.db')
# cur = con.cursor()
# cur.execute("select * from users")
# user_list = cur.fetchall()
# print(user_list)

@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    if session['admin'] > 0:
        return render_template('index.html', name=session['username'], flag=FLAG)
    else:
        # print(f"{session['username']} login")
        return render_template('index.html', name=session['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form["pwd"]
        fetched = accessdb.get_users(username, password)
        if len(fetched) == 0:
            return render_template('login.html', response='user not found')
        session['username'] = fetched[0][NAME_IDX]
        session['admin'] = fetched[0][ADMIN_IDX]
        print(username, password)
        return redirect(url_for('home'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)