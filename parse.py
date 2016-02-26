from xml.dom import minidom
import re

pattern = '(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})\s{1}(?P<time>\d{2}:\d{2}\:\d{2})\s{1}(?P<gmt_offset>.\d{4})' #2015-11-03 22:43:31 +0800
xmldoc = minidom.parse('export.xml')
recordlist = xmldoc.getElementsByTagName('Record')
for s in recordlist:
    if s.attributes['type'].value == 'HKQuantityTypeIdentifierStepCount':
        m = re.match(pattern, s.attributes['startDate'].value)
        if m:
            try:
                print '%s,%s,%s,%s,%d' % (m.group('year'), m.group('month'), m.group('day'), m.group('time'),   float(s.attributes['value'].value))
            except:
                print 'in except block, TODO!'
