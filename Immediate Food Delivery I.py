import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # df = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']]
    # per = round((len(df)/len(delivery)) * 100,2)
    # return pd.DataFrame([per],columns = ['immediate_percentage'])

    series = delivery['order_date'] == delivery['customer_pref_delivery_date']
    print(series)
    imm = series.sum()
    return pd.DataFrame([round((imm/len(delivery)) * 100,2)],columns = ['immediate_percentage'])

    
    