from datetime import datetime
print datetime.fromtimestamp(1346236702.123456)
print datetime.fromtimestamp(1346236702)

print datetime.fromtimestamp(1346236703)
print datetime.fromtimestamp(1346236712)
print datetime.fromtimestamp(1346236802)
print datetime.fromtimestamp(1346237702)
print datetime.fromtimestamp(1346246702)
print datetime.fromtimestamp(1346336702)

# code from https://chenyuzuoo.github.io/posts/ecf5d190/
def totimestamp(dt, epoch=datetime(1970,1,1)):
    td = dt - epoch
    # return td.total_seconds()
    return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6 
#for sec in range(0,60):
#    dt = datetime(2018,2,26,12,30,sec)
#    print str(totimestamp(dt)) + ', ' + str(datetime.fromtimestamp(totimestamp(dt)))
for min in range(0,60):
    dt = datetime(2018,2,26,12,min,0)
    print str(totimestamp(dt)) + ', ' + str(datetime.fromtimestamp(totimestamp(dt)))
for min in range(0,60):
    dt = datetime(2018,2,26,13,min,0)
    print str(totimestamp(dt)) + ', ' + str(datetime.fromtimestamp(totimestamp(dt)))
for min in range(25,60):
    dt = datetime(2018,2,26,12,min,0)
    print 'demo,target=distance value=354 ' + str(totimestamp(dt)) + '000000000'
for min in range(0,60):
    dt = datetime(2018,2,26,13,min,0)
    print 'demo,target=distance value=354 ' + str(totimestamp(dt)) + '000000000'
