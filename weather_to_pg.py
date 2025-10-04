import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import date

# ---------------- Configurations ----------------
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Patna"

# PostgreSQL connection string
# Replace YOUR_PASSWORD with your PostgreSQL password
PG_CONN_STRING = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

# ---------------- Functions ----------------
def fetch_weather(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return {
        'weather_date': date.today(),
        'city': city,
        'temp_c': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description'],
    }

def store_weather_to_db(weather_data, conn_string):
    engine = create_engine(conn_string)
    df = pd.DataFrame([weather_data])
    df.to_sql('weather', engine, if_exists='append', index=False)
    print(f"Weather data for {weather_data['city']} stored successfully in PostgreSQL.")

# ---------------- Main Script ----------------
def main():
    weather = fetch_weather(API_KEY, CITY)
    store_weather_to_db(weather, PG_CONN_STRING)

if __name__ == "__main__":
    main()


