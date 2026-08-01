FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/data

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
# FROM python:3.11-slim	Downloaded a lightweight Python environment
# WORKDIR /app	Created a folder called /app inside the container
# COPY requirements.txt .	Copied your requirements file in
# RUN pip install -r requirements.txt	Installed Streamlit inside the container
# COPY . .	Copied your app.py in
# EXPOSE 8501	Opened port 8501 (Streamlit's default)
# CMD [...]	The command to run when container starts