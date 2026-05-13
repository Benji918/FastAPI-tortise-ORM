# FastAPI Tortoise ORM Test

This repository is for testing out **Tortoise ORM** queries and **Aerich** migration handling.

## Purpose
The main goal of this project is to experiment with:
- Database schema definitions using Tortoise ORM models.
- Managing database migrations (version control for your database) using Aerich.
- Basic CRUD operations within a FastAPI environment.

## Tech Stack
- **FastAPI**: The web framework.
- **Tortoise ORM**: An easy-to-use asyncio ORM.
- **Aerich**: A database migration tool for Tortoise ORM.
- **PostgreSQL**: The database (via Neon).
- **UV**: Fast Python package manager.

## Setup

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Environment Variables**:
   Create a `.env` file in the root directory and add your connection string:
   ```env
   DATABASE_URL=postgres://user:password@host:port/dbname
   ```

## Database Migrations (Aerich)

- **Initialize Aerich**:
  ```bash
  aerich init -t database.TORTOISE_ORM
  ```

- **Initialize Database**:
  ```bash
  aerich init-db
  ```

- **Create a new migration** (after changing models):
  ```bash
  aerich migrate --name descriptive_name
  ```

- **Apply migrations**:
  ```bash
  aerich upgrade
  ```
