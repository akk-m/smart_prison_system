from flask import*
from database import*


public=Blueprint('public',__name__)

@public.route('/')
def homepage():
    return render_template('homepage.html')

@public.route('/login',methods=['post','get'])
def login():
    if 'enter' in request.form:
        uname=request.form['username']
        psw=request.form['password']

        q="select * from login where username='%s' and password='%s' "%(uname,psw)
        
        a=select(q)

        if a:
            session['login_id']=a[0]['login_id']

            if a[0]['usertype']=='admin':
                return redirect(url_for('admin.admin_home'))
            if a[0]['usertype']=='superintendent':
                qry="select * from superintendent where login_id='%s'"%(session['login_id'])
                res=select(qry)
                session['superintendent']=res[0]['superintendent_id']
                return redirect(url_for('superintendent.superintendent_home'))
            if a[0]['usertype']=='warden':
                qry="select * from warden where login_id='%s'"%(session['login_id'])
                res=select(qry)
                session['warden']=res[0]['warden_id']
                return redirect(url_for('warden.warden_home'))
            if a[0]['usertype']=='guard':
                qry="select * from guard where login_id='%s'"%(session['login_id'])
                res=select(qry)
                session['guard']=res[0]['guard_id']
                session['g_warden']=res[0]['warden_id']
                return redirect(url_for('guard.guard_home'))
            
            if a[0]['usertype']=='customers':
                qry="select * from customers where login_id='%s'"%(session['login_id'])
                res=select(qry)
                session['customer']=res[0]['customer_id']
                # session['g_warden']=res[0]['warden_id']
                return redirect(url_for('customers.customers_home'))
            
        else:
            return "<script>alert('Invalid username or password');window.location='/login'</script>"
            

            
    return render_template('login.html') 


# @public.route('/admin_register_superintendent',methods=['post','get'])

# def admin_register_superintendent():

#     data={}
#     a="select * from superintendent"
#     data['view']=select(a)


#     if 'set' in request.form:
#         usname=request.form['username']
#         pswd=request.form['password']
#         fname=request.form['first_name']
#         lname=request.form['last_name']
#         pl=request.form['area']
#         ph=request.form['phone_number']
#         ema=request.form['email']

#         quy="insert into login values(null,'%s','%s','superintendent')"%(usname,pswd)
#         a=insert(quy)
#         quy1="insert into superintendent values(null,'%s','%s','%s','%s','%s','%s')"%(a,fname,lname,pl,ph,ema)
#         b=insert(quy1)

#         if b:
#             return """<script>alert('Registration of successfully');window.location="/admin_home"</script>"""




#     return render_template('admin_register_superintendent.html',data=data)    
         



            

  
  



