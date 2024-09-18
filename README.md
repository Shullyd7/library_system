# Library Management API

## Overview

This project consists of two Django-based APIs for managing a library's book catalog and user interactions. The Frontend API allows users to browse and borrow books, while the Backend API enables admin operations such as adding or removing books and viewing user data.

## URLs

### Frontend API

- **Enroll a User**: `POST /api/enroll_user/`
- **List Available Books**: `GET /api/list_books/`
- **Get a Single Book by ID**: `GET /api/get_book/<int:book_id>/`
- **Filter Books**: `GET /api/filter_books/?publisher=<publisher>&category=<category>`
- **Borrow a Book**: `POST /api/borrow_book/`
- **Return a Book**: `POST /api/return_book/`

### Backend API

- **Add a New Book**: `POST /api/add_book/`
- **Remove a Book**: `DELETE /api/remove_book/<int:book_id>/`
- **Fetch All Users**: `GET /api/list_users/`
- **Fetch Borrowed Books**: `GET /api/list_borrowed_books/`

## RabbitMQ Integration

RabbitMQ is used for cross-communication between the Frontend and Backend APIs. When a book is added or removed in the Backend API, RabbitMQ publishes a message to notify the Frontend API of the change.

### RabbitMQ Setup Locally
Access your management console after starting rabbitmq locally 

- **Ports**:
  - Management Console: `http://localhost:15672/` (username: `guest`, password: `guest`)

**Backend API Integration**: The `notify_frontend` function in the Backend API sends a message to RabbitMQ whenever a book is added or removed.

**Frontend API Handling**: Implement a consumer to listen for messages from RabbitMQ and update the book catalog accordingly.

## Running Tests

To run the tests for both APIs:

1. **Navigate to the Frontend API directory**:
   ```bash
   cd frontendapi
   ```

2. **Run the Frontend API tests**:
   ```bash
   python manage.py test
   ```

3. **Navigate to the Backend API directory**:
   ```bash
   cd backendapi
   ```

4. **Run the Backend API tests**:
   ```bash
   python manage.py test
   ```

Ensure that RabbitMQ is running before executing the tests, as some tests might depend on it.

## Deploying with Docker Containers

1. **Build and Run Containers**:

   Ensure you are in the directory containing the `docker-compose.yml` file. Run the following command to build and start the containers:

   ```bash
   docker-compose up --build
   ```

2. **Access the Services**:

   - **Frontend API**: `http://localhost:8001`
   - **Backend API**: `http://localhost:8002`
   - **RabbitMQ Management Console**: `http://localhost:15672` (username: `guest`, password: `guest`)

3. **Stop Containers**:

   To stop the running containers, use:

   ```bash
   docker-compose down
   ```