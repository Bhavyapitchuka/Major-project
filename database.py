import sqlite3
import hashlib
import datetime
import MySQLdb
from flask import session
from datetime import datetime

def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="root",
                            passwd="root", db="disease projection ml")
    c = _conn.cursor()

    return c, _conn

# -------------------------------Loginact-----------------------------------------------------------------


def admin_login(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from admin where Username='" +
                      username+"' and Password='"+password+"'")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))

def patient_login(id, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from patient where Pid='" +
                      id+"' and Password='"+password+"'")
        data = c.fetchall()              
        for a in data:              
            session['id'] = a[0]
        conn.close()
        return j
    except Exception as e:
        return(str(e))

def doctor_login(id, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from doctor where Did='" +
                      id+"' and    Password  ='"+password+"'")
        data = c.fetchall()              
        for a in data:              
            session['name'] = a[1]  
        conn.close()
        return j
    except Exception as e:
        return(str(e))

def patient_reg(id,name, email, phone, address,psw):
        c, conn = db_connect()
        print(id,name, email, phone, address,psw)
        j = c.execute("insert into patient (Pid, Pname,Email,Phone, Address,Password) values ('"+id+"','"+name+"','"+email+"','"+phone+"','"+address+"','"+psw+"')")
        conn.commit()
        conn.close()
        print(j)
        return j  

def doctor_reg(id,name, phone, email,  address,psw):
        c, conn = db_connect()
        print(id,name, email, phone, address,psw)
        j = c.execute("insert into doctor (Did,Dname,Dphone,Email,Address,Password) values ('"+id+"','"+name+"','"+phone+"','"+email+"','"+address+"','"+psw+"')")
        conn.commit()
        conn.close()
        print(j)
        return j 

def book_act(id,name, fee, dt, pid,  pname, cn ,cvv, tt):
        c, conn = db_connect()
        print(id,name, fee, dt, pid,  pname, cn ,cvv, tt)
        status = "pending"
        j = c.execute("insert into request (id,name, fee, dt, pid,  pname, cn ,cvv, tt, status) values ('"+id+"','"+name+"','"+fee+"','"+dt+"','"+pid+"','"+pname+"','"+cn+"','"+cvv+"','"+tt+"','"+status+"')")
        conn.commit()
        conn.close()
        print(j)
        return j 


def pmed_act(mname, price, f, name, id,  phone ,cn, cvv):
        c, conn = db_connect()
        print(mname, price, f, name, id,  phone ,cn, cvv)
        status = "pending"
        j = c.execute("insert into purchase (mname, price, f, name, id,  phone ,cn, cvv) values ('"+mname+"','"+price+"','"+f+"','"+name+"','"+id+"','"+phone+"','"+cn+"','"+cvv+"')")
        conn.commit()
        conn.close()
        print(j)
        return j 

def dp_add(did, doctor, pid, pname, pres):
        c, conn = db_connect()
        print(did, doctor, pid, pname, pres)
        status = "pending"
        j = c.execute("insert into dpres (did, doctor, pid, pname, pres) values ('"+did+"','"+doctor+"','"+pid+"','"+pname+"','"+pres+"')")
        conn.commit()
        conn.close()
        print(j)
        return j 

def med_act(tname, price,image):
        c, conn = db_connect()
        print(tname, price,image)
        status = "pending"
        j = c.execute("insert into medicene (tname, price,image, status) values ('"+tname+"','"+price+"','"+image+"','"+status+"')")
        conn.commit()
        conn.close()
        print(j)
        return j 

def add_symptoms(id,s1, s2, s3,  s4,s5,des):
        c, conn = db_connect()
        print(id, s1, s2,s3,s4,s5)
        now = datetime.now()
        dt  = now.strftime("%d/%m/%Y %H:%M:%S")
        j = c.execute("insert into patientsymptoms (Pid,symptom1,symptom2,symptom3,symptom4,symptom5,dt) values ('"+id+"','"+s1+"','"+s2+"','"+s3+"','"+s4+"','"+s5+"','"+des+"')")
        conn.commit()
        conn.close()
        print(j)
        return j 
def view_patient():
        c, conn = db_connect()
        c.execute("select * from request where status = 'pending' ")
        result=c.fetchall()
        conn.commit()
        conn.close()
        print(result)
        return result 

