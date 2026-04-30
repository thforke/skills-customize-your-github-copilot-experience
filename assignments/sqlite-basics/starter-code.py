"""Starter code: SQLite Basics with Python.

Run:
    python3 starter-code.py
"""

import sqlite3

DB_NAME = "library.db"


def create_database() -> None:
    """Create the books table if it does not already exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL
        )
        """
    )

    conn.commit()
    conn.close()


def add_book(title: str, author: str, year: int) -> None:
    """Insert one book into the books table."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        (title, author, year),
    )

    conn.commit()
    conn.close()


def list_books() -> list[tuple[int, str, str, int]]:
    """Return all books sorted by id."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, author, year FROM books ORDER BY id")
    rows = cursor.fetchall()

    conn.close()
    return rows


def find_books_by_author(author: str) -> list[tuple[int, str, str, int]]:
    """Return all books for a specific author."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, author, year FROM books WHERE author = ? ORDER BY id",
        (author,),
    )
    rows = cursor.fetchall()

    conn.close()
    return rows


def print_books(rows: list[tuple[int, str, str, int]]) -> None:
    """Print rows in a readable one-line format."""
    if not rows:
        print("No books found.")
        return

    for book_id, title, author, year in rows:
        print(f"{book_id} | {title} | {author} | {year}")


if __name__ == "__main__":
    create_database()

    # Sample data students can replace.
    add_book("The Hobbit", "J.R.R. Tolkien", 1937)
    add_book("Dune", "Frank Herbert", 1965)
    add_book("1984", "George Orwell", 1949)

    print("All books:")
    print_books(list_books())

    print("\nBooks by Frank Herbert:")
    print_books(find_books_by_author("Frank Herbert"))
