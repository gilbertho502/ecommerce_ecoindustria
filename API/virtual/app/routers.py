from flask import redirect, render_template, request, flash, url_for, make_response, jsonify
from app import app, db
from app.models import Users, product_category, Products, Proveedores
from app.serializers import user_schema, users_schema, categoria_schema, categorias_schema, producto_schema, productos_schema, proveedor_schema, proveedores_schema
from flask_cors import cross_origin


@app.route('/')
def index():
    template_name="index.html"
    #usuarios=users.query.all()
    return render_template(template_name)#,usuarios=usuarios)
      

@cross_origin
@app.route('/autenticar/<uname>/<passw>',methods=["POST"])
def autenticar(uname,passw):
    login=Users.query.filter_by(user_name=uname,password=passw).first()
    result=user_schema.dump(login)
    if login is not None:
        data ={
            'message':'Bienvenido',
            'status':200,
            'data':result
        }
    else:
        data ={
            'message':'Error',
            'status':200
            
        }
    return make_response(jsonify(data))  

@cross_origin
@app.route("/autenticar",methods=["GET","POST"])
def login():
    if request.method=="POST":
        mail=request.json["mail"]
        passw=request.json["passw"]
        login=Users.query.filter_by(mail=mail,password=passw).first()
        result=user_schema.dump(login)
        if login is not None:
            data ={
            'message':'Bienvenido',
            'status':200,
            'data':result
        }
        else:
            data ={
            'message':'Error de credenciales',
            'status': 404
        }
    return make_response(jsonify(data)) 


@cross_origin
@app.route("/add_usuarios",methods=["POST"])
def add_usuarios():
    uname=request.json['uname']
    passw=request.json['passw']
    first_name=request.json['first_name']
    last_name=request.json['last_name']
    phone_number=request.json['phone_number']
    mail = request.json['mail']
    new_usuario=Users(user_name=uname,password=passw,first_name=first_name,last_name=last_name,phone_number=phone_number, mail=mail)
    db.session.add(new_usuario)
    db.session.commit()
    result=user_schema.dump(new_usuario)
    data ={
            'message':'Se Registro el usuario con exito',
            'status':200,
            'data':result
        }
    return make_response(jsonify(data))
    

@cross_origin
@app.route("/add_proveedor",methods=["POST"])
def add_proveedor():
    first_name=request.json['first_name']
    last_name=request.json['last_name']
    phone_number=request.json['phone_number']
    mail = request.json['mail']
    opinion = request.json['opinion']
    new_prov=Proveedores(first_name=first_name,last_name=last_name,phone_number=phone_number, mail=mail,opinion=opinion)
    db.session.add(new_prov)
    db.session.commit()
    result=proveedor_schema.dump(new_prov)
    data ={
            'message':'Proveedor agregado',
            'status':200,
            'data':result
        }
    return make_response(jsonify(data))


@cross_origin
@app.route("/listar_usuarios",methods=["GET"])
def listar_usuarios():
    usuarios=Users.query.all()
    result=users_schema.dump(usuarios)
    data={
        'message':'Todas mis usuarios',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))


@cross_origin
@app.route("/productos", methods=["GET"])
def productos():
    productos=Products.query.all()
    result = productos_schema.dump(productos)
    data={
        "message": "Todos los productos",
        "status": 200,
        "data": result
    }
    return make_response(jsonify(data))

#listar proveedores
@cross_origin
@app.route("/listar_proveedores",methods=["GET"])
def listar_proveedores():
    proveedores=Proveedores.query.all()
    result=proveedores_schema.dump(proveedores)
    data={
        'message':'Todas nuestros proveedores',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))


@cross_origin
@app.route("/product/<id>", methods=["GET"])
def product(id):
    producto=Products.query.get(id)
    if producto:
        result = producto_schema.dump(producto)
        data= {
            "message": 'Detalles',
            "status": 200,
            "data": result
        }
    else:
        data={
            "message": "Producto no encontrado",
            "status": 404
        }
    return make_response(jsonify(data))

@cross_origin
@app.route('/category_product/<int:id_category>', methods=['GET'])
def category_product(id_category):
    #selecciona una categoria en especifico
    cate_product =product_category.query.get(id_category)
    return jsonify(id_category=cate_product.id_category, name=cate_product.name, 
                description=cate_product.description,
                items=[dict(id_product=item.id,
        name=item.name, description=item.description, category_id=item.category_id, price=item.price, discount=item.discount, photo_1=item.photo_1, photo_2=item.photo_2, photo_3=item.photo_3) for item in
        cate_product.items])
            
@cross_origin
@app.route('/moda', methods=['GET'])
def listar_moda(id_category = 20):
    #selecciona una categoria en especifico
    cate_product =product_category.query.get(id_category)
    return jsonify(id_category=cate_product.id_category, name=cate_product.name, 
                description=cate_product.description,
                items=[dict(id_product=item.id_product,
        name=item.name, description=item.description, category_id=item.category_id, price=item.price, discount=item.discount, photo_1=item.photo_1, photo_2=item.photo_2, photo_3=item.photo_3) for item in
        cate_product.items])
        

@cross_origin
@app.route('/hogar', methods=['GET'])
def listar_hogar(id_category = 30):
    #selecciona una categoria en especifico
    cate_product =product_category.query.get(id_category)
    return jsonify(id_category=cate_product.id_category, name=cate_product.name, 
                description=cate_product.description,
                items=[dict(id_product=item.id_product,
        name=item.name, description=item.description, category_id=item.category_id, price=item.price, discount=item.discount, photo_1=item.photo_1, photo_2=item.photo_2, photo_3=item.photo_3) for item in
        cate_product.items])
        

@cross_origin
@app.route('/alimentacion', methods=['GET'])
def listar_alimentacion(id_category = 10):
    #selecciona una categoria en especifico
    cate_product =product_category.query.get(id_category)
    return jsonify(id_category=cate_product.id_category, name=cate_product.name, 
                description=cate_product.description,
                items=[dict(id_product=item.id_product,
        name=item.name, description=item.description, category_id=item.category_id, price=item.price, discount=item.discount, photo_1=item.photo_1, photo_2=item.photo_2, photo_3=item.photo_3) for item in
        cate_product.items])
        
