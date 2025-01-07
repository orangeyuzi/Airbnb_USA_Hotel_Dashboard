import plotly.express as px
import plotly.colors as colors

# 視覺化統計圖

# 地圖散點圖
# 此函數生成一個地圖散點圖，根據價格範圍和選定的地區過濾資料，並以取消方式作為顏色分類
def generate_map_plot(df, dropdown_value_1, slider_value_1):
    # 過濾價格範圍
    filtered_df = df[(df["price_sum"] >= slider_value_1[0]) & (df["price_sum"] <= slider_value_1[1])]
    c_lat_lon = dict(lat=filtered_df['lat'].median(), lon=filtered_df['long'].median())

    # 如果有選擇地區，則進行地區過濾
    if dropdown_value_1 and dropdown_value_1 != 'All':
        filtered_df = filtered_df[filtered_df["neighbourhood_group"] == dropdown_value_1]
        c_lat_lon = dict(lat=filtered_df['lat'].median(), lon=filtered_df['long'].median())

    # 設定取消政策的顏色映射
    color_map = {
        'strict': '#1f77b4',  # 藍色
        'flexible': '#ff7f0e',  # 橙色
        'moderate': '#2ca02c'   # 綠色
    }

    # 生成散點地圖
    fig = px.scatter_map(
        filtered_df, 
        lat="lat", 
        lon="long", 
        color="cancellation_policy",
        hover_name="name",            # 顯示名稱
        hover_data={"host name": True, "review_rate_number": True, "room_type": True, "host_identity_verified": True},    # 顯示其他詳細資訊
        center=c_lat_lon,
        zoom=12, 
        color_discrete_map=color_map,
        title='旅館分布'
    )

    # 更新佈局，防止溢出，並設定標題
    fig.update_layout(
        title_font_shadow='1px 1px #558ABB', 
        template='plotly_white', 
        font=dict(color='black'),
        margin=dict(l=0, r=0, t=0),  # 防止圖表內容溢出
        mapbox_style="open-street-map",
    )

    return fig

# 價格分布圖
# 此函數生成一個價格分布的直方圖
def generate_hist_price(df, dropdown_value):
    if dropdown_value is None:
        # 如果沒有選擇有效選項，回傳空圖表
        fig = px.bar(title="請選擇有效的選項")
        fig.update_layout(
            template='plotly', 
            plot_bgcolor="#10375c",
            paper_bgcolor="#10375c",
            font=dict(color='white')
        )
        return fig

    # 過濾選定地區的資料
    df_filtered = df[df['neighbourhood'] == dropdown_value]

    # 生成價格分布圖
    fig = px.histogram(df_filtered, x='price_sum', nbins=20, title=f'{dropdown_value}附近旅館的價格分布')
    fig.update_xaxes(title_text="價格")
    fig.update_traces(marker_color='#f3c623')
    fig.update_layout(
        template='plotly', 
        plot_bgcolor="#10375c",
        paper_bgcolor="#10375c",
        font=dict(color='white')
    )
    return fig

# 評價分布圖
# 此函數生成旅館的評價分布圖
def generate_hist_score(df, dropdown_value):
    if dropdown_value is None:
        # 如果沒有選擇有效選項，回傳空圖表
        fig = px.bar(title="請選擇有效的選項")
        fig.update_layout(
            template='plotly', 
            plot_bgcolor="#10375c",
            paper_bgcolor="#10375c",
            font=dict(color='white')
        )
        return fig

    # 過濾選定地區的資料
    df_filtered = df[df['neighbourhood'] == dropdown_value]
    # 替換評價中的特殊值
    df_filtered.loc[:, 'review_rate_number'] = df_filtered.loc[:, 'review_rate_number'].replace({6: '無'})

    # 計算評價的分布情況
    type_counts = df_filtered['review_rate_number'].value_counts().reindex([1, 2, 3, 4, 5, '無'], fill_value=0).reset_index()
    type_counts.columns = ['review_rate_number', 'count']
    type_counts['percentage'] = (type_counts['count'] / type_counts['count'].sum()) * 100

    # 生成評價分布的長條圖
    fig = px.bar(type_counts, x='review_rate_number', y='count',
                 color='count', text='percentage',
                 title=f'{dropdown_value}附近旅館的評價分布',
                 labels={'count': 'Count', 'index': 'room_type', 'percentage': 'Percentage'},
                 color_continuous_scale='Viridis')
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig.update_xaxes(title_text="評價")
    fig.update_traces(marker_color='#f3c623')
    fig.update_layout(
        template='plotly', 
        plot_bgcolor="#10375c",
        paper_bgcolor="#10375c",
        font=dict(color='white')
    )
    return fig

