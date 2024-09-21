import streamlit as st
import sqlite3
import pandas as pd
from PIL import Image
import io

db_url = 'https://raw.githubusercontent.com/Joelroys637/firebasedatabase/df0963c8929de6a52115df621afff3a83d8b0385/datasignup.db'

# Download the database file
response = requests.get(db_url)

# Save the file locally
with open('datasignup.db', 'wb') as f:
    f.write(response.content)

# Now connect to the downloaded database
conn = sqlite3.connect('datasignup.db')

c = conn.cursor()

# Create a table for storing user credentials if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS user (username TEXT, password TEXT,phone TEXT)''')
conn.commit()

user=st.text_input('username')
password1=st.text_input('password')
phone=st.text_input('Mobile number OR Email id')
if st.button("SIGUP"):
            
    c.execute("INSERT INTO user VALUES (?, ?, ?)", (user,password1,phone))
    st.success("Sigup Successfully Thank you!")
    conn.commit()

elif st.button("data"):
    c.execute('SELECT * FROM user')
    data = c.fetchall()
    df = pd.DataFrame(data, columns=['username', 'password','phone'])
    conn.close()

    st.dataframe(df)
