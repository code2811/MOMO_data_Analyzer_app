from models import create_tables
from insert import add_user, add_transaction
from view import show_users, show_transactions

create_tables()

add_user("Amina", "0789123456")
add_transaction(1, "deposit", 20000)
add_transaction(1, "withdraw", 5000)

show_users()
show_transactions()

