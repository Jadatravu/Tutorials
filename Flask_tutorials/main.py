from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.sqlite3'
app.config['SECRET_KEY'] = "qwerty"

db = SQLAlchemy(app)

class employee(db.Model):
   id = db.Column('emp_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   department = db.Column(db.String(50))

   def __init__(self, name, department):
      self.name = name
      self.department = department

@app.route('/')
def list_all():
   return render_template('list_all.html', emps = employee.query.all() )

@app.route('/new_emp/', methods = ['GET','POST'])
def new_emp():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['department']:
         print("needed form ids in form doesnot exist")
      else:
         emp = employee(request.form['name'], request.form['department'])        
         db.session.add(emp)
         db.session.commit()
         return redirect(url_for('list_all'))
   else:
        return render_template('new.html')

@app.route('/search/', methods = ['GET'])
def search():
   if request.method == 'GET':
      #emp_list = employee.query.filter_by(name=request.args.get('name'))
      emp_list = employee.query.filter(employee.name.contains(request.args.get('name')))
      return render_template('list_all.html', emps = emp_list )         
   return render_template('new.html')

if __name__ == "__main__":
    db.create_all()
    app.debug=True
    app.run(host="127.0.0.1",port=5000)
