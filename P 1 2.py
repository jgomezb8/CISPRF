def main():
    filenamein ='c:/temp/myfile.txt'
    rcdcnt = 0
    infile = open(filenamein,'r')
    line=infile.readline()
    rain= []
    while (line !=""):
        line=line.strip()
        aa= float(line)
        rain.append(aa)
        print (line)
 
        line=infile.readline()
    print(rain)   
    print('highest -> ',max(rain))
    print('lowest -> ',min(rain))
    print('Total -> ', sum(rain))
    ss= sum(rain)/12
    print('average is ',ss)
    infile.close()
    
main()

