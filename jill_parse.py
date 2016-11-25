import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
from dateutil import parser
import re
plt.ion()

observations = [
    (parser.parse(' '.join(line.split()[:-1])),
     float(re.sub('[$,]', '', line.split()[-1])))
    for line in open('jill.log').readlines()
]

times, amounts = zip(*observations)

def dollars(x, pos):
    'Convert float back to dollar value'
    return '${:,}'.format(x)

def print_time(x, pos):
    print pos
    return x


fig, ax = plt.subplots(1, 1)
ax.plot(times, amounts)
fig.autofmt_xdate()
ax.yaxis.set_major_formatter(tkr.FuncFormatter(dollars))
plt.show()
