from flask import*
from database import*

warden=Blueprint('warden',__name__)

@warden.route('/warden_home')
def warden_home():
  return render_template ('warden_home.html')


@warden.route('/warden_register_security_guard',methods=['get','post'])
def warden_register_security_guard():

    data={}
    a="select * from guard where  warden_id='%s'"%(session['warden'])
    data['view']=select(a)


    if 'set' in request.form:
        usnam=request.form['username']
        psw=request.form['password']
        finame=request.form['first_name']
        laname=request.form['last_name']
        pla=request.form['area']
        pho=request.form['phone_number']
        emai=request.form['email']

        quy4="insert into login values(null,'%s','%s','guard')"%(usnam,psw)
        a=insert(quy4)
        quy5="insert into guard values(null,'%s','%s','%s','%s','%s','%s','%s')"%(a,session['warden'],finame,laname,pla,pho,emai)
        b=insert(quy5)

        if b:
            return """<script>alert('Registration of successfully');window.location="/warden_home"</script>"""
        
    if 'action' in request.args:
        act=request.args['action']
        gr_id=request.args['g_id']

        


        if act == 'delete':
            qry="delete from guard where guard_id='%s'"%(gr_id)
            res=delete(qry)
            return """<script>alert('deletion of successfully');window.location="/warden_register_security_guard"</script>"""
        
        if act == 'update':
            qry="select * from guard where guard_id='%s'"%(gr_id)
            res=select(qry)
            data['up']=res

            if 'update' in request.form:
                finame=request.form['first_name']
                laname=request.form['last_name']
                pla=request.form['area']
                pho=request.form['phone_number']
                emai=request.form['email']

                qry="update guard set first_name='%s', last_name = '%s',place ='%s', phone = '%s',email = '%s' "%(finame,laname,pla,pho,emai)
                res=update(qry)
                return """<script>alert('updated of successfully');window.location="/warden_register_security_guard"</script>"""
    
    return render_template('warden_register_security_guard.html',data=data)





@warden.route('/warden_register_criminal',methods=['get','post'])
def warden_register_criminal():

    data={}
    a="select * from criminal_record where  warden_id='%s'"%(session['warden'])
    data['view']=select(a)


    if 'set' in request.form:
       
        crname=request.form['criminal_name']
        pla=request.form['area']
        cell=request.form['cell_no']
        det=request.form['detail']
        ver=request.form['verdict']
        sta=request.form['status']

        quy7="insert into criminal_record values(null,'%s','%s','%s','%s','%s','%s','%s')"%(session['warden'],crname,pla,cell,det,ver,sta)
        b=insert(quy7)

        if b:
            return """<script>alert('Registration of successfully');window.location="/warden_home"</script>"""
        
    if 'action' in request.args:
        act=request.args['action']
        gr_id=request.args['g_id']

        print("JJJJJJJJJJJJJJJJJ")


        if act == 'delete':
            qry="delete from criminal_record where record_id='%s'"%(gr_id)
            res=delete(qry)
            return """<script>alert('deletion of successfully');window.location="/warden_register_criminal"</script>"""
            
        if act == 'update':
            qry="select * from criminal_record where record_id='%s'"%(gr_id)
            res=select(qry)
            data['up']=res

            if 'update' in request.form:
                crname=request.form['first_name']
                pla=request.form['area']
                cell=request.form['cell_no']
                det=request.form['detail']
                ver=request.form['verdict']
                sta=request.form['status']
                

                qry="update criminal_record set criminal_name='%s', place = '%s',cell_no ='%s', details = '%s',verdict = '%s',status = '%s' where record_id='%s' "%(gr_id,crname,pla,cell,det,ver,sta)
                res=update(qry)
                return """<script>alert('updated of successfully');window.location="/warden_register_criminal"</script>"""

    return render_template('warden_register_criminal.html',data=data)






@warden.route('/warden_register_security_alert',methods=['get','post'])
def warden_register_security_alert():
    guard_id=request.args['g_id']
    data={}
    a="select * from alert"
    data['view']=select(a)

    if 'set' in request.form:
       
        des=request.form['description']
        da=request.form['date']
        ti=request.form['time']
        

        
        quy8="insert into alert values(null,'%s','%s','%s','%s','%s','pending')"%(session['warden'],guard_id,des,da,ti)
        b=insert(quy8)

        if b:
            return """<script>alert('Registration of successfully');window.location="/warden_register_security_guard"</script>"""
        
    if 'action' in request.args:
        act=request.args['action']
        alert_id=request.args['alert_id']

        print("JJJJJJJJJJJJJJJJJ")


        if act == 'delete':
            qry="delete from alert where alert_id='%s'"%(alert_id)
            res=delete(qry)
            return """<script>alert('deletion of successfully');window.location="warden_register_security_alert?g_id={guard_id}"</script>"""
            
        if act == 'update':
            qry="select * from alert where alert_id='%s'"%(alert_id)
            res=select(qry)
            data['up']=res

            print(data['up'],"YYYYYYYYYYYYYYYYYYYY")

            if 'update' in request.form:
                des=request.form['description']
                da=request.form['date']
                ti=request.form['time']        
                status=request.form['status']        
                qry="update alert set description='%s', date = '%s',time ='%s', status = '%s' where alert_id='%s' " %(des,da,ti,status,alert_id)
                res=update(qry)
                return """<script>alert('updated of successfully');window.location="/warden_register_security_alert?g_id={guard_id}"</script>"""

    return render_template('warden_register_security_alert.html',data=data,g_id=guard_id)
  

