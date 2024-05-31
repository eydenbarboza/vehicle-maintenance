def test_create_service_order(client):
    response = client.post("/service_orders/", json={"description": "Cambio de aceite", "vehicle_id": 1})
    assert response.status_code == 200
    data = response.json()
    assert data["description"] == "Cambio de aceite"
    assert data["vehicle_id"] == 1

def test_get_service_order(client):
    response = client.post("/service_orders/", json={"description": "Cambio de aceite", "vehicle_id": 1})
    order_id = response.json()["id"]
    response = client.get(f"/service_orders/{order_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["description"] == "Cambio de aceite"
    assert data["vehicle_id"] == 1

def test_update_service_order_state(client):
    response = client.post("/service_orders/", json={"description": "Cambio de aceite", "vehicle_id": 1})
    assert response.status_code == 200
    order_id = response.json()["id"]
    
    response = client.patch(f"/service_orders/{order_id}", json={"transition": "start_service"})
    assert response.status_code == 200
    data = response.json()
    
    assert data["state"] == "IN_PROGRESS"

