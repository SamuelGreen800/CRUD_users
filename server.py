
from flask import Flask, redirect, render_template, request
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    
    return redirect('/users')


@app.route('/users')
def read():
    users = User.get_all()
    print(users)
    return render_template('read.html', all_users = users)



@app.route('/users/new')
def new():
    return render_template('create.html')

@app.route('/users/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')


if __name__=='__main__':
    app.run(debug=True, port = 5001)