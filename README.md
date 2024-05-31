# Vehicle Maintenance Management Solution

## Introduction
This repository contains a minimal solution to manage the maintenance of vehicles in a transport company. The solution is designed with a robust layered architecture, design patterns, and is oriented to Domain-Driven Design (DDD). The project includes unit and integration tests and is documented using Swagger/OpenAPI.



# Architecture 

```
+-------------------------------------------+
|                   API                     |
|       (FastAPI + Swagger/OpenAPI)         |
+------------------------+------------------+
                         |
                         |
+------------------------v------------------+
|                Application Layer          |
|  (Service handlers, DTOs, API controllers)|
+------------------------+------------------+
                         |
                         |
+------------------------v------------------+
|                Domain Layer               |
|   (Entities, Value Objects, Aggregates,   |
|           Domain Services)                |
+------------------------+------------------+
                         |
                         |
+------------------------v------------------+
|                Infrastructure Layer       |
|    (Repositories, Data Sources,           |
|     External Service Integrations)        |
+------------------------+------------------+
                         |
                         |
+------------------------v------------------+
|                Database                   |
|            (PostgreSQL)                   |
+-------------------------------------------+
```



# Use Cases Supported

- Add Vehicle: Add a new vehicle to the system.
- Get vehicle details : Get details of an existing vehicle.
- Update order status : Update order status of an existing vehicle with state machine support, supported transitions : Pending, In progress, Completed
- View Maintenance History: Not yet

# Steps for running endpoints
- first create a vehicle
- create order service for existing vehicle
- Update order service for existing vehicle 

# State machine support
supported transitions for now : 
- Pending
- In progress 
- Completed

Business rules could be added to not be able to go from one transition to another (coming soon in another commit )




# Access the API documentation
Open your browser and go to http://localhost:8000/docs to see the Swagger UI.

# Testing

docker-compose run tests
