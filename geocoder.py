import geopy
import pandas
from geopy.geocoders import Nominatim
# versions used: geopy 1.10.0, pandas 0.16.2, python 2.7.8

def main():
  io = pandas.read_csv('census.csv', index_col=None, header=0, sep=",")

  def get_latitude(x):
    return x.latitude

  def get_longitude(x):
    return x.longitude

  geolocator = Nominatim()
  # geolocator = GoogleV3()
  # uncomment the geolocator you want to use

  geolocate_column = io['Area_Name'].apply(geolocator.geocode)
  io['latitude'] = geolocate_column.apply(get_latitude)
  io['longitude'] = geolocate_column.apply(get_longitude)
  io.to_csv('geocoding-output.csv')

if __name__ == '__main__':
  main()