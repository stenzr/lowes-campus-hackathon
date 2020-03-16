from flask import Flask,request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import re
#from flask_marshmallow import Marshmallow
#from flask_migrate import Migrate
import os


# Init app
app = Flask(__name__)
api = Api(app)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'lowesProductDatabase.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init ma
# ma = Marshmallow(app)

# Init migrate
# migrate = Migrate(app, db)

# Create a SQLAlchemy orm from existing database tables
db.Model.metadata.reflect(db.engine)

# Tables in database  >> models in SQLAlchemy
class SubcategoryAisleArrangement(db.Model):
    __tablename__ = 'subcategoryAisleArrangements'
    __table_args__ = {'extend_existing' : True }
    subCatId = db.Column(db.Text, primary_key=True)

    def __repr__(self):
        return 'product subCategory: {}, aisle: {}'.format(self.subCategory, self.aisle)


class SubcategoryProducts(db.Model):
    __tablename__ = 'subcategoryProducts'
    __table_args__ = {'extend_existing' : True }
    productId = db.Column(db.Text, primary_key=True)

    def __repr__(self):
        return 'productName: {}, subCategory: {}'.format(self.productName, self.subCategory)



# Endpoint Class
class Root(Resource):
   def get(self):  
        """
        root endpoint of the api
        """        
        return jsonify({"endpoint1" : "i am the root",
                "endpoint2" : "/get_aisle/",
                "endpoint3" : "/get_optimal_path/",
                "endpoint4" : "/get_product_details/"
            })

class Get_product_location_detail(Resource):
    def get(self):
        return(jsonify({'endpoint task': 'send a product name to get its complete location detail in the store'}))

    def post(self):
        json_post = request.get_json()
        if len(json_post['product']) == 0:
            return jsonify({'Product' : 'no product to search'})

        else:
            product = json_post['product']
            response = {'Product' : product}
 
            try:
                SubCategory = SubcategoryProducts.query.filter(func.lower(SubcategoryProducts.productName) == product.lower()).first().subCategory
                aisle_number = SubcategoryAisleArrangement.query.filter_by(subCategory=SubCategory).first().aisle
                department_ = SubcategoryAisleArrangement.query.filter_by(subCategory=SubCategory).first().department

            except Exception:
                aisle_number = "Product not found or Incorrect Product"
                SubCategory = "Product not found or Incorrect Product"
                department_ = "Product not found or Incorrect Product"

            response.update({'aisle': aisle_number})
            response.update({'sub_category': SubCategory})
            response.update({'department': department_})


        return jsonify(response) 


        

class Get_aisle(Resource):
    def get(self):
        return jsonify({'endpoint task' : 'send a list of products to get the respective aisle numbers, <br> the list should begin with the number of products'})
    
    def post(self):
        json_post = request.get_json()

        if (json_post['length']) == '0':
            return jsonify({'Products' : 'no product to search'})

        else:
            number_of_products = int(json_post['length'])
            response = {'Products' : 'Aisle Numbers'}
            for i in range(1, number_of_products+1, 1):
                product = json_post['product{}'.format(i)]

                try:
                    SubCategory = SubcategoryProducts.query.filter(func.lower(SubcategoryProducts.productName) == product.lower()).first().subCategory
                    aisle_number = SubcategoryAisleArrangement.query.filter_by(subCategory=SubCategory).first().aisle
                except Exception:
                    aisle_number = "Product not found or Incorrect Product"

                try:
                    SubCategory = SubcategoryProducts.query.filter(func.lower(SubcategoryProducts.productName) == product.lower()).first().subCategory
                    aisle_number = SubcategoryAisleArrangement.query.filter_by(subCategory=SubCategory).first().aisle
                except Exception:
                    aisle_number = "Product not found or Incorrect Product"

                response.update({product : aisle_number})

        
        return jsonify(response)   


class Get_optimal_route(Resource):
    def get(self):
        return jsonify({'endpoint task' : 'send a list of aisle numbers to get the optimal path <br> the list should begin with the number of aisles required to visit'})
    
    def post(self):
        json_post = request.get_json()

        if (json_post['number_of_aisles']) == '0':
            return jsonify({'Route' : 'no aisles to visit'})

        else:
            number_of_aisles = int(json_post['length'])
            response = {'Route' : 'Path to be taken'}






        return jsonify(response)


# Api endpoints
api.add_resource(Root,'/')
api.add_resource(Get_aisle, '/get_aisle/')
api.add_resource(Get_optimal_route, '/get_optimal_path/')
api.add_resource(Get_product_location_detail, '/get_product_details/')


# Run Server
if __name__ == '__main__':
    #creating a server
    #set debug=False on production
    app.run(host='0.0.0.0', debug=False)


