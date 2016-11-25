import time, BeautifulSoup as bs, urllib, os, re, sys

while True:
    cxn = urllib.urlopen('https://jillstein.nationbuilder.com/recount')
    page = cxn.read()
    elements = bs.BeautifulSoup(page)
    print os.popen('date').read().strip(),
    amountdiv = elements.findAll('div', {'class': 'bar-text'})
    amountstring = amountdiv[0].getText().split()[0]
    if not re.match('\$\d{,2},\d{3},\d{3}\.\d{2}', amountstring):
        assert not os.system('zwrite alex_c -m "Parse failed"')
    print amountstring
    sys.stdout.flush()
    time.sleep(15)
