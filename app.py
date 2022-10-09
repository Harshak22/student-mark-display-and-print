from flask import Flask,render_template,request,redirect
import mysql.connector
app=Flask(__name__)

@app.route('/')
def loginindex():
    return render_template("login.html")
database={'Admin':'admin'}

@app.route('/loginform',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html',info='Invalid User')
    elif database[name1]!=pwd:
        return render_template('login.html',info='Invalid Password')
    else:
        return redirect('/admin')


@app.route('/admin')
def index():
    try:
        db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Varshu@2001",
            database="sql_training"
        )
        cu=db.cursor()
        sql="select*from student"
        cu.execute(sql)
        data=cu.fetchall()
        return render_template('dashboard.html',d=data)
    except Exception as e:
        print("Error:",e)

@app.route('/form')
def add():
    return render_template('form.html')

@app.route('/store',methods=["POST"])
def store():
    n=request.form['name']
    em = request.form['Email']
    p=request.form['password']
    ma = request.form['Maths']
    ch = request.form['Chemistry']
    en = request.form['English']
    b=request.form['Biology']
    y=request.form['year']
    ed=request.form['examdate']
    et=request.form['examtype']
    try:
        db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Varshu@2001",
            database="sql_training"
        )
        cu=db.cursor()
        sql="insert into student(name,Email,password,Maths,Chemistry,English,Biology,year,examdate,examtype)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(n,em,p,ma,ch,en,b,y,ed,et)
        cu.execute(sql)
        db.commit()
        return redirect('/admin')
    except Exception as e:
        print("Error",e)

@app.route('/edit/<rid>')
def edit(rid):
    try:
        db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Varshu@2001",
            database="sql_training"
        )
        cu=db.cursor()
        sql="select * from student where id='{}'".format(rid)
        cu.execute(sql)
        data=cu.fetchone()
        return render_template('editform.html',d=data)
    except Exception as e:
        print("Error:",e)

@app.route('/update/<rid>', methods=['POST'])
def update(rid):
    n = request.form['name']
    em = request.form['Email']
    p = request.form['password']
    ma = request.form['Maths']
    ch = request.form['Chemistry']
    en = request.form['English']
    b = request.form['Biology']
    y = request.form['year']
    ed = request.form['examdate']
    et = request.form['examtype']
    try:
        db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Varshu@2001",
            database="sql_training"
        )
        cu=db.cursor()
        sql = "update student SET name='{}',Email='{}',password='{}',Maths='{}',Chemistry='{}',English='{}',Biology='{}',year='{}',examdate='{}',examtype='{}' where id='{}'".format(n,em,p,ma,ch,en,b,y,ed,et,rid)
        cu.execute(sql)
        db.commit()
        return redirect('/admin')
    except Exception as e:
        print("Error:",e)

@app.route('/delete/<rid>')
def delete(rid):
    try:
        db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Varshu@2001",
            database="sql_training"
        )
        cu=db.cursor()
        sql="delete from student where id='{}'".format(rid)
        cu.execute(sql)
        db.commit()
        return redirect('/admin')
    except Exception as e:
        print("Error",e)


@app.route('/studentpage/<rid>')
def studentpage(rid):
    try:
        db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Varshu@2001",
            database="sql_training"
        )
        cu=db.cursor()
        sql="select* from student where id='{}'".format(rid)
        cu.execute(sql)
        data=cu.fetchone()
        return render_template('sdashboard.html',d=data)
    except Exception as e:
        print("Error:",e)

@app.route('/studentloginpage',methods=['POST','GET'])
def slogin():
    try:
        if request.method=='POST':
            Email = request.form['Email']
            password=request.form['password']

            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Varshu@2001",
                database="sql_training"
            )
            cu = db.cursor()
            sql=f"select * from student where Email='{Email}' and password='{password}';where id='{id}'"
            cu.execute(sql)
            data=cu.fetchone()
            if not cu.fetchone():
                return render_template('sdashboard.html',d=data)
            else:
                return render_template('slogin.html', info="invalid user or password!")
        else:
           return render_template('slogin.html')

    except Exception as e:
        return render_template('slogin.html',info="invalid username or password!")
@app.route('/logout')
def logout():
    return redirect('/')
@app.route('/home')
def home():
    return redirect('/admin')
if __name__=="__main__":
    app.run(debug=True)
    