def view_p1(id):
        c, conn = db_connect()
        print(id)
        c.execute("select * from patientsymptoms where Pid='"+id+"'")
        result=c.fetchall()
        conn.commit()
        conn.close()
        print("yyyyyyyyyyyyyyyyy")
        print(result)
        return result     



def find_dis(s1,s2,s3):
    c, conn = db_connect()
    c.execute("select result from disease where  symptom1='"+s1+"' and symptom2='"+s2+"' and symptom3='"+s3+"'")
    result=c.fetchall()
    conn.commit()
    conn.close()
    print(result)
    return result

def add_bill(id, pres,  sugg,amount):
        c, conn = db_connect()
        print(id, pres,  sugg,amount)
        status='pending'
        j = c.execute("insert into billdetails (Pid,Prescription,Suggestion,amount,status) values ('"+id+"','"+pres+"','"+sugg+"','"+amount+"','"+status+"')")
        conn.commit()
        conn.close()
        print(j)
        return j


def accp(a, e,  f):
        c, conn = db_connect()
        print(a, e,  f)
        j = c.execute("update request set status='accepted' where id='"+a+"' and pid='"+e+"' ")
        conn.commit()
        conn.close()
        print(j)
        return j
    
def view_bill():
        c, conn = db_connect()
        no=session['id']
        print(no)
        c.execute("select * from billdetails where Pid='"+str(no)+"'")
        result=c.fetchall()
        conn.commit()
        conn.close()
        print("yyyyyyyyyyyyyyyyy")
        print(result)
        return result   

def payment_act(id):
    c, conn = db_connect()
    print("xxxxxxxxxxxxxxxxx")
    print(id)
    c.execute("select * from billdetails where Pid='"+id+"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result   

def docc():
    c, conn = db_connect()
    print("xxxxxxxxxxxxxxxxx")
    c.execute("select * from doctor")
    result = c.fetchall()
    conn.close()
    print("result")
    return result 


def status1():
    c, conn = db_connect()
    print("xxxxxxxxxxxxxxxxx")
    c.execute("select * from request")
    result = c.fetchall()
    conn.close()
    print("result")
    return result 

def pvmed():
    c, conn = db_connect()
    print("xxxxxxxxxxxxxxxxx")
    c.execute("select * from medicene")
    result = c.fetchall()
    conn.close()
    print("result")
    return result 

def pp_act():
    c, conn = db_connect()
    no=session['id']
    print("xxxxxxxxxxxxxxxxx")
    c.execute("select * from dpres where pid='"+str(no)+"' ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result 

def add_amount(id, amount,  tno,cvv):
        c, conn = db_connect()
        print(id, amount,  tno,cvv)
        status='paid'
        now = datetime.now()
        dt  = now.strftime("%d/%m/%Y %H:%M:%S")
        j = c.execute("insert into transcationdetails (Pid,amount, Tno, Cvv, dt,status) values ('"+id+"','"+amount+"','"+tno+"','"+cvv+"','"+dt+"','"+status+"')")
        j=c.execute("update billdetails set status='paid'where Pid='"+id+"'")
        conn.commit()
        conn.close()
        print(j)
        return j 

def upload_file(filename,file,username,pk,mk):
    c, conn = db_connect()
    c = conn.cursor()
    current_timestamp = str(datetime.datetime.now())
    name = file.filename
    data = file.read()
    privatekey = "No"
    c.execute("insert into file values(?,?,?,?,?,?,?,?)", (data,filename,current_timestamp,data.decode('utf-8'),username,"no","no","no"))
    conn.commit()
    conn.close()
    return True          

def viewbilltable():
    c, conn = db_connect()
    print("xxxxxxxxxxxxxxxxx")
    print(id)
    c.execute("select * from request")
    result = c.fetchall()
    conn.close()
    print("result")
    return result 


def ps1():
    c, conn = db_connect()
    print("xxxxxxxxxxxxxxxxx")
    c.execute("select * from patientsymptoms")
    result = c.fetchall()
    conn.close()
    print("result")
    return result 

def pmed1():
    c, conn = db_connect()
    print("xxxxxxxxxxxxxxxxx")
    print(id)
    c.execute("select * from purchase")
    result = c.fetchall()
    conn.close()
    print("result")
    return result 
# -------------------------------Registration-----------------------------------------------------------------





# ----------------------------------------------Update Items------------------------------------------


if __name__ == "__main__":
    print(db_connect())
