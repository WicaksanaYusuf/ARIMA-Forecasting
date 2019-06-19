from pandas import datetime, read_csv
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot

def parser(x):
    return datetime.strptime('200'+x,'%Y-%m')

series = read_csv("shampoo.csv",header=0,parse_dates =[0],index_col=0,squeeze=True,date_parser=parser)
autocorrelation_plot(series)
pyplot.show()