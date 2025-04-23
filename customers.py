from flask import*
from database import*

customers=Blueprint('customers',__name__)

@customers.route('/customers_home')
def customers_home():
  return render_template ('customers_home.html')



@customers.route('/customers_register_user',methods=['post','get'])

def customers_register_user():

    data={}
    a="select * from customers"
    data['view']=select(a)


    if 'set' in request.form:
        usname=request.form['username']
        pswd=request.form['password']
        fname=request.form['first_name']
        lname=request.form['last_name']
        pl=request.form['place']
        ph=request.form['phone']
        ema=request.form['email']
        ads=request.form['address']

        quy="insert into login values(null,'%s','%s','customers')"%(usname,pswd)
        a=insert(quy)
        quy10="insert into customers values(null,'%s','%s','%s','%s','%s','%s','%s')"%(a,fname,lname,pl,ph,ema,ads)
        b=insert(quy10)

        if b:
            return """<script>alert('Registration of successfully');window.location="/customers_home"</script>"""
        

    return render_template("customers_register_user.html",data=data)


@customers.route('/customers_send_complaint', methods=['POST', 'GET'])
def customers_send_complaint():
    if 'submit_complaint' in request.form:
        complaint_text = request.form['complaint']
        quy = "INSERT INTO complaint VALUES (null,'%s', '%s', 'pending', curdate())" % (session['customer'],complaint_text)
        insert(quy)


    data={}
    
    return render_template("customers_send_complaint.html")



@customers.route('/customers_view_reply', methods=['POST', 'GET'])
def customers_view_reply():
    data = {}
    customer_id = session.get('customer')  # Assuming customer is logged in
    print(session['customer'])
    query = "SELECT * FROM complaint WHERE sender_id='%s'" % (session['customer'])
    data['view'] = select(query)


    print(data,"MMMMMMMMMMMMM")

    return render_template('customers_view_reply.html', data=data)



@customers.route('/customers_view_food_item',methods=['post','get'])
def customers_view_food_item():
  data={}
  a="select * from food_item"
  data['view']=select(a)
  return render_template('customers_view_food_item.html',data=data)



@customers.route('/customers_purchase_item',methods=['post','get'])
def customers_purchase_item():
  # data={}
  # a="select * from purchase_details where customer_id='%s'"%(session['customer'])
  # data['cart']=select(a)

  id=request.args['id']
  amount=request.args['amount']

  if 'submit' in request.form:
    qua=request.form['q'] 

    total=int(amount)*int(qua)
    a="insert into purchase_details values(null,'%s','%s','%s','%s','purchased')"%(session['customer'],id,qua,total)
    insert(a)
    if a:
      return """<script>alert('Purchsed successfully');window.location="/customers_home"</script>"""
  return render_template('customers_purchase_item.html')




@customers.route('/customers_view_order')
def customers_view_order():
  data={}
  a="SELECT * FROM purchase_details INNER JOIN food_item USING(item_id) where customer_id='%s'"%(session['customer'])
  b=select(a)
  data['view']=b
  

  return render_template('customers_view_order.html',data=data)




@customers.route('/customers_register_delivery', methods=['GET', 'POST'])
def customers_register_delivery():
    data = {}

    # Fetch existing delivery data for logged-in user
    query = "SELECT * FROM delivery WHERE delivery_id='%s'" % (session['customers'])
    data['view'] = select(query)

    if request.method == 'POST':
        if 'set' in request.form:
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            place = request.form['place']
            city = request.form['city']
            district = request.form['district']
            pincode = request.form['pincode']

            # Insert new delivery record
            insert_query = "INSERT INTO delivery VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                session['customers'], name, phone, email, place, city, district, pincode
            )
            insert_result = insert(insert_query)

            if insert_result:
                return """<script>alert('Registration successful');window.location='/customers_home'</script>"""

    # Check for action in request arguments
    if 'action' in request.args:
        action = request.args['action']
        c_id = request.args['c_id']

        if action == 'delete':
            delete_query = "DELETE FROM delivery WHERE delivery_id='%s'" % (c_id)
            delete(delete_query)
            return """<script>alert('Deletion successful');window.location='/customers_register_delivery'</script>"""

        elif action == 'update':
            # Fetch user details for update
            select_query = "SELECT * FROM delivery WHERE delivery_id='%s'" % (c_id)
            data['up'] = select(select_query)

            if request.method == 'POST' and 'update' in request.form:
                name = request.form['name']
                email = request.form['email']
                phone = request.form['phone']
                place = request.form['place']
                city = request.form['city']
                district = request.form['district']
                pincode = request.form['pincode']

                # Update user details
                update_query = """
                    UPDATE delivery SET name='%s', email='%s', phone='%s', place='%s',
                    city='%s', district='%s', pincode='%s' WHERE delivery_id='%s'
                """ % (name, email, phone, place, city, district, pincode, c_id)

                update(update_query)
                return """<script>alert('Update successful');window.location='/customers_register_delivery'</script>"""

    return render_template('customers_register_delivery.html', data=data)
