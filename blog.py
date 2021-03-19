from flask import Flask,render_template,request,redirect,flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key='raj'


app.config['MYSQL_USER'] = 'sql12394382'
app.config['MYSQL_PASSWORD'] = 'MKjCIBmjMp'
app.config['MYSQL_DB'] = 'sql12394382'
app.config['MYSQL_HOST'] = 'sql12.freemysqlhosting.net'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql=MySQL(app)



@app.route('/',methods=['POST','GET'])
def home():
        
    if request.method=='POST':
        
        if request.form.get("addblog"):
            return redirect('/ab')
        
    else:
        return render_template('home.html')

@app.route('/login',methods=['POST','GET'])
def lin():
    if request.method=='POST':
        if request.form.get("lin"):
            return redirect('/login')
    else:
        return render_template('login.html')
    


@app.route('/about',methods=['POST','GET'])
def abt():
    return render_template('abt.html')

@app.route('/ab',methods=['POST','GET'])
def addblog():
    if request.method=='POST':
        
        if request.form.get("se"):
            b=request.form['tit']
            c=request.form['sub']
            d=request.form['au']
            e=request.form['bc']
            f=request.form['gen']
            
            cur=mysql.connection.cursor()
            cur.execute("insert into blog2(tit, sub, au , bc,cat) values(%s,%s,%s,%s,%s)",(b,c,d,e,f))
            mysql.connection.commit()
            flash("blog submitted successfully")
            
            
            return redirect('/ab')
        if request.form.get("lo"):
            return redirect('/')
    else:
        return render_template('add.html')
    
    
        
    
@app.route('/ct',methods=['POST','GET'])
def ct():
   if request.method=='POST':
       if request.form.get("ct"):
                b=request.form['Name']
                c=request.form['Email']
                d=request.form['Message']
    
                cur=mysql.connection.cursor()
                cur.execute("insert into ct(nam,emal,msg) values(%s,%s,%s)",(b,c,d))
                mysql.connection.commit()
                flash("We Will Back To You Soon...")
                
                
                return redirect('/ct')
            
   else:
       return render_template('cont.html')
       

@app.errorhandler(404) 
def not_found(e):
    k=0
    d=request.url
    na=''
    for i in d[::-1]:
        na=na+i
        if i=='/':
            break
    num=na[::-1]
    cur=mysql.connection.cursor()
    cur.execute("select * from blog2 where cat like %s",(num[1:],))
    mysql.connection.commit()
    r=cur.fetchall()
    if len(r)==0:
        k=1
        cur=mysql.connection.cursor()
        cur.execute("select * from blog2 where uidd like %s",(num[1:],))
        mysql.connection.commit()
        r=cur.fetchall()
        
    return render_template("view.html",r=r,k=k)

 

if __name__ == '__main__':
    app.run()