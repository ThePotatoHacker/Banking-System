
# Responsibilities:
# 1. DATABASE CONNECTION
#    - Creates/connects to SQLite or MySQL database
#    - Automatically reconnects if connection drops

# 2. TABLE MANAGEMENT
#    - Creates tables on first launch (accounts, transactions)
#    - Example schema:
#      accounts (account_num, pin_hash, name, balance, avatar, join_date)
#      transactions (id, account_num, amount, type, timestamp, memo)

# 3. SAFE QUERY EXECUTION
#    - Uses parameterized queries to prevent SQL injection
#    - Handles errors gracefully (e.g., duplicate accounts)

# 4. COMMON OPERATIONS
#    - execute(query, params) → Runs any SQL safely
#    - fetch_one(query, params) → Gets single record
#    - fetch_all(query, params) → Gets multiple records

# 5. CLEANUP
#    - Closes connections automatically
#    - backup system