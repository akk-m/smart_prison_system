from flask import*
from database import*
from public import*
from admin import*
from superintendent import*
from warden import*
from guard import*
from customers import*

app=Flask(__name__)

app.secret_key="sdfghj"

app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(superintendent)
app.register_blueprint(warden)
app.register_blueprint(guard)
app.register_blueprint(customers)

app.run(debug=True,port=5006)
