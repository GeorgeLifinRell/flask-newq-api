
## Running the Application

Navigate to your project directory.
Install the dependencies:
sh
Copy code
pip install -r requirements.txt
Run the Flask application:
sh
Copy code
python app.py
Endpoints
Vendors
Create a new vendor: POST /vendors

Request body: {"name": "vendor_name"}
Response: 201 Created with the created vendor object.
Get all vendors: GET /vendors

Response: 200 OK with a list of all vendors.
Get a specific vendor by ID: GET /vendors/<id>

Response: 200 OK with the vendor object, or 404 Not Found if the ID does not exist.
Update a vendor by ID: PUT /vendors/<id>

Request body: {"name": "new_vendor_name"}
Response: 200 OK with the updated vendor object, or 404 Not Found if the ID does not exist.
Delete a vendor by ID: DELETE /vendors/<id>

Response: 204 No Content if the deletion is successful, or 404 Not Found if the ID does not exist.
Shops
Create a new shop: POST /shops

Request body: {"name": "shop_name", "vendor_id": vendor_id}
Response: 201 Created with the created shop object.
Get all shops: GET /shops

Response: 200 OK with a list of all shops.
Get a specific shop by ID: GET /shops/<id>

Response: 200 OK with the shop object, or 404 Not Found if the ID does not exist.
Update a shop by ID: PUT /shops/<id>

Request body: {"name": "new_shop_name", "vendor_id": new_vendor_id}
Response: 200 OK with the updated shop object, or 404 Not Found if the ID does not exist.
Delete a shop by ID: DELETE /shops/<id>

Response: 204 No Content if the deletion is successful, or 404 Not Found if the ID does not exist.
MenuItems
Create a new menu item: POST /menuitems

Request body: {"name": "item_name", "price": item_price, "shop_id": shop_id}
Response: 201 Created with the created menu item object.
Get all menu items: GET /menuitems

Response: 200 OK with a list of all menu items.
Get a specific menu item by ID: GET /menuitems/<id>

Response: 200 OK with the menu item object, or 404 Not Found if the ID does not exist.
Update a menu item by ID: PUT /menuitems/<id>

Request body: {"name": "new_item_name", "price": new_item_price, "shop_id": new_shop_id}
Response: 200 OK with the updated menu item object, or 404 Not Found if the ID does not exist.
Delete a menu item by ID: DELETE /menuitems/<id>

Response: 204 No Content if the deletion is successful, or 404 Not Found if the ID does not exist.