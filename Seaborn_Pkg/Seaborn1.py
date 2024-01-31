# pip install seaborn
import seaborn as sb

tipdata = sb.load_dataset('tips')

# grouping variables based on table size
tipsize = tipdata[['tip','size']].groupby('size').mean().reset_index()
sb.lineplot(data=tipsize, x='size', y='tip')

# pip install scikit-learn
from sklearn.preprocessing import LabelEncoder

label_transfer = LabelEncoder()
label_transfer.fit(tipdata['time'])
time_dummy = label_transfer.transform(tipdata['time'])
# 0 is dinner; 1 is lunch

tipdata['time_dummy'] = time_dummy
print(tipdata)

# Split data set based on the time_dummy
tipdata_dinner = tipdata[tipdata['time_dummy']==0]
tipdata_dinner = tipdata_dinner.reset_index(drop=True)

# Lunch
tipdata_lunch = tipdata[tipdata['time_dummy']==1]
tipdata_lunch = tipdata_lunch.reset_index(drop=True)

tipsize_dinner = tipdata_dinner[['tip','size']].groupby('size').mean().reset_index()
sb.lineplot(data=tipsize_dinner, x='size', y='tip')
tipsize_dinner

# grouping variables based on table size and lunch
tipsize_lunch = tipdata_lunch[['tip','size']].groupby('size').mean().reset_index()
sb.lineplot(data=tipsize_lunch, x='size', y='tip')
tipsize_lunch






