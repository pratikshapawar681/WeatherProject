
# Weather Data to PostgreSQL

## 📌 Overview

A Python project that fetches **current weather data** from a public API and stores it in **PostgreSQL** for future analysis.

---

## ⚙️ Tech Stack

* Python, PostgreSQL
* Libraries: `requests`, `pandas`, `sqlalchemy`, `psycopg2-binary`

---

## 🚀 Setup

1. Clone repo:

   ```bash
   git clone https://github.com/your-username/WeatherProject.git
   cd WeatherProject
   ```
2. Install dependencies:

   ```bash
   pip install psycopg2-binary sqlalchemy pandas requests
   ```
3. Update DB connection in `weather_to_pg.py`.
4. Run:

   ```bash
   python weather_to_pg.py
   ```

---

## 📊 Database

Tables:

* **sales** – sample sales data
* **weather** – city, temperature, description, timestamp

---

## ✅ Output

```
Weather data for Patna stored successfully in PostgreSQL.
```


