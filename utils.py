

import csv



from station import Station


STATION_INFO = {}


def populate_stations():
    # load the csv

    station_file  = open('data/station_info.csv', "rb")
    station_data = csv.reader(station_file)
    #station_data = load_csv("data/station_info.csv")

    for name, lat, lon, elev in station_data:
        station = Station(name, lat, long, elev)
        STATION_INFO[name] = station


def get_station(station_name):
    return STATION_INFO[station_name]



def main():
    populate_stations()

if __name__ =="__main__":
    main()
    print STATION_INFO
