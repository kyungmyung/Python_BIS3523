# pip install seaborn
import seaborn as sb
tipdata = sb.load_dataset('tips')

# pip install statsmodels
import statsmodels.api as sm

slr_data = tipdata['size']
ols_data = sm.add_constant(slr_data)
ols = sm.OLS(tipdata['tip'], ols_data)
olsfitted = ols.fit()
print(olsfitted.summary())

# pip install scikit-learn
from sklearn.preprocessing import LabelEncoder
label_transfer = LabelEncoder()
label_transfer.fit(tipdata['time'])
time_dummy = label_transfer.transform(tipdata['time'])
# 0 is dinner; 1 is lunch
tipdata['time_dummy'] = time_dummy

slr_data_with_time = tipdata[['size','time_dummy']]
ols_data_with_time = sm.add_constant(slr_data_with_time)
ols_time = sm.OLS(tipdata['tip'], ols_data_with_time)
ols_time_fitted = ols_time.fit()
print(ols_time_fitted.summary())








