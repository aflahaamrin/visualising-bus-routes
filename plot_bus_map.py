import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import LineString
from utils import readGTRSData
import folium

def main():
    df_shapes, df_stops, = readGTRSData(["filtered_shapes.txt","filtered_stops.txt"],data_path="data/processed/metlink_bus/")

    # converts stops dataframe to geodataframe
    gdf_stops = gpd.GeoDataFrame(
        df_stops, geometry=gpd.points_from_xy(df_stops.stop_lon, df_stops.stop_lat), crs="EPSG:4326"
    )

    # converts shapes dataframe to geodataframe
    gdf_shapes = gpd.GeoDataFrame(
        df_shapes, geometry=gpd.points_from_xy(df_shapes.shape_pt_lon, df_shapes.shape_pt_lat), crs="EPSG:4326"
    )

    # converts shapes geometry from points to a line
    line = LineString(gdf_shapes.geometry.tolist())
    gdf_shapes = gpd.GeoDataFrame(geometry=[line], crs=gdf_shapes.crs)

    # create map of the bus route
    m = folium.Map(location=[-41.2924, 174.7787], zoom_start=13, tiles="CartoDB positron")
    for _, r in gdf_shapes.iterrows():
        sim_geo = gpd.GeoSeries(r["geometry"])
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {"fillColor": "red"})
        geo_j.add_to(m)
    for _, r in gdf_stops.iterrows():
        sim_geo = gpd.GeoSeries(r["geometry"])
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {"fillColor": "red"})
        folium.Popup(r["stop_name"]).add_to(geo_j)
        geo_j.add_to(m)
    m.save("bus_routes_map.html")

if __name__ == "__main__":
    main()