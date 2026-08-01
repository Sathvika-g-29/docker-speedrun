import streamlit as st
import sqlite3

conn = sqlite3.connect('visits.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS visits (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
conn.commit()

st.title("🐳 Dockerized Streamlit + SQLite!")

count = c.execute('SELECT COUNT(*) FROM visits').fetchone()[0]
st.info(f"👥 Total visitors so far: {count}")

name = st.text_input("Enter your name to sign the guestbook:")
if st.button("Sign! ✍️"):
    if name:
        c.execute('INSERT INTO visits (name) VALUES (?)', (name,))
        conn.commit()
        st.balloons()
        st.success(f"Welcome {name}! You're visitor #{count + 1} 🚀")
    else:
        st.warning("Please enter your name first!")

st.subheader("📋 Guestbook")
visitors = c.execute('SELECT id, name FROM visits ORDER BY id DESC').fetchall()
if visitors:
    for v in visitors:
        st.write(f"#{v[0]} — {v[1]}")
else:
    st.write("No visitors yet — be the first!")