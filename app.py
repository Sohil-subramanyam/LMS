from flask import Flask, render_template, request, redirect, url_for
import cx_Oracle

app = Flask(__name__)

# Oracle Database connection function
def get_db_connection():
    # Change the connection details based on your Oracle DB configuration
    dsn = cx_Oracle.makedsn("localhost", 1521, service_name="xe")  # Update with your host, port, and SID
    connection = cx_Oracle.connect("username", "password", dsn)  # Replace with your Oracle DB username and password
    return connection

# Home route (library catalog page)
@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')  # Fetch all books from the database
    books = cursor.fetchall()  # Fetch all rows
    cursor.close()
    conn.close()
    return render_template('lib1.html', books=books)  # Pass books data to the HTML template

# Login route (for the login page)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = :username AND password = :password', 
                       {'username': username, 'password': password})
        user = cursor.fetchone()  # Fetch one user record
        cursor.close()
        conn.close()

        if user:
            return redirect(url_for('home'))  # Redirect to home page upon successful login
        else:
            return 'Invalid credentials, try again.'

    return render_template('login.html')

# Handle book availability change (simplified)
@app.route('/toggle_availability/<int:book_id>')
def toggle_availability(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT availability FROM books WHERE id = :book_id', {'book_id': book_id})
    availability = cursor.fetchone()[0]  # Fetch the availability value (1 or 0)

    new_availability = 0 if availability == 1 else 1
    cursor.execute('UPDATE books SET availability = :availability WHERE id = :book_id', 
                   {'availability': new_availability, 'book_id': book_id})
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
