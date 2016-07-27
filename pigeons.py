import urllib2
import matplotlib.pyplot as plt

f=urllib2.urlopen("http://blog.yhat.com/static/img/pigeon-racing-logo.png")
a = plt.imread(f)
plt.imshow(a)
plt.show()

### moving on to our pigeon data!

from ggplot import *
import numpy as np
import pandas as pd

np.shape(pigeons)
pigeons.head()


## looking into speed distributions
ggplot(pigeons, aes(x='speed')) + stat_density() 

top_pigeons = pigeons[:100]

# doesnt look very normal
pigeons.speed.describe()

# seems like we could make a nice split around the 50% percentile mark
pigeons['pigeons_split'] = pigeons.speed.map(lambda x: True if x>131 else False)

ggplot(pigeons, aes(x='speed', fill='pigeons_split')) + geom_histogram()

#find our most valuable breeder MVB
# create a log-weight for each place
ranker= pd.DataFrame({"place":range(100)})
ranker['log_weight'] = ranker.place.map(lambda x: 1/np.log(x+1))


ggplot(ranker,aes(x='place',y='log_weight')) + geom_line()
by_breeder=pigeons.groupby('breeder')
by_breeder.pos.sum()
