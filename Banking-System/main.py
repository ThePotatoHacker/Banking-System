# Initialize application
# Load GUI and show welcome screen
# Handle main program loop:
#   - Route to login/create account
#   - Redirect to admin/user menus
#   - Exit cleanup


#First 
 #Imports
#    - Import gui (to show cute windows)
import gui

#    - Import auth (to check passwords)
import auth

#    - Import database (to remember accounts)
import database


# Open database here once created 

# Displaying Welcome

print("📦 Starting program...")
from gui import front_page

if __name__ == "__main__":
    front_page()  # Launch the honeybee window!
print("✅ Welcome message shown")