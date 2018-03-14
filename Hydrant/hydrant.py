import math, json, csv, sys, ast
temp = []
datafile = []
bigdata = {}

def main():
    args = str(sys.argv)
    args = ast.literal_eval(args)
    for x in range(0, len(args)):
        if x != 0:
            datafile.append(args[x]);
    getHydrant()
    export()
    return True

def getHydrant():
        for x in range(0, len(datafile)):
            data={}
            with open(datafile[x]) as csvfile:
                reader = csv.DictReader(csvfile)
                temp=0
                for row in reader:
                  data[int(temp)]=row
                  temp=temp+1
            datafile[x] = datafile[x].replace(".csv","")
            bigdata[datafile[x]]=data

def export():
    with open('hydrant.json', 'w') as f:
         r = json.dumps(bigdata)
         print >> f, "["
         print >> f, r
         print >> f, "]"

if main()==True:
    print "Success"
            


