from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vendors_shops_menuitems.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)  # Ensure unique vendor names
    shops = db.relationship('Shop', backref='vendor', cascade="all, delete-orphan", lazy=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name}

class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    vendor_id = db.Column(db.Integer, nullable=False)
    menu_items = db.relationship('MenuItem', backref='shop', cascade="all, delete-orphan", lazy=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "vendor_id": self.vendor_id}

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    shop_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price, "shop_id": self.shop_id}

def create_tables():
    db.create_all()

@app.before_request
def before_request_func():
    if not hasattr(app, 'initialized'):
        create_tables()
        app.initialized = True

# Vendor endpoints
@app.route('/vendors', methods=['POST'])
def create_vendor():
    data = request.get_json()
    existing_vendor = Vendor.query.filter_by(name=data['name']).first()
    if existing_vendor:
        return jsonify({"error": "Vendor with this name already exists"}), 400
    new_vendor = Vendor(id=data['id'], name=data['name'])
    db.session.add(new_vendor)
    db.session.commit()
    return jsonify(new_vendor.to_dict()), 201

@app.route('/vendors', methods=['GET'])
def get_vendors():
    vendors = Vendor.query.all()
    return jsonify([vendor.to_dict() for vendor in vendors]), 200

@app.route('/vendors/<int:id>', methods=['GET'])
def get_vendor(id):
    vendor = Vendor.query.get(id)
    if vendor:
        return jsonify(vendor.to_dict()), 200
    return jsonify({"error": "Vendor not found"}), 404

@app.route('/vendors/<int:id>', methods=['PUT'])
def update_vendor(id):
    data = request.get_json()
    vendor = Vendor.query.get(id)
    if vendor:
        vendor.name = data['name']
        db.session.commit()
        return jsonify(vendor.to_dict()), 200
    return jsonify({"error": "Vendor not found"}), 404

@app.route('/vendors/<int:id>', methods=['DELETE'])
def delete_vendor(id):
    vendor = Vendor.query.get(id)
    if vendor:
        db.session.delete(vendor)
        db.session.commit()
        return '', 204
    return jsonify({"error": "Vendor not found"}), 404

# Shop endpoints
@app.route('/shops', methods=['POST'])
def create_shop():
    data = request.get_json()
    new_shop = Shop(id=data['id'], name=data['name'], vendor_id=data['vendor_id'])
    db.session.add(new_shop)
    db.session.commit()
    return jsonify(new_shop.to_dict()), 201

@app.route('/shops', methods=['GET'])
def get_shops():
    shops = Shop.query.all()
    return jsonify([shop.to_dict() for shop in shops]), 200

@app.route('/shops/<int:id>', methods=['GET'])
def get_shop(id):
    shop = Shop.query.get(id)
    if shop:
        return jsonify(shop.to_dict()), 200
    return jsonify({"error": "Shop not found"}), 404

@app.route('/shops/<int:id>', methods=['PUT'])
def update_shop(id):
    data = request.get_json()
    shop = Shop.query.get(id)
    if shop:
        shop.name = data['name']
        shop.vendor_id = data['vendor_id']
        db.session.commit()
        return jsonify(shop.to_dict()), 200
    return jsonify({"error": "Shop not found"}), 404

@app.route('/shops/<int:id>', methods=['DELETE'])
def delete_shop(id):
    shop = Shop.query.get(id)
    if shop:
        db.session.delete(shop)
        db.session.commit()
        return '', 204
    return jsonify({"error": "Shop not found"}), 404

# MenuItem endpoints
@app.route('/menuitems', methods=['POST'])
def create_menu_item():
    data = request.get_json()
    new_menu_item = MenuItem(id=data['id'], name=data['name'], price=data['price'], shop_id=data['shop_id'])
    db.session.add(new_menu_item)
    db.session.commit()
    return jsonify(new_menu_item.to_dict()), 201

@app.route('/menuitems', methods=['GET'])
def get_menu_items():
    menu_items = MenuItem.query.all()
    return jsonify([item.to_dict() for item in menu_items]), 200

@app.route('/menuitems/<int:id>', methods=['GET'])
def get_menu_item(id):
    menu_item = MenuItem.query.get(id)
    if menu_item:
        return jsonify(menu_item.to_dict()), 200
    return jsonify({"error": "MenuItem not found"}), 404

@app.route('/menuitems/<int:id>', methods=['PUT'])
def update_menu_item(id):
    data = request.get_json()
    menu_item = MenuItem.query.get(id)
    if menu_item:
        menu_item.name = data['name']
        menu_item.price = data['price']
        menu_item.shop_id = data['shop_id']
        db.session.commit()
        return jsonify(menu_item.to_dict()), 200
    return jsonify({"error": "MenuItem not found"}), 404

@app.route('/menuitems/<int:id>', methods=['DELETE'])
def delete_menu_item(id):
    menu_item = MenuItem.query.get(id)
    if menu_item:
        db.session.delete(menu_item)
        db.session.commit()
        return '', 204
    return jsonify({"error": "MenuItem not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

