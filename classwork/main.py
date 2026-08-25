# 1. Standard import
import greet
greet.greet_user("Alice")

# 2. Import specific function
from greet import greet_user
greet_user("Bob")

# 3. Import with alias for function
from greet import greet_user as gu
gu("Charlie")

# 4. Import module with alias
import greet as gr
gr.greet_user("Diana")

# 5. Import all functions (not recommended, but possible)
from greet import *
greet_user("Eve")