# 各類型房源數量長條圖
# 此函數生成一個長條圖，顯示各類型房源的數量
def generate_bar(df, dropdown_value):
    if dropdown_value is None:
        # 如果沒有選擇有效選項，回傳空圖表
        fig_bar = px.bar(title="請選擇有效的選項")
        fig_bar.update_layout(
            template='plotly', 
            plot_bgcolor="#10375c",
            paper_bgcolor="#10375c",
            font=dict(color='white')
        )
        return fig_bar

    # 過濾選定地區的資料
    df_filtered = df[df['neighbourhood'] == dropdown_value]

    # 計算各類型房源的數量
    type_counts = df_filtered['room_type'].value_counts().reset_index()
    type_counts.columns = ['room_type', 'count']
    type_counts['percentage'] = (type_counts['count'] / type_counts['count'].sum()) * 100

    # 生成長條圖
    fig_bar = px.bar(type_counts, x='room_type', y='count',
                     color='count', text='percentage',
                     title=f'{dropdown_value}附近旅館的各類型房源數量長條圖',
                     labels={'count': 'Count', 'index': 'room_type', 'percentage': 'Percentage'},
                     color_continuous_scale='Viridis')

    fig_bar.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig_bar.update_xaxes(title_text="各類型房源")
    fig_bar.update_yaxes(title_text="數量")
    fig_bar.update_layout(yaxis=dict(categoryorder='total ascending'))
    fig_bar.update_layout(
        template='plotly', 
        plot_bgcolor="#10375c",
        paper_bgcolor="#10375c",
        font=dict(color='white')
    )
    return fig_bar

# 圓餅圖
# 此函數生成一個圓餅圖，顯示房東是否認證的比例
def generate_pie(df, dropdown_value):
    if dropdown_value is None:
        # 如果沒有選擇有效選項，回傳空圖表
        fig_pie = px.pie(title="請選擇有效的選項")
        fig_pie.update_layout(
            template='plotly', 
            plot_bgcolor="#10375c",
            paper_bgcolor="#10375c",
            font=dict(color='white')
        )
        return fig_pie

    # 過濾選定地區的資料
    df_group = df[df['neighbourhood'] == dropdown_value]

    # 計算房東認證與否的分布
    df_counts = df_group['host_identity_verified'].value_counts().reset_index(name='count')
    df_counts['percentage'] = (df_counts['count'] / df_counts['count'].sum()) * 100

    # 生成圓餅圖
    fig_pie = px.pie(
        df_counts, 
        names=["verified", "unconfirmed"],  # 圓餅圖的標籤欄位
        values='count',  # 圓餅圖的數值欄位 
        color='count',
        title=f'{dropdown_value}附近旅館的房東認證與否(不完全代表安全性，但認證可以降低詐騙行為)',
        color_discrete_sequence=colors.sequential.Viridis  # 圖表標題
    )

    # 更新圖表樣式
    fig_pie.update_layout(
        template='plotly', 
        plot_bgcolor="#10375c",
        paper_bgcolor="#10375c",
        font=dict(color='white')
    )
    return fig_pie
