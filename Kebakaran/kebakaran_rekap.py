import math, json, csv, sys, ast
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
geolocator = Nominatim()
temp = []
datafile = []
bigdata = {}

def main():
    args = str(sys.argv)
    args = ast.literal_eval(args)
    for xx in range(0, len(args)):
        if xx != 0:
            datafile.append(args[xx]);
    getKebakaranRekap()
    export()
    return True

def getLocation(location):
    try:
        return location.address
    except: return ""

def getLatitude(location):
    try:
        return location.latitude
    except: return ""

def getLongitude(location):
    try:
        return location.longitude
    except: return ""

def getKebakaranRekap():
    for xx in range(0, len(datafile)):
        data={}
        with open(datafile[xx]) as csvfile:
            reader = csv.DictReader(csvfile)
            temp=0
            for row in reader:
                databaris = {}
                daerah = row['lokasi_kejadian'].split("Kec.")
                try:
                    kecamatan = daerah[1];
                    kecamatan = kecamatan.replace(" ","")
                except:
                    kecamatan = ""

                try:
                    daerah2 = daerah[0].split("Kel.")
                    kelurahan = daerah2[1]
                    kelurahan = kelurahan.replace(" ","")
                except:
                    kelurahan=""
                
                try:
                    location = geolocator.geocode(kelurahan+","+kecamatan, timeout=None)
                except GeocoderTimedOut as e:
                    location = geolocator.geocode(kelurahan+","+kecamatan, timeout=None)
                row['latitude']=str(getLatitude(location))
                row['longitude']=str(getLongitude(location))
                data[temp]=row
                temp=temp+1
        datafile[xx] = datafile[xx].replace(".csv","")
        bigdata[datafile[xx]]=data




def export():
    with open('kebakaran.json', 'w') as f:
         r = json.dumps(bigdata)
         print >> f, "["
         print >> f, r
         print >> f, "]"
     
if main()==True:
    print "Success"
            


