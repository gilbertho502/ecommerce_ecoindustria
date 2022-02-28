from app import app

from app.models import Users, product_category, Products, Proveedores #, Orders, OrderProduct, UserAddress #, Payment
from flask_marshmallow import Marshmallow

ma=Marshmallow(app)

class UserSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Users
        fields=('id','user_name','password', 'first_name','last_name','phone_number', 'mail')
        
user_schema=UserSerializer()
users_schema=UserSerializer(many=True)        


class CategoriaSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        # model=product_category
        model = product_category
        fields=('id_category','name','description')
        
categoria_schema=CategoriaSerializer()
categorias_schema=CategoriaSerializer(many=True)  

class ProductosSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Products
        fields=('id_producto','name','description','category_id','category','price','discount', 'photo_1','photo_2','photo_3' )
        
producto_schema=ProductosSerializer()
productos_schema=ProductosSerializer(many=True)

class ProveedoresSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Proveedores
        fields=('id','first_name','last_name', 'phone_number', 'mail', 'opinion')

proveedor_schema= ProveedoresSerializer()
proveedores_schema = ProveedoresSerializer(many=True)

# class OrderSerializer(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Orders
#         fields= ('id', 'user_id', 'user', 'order_num', 'delivery_date')

# order_schema = OrderSerializer()
# orders_schema = OrderSerializer(many=True)


# class OrderProductSerializer(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = OrderProduct
#         fields=('id','order_id','order','product_id','product', 'quantity')

# orderproduct_schema = OrderProductSerializer()
# orderproducts_schema = OrderProductSerializer(many=True)


# class UserAddressSerializer(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model= UserAddress
#         fields = ('id_user_address','user_id','user','address_place1','address_place2','zipcode','country','town', 'phone')

# UserAddress_schema = UserAddressSerializer()
# UserAddresses_schema = UserAddressSerializer(many = True)


# class PaymentSerializer(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Payment
#         fields = ('id', 'order_id', 'order', 'paymant_date', 'paymant_type')

# Payment_schema = PaymentSerializer()
# Payments_schema = PaymentSerializer(many = True)