import uuid 

@warden.route('/warden_register_food_item',methods=['get','post'])
def warden_register_food_itemt():
    
    data={}
    a="select * from food_item"
    data['view']=select(a)

    if 'set' in request.form:

        item=request.form['item_name']
        img=request.files['img']

        path="static/"+str(uuid.uuid4())+img.filename
        img.save(path)

        des=request.form['description']
        sto=request.form['stock']
        am=request.form['amount']
                
        quy9="insert into food_item values(null,'%s','%s','%s','%s','%s','%s')"%(session['warden'],item,des,sto,am,path)
        b=insert(quy9)

        if b:
            return """<script>alert('Registration of successfully');window.location="/warden_home"</script>"""
        
    if 'action' in request.args:
        act=request.args['action']
        item_id=request.args['item_id']

        print("JJJJJJJJJJJJJJJJJ")


        if act == 'delete':
            qry="delete from food_item where item_id='%s'"%(item_id)
            res=delete(qry)
            return f"""<script>alert('deletion of successfully');window.location="warden_register_food_item?g_id={item_id}"</script>"""
            
        if act == 'update':
            qry="select * from food_item where item_id='%s'"%(item_id)
            res=select(qry)
            data['up']=res

            print(data['up'],"YYYYYYYYYYYYYYYYYYYY")

            if 'update' in request.form:
                item=request.form['item_name']
                des=request.form['description']
                sto=request.form['stock']
                am=request.form['amount']        
                qry="update food_item set item_name='%s', description = '%s',stock ='%s', amount = '%s' where item_id='%s' " %(item,des,sto,am)
                res=update(qry)
                return """<script>alert('updated of successfully');window.location="/warden_register_food_itemt?g_id={item_id}"</script>"""

    return render_template('warden_register_food_item.html',data=data)



@warden.route('/warden_view_purchase_report',methods=['post','get'])
def warden_view_purchase_report():
  data={}
  a="select * from purchase_details"
  data['view']=select(a)
    
  return render_template('warden_view_purchase_report.html',data=data)






@warden.route('/warden_register_delivery', methods=['GET', 'POST'])
def warden_register_delivery():
    data = {}

    
    if request.method == 'POST':
        if 'set' in request.form:
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            place = request.form['place']
            city = request.form['city']
            district = request.form['district']
            pincode = request.form['pincode']

            qry="insert into login values(null,'%s','%s','delivery')"%()
            res=insert(qry)




            
            insert_query = "INSERT INTO delivery VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                session['warden'], name, phone, email, place, city, district, pincode)
            insert_result = insert(insert_query)

            if insert_result:
                return """<script>alert('Registration successful');window.location='/warden_home'</script>"""

    if 'action' in request.args:
        action = request.args['action']
        w_id = request.args['w_id']

        if action == 'delete':
            delete_query = "DELETE FROM delivery WHERE delivery_id='%s'" % (w_id)
            delete(delete_query)
            return """<script>alert('Deletion successful');window.location='/warden_register_delivery'</script>"""

        elif action == 'update':
           
            select_query = "SELECT * FROM delivery WHERE delivery_id='%s'" % (w_id)
            data['up'] = select(select_query)

            if request.method == 'POST' and 'update' in request.form:
                name = request.form['name']
                email = request.form['email']
                phone = request.form['phone']
                place = request.form['place']
                city = request.form['city']
                district = request.form['district']
                pincode = request.form['pincode']

               
                update_query = """
                    UPDATE delivery SET name='%s', email='%s', phone='%s', place='%s',
                    city='%s', district='%s', pincode='%s' WHERE delivery_id='%s'
                """ % (name, email, phone, place, city, district, pincode, w_id)

                update(update_query)
                return """<script>alert('Update successful');window.location='/warden_register_delivery'</script>"""

    return render_template('warden_register_delivery.html', data=data)






@warden.route('/update_item',methods=['post','get'])
def update_item():

  id=request.args['id']
 
  

  if 'update' in request.form:    
      status=request.form['status']
      qry2="update purchase_details set status='%s' where purchase_id='%s'"%(status,id)
      update(qry2)
      return """<script>alert('updated successfully');window.location="/warden_view_purchase_report"</script>"""
    
  return render_template('warden_update_item.html')



from emotion import *


@warden.route('/emotion')
def emotion():

    a=detect_emotion()
    return """<script>alert('Session Stopped');window.location="/warden_home"</script>"""
  
