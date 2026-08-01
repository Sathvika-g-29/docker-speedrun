import streamlit as st
import sqlite3
import pandas as pd

# DB setup
conn = sqlite3.connect('visits.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS visits (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, mood TEXT)')
conn.commit()

# Page config
st.set_page_config(page_title="🐳 Docker Guestbook", layout="wide")

# Header
st.title("🐳 Docker Guestbook")
st.caption("Built with Streamlit + SQLite + Docker — deployed on Render!")

# Stats row
total = c.execute('SELECT COUNT(*) FROM visits').fetchone()[0]
col1, col2, col3 = st.columns(3)
col1.metric("👥 Total Visitors", total)
col2.metric("🐳 Docker Image", "sathvikaaa/my-streamlit-app")
col3.metric("🚀 Status", "Live on Render!")

st.divider()

# Input section
col_a, col_b = st.columns(2)
with col_a:
    st.subheader("✍️ Sign the Guestbook")
    name = st.text_input("Your name:")
    mood = st.selectbox("Your mood today:", ["😄 Excited", "🤯 Mind blown", "💪 Confident", "🐳 Docker fan now!"])
    if st.button("Sign!", use_container_width=True):
        if name:
            c.execute('INSERT INTO visits (name, mood) VALUES (?, ?)', (name, mood))
            conn.commit()
            st.balloons()
            st.success(f"Welcome {name}! You're visitor #{total + 1} 🚀")
        else:
            st.warning("Enter your name first!")

with col_b:
    st.subheader("📊 Mood Chart")
    moods = c.execute('SELECT mood, COUNT(*) FROM visits GROUP BY mood').fetchall()
    if moods:
        df = pd.DataFrame(moods, columns=["Mood", "Count"])
        st.bar_chart(df.set_index("Mood"))
    else:
        st.info("Sign the guestbook to see the chart!")

st.divider()

# Guestbook table
st.subheader("📋 All Visitors")
visitors = c.execute('SELECT id, name, mood FROM visits ORDER BY id DESC').fetchall()
if visitors:
    df2 = pd.DataFrame(visitors, columns=["#", "Name", "Mood"])
    st.dataframe(df2, use_container_width=True)
else:
    st.write("No visitors yet!")