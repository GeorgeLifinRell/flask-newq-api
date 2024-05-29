Sure! Here are the `curl` commands to interact with each endpoint:

### Vendor Endpoints

#### 1. Create a New Vendor
```bash
curl -X POST http://localhost:5000/vendors -H "Content-Type: application/json" -d '{"id": 1, "name": "Vendor 1"}'
```

#### 2. Get All Vendors
```bash
curl -X GET http://localhost:5000/vendors
```

#### 3. Get a Specific Vendor by ID
```bash
curl -X GET http://localhost:5000/vendors/1
```

#### 4. Update a Vendor by ID
```bash
curl -X PUT http://localhost:5000/vendors/1 -H "Content-Type: application/json" -d '{"name": "Vendor 1 Updated"}'
```

#### 5. Delete a Vendor by ID
```bash
curl -X DELETE http://localhost:5000/vendors/1
```

### Shop Endpoints

#### 6. Create a New Shop
```bash
curl -X POST http://localhost:5000/shops -H "Content-Type: application/json" -d '{"id": 1, "name": "Shop 1", "vendor_id": 1}'
```

#### 7. Get All Shops
```bash
curl -X GET http://localhost:5000/shops
```

#### 8. Get a Specific Shop by ID
```bash
curl -X GET http://localhost:5000/shops/1
```

#### 9. Update a Shop by ID
```bash
curl -X PUT http://localhost:5000/shops/1 -H "Content-Type: application/json" -d '{"name": "Shop 1 Updated", "vendor_id": 1}'
```

#### 10. Delete a Shop by ID
```bash
curl -X DELETE http://localhost:5000/shops/1
```

### MenuItem Endpoints

#### 11. Create a New Menu Item
```bash
curl -X POST http://localhost:5000/menuitems -H "Content-Type: application/json" -d '{"id": 1, "name": "Item 1", "price": 9.99, "shop_id": 1}'
```

#### 12. Get All Menu Items
```bash
curl -X GET http://localhost:5000/menuitems
```

#### 13. Get a Specific Menu Item by ID
```bash
curl -X GET http://localhost:5000/menuitems/1
```

#### 14. Update a Menu Item by ID
```bash
curl -X PUT http://localhost:5000/menuitems/1 -H "Content-Type: application/json" -d '{"name": "Item 1 Updated", "price": 11.99, "shop_id": 1}'
```

#### 15. Delete a Menu Item by ID
```bash
curl -X DELETE http://localhost:5000/menuitems/1
```

Ensure to replace `localhost:5000` with the appropriate host and port if your server is running elsewhere. Additionally, replace the IDs and other data in the JSON payload with actual data as needed for your testing.