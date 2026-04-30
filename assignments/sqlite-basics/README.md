# 📘 Assignment: SQLite Basics with Python

## 🎯 Objective

In this assignment, you will learn how to store and retrieve data using SQLite in Python. You will create a small local database app that can add, list, and search records.

## 📝 Tasks

### 🛠️	Create and Initialize the Database

#### Description
Set up a local SQLite database file and create a table for storing book records. This task helps you understand database connections and table schemas.

#### Requirements
Completed program should:

- Create or connect to a local SQLite database file named `library.db`
- Create a `books` table with columns: `id`, `title`, `author`, `year`
- Use `id` as an auto-incrementing primary key
- Commit changes and close the connection safely


### 🛠️	Insert and List Books

#### Description
Implement functions to add new books into the database and print all saved books in a clear format.

#### Requirements
Completed program should:

- Implement a function to insert a new book (`title`, `author`, `year`)
- Implement a function to fetch all books from the database
- Print each row in a readable format, for example:
  ```text
  1 | The Hobbit | J.R.R. Tolkien | 1937
  ```
- Include at least 3 sample inserts for testing


### 🛠️	Search by Author

#### Description
Add a search feature that filters books by author name using a parameterized SQL query.

#### Requirements
Completed program should:

- Implement a function that takes an author name as input
- Return only books written by that author
- Use parameterized queries (not string concatenation)
- Show a friendly message when no results are found
