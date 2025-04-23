from flask import*
from database import*

superintendent=Blueprint('superintendent',__name__)

@superintendent.route('/superintendent_home')
def superintendent_home():
  return render_template ('superintendent_home.html')


@superintendent.route('/superintendent_register_warden',methods=['get','post'])
def superintendent_register_warden():

    data={}
    a="select * from warden where  superintendent_id='%s'"%(session['superintendent'])
    data['view']=select(a)


    if 'set' in request.form:
        usnam=request.form['username']
        psw=request.form['password']
        finame=request.form['first_name']
        laname=request.form['last_name']
        pla=request.form['area']
        pho=request.form['phone_number']
        emai=request.form['email']

        quy2="insert into login values(null,'%s','%s','warden')"%(usnam,psw)
        a=insert(quy2)
        quy3="insert into warden values(null,'%s','%s','%s','%s','%s','%s','%s')"%(a,session['superintendent'],finame,laname,pla,pho,emai)
        b=insert(quy3)

        if b:
            return """<script>alert('Registration of successfully');window.location="/superintendent_home"</script>"""
        

    if 'action' in request.args:
        action=request.args['action']
        w_id=request.args['w_id']

        if action == 'delete':
            qry="delete from warden where warden_id='%s'"%(w_id)
            res=delete(qry)
            return """<script>alert('deletion of successfully');window.location="/superintendent_register_warden"</script>"""
        
        if action == 'update':
            qry="select * from warden where warden_id='%s'"%(w_id)
            res=select(qry)
            data['up']=res

            if 'update' in request.form:
                finame=request.form['first_name']
                laname=request.form['last_name']
                pla=request.form['area']
                pho=request.form['phone_number']
                emai=request.form['email']


                # print(finame,laname,pla,pho,emai)
                qry="update warden set first_name='%s', last_name = '%s',place ='%s', phone = '%s',email = '%s' "%(finame,laname,pla,pho,emai)
                res=update(qry)
                return """<script>alert('updated of successfully');window.location="/superintendent_register_warden"</script>"""
                # qry="update warden set last_name='%s',"%(laname)
                # qry="update warden set area='%s',"%(pla)
                # qry="update warden set phone_number='%s',"%(pho)
                # qry="update warden set email='%s',"%(emai)
                


        
    print(data,"NNNNNNNNNNNN")
    return render_template('superintendent_register_warden.html',data=data)



@superintendent.route('/superintendent_view_security_guard')
def superintendent_view_security_guard():
    data={}


    a="select * from guard"
    data['view']=select(a)
    return render_template('superintendent_view_security_guard.html',data=data)






@superintendent.route('/superintendent_view_criminal',methods=['post','get'])

def superintendent_view_criminal():
    data={}
    a="select * from criminal_record"
    data['view']=select(a)
    
    return render_template('superintendent_view_criminal.html',data=data)



@superintendent.route('/superintendent_view_report',methods=['post','get'])

def superintendent_view_report():
    data={}
    a="select * from report"
    data['view']=select(a)
    
    return render_template('superintendent_view_report.html',data=data)


@superintendent.route('/superintendent_view_food_item',methods=['post','get'])
def superintendent_view_food_item():
  data={}
  a="select * from food_item"
  data['view']=select(a)
    
  return render_template('superintendent_view_food_item.html',data=data)



@superintendent.route('/superindentent_view_purchase_detail',methods=['post','get'])
def superindentent_view_purchase_detail():
  data={}
  a="select * from purchase_details"
  data['view']=select(a)
    
  return render_template('superintendent_view_purchase_detail.html',data=data)