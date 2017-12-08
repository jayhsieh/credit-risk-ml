from sklearn import datasets
iris = datasets.load_iris()
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
import pandas as pd
# read data into a DataFrame
data1 = pd.DataFrame.from_csv('data1.csv', sep=',', index_col=0)
data2 = pd.DataFrame.from_csv('data2.csv', sep=',', index_col=0)
data3 = pd.DataFrame.from_csv('data3.csv', sep=',', index_col=0)
data4 = pd.DataFrame.from_csv('data4.csv', sep=',', index_col=0)
data5 = pd.DataFrame.from_csv('data5.csv', sep=',', index_col=0)
test = pd.DataFrame.from_csv('test.csv', sep=',', index_col=0)

data1X = data1.filter(['feature_transaction_usd_send', 'feature_local_receive','feature_kount_score',
                    'feature_kount_velocity', 'feature_sift_score','feature_days_since_first_completed',
                    'feature_six_month_send_limit', 'feature_account_type', #'feature_send_bank',
                    'feature_day_of_month', 'feature_customer_age', 'feature_previous_transactions'])
data1Y = data1.filter(['label_error_code'])

data2X = data1.filter(['feature_transaction_usd_send', 'feature_local_receive','feature_kount_score',
                    'feature_kount_velocity', 'feature_sift_score','feature_days_since_first_completed',
                    'feature_six_month_send_limit', 'feature_account_type', #'feature_send_bank',
                    'feature_day_of_month', 'feature_customer_age', 'feature_previous_transactions'])
data2Y = data1.filter(['label_error_code'])

data3X = data1.filter(['feature_transaction_usd_send', 'feature_local_receive','feature_kount_score',
                    'feature_kount_velocity', 'feature_sift_score','feature_days_since_first_completed',
                    'feature_six_month_send_limit', 'feature_account_type', #'feature_send_bank',
                    'feature_day_of_month', 'feature_customer_age', 'feature_previous_transactions'])
data3Y = data1.filter(['label_error_code'])

data4X = data1.filter(['feature_transaction_usd_send', 'feature_local_receive','feature_kount_score',
                    'feature_kount_velocity', 'feature_sift_score','feature_days_since_first_completed',
                    'feature_six_month_send_limit', 'feature_account_type', #'feature_send_bank',
                    'feature_day_of_month', 'feature_customer_age', 'feature_previous_transactions'])
data4Y = data1.filter(['label_error_code'])

data5X = data1.filter(['feature_transaction_usd_send', 'feature_local_receive','feature_kount_score',
                    'feature_kount_velocity', 'feature_sift_score','feature_days_since_first_completed',
                    'feature_six_month_send_limit', 'feature_account_type', #'feature_send_bank',
                    'feature_day_of_month', 'feature_customer_age', 'feature_previous_transactions'])
data5Y = data1.filter(['label_error_code'])

X = data1X
X = X.append(data2X)
X = X.append(data3X)
X = X.append(data4X)
X = X.append(data5X)

Y = data1Y
Y = Y.append(data2Y)
Y = Y.append(data3Y)
Y = Y.append(data4Y)
Y = Y.append(data5Y)

testX = test.filter(['feature_transaction_usd_send', 
                            'feature_local_receive',
                            'feature_kount_score',
                            'feature_kount_velocity',
                            'feature_sift_score',
                            'feature_days_since_first_completed',
                            'feature_six_month_send_limit',
                            'feature_account_type',
                            #'feature_send_bank',
                            'feature_day_of_month',
                            'feature_customer_age',
                            'feature_previous_transactions'])
testY = test.filter(['label_error_code'])

y_pred = gnb.fit(X, Y['label_error_code']).predict(testX)
print("Number of mislabeled points out of a total %d points : %d accuracy %0.2f" % 
      ( testX.shape[0],
        (testY['label_error_code'] != y_pred).sum(),
        ((testX.shape[0]-(testY['label_error_code'] != y_pred).sum())*100)/testX.shape[0]
      )
     )
