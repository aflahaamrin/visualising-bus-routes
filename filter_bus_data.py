from utils import readGTRSData, writeGTRSData

def main(trip_id : str):

    df_trips, df_shapes, = readGTRSData(["trips.txt","shapes.txt"])
    df_stop_pattern_trips, df_stop_patterns, df_stops, = readGTRSData(["stop_pattern_trips.txt","stop_patterns.txt", "stops.txt"])

    # Look for shapes associated with the trip id
    df_trip = df_trips[df_trips["trip_id"] == trip_id]
    df_shapes = df_shapes[df_shapes["shape_id"] == df_trip["shape_id"].iloc[0]]

    # Look for stops on the trip id
    df_stop_pattern_trips = df_stop_pattern_trips[df_stop_pattern_trips["trip_id"]==trip_id]
    df_stop_patterns = df_stop_patterns[df_stop_patterns["stop_pattern_id"]==df_stop_pattern_trips["stop_pattern_id"].iloc[0]]
    df_stops = df_stops[df_stops["stop_id"].isin(df_stop_patterns["stop_id"].to_list())]

    # Export to a comma-separated text file
    writeGTRSData([df_stops, df_shapes], ["filtered_stops.txt","filtered_shapes.txt"])

if __name__ == "__main__":
    main("1__0__279__TZM__212__6__212__6_20251005")





