import json
from pathlib import Path
from datetime import datetime
import requests

DATA_DIR=Path(__file__).resolve().parents[1]/"data"/"raw"
DATA_DIR.mkdir(parents=True,exist_ok=True)

def extract_weather_data(lat=17.385044,lon=-62.718750,days=1):
    url="https://api.open-meteo.com/v1/forecast"
    params={
        "latitude":lat,
        "longitude":lon,
        "hourly":"temperature_2m,relativehumidity_2m,windspeed_10m,winddirection_10m",
        "forecast_days":days,
        "timezone":"auto"
    }
    response=requests.get(url,params=params)
    response.raise_for_status()
    data=response.json()
    filename=DATA_DIR/f"weather_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    filename.write_text(json.dumps(data,indent=2))
    print(f"Data saved to {filename}")
    return data

if __name__=="__main__":
    extract_weather_data()
