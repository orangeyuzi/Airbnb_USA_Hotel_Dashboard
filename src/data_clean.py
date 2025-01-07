import pandas as pd

def travel_data_clean(travel_df):
    # 因為原檔過大，有些資料有位移、亂碼及誤植的狀況，因此有對原檔先做一些手動篩選及處理
    # 並刪除一些不必要的column，和必要欄位中的空值row

    # 去除空的column(可能因為我在刪column的時候沒刪好)
    travel_df = travel_df.copy()
    travel_df = travel_df.loc[:, travel_df.isnull().mean() < 0.9]

    # 處理價格欄位
    travel_df.loc[:, 'price'] = travel_df.loc[:, 'price'].str.replace('$', '')
    travel_df.loc[:, 'price'] = travel_df.loc[:, 'price'].str.replace(',', '')
    travel_df.loc[:, 'price'] = travel_df.loc[:, 'price'].str.replace(' USD', '')
    travel_df.loc[:, 'price'] = travel_df.loc[:, 'price'].astype(float)

    # 處理服務費欄位
    travel_df.loc[:, 'service_fee'] = travel_df.loc[:, 'service_fee'].str.replace('$', '')
    travel_df.loc[:, 'service_fee'] = travel_df.loc[:, 'service_fee'].str.replace(',', '')
    travel_df.loc[:, 'service_fee'] = travel_df.loc[:, 'service_fee'].str.replace(' USD', '')
    travel_df.loc[:, 'service_fee'] = travel_df.loc[:, 'service_fee'].astype(float)

    # 去除空值及填充缺失值
    travel_df = travel_df.infer_objects()
    travel_df.loc[:, 'service_fee'] = travel_df['service_fee'].fillna(0)
    travel_df.loc[:, 'review_rate_number'] = travel_df['review_rate_number'].fillna(6)

    # 處理評分欄位，將評分轉換為整數型態
    travel_df.loc[:, 'review_rate_number'] = travel_df['review_rate_number'].astype(int)
    
    # 計算總價，並建立新欄位 
    travel_df.loc[:, 'price_sum'] = travel_df.loc[:, 'price'] + travel_df.loc[:, 'service_fee']

    # 將經緯度轉換為數值型態
    travel_df.loc[:, 'lat'] = pd.to_numeric(travel_df['lat'], errors='coerce')
    travel_df.loc[:, 'long'] = pd.to_numeric(travel_df['long'], errors='coerce')
    
    return travel_df