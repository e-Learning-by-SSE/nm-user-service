from flask import Flask
from redis import Redis
import psycopg2
from flask_restx import Resource, Api
from ma import ma
from db import db
import connexion



redis = Redis(host='redis', port=6379)
#conn = psycopg2.connect(database="user",
#                        host="db",
#                        user="cw",
#                        password="cwpw",
#                        port="5432")
connex_app = connexion.App("__name__",specification_dir='./')
#read the swagger to configure the endpoints
connex_app.add_api('swagger.yml')

app = connex_app.app

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://cw:cwpw@db/user"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True




#@api.route('/hello')
#class HelloWorld1(Resource):
 #   def get(self):
 #       return {'hello': 'world'}

#@api.route('/showUser')
#class HelloWorld2(Resource):
 #   def get(self):
  #      redis.incr('hits')
   #     counter = str(redis.get('hits'),'utf-8')
    #    cursor = conn.cursor()
     #   cursor.execute("SELECT * FROM user_data WHERE id = 1")
      #  var1 = cursor.fetchone()
       # text = 'name ist {}'.format(var1[1])
        
        # return {'user': text}

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=8000, debug=True)
    


