from pandas import datetime, read_csv, DataFrame
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot

def parser(x):
    return datetime.strptime('200'+x,'%Y-%m')

series = read_csv("sparepart-contoh.csv",header=0,parse_dates =[0],index_col=0,squeeze=True,date_parser=parser)

# fit model

model = ARIMA(series,order=(5,1,0))
fit_model = model.fit(disp=0)
print(fit_model.summary())
# plot residual errors

residu = DataFrame(fit_model.resid)
residu.plot()
pyplot.show()

residu.plot(kind='kde')
pyplot.show()
print(residu.describe())

