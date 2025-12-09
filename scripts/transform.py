import pandas as pd
import numpy as np
import json
import glob
import os
def transform_data(data):
    os.makedirs("../data/staged",exist_ok=True)
    latest_file=sorted(glob.glob("../data/raw/weather_*.json"))[-1]
    with open(latest_file) as f:
        data=json.load(f)
    hourly=pd.DataFrame(data["hourly"])
    df=pd.DataFrame({
        "time":hourly["time"],
        "temperature":hourly["temperature_2m"],
        "humidity":hourly["relativehumidity_2m"],
        "wind_speed":hourly["windspeed_10m"],
        "wind_direction":hourly["winddirection_10m"]
    })

    df["city"]="Hyderabad"
    df["extracted_at"]=pd.Timestamp.now()
    output_path="../data/staged/weather_cleaned.csv"
    df.to_csv(output_path,index=False)
    print(f"Data saved to {output_path}")
    return df

if __name__=="__main__":    
    transform_data(data=None)