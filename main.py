import tkinter as tk
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error



def parser(x):
    return datetime.strptime('200' + x, '%Y-%m')

def starting(order1,order2,order3):

    try:
        series = read_csv('sparepart3tahun.csv', header=0, parse_dates=[0], index_col=0, squeeze=True,
                          date_parser=parser)
        data_parsing = series.values
        size = int(len(data_parsing) * 0.66)
        train, test = data_parsing[0:size], data_parsing[size:len(data_parsing)]
        history = [x for x in train]

        predictions = list()

        for t in range(len(test)):
            o1 = int(order1)
            o2 = int(order2)
            o3 = int(order3)

            model = ARIMA(history, order=(o1, o2, o3))
            model_fit = model.fit(disp=0)
            output = model_fit.forecast()
            yhat = output[0]
            predictions.append(yhat)
            obs = test[t]
            history.append(obs)
            print('predicted=%f, expected=%f' % (yhat, obs))
        error = mean_squared_error(test, predictions)
        print('Test MSE: %.3f' % error)
    except:
        print("Something was wrong!!")
        print("Data harus stasioner berdasarkan order yang diinput!")



    #plotting ke matplotlib
    # pyplot.plot(test)
    # pyplot.plot(predictions,color='red')
    # pyplot.show()

root = tk.Tk()

root.geometry("250x100")
root.title("ARIMA Prototype")

windowLabel = tk.Label(root,text="Forecasting Produksi Sparepart")
windowLabel.pack()
authorLabel = tk.Label(root,text="Cici Emilia Sukmawati")
authorLabel.pack()

orderLabel = tk.Label(root,text="Order:")
orderLabel.pack(padx=5,pady=5,side=tk.LEFT)
entry = tk.Entry(root,width="5")
entry.pack(padx=5, pady=10, side=tk.LEFT)

entry2 = tk.Entry(root,width="5")
entry2.pack(padx=5,pady=20,side=tk.LEFT)

entry3 = tk.Entry(root,width="5")
entry3.pack(padx=5,pady=20,side=tk.LEFT)

button = tk.Button(root,text="Submit",command=lambda : starting(entry.get(),entry2.get(),entry3.get()))
button.pack(padx=5,pady=20,side=tk.LEFT)



root.mainloop()

