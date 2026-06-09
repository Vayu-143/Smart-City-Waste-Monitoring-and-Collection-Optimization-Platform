import random
import pandas as pd
from datetime import datetime

BIN_HEIGHT = 40

def calculate_fill(distance):

    fill = ((BIN_HEIGHT-distance)/BIN_HEIGHT)*100

    if fill < 0:
        fill = 0

    if fill > 100:
        fill = 100

    return round(fill,2)

def get_status(fill):

    if fill < 40:
        return "EMPTY"

    elif fill < 80:
        return "HALF FULL"

    else:
        return "FULL"

data=[]

for _ in range(50):

    distance=random.uniform(1,40)

    fill=calculate_fill(distance)

    status=get_status(fill)

    alert="YES" if fill>=80 else "NO"

    data.append([
        datetime.now(),
        distance,
        fill,
        status,
        alert
    ])

df=pd.DataFrame(
data,
columns=[
"Timestamp",
"Distance",
"FillPercent",
"Status",
"Alert"
]
)

df.to_csv("data/waste_data.csv",index=False)

print(df.tail())