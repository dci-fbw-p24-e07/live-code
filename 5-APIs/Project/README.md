# Build Your Own API with Django Rest Framework

## Objective
Students will design and implement a RESTful API using DRF that demonstrates a complete understanding of serialization, validation, authentication, authorization, and error handling. The API can be built around any domain (e.g., books, movies, travel, e-commerce, learning management, social media, etc.).

## Project Breakdown

1. Project Setup & API Planning
    Set up the environment:
    - Create a new Django project and app.
    - Install and configure Django Rest Framework.
  
    Plan your API:
    - Choose a domain (e.g., "Library API", "Movie Reviews API").
    - Define the models and the relationships between them.
    - Identify endpoints (CRUD operations).
    - Decide which endpoints will be public vs protected.
    ***Deliverable:*** Project initialized, basic models created, requirements.txt updated.

2. Serialization & Deserialization
    - Create DRF serializers for your models.
    - Demonstrate how serializers transform Python objects → JSON (serialization) and JSON → Python objects (deserialization).
    - Add custom validation methods (field-level and object-level).
    ***Deliverable:*** Working serializers that validate and transform data.

3. Data Validation & Security
    - Implement validations in serializers to ensure clean data entry (e.g., unique fields, length restrictions, disallowed content) if needed
    - Discuss how improper validation can lead to vulnerabilities (e.g., SQL injection, XSS).
    - Sanitize input where necessary.
    ***Deliverable:*** Validations enforced in serializers and clear error messages returned.

5. Views vs ViewSets
    - Build at least one API endpoint using APIView.
    - Build the rest of the API using ViewSets + Routers.
    - Compare when to use each.
    ***Deliverable:*** API endpoints available through both View and ViewSet usage.

5. Authentication
    Implement:
    - Basic Authentication for initial testing.
    - Token Authentication for real-world API usage.
    - Secure sensitive endpoints so only authenticated users can access them.
    ***Deliverable:*** Endpoints protected by authentication.

6. Authorization & Role-Based Access
    - Use DRF’s permissions system to restrict certain actions (e.g., only Admin can delete, Regular User can only read/write their own objects).
    - Protect routes accordingly.
    ***Deliverable:*** Routes protected based on roles and permissions.

7. Error Handling
   - Translate exceptions into proper HTTP status codes (400, 401, 403, 404, 500).
   ```json
   {
     "error": {
       "code": 400,
       "message": "Invalid input data",
       "errors": [
         { "field": "email", "reason": "invalid", "message": "Email is not valid" }
       ]
     }
   }
   ```
   - Demonstrate both custom exception handling and DRF’s built-in exception handling.
   ***Deliverable:*** API returns consistent and standardized error messages.

### Final Deliverable

A fully functional API with:
- CRUD operations via serializers and viewsets.
- Proper data validation and sanitization.
- Authentication (basic & token-based).
- Role-based authorization.
- Standardized error handling.