import requests
import random
import pandas as pd
import time
from datetime import datetime

# ==================================
# SMART CITY WASTE MONITORING
# ==================================

WRITE_API_KEY = "YOUR_THINGSPEAK_WRITE_API_KEY"

THINGSPEAK_URL = "https://api.thingspeak.com/update"

BIN_HEIGHT = 40

# ==================================
# CALCULATE FILL %
# ==================================

def calculate_fill(distance):

    fill_percent = (
        (BIN_HEIGHT - distance) / BIN_HEIGHT
    ) * 100

    fill_percent = max(
        0,
        min(fill_percent, 100)
    )

    return round(fill_percent, 2)


# ==================================
# BIN STATUS
# ==================================

def get_status(fill):

    if fill < 40:
        return "EMPTY"

    elif fill < 80:
        return "HALF FULL"

    else:
        return "FULL"


# ==================================
# ALERT LOGIC
# ==================================

def get_alert(fill):

    return 1 if fill >= 80 else 0


# ==================================
# COLLECTION REQUIRED
# ==================================

def collection_required(fill):

    return 1 if fill >= 80 else 0


# ==================================
# PRIORITY SCORE
# ==================================

def get_priority(fill):

    if fill >=80:
        return "HIGH"

    elif fill >= 40:
        return "MEDIUM"

    else:
        return "LOW"


# ==================================
# THINGSPEAK UPLOAD
# ==================================

def send_to_thingspeak(
    distance,
    fill,
    status,
    alert,
    collection
):

    payload = {

        "api_key": WRITE_API_KEY,

        "field1": distance,
        "field2": fill,
        "field3": status,
        "field4": alert,
        "field5": collection

    }

    try:

        response = requests.get(
            THINGSPEAK_URL,
            params=payload,
            timeout=10
        )

        print(
            "ThingSpeak Response:",
            response.text
        )

    except Exception as e:

        print(
            "ThingSpeak Error:",
            e
        )


# ==================================
# DATA LOGGING
# ==================================

csv_file = "data/waste_data.csv"

try:

    df = pd.read_csv(csv_file)

except:

    df = pd.DataFrame(
        columns=[
            "Timestamp",
            "Distance",
            "FillPercent",
            "Status",
            "Alert",
            "CollectionRequired",
            "Priority"
        ]
    )

print(
    "\nSMART CITY WASTE MONITORING STARTED\n"
)

# ==================================
# MAIN LOOP
# ==================================

while True:

    distance = round(
    random.uniform(2, 40),
    2
)

    fill = calculate_fill(distance)

    status = get_status(fill)

    alert = get_alert(fill)

    collection = collection_required(fill)

    priority = get_priority(fill)

    print("\n" + "=" * 50)

    print(
        "Timestamp :",
        datetime.now()
    )

    print(
        "Distance :",
        distance,
        "cm"
    )

    print(
        "Fill Percentage :",
        fill,
        "%"
    )

    print(
        "Bin Status :",
        status
    )

    print(
        "Alert Status :",
        alert
    )

    print(
        "Collection Required :",
        collection
    )

    print(
        "Priority Level :",
        priority
    )

    send_to_thingspeak(
        distance,
        fill,
        status,
        alert,
        collection
    )

    new_row = pd.DataFrame(
        [[
            datetime.now(),
            distance,
            fill,
            status,
            alert,
            collection,
            priority
        ]],
        columns=[
            "Timestamp",
            "Distance",
            "FillPercent",
            "Status",
            "Alert",
            "CollectionRequired",
            "Priority"
        ]
    )

    df = pd.concat(
        [df, new_row],
        ignore_index=True
    )

    df.to_csv(
        csv_file,
        index=False
    )

    print(
        "Data Logged Successfully"
    )

    time.sleep(20)