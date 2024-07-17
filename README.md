A simple FastAPI project demonstrating how to create a RESTful API using Python FastAPI, SQLAlchemy, and PostgreSQL.
<br>
### Project Structure
<br>
your-project/
├── main.py # FastAPI application
<br>
├── database.py # Database connection setup
<br>
├── models.py # SQLAlchemy models
<br>
├── create_db.py # Create tables in the database
<br>
├── .gitignore # Git ignore file
<br>
└── README.md # Project documentation
<br>
### Prerequisites
<br>
- Python 3.7+
<br>
- PostgreSQL
<br>
- `pip` package installer
<br>
### API Endpoints
<br>
1. GET /: Fetch all persons
<br>
2. GET /getbyID/{person_id}: Fetch a person by ID
<br>
3. POST /addperson: Add a new person
<br>
4. PUT /update_person/{person_id}: Update a person by ID
<br>
5. DELETE /delete_person/{person_id}: Delete a person by ID
<br>
### Dependencies
<br>
1. fastapi
<br>
2. pydantic
<br>
3. sqlalchemy
<br>
4. psycopg2-binary
<br>