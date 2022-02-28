from app import db

'''    
class users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(15))
    password=db.Column(db.String(25))
    first_name=db.Column(db.String(15))
    last_name=db.Column(db.String(15))
    phone_number=db.Column(db.String(20))
    mail = db.Column(db.String(100))
    photo_user = db.Column(db.String(120))

'''  
class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True, autoincrement=True)
    user_name=db.Column(db.String(15), unique=True)
    password=db.Column(db.String(25))
    first_name=db.Column(db.String(15))
    last_name=db.Column(db.String(15))
    phone_number=db.Column(db.String(20))
    mail = db.Column(db.String(100), unique=True)
    
    # def __repr__(self):
    #     return self.username


class product_category(db.Model):
    id_category=db.Column(db.Integer,primary_key=True, autoincrement=True)
    name=db.Column(db.String(23))
    description=db.Column(db.String(250))
    items = db.relationship('Products', backref='product_category', lazy='dynamic')
    
    # def __repr__(self):
    #     return self.name

class Products(db.Model):
    id_product=db.Column(db.Integer,primary_key=True, autoincrement=True)
    name=db.Column(db.String(50))
    description=db.Column(db.Text)    
    category_id=db.Column(db.Integer,db.ForeignKey('product_category.id_category'))
    # category =db.relationship('ProductCategory', backref='Products')
    price=db.Column(db.Float)
    discount=db.Column(db.Integer)
    photo_1 = db.Column(db.String(180))
    photo_2 = db.Column(db.String(180))
    photo_3 = db.Column(db.String(180))

    # def __repr__(self):
    #     return self.name

class Proveedores(db.Model):
    id=db.Column(db.Integer,primary_key=True, autoincrement=True)
    first_name=db.Column(db.String(15))
    last_name=db.Column(db.String(15))
    phone_number=db.Column(db.String(20))
    mail = db.Column(db.String(100), unique=True)
    opinion =db.Column(db.Text)

# class Orders(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
#     user =db.relationship('Users', backref='users_orders')
#     order_num = db.Column(db.String(50), unique=True)
#     delivery_date = db.Column(db.Date)

#     # def __repr__(self):
#     #     return self.order_num


# class OrderProduct(db.Model):
#     id = db.Column(db.Integer, primary_key= True, autoincrement=True)
#     order_id = db.Column(db.Integer, db.ForeignKey('Orders.id'))
#     order =db.relationship('Orders', backref='order_order_products')
#     product_id = db.Column(db.Integer, db.ForeignKey('Products.id'))
#     product = db.relationship('Products', backref='product_order_products')
#     quantity = db.Column(db.Integer)

#     # def __repr__(self):
#     #     return f'{self.order.user.username} - {self.product.name}' 

# class UserAddress(db.Model):
#     id_user_address = db.Column(db.Integer, primary_key= True, autoincrement=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
#     user =db.relationship('Users', backref='user_user_addresses')
#     address_place1 = db.Column(db.String(150))
#     address_place2 = db.Column(db.String(150))
#     zipcode = db.Column(db.String(150))
#     country = db.Column(db.String(50))
#     town = db.Column(db.String(50))
#     phone = db.Column(db.Integer)

    # def __repr__(self):
    #     return self.user.username

# class Payment(db.Model):
#     id_payment = db.Column(db.Integer, primary_key= True, autoincrement=True)
#     order_id = db.Column(db.Integer, db.ForeignKey('Orders.id'))
#     order =db.relationship('Orders', backref='order_payments')
#     paymant_date = db.Column(db.Date)
#     payment_type = db.Column(db.String(20))

    # def __repr__(self):
    #     return self.order.order_id