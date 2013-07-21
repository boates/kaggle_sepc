

from utils import populate_stations
from utils import populate_probes

import globals




def main():

    populate_stations()
    print globals.STATIONS

    populate_probes()
    print globals.PROBES


if __name__ =="__main__":
    main()

