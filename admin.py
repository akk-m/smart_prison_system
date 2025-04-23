from flask import*
from database import*

admin=Blueprint('admin',__name__)


@admin.route('/admin_home')
 
def admin_home():
  return render_template ('admin_home.html')

@admin.route('/admin_register_superintendent',methods=['post','get'])

def admin_register_superintendent():

    data={}
    a="select * from superintendent"
    data['view']=select(a)


    if 'set' in request.form:
        usname=request.form['username']
        pswd=request.form['password']
        fname=request.form['first_name']
        lname=request.form['last_name']
        pl=request.form['area']
        ph=request.form['phone_number']
        ema=request.form['email']

        quy="insert into login values(null,'%s','%s','superintendent')"%(usname,pswd)
        a=insert(quy)
        quy1="insert into superintendent values(null,'%s','%s','%s','%s','%s','%s')"%(a,fname,lname,pl,ph,ema)
        b=insert(quy1)

        if b:
            return """<script>alert('Registration of successfully');window.location="/admin_home"</script>"""
    if 'action' in request.args:
        action=request.args['action']
        s_id=request.args['s_id']

        if action == 'delete':
            qry="delete from superintendent where superintendent_id='%s'"%(s_id)
            res=delete(qry)
            return """<script>alert('deletion of successfully');window.location="/admin_register_superintendent"</script>"""
        
        if action == 'update':
            qry="select * from superintendent where superintendent_id='%s'"%(s_id)
            res=select(qry)
            data['up']=res

            if 'update' in request.form:
                finame=request.form['first_name']
                laname=request.form['last_name']
                pla=request.form['area']
                pho=request.form['phone_number']
                emai=request.form['email']


                # print(finame,laname,pla,pho,emai)
                qry="update superintendent set first_name='%s', last_name = '%s',place ='%s', phone = '%s',email = '%s' where superintendent_id= '%s' "%(finame,laname,pla,pho,emai,s_id)
                res=update(qry)
                return """<script>alert('updated of successfully');window.location="/admin_register_superintendent"</script>"""




    return render_template('admin_register_superintendent.html',data=data)    



@admin.route('/admin_view_wardens',methods=['post','get'])

def admin_view_wardens():
    data={}
    a="select * from warden"
    data['view']=select(a)
    
    return render_template('admin_view_wardens.html',data=data)


@admin.route('/admin_view_security_guard',methods=['post','get'])

def admin_view_security_guard():
    data={}
    a="select * from guard"
    data['view']=select(a)
    
    return render_template('admin_view_security_guard.html',data=data)



@admin.route('/admin_view_complaint',methods=['post','get'])
def admin_view_complaint():
  data={}
  a="select * from complaint"
  data['view']=select(a)
    
  return render_template('admin_view_complaint.html',data=data)



@admin.route('/admin_send_reply',methods=['post','get'])
def admin_send_reply():
  id=request.args['id']
  if 'set' in request.form:
     sendrep=request.form['reply']

     qrt="update complaint set reply='%s' where complaint_id='%s'"%(sendrep,id)
     update(qrt)


  return render_template('admin_send_reply.html')




@admin.route('/admin_view_food_item',methods=['post','get'])
def admin_view_food_item():
  data={}
  a="select * from food_item"
  data['view']=select(a)
    
  return render_template('admin_view_food_item.html',data=data)


@admin.route('/admin_view_purchase_detail',methods=['post','get'])
def admin_view_purchase_detail():
  data={}
  a="select * from purchase_details"
  data['view']=select(a)
    
  return render_template('admin_view_purchase_detail.html',data=data)



@admin.route('/admin_view_criminal',methods=['post','get'])

def admin_view_criminal():
    data={}
    a="select * from criminal_record"
    data['view']=select(a)
    
    return render_template('admin_view_criminal.html',data=data)



@admin.route('/admin_view_report',methods=['post','get'])

def admin_view_report():
    data={}
    a="select * from report"
    data['view']=select(a)
    
    return render_template('admin_view_report.html',data=data)