#!/usr/bin/env python3
import sys
import csv
import json

from datetime import datetime

#
# Get stops list ready
stops = []
with open('locations.csv') as f:
    reader = csv.reader(f)

    i = 0
    for row in reader:
        # Skip header
        if i == 0:
            i += 1
            continue
        i += 1

        # Add stop
        id = int(row[0])
        lat = float(row[1])
        lon = float(row[2])
        stops.append(
            {
                "strId": str(id),
                "id": id,
                "name": str(id),
                "attributes": {"STATUS": "active", "EXTRA_PADDING_MILLISECONDS": "0"},
                "latitude": lat,
                "longitude": lon,
            }
        )

#
# Prepare entire OD-matrix OBJECT
records = {}
aggregate = {
    "timeStamp": datetime.now().strftime("%c"),
    "notes": [
        "All times are in milliseconds.",
        "Travel time provided in ODMatrix already includes all the necessary padding.",
    ],
    "nStops": len(stops),
    "stops": stops,
    "ODMatrix": {"nRecords": len(stops) ** 2},
}

#
# Populate the cells
with open('durations.csv') as f:
    reader = csv.reader(f)

    i = 0
    for row in reader:
        # Skip header
        if i == 0:
            i += 1
            continue
        i += 1

        # Parse row
        o = row[0]
        d = row[1]
        duration = float(row[2])

        # Add cell
        if not o in records:
            records[o] = {}
        records[o][d] = duration
aggregate['ODMatrix']['records'] = records

# Write out
json.dump(aggregate, open('matrix.json', 'w+'), indent=2)
