from flask import*
from database import*

guard=Blueprint('guard',__name__)

@guard.route('/guard_home')
def guard_home():
  return render_template ('guard_home.html')


@guard.route('/guard_view_security_alert',methods=['post','get'])
def guard_view_security_alert():
  data={}
  a="select * from alert"
  data['view']=select(a)

  if 'action' in request.args:
    action=request.args['action']
    alert_id=request.args['alert_id']
  else:
    action=None
  

  if 'action' == 'update':
          qry="select * from alert where alert_id='%s'"%(alert_id)
          res=select(qry)
          data['up']=res

  if 'update' in request.form:
      status=request.form['status']
      qry2="update alert set status='%s' where alert_id='%s'"%(status,alert_id)
      update(qry2)
    # return """<script>alert('Registration of successfully');window.location="/guard_home"</script>"""
    
  return render_template('guard_view_security_alert.html',data=data)




@guard.route('/update_alert',methods=['post','get'])
def update_alert():

  id=request.args['id']
 
  

  if 'update' in request.form:    
      status=request.form['status']
      qry2="update alert set status='%s' where alert_id='%s'"%(status,id)
      update(qry2)
      return """<script>alert('updated successfully');window.location="/guard_view_security_alert"</script>"""
    
  return render_template('guard_update_alert_status.html')


@guard.route('/guard_add_report',methods=['get','post'])
def guard_add_reportt():
    
    data={}
    a="select * from report"
    data['view']=select(a)

    if 'set' in request.form:
        
        # gua=request.form['guard_id']
        det=request.form['details']
        da=request.form['date']
        
        

        
        quy9="insert into report values(null,'%s','%s','%s')"%(session['guard'],det,da)
        b=insert(quy9)

        if b:
            return """<script>alert('Added of successfully');window.location="/guard_add_report"</script>"""
        
    if 'action' in request.args:
        act=request.args['action']
        report_id=request.args['id']

        print("JJJJJJJJJJJJJJJJJ")


        if act == 'delete':
            qry="delete from report where report_id='%s'"%(report_id)
            res=delete(qry)
            return """<script>alert('deletion of successfully');window.location="guard_add_report"</script>"""
            
        if act == 'update':
            qry="select * from report where report_id='%s'"%(report_id)
            res=select(qry)
            data['up']=res

            print(data['up'],"YYYYYYYYYYYYYYYYYYYY")

            if 'update' in request.form:
                
                det=request.form['details']
                da=request.form['date']               
                qry="update report set  details='%s', date = '%s'" %(det,da)
                res=update(qry)
                return """<script>alert('updated of successfully');window.location="/guard_add_report"</script>"""

    return render_template('guard_add_report.html',data=data)





@guard.route('/guard_view_food_item',methods=['post','get'])
def guard_view_food_item():
  data={}
  a="select * from food_item"
  data['view']=select(a)
  return render_template('guard_view_food_item.html',data=data)

