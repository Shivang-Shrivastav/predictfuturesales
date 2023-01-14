
import pandas as pd
import pickle5 as pickle

df = pd.read_csv('df_data.csv')

path = 'LGBM_Final_Model.pkl'

with open(path,'rb') as dt:
	model = pickle.load(dt)

# model = pickle.load(open('LGBM_Final_Model.pkl', 'rb'))

X_test = df[df["date_block_num"]==34]
X_test = X_test.drop("item_cnt_month", axis=1)



def forecast(item_id,shop_id, X_test = X_test):

  data = X_test[(X_test['shop_id'] == shop_id) &  (X_test['item_id'] == item_id) ]
  result = model.predict(data, predict_disable_shape_check=True)
  result = int(result)
  return result