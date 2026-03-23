# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will learn how to design and implement REST API endpoints using FastAPI, including request handling, validation, and simple in-memory data storage.

## 📝 Tasks

### 🛠️ Build Core CRUD Endpoints

#### Description
Create a FastAPI application for managing a small collection of books. Implement endpoints to create, read, update, and delete book records.

#### Requirements
Completed program should:

- Create a FastAPI app instance and run it locally
- Define a `Book` model with fields such as `id`, `title`, `author`, and `year`
- Implement endpoints for `GET /books`, `GET /books/{book_id}`, `POST /books`, `PUT /books/{book_id}`, and `DELETE /books/{book_id}`
- Return appropriate HTTP status codes for successful requests and missing records


### 🛠️ Add Validation and Query Features

#### Description
Enhance the API by validating incoming data and supporting query-based filtering for book searches.

#### Requirements
Completed program should:

- Use Pydantic models to validate request bodies
- Add query parameters to filter books by author or publication year
- Handle invalid input with clear error responses
- Test all endpoints using FastAPI Swagger UI at `/docs`
