import sqlite3
from flask import Flask, render_template, request, redirect, session, url_for

conn = sqlite3.connect("marks",check_same_thread=False)
cur = conn.cursor()
app = Flask(__name__)

@app.route('/index', methods=["GET","POST"])
@app.route("/", methods = ["GET","POST"])
def index():
        return render_template("index.html")


@app.route("/sdisplay", methods = ["POST"])
def sdisplay():
        usn2=request.form.get("usn")
        sem2=request.form.get("selectsem")
        #print(usn2,sem2)
        cur.execute("select * from marks where usn=? and sem= ?",(usn2,sem2))
        row1=cur.fetchall()
        x=len(row1)
        conn.commit()
        print(row1)
        return render_template("sdisplay.html",row1=row1,x=x)

    

@app.route("/logout", methods = ["GET","POST"])
def logout():
        return render_template("index.html")

@app.route("/reportform", methods = ["GET","POST"])
def reportform():
        return render_template("reportform.html")

@app.route("/report", methods = ["POST"])
def report():
        sem2=request.form.get("sem")
        sub2=request.form.get("selectsub")
        cur.execute("select ia1,ia2,ia3 from marks where sem=? and subname=?",(sem2,sub2))
        res=cur.fetchall()
        conn.commit()
        l = len(res)
        return render_template("report.html",sem2=sem2,sub2=sub2,res=res,l=l,)


@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "GET" :
        return render_template("login.html")

@app.route("/teacher", methods = ["GET","POST"])
def teacher():
    if request.method == "GET":
        return render_template("teacher.html")
    else:
        email=request.form.get("email")
        pwd=request.form.get("pwd")
        if email=="isebit@gmail.com" and pwd== "ise123":
            return render_template("teacher.html")
        else:
            flag1=1
            return render_template("login.html",flag1=flag1)
semg=0
subg=""
markg=""
tmarkg = ""
@app.route("/tdisplay", methods = ["POST"])
def tdisplay():
        global semg,subg,markg,tmarkg
        semg=request.form.get("sem")
        subg=request.form.get("selectsub")
        markg=request.form.get("mark")
        tmarkg = request.form.get("tmark")
        print(semg,subg,markg,tmarkg)
        return render_template("tdisplay.html",sem=semg,sub=subg,mark=markg,tmark=tmarkg)

@app.route("/teacher1", methods = ["GET","POST"])
def teacher1():
        print("hello")
        global semg,subg,markg,tmarkg
        for i in range(1,10):
            usn1="1BI16IS00"+str(i)
            sub1=subg
            sem1=semg
            mark1=markg
            mark2=request.form.get("1BI16IS00"+str(i))
            if mark2 is "" :
                break
            if tmarkg == "ta1":
                print("quiz")
                quiz=request.form.get("Q1BI16IS00"+str(i))
                if quiz is "" :
                    break
                print(type(quiz))
                quiz=int(quiz)
                mark2=int(mark2)
                mark2=int((mark2+quiz))/2
            else:
                mark2 = int(mark2)/2
            param=(usn1,sub1,sem1,mark2)
            #print(param)
            cur.execute("select * from marks where usn=? and subname=?",(usn1,sub1))
            rows=cur.fetchone()
            # print(rows)
            conn.commit()
            if rows == None:
                # print("hii")
                cur.execute("insert into marks (usn,subname,sem,"+mark1+") values(?,?,?,?)",param)
                conn.commit()
            else:
                print("hey")
                param1=(mark2,usn1,sub1)
                cur.execute("update marks set "+mark1+"= ? where usn=? and subname=?",param1)
                conn.commit()
        for i in range(10,21):
            usn1="1BI16IS0"+str(i)
            sub1=subg
            sem1=semg
            mark1=markg
            mark2=request.form.get("1BI16IS0"+str(i))
            if mark2 is "" :
                break
            if tmarkg == "ta1":
                quiz=request.form.get("Q1BI16IS0"+str(i))
                if quiz is "":
                    break
                quiz=int(quiz)
                mark2=int(mark2)
                mark2=int((mark2+quiz)/2)
            else:
                mark2=int(mark2)/2
            param=(usn1,sub1,sem1,mark2)
            if rows == None:
                # print("hii")
                cur.execute("insert into marks (usn,subname,sem,"+mark1+" ) values(?,?,?,?)",param)
                conn.commit()
            else:
                # print("hey")
                param1=(mark2,usn1,sub1)
                cur.execute("update marks set "+mark1+"= ? where usn=? and subname=?",param1)
                conn.commit()
        return render_template("teacher.html")


        #rf=request.form
        #print(rf)
        # usn=request.form.get("usn")
        # sem=request.form.get("selectsem")
        # sub=request.form.get("selectsub")
        # ia1=request.form.get("ia1")
        # ia2=request.form.get("ia2")
        # ia3=request.form.get("ia3")
        # #seme,subb=request.data()
        # param=(usn,sub,sem,ia1,ia2,ia3)
        # cur.execute("insert into marks (usn,subname,sem,ia1,ia2,ia3) values(?,?,?,?,?,?)", param)
        # conn.commit()
        # print(usn,ia1,ia2,ia3,sem,sub)
        # return render_template("teacher.html")
        

@app.route('/selectsem', methods=['GET'])
def selectsem():
    ret = ''
    print('hello')
    seme=request.args.get('semes')
    print(seme)
    cur.execute("select sub1,sub2,sub3,sub4,sub5,sub6,sub7,sub8 from semester where sem=?",(seme,))
    rows=cur.fetchall()
    conn.commit()
    print(rows)
    for entry in rows[0]:
         ret += '<option value=%s>%s</option>'%(entry,entry)
    print(ret)
    ret='<select name="selectsub" class="orderby" id="selectsub" style="border-radius:10px">'+ret+'</select>'
    return ret

# @app.route('/sem1', methods=['GET'])
# def sem1():
#     ret1 = ''
#     #print('hello')
#     seme1=request.args.get('semes1')
#     #print(seme)
#     cur.execute("select * from semester where sem=?",(seme1))
#     rows1=cur.fetchall()
#     conn.commit()
#     print(rows1)
#     for entry1 in rows1[0]:
#          ret1 += '<option value=%s>%s</option>'%(entry1,entry1)
#     print(ret1)
#     ret1='<select name="sem1" class="orderby" id="sem1">'+ret1+'</select>'
#     return ret1

if __name__ == '__main__' :
    app.run(debug=True)