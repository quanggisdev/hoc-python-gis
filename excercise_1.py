import pandas as pd
import geopandas as gpd
import os

from shapely.geometry import Point, Polygon

df=pd.DataFrame(
                {
                    "City": ["Seoul", "Lima", "Johannesburg"],
                    "Country": ["South Korea", "Peru", "South Africa"],
                    "Lat":[37.57, -12.05, -26.20],
                    "Long": [126.98, -77.04, 28.04]
                }
                )

# Lệnh zip kéo Kinh độ và Vĩ độ lại với nhau để tạo thành các cặp tọa độ
df["Coord"]=list(zip(df.Long, df.Lat))

#đi qua từng cặp tọa độ vừa tạo và biến chúng thành đối tượng hình học POINT

df["Coord"]=df["Coord"].apply(Point)

#Nâng cấp DataFrame lên GeoPandas (GeoDataFrame)
gdf=gpd.GeoDataFrame(df, geometry='Coord', crs="EPSG:4326")

print("Bạn đã xuất ra Table", gdf)

city_plg=Polygon(list(zip(df.Long, df.Lat)))

print("Bạn đã tạo vùng thành công",city_plg)

# Kiểm tra nếu thư mục 'data' chưa có thì tự tạo mới
if not os.path.exists('data'):
    os.makedirs('data')

gdf.to_file("data/shape.shp")