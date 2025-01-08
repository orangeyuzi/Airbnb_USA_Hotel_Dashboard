from dash import Dash, html, dcc, Input, Output, State, no_update, ctx, ALL
import dash_bootstrap_components as dbc
import pandas as pd

# 導入其他模組中的函數
from src.generate_visualization import generate_map_plot, generate_hist_price, generate_hist_score, generate_bar, generate_pie
from src.data_clean import travel_data_clean

# Load cleaned Airbnb data
file_path = './data/newyork2.csv'
data = pd.read_csv(file_path, sep=',', dtype='unicode')
data = travel_data_clean(data)

# 欲添加的新字體
external_stylesheets = [
    "https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&family=Poller+One&display=swap",
    dbc.themes.BOOTSTRAP # Initialize the Dash app with a Bootstrap theme
]# [dbc.themes.BOOTSTRAP]

# 初始化應用程式
app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)

#----------------------------------------------------------------------------------------------------------------
# ------------------------------------------------CSS------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
# 存放各種外觀設定
# 整個頁面
container = {
    'padding': '0px', 
    'display': 'flex', 
    'flex-direction': 'column', 
    'margin': '0px', 
    'max-width': '100%', 
    'font-family': 'Open Sans', # 內文字體
    'backgroundColor': 'white',
    'minHeight': '100vh',
}
# ----------------------------
# ----------head set----------
# ----------------------------
# 整個頂部
head_block = {
    'color': 'white', 
    'display':'flex',  
    'justifyContent':'center', 
    'fontWeight': 'bold',
    'backgroundColor': '#10375c', 
    'padding': '20px 0px',
}
# 頂部大標題
title = {
    'align-self': 'center',
    'font-family': 'Poller One, serif', # 大標字體
    'padding-left': '50px'
}
# nav-bar
nav_bar = {
    'padding-left': '50px',
    "position": "relative"
}
# 按鍵設定
tab_style = {
    # 按鍵原樣
    'idle':{
        'padding': '0px', 
        'marginInline': '5px',
        'display':'flex',
        'alignItems':'center',
        'justifyContent':'center',
        'fontWeight': 'bold',
        'backgroundColor': '#10375c',
        'color': 'white',
        'border':'none',
        'fontSize': '26px',
        'height': '100px',
        'width': '150px'
    },
    # 按鍵點擊後
    'active':{
        'padding': '0px', 
        'marginInline': '5px',
        'display':'flex',
        'alignItems':'center',
        'justifyContent':'center',
        'fontWeight': 'bold',
        'border':'none',
        'textDecoration': 'underline',
        'color': 'white',
        'fontSize': '30px',
        'backgroundColor': '#10375c',
        'height': '100px',
        'width': '150px'
    },
    # 清單按鍵(特殊按鍵)
    'star_idle': {
        'padding': '34px 0px 0px 0px',
        'textAlign': 'center', 
        'fontSize': '26px',
        'backgroundImage': 'url(./assets/star.png)',
        'backgroundSize': '100px 100px',
        'backgroundRepeat': 'no-repeat',
        'backgroundPosition': 'center',
        'backgroundColor': '#10375c',
        'color': 'black',
        'fontWeight': 'blod',
        'border': 'none',
        'width': '150px'
    }
}
# 若清單裡有資料，就會有紅點
red_dot_style = {
    "width": "30px",
    "height": "30px",
    "borderRadius": "50%",
    "backgroundColor": "red",
    "color": "white",
    "textAlign": "center",
    "lineHeight": "30px",
    "fontSize": "12px",
    "position": "absolute",
    "top": "10px",
    "right": "80px",
    "border": "0px",
    "padding": "0px",
    "visibility": "visible",
    "overflow": "visible",
    "opacity": "1",
    "pointerEvents": "none", # 不能被點擊
    "display": "none" # 預設隱藏
}
# ----------------------------------
# ----------first page set----------
# ----------------------------------
# 頂部圖片
img = {
    'width': '100%',
    'padding': '0px',
    'overflow': 'hidden'
}
img_col = {
    'padding': '0px'
}

# 頁面設定
middle_block_1 = {
    'padding': '50px 100px 0px 100px',
    'display':'flex',
    'flexDirection': 'row',
    'justifyContent': 'space-evenly',
}
middle_block_2 = {
    'padding': '0px 100px 0px 100px'
}

# 下拉選單的標題
drop_down_title = {
    'color': 'black', 
    'margin': '15px', 
    'display':'flex', 
    'fontWeight': 'bold'
}

# 下拉選單(第一頁的)
drop_down = {
    'marginLeft': '5px',
}

# 最下面推薦住宿部分(整體)
hotel_three_block = {
    'display':'flex',
    'flexWrap': 'nowrap',
    'justifyContent': 'space-evenly',
    'padding': '50px 20px',
    'alignItems': 'flex-start',
}

# 最下面推薦住宿部分(每個旅館資訊)
hotel_three_card = {
    'display':'flex',
    'flexDirection': 'column',
    'padding': '10px',
    "backgroundColor": "white",
    'maxWidth': '400px',
    'boxSizing': 'border-box'
}

# 地圖散點圖
map_plot_graph = {
    'width': '90%', 
    'display': 'inline-block',
    'marginLeft': '12px',
    'marginTop': '20px'
}

# 最下面推薦住宿部分的標題+分隔線
hotel_three_title = {
    'position': 'absolute',
    'top': '-18px',
    'left': '50%',
    'transform': 'translateX(-50%)',
    'backgroundColor': 'white', 
    'padding': '0 10px',
    'fontSize': '24px',
    'fontWeight': 'bold',
    'color': '#B3B3B3' 
}
hotel_three_line = {
    'width': '100%',
    'borderTop': '2px solid #B3B3B3',
    'textAlign': 'center',
    'position': 'relative',
}

# 旅館圖片
no_pic_img = {
    'width': '100%',
    'padding': '10px 20px',
    'overflow': 'hidden',
    'height': '100%',
    'border': '1px solid black',
}

# 加入清單按鈕及上一頁下一頁按紐
button_set = {
    'alignSelf': 'center',
    'backgroundColor': '#EB8317',
    'color': 'white',
    'border': '0px',
    'fontWeight': 'bold',
    'padding': '10px 20px',
    'justifyContent':'center', 
}

# 旅館的名字
hotel_title = {
    'fontWeight': 'bold',
    'marginTop': '10px'
}
# -----------------------------------
# ----------second page set----------
# -----------------------------------
# 下拉選單(第二頁的)
drop_down_2 = {
    'marginLeft': '5px',
    'max-width': '50%'
}

# 下拉選單區塊
top_block = {
    'padding': '20px 100px 0px 100px'
}

# 圖表結果的標題部分
multi_graph_title_block = {
    'color': 'white', 
    'display':'flex',
    'alignItem':'center', 
    'justifyContent':'center',
    'backgroundColor': '#10375c', 
    'padding': '20px 0px',
    'margin': '50px 0px'
}
multi_graph_title = {
    'fontSize': '26px',
    'fontWeight': 'bold',
    'margin': '0px'
} # 圖表結果的標題部分(文字)

# 左邊圖表排版
graph_left = {
    'margin': '50px 0px',
    'display': 'inline-block',
    'overflow': 'hidden',
    'display':'flex', 
    'justifyContent':'left',
}

# 右邊圖表排版
graph_right = {
    'margin': '50px 0px', 
    'display': 'inline-block',
    'overflow': 'hidden',
    'display':'flex',
    'justifyContent':'right',
}
# ----------------------------------
# ----------third page set----------
# ----------------------------------
# 每個查詢結果區塊
hotel_info_block = {
    "border": "1px solid #ddd",
    "padding": "50px",
    "borderRadius": "5px",
    "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.1)",
    'backgroundColor': 'rgba(16, 55, 92, 0.12)',
    'display': 'flex',
    'margin': '30px 0px 100px 0px',
    'position': 'relative'
}

# 上一頁下一頁按鈕的區塊
page_set = {
    'display': 'flex',
    'justifyContent':'center',
}

# 上一頁下一頁按鈕的文字
page_info = {
    'margin': '10px',
    'fontWeight': 'bold',
}

# 查詢結果中，旅館資訊的部分
hotel_content = {
    "marginLeft": "150px",
}

# 查詢結果中的加入清單按鈕
button_set_2 = {
    'backgroundColor': '#EB8317',
    'color': 'white',
    'border': '0px',
    'fontWeight': 'bold',
    'padding': '10px 40px',
    'height': '50px',
    'justifyContent':'right',
    'position': 'absolute',
    'bottom': '50px',
    'right': '50px'
}

# 旅館資訊中的旅館名稱
hotel_title_2 = {
    'fontWeight': 'bold',
    'margin': '0px 0px 20px 0px'
}

# 旅館資訊中的旅館價格
hotel_price = {
    'fontWeight': 'bold',
    'margin': '30px 0px 0px 0px'
}
# ----------------------------------
# ----------forth page set----------
# ----------------------------------
# 清單頁面的標題
list_title_block = {
    'color': 'white', 
    'display':'flex',
    'alignItem':'center', 
    'justifyContent':'center',
    'backgroundColor': '#EB8317', 
    'padding': '20px 0px',
    'margin': '50px 0px'
}
list_title = {
    'fontSize': '30px',
    'fontWeight': 'bold',
    'margin': '0px'
} # 清單頁面的標題文字

# X部分的設定
button_set_3 = {
    'backgroundColor': 'rgba(91, 145, 196, 0.12)',
    'color': 'black',
    'border': '0px',
    'fontWeight': 'bold',
    'padding': '10px',
    'justifyContent':'right',
    'position': 'absolute',
    'top': '50px',
    'right': '50px'
}

# 最下面固定住的總價區塊
all_price_block = {
    'color': 'white', 
    'display':'flex',
    'alignItem':'center', 
    'justifyContent':'center',
    'fontWeight': 'bold',
    'backgroundColor': '#EB8317',
    'position': 'fixed', 
    'padding': '30px 20px',
    'bottom': '0px',
    'width': '100%',
    'overflow': 'hidden',
    'boxSizing': 'content-box'
}


#----------------------------------------------------------------------------------------------------------------
#---------------------------------------------HTML---------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
# 定義系統的佈局
app.layout = html.Div([
    dcc.Store(id="saved-items", data=[]),
    dbc.Container([
        html.Div([
            # 頂部的切換頁面
            dbc.Row([
                dbc.Col(html.H2("Find the Perfect Hotel for You!"), style=title),
                dbc.Col(
                    dcc.Tabs(id='graph-tabs', value='all_hotel', children=[
                        # 總共四個頁面
                        dcc.Tab(label='總覽', value='all_hotel',style=tab_style['idle'],selected_style=tab_style['active']),
                        dcc.Tab(label='住宿比較', value='hotel_compare',style=tab_style['idle'],selected_style=tab_style['active']),
                        dcc.Tab(label='選擇旅館', value='choose_hotel',style=tab_style['idle'],selected_style=tab_style['active']),
                        dcc.Tab(label='清單', value='hotel_list',style=tab_style['star_idle'],selected_style=tab_style['active']),
                        # 紅點顯示
                        html.Div(
                            id="red-dot",
                            children=[
                               html.Div("0", id="red-dot-text")
                            ],  # 初始數字為 0
                            style=red_dot_style
                        )
                    ], style = nav_bar)
                ),
            ], style = head_block),
        ]),

        # 用於顯示不同頁面的內容
        html.Div(id='graph-content')

    ], style=container)

])
# 呼叫切換頁面
@app.callback(
    Output('graph-content', 'children'),
    [Input('graph-tabs', 'value')]
)
def render_tab_content(tab):
    # 總覽
    if tab == 'all_hotel':
        return html.Div([
            # 首頁圖片
            dbc.Row([
                dbc.Col(html.Img(src="./assets/city.jpg", style=img), style=img_col),
            ]),
            # 篩選地區及價格範圍
            dbc.Row([
                dbc.Col([
                    html.H5("選擇地區", style=drop_down_title),
                    dcc.Dropdown(
                        id='dropdown-group-1',
                        placeholder='選擇地區',
                        options=[{'label': 'All', 'value': 'All'}] + [{'label': str(i), 'value': str(i)} for i in data['neighbourhood_group'].unique()],
                        style = drop_down   
                    )
                ]),
                dbc.Col([
                    html.H5("選取價格範圍(USD$)", style=drop_down_title),
                    dcc.RangeSlider(id='slider-1', value=[0, max(data['price_sum'])], step=100, min=0, max=max(data['price_sum']))
                ], style = drop_down ),
            ], style=middle_block_1),
            # 顯示地圖散點圖
            dbc.Row([
                dbc.Col([
                    dcc.Loading([
                        html.Div(id='tabs-content-1'),
                    ], 
                    type='default', color='white')
                ]),
            ], style=middle_block_2),
            # 推薦住宿/旅館(以三個為主)
            dbc.Row([
                dbc.Col([
                    html.Div(
                        style=hotel_three_line,
                        children=[
                            html.Div("推薦住宿", style=hotel_three_title),
                        ]
                    )
                ]),
            ], style=middle_block_2),
            dbc.Row([
                dbc.Col([
                    dcc.Loading([
                        html.Div(id='three-content', style=hotel_three_block),
                    ])
                ]),
            ], style=middle_block_2),
        ])
    # 旅館比較
    elif tab == 'hotel_compare':
        return html.Div([
            # 篩選地區(非必選)
            dbc.Row([
                dbc.Col([
                    html.H5("選擇地區", style=drop_down_title),
                    dcc.Dropdown(
                        id='dropdown-group-2',
                        placeholder='選擇地區',
                        options=[{'label': str(i), 'value': str(i)} for i in data['neighbourhood_group'].unique()],
                        style = drop_down_2   
                    )
                ]),
            ], style=top_block),
            # 下拉式選單顯示該地區囊括的景點(預設是全部地區的景點)，並篩選景點(必選)
            dbc.Row([
                dbc.Col([
                    html.H5("選擇景點", style=drop_down_title),
                    dcc.Loading([
                        html.Div(id='dropdown-group-5'),
                    ])
                ]),
            ], style=top_block),
            dbc.Row([
                dbc.Col([
                   html.H3("旅館分析列表", style=multi_graph_title), 
                ], style=multi_graph_title_block),
            ]),
            dbc.Row([
                # 價格分布直方圖
                dbc.Col([
                    dcc.Loading([
                        html.Div(id='tabs-content-2'),
                    ])
                ]),
                # 評分分布長條圖
                dbc.Col([
                    dcc.Loading([
                        html.Div(id='score-content'),
                    ])
                ], style={'padding': '0px'}),
            ]),
            dbc.Row([
                # 旅館類型長條圖
                dbc.Col([
                    dcc.Loading([
                        html.Div(id='type-content'),
                    ])
                ]),
                # 房東認證與否圓餅圖
                dbc.Col([
                    dcc.Loading([
                        html.Div(id='host-content'),
                    ])
                ], style={'padding': '0px'}),
            ]),
        ])
    # 旅館選擇
    elif tab == 'choose_hotel':
        return html.Div([
            # 篩選地區、價格範圍、評價範圍
            dbc.Row([
                dbc.Col([
                    html.H5("選擇地區", style=drop_down_title),
                    dcc.Dropdown(
                        id='dropdown-group-5',
                        placeholder='選擇地區',
                        options=[{'label': 'All', 'value': 'All'}] + [{'label': str(i), 'value': str(i)} for i in data['neighbourhood_group'].unique()],
                        style={'margin': '10px'}   
                    )
                ], style = drop_down_2),
            ], style = top_block),
            dbc.Row([
                dbc.Col([
                    html.H5("選取價格範圍(USD$)", style=drop_down_title),
                    dcc.RangeSlider(id='slider-2', value=[0, max(data['price_sum'])], step=100, min=0, max=max(data['price_sum']))
                ], style = drop_down_2 ),
            ], style=top_block),
            dbc.Row([
                dbc.Col([
                    html.H5("選取評價範圍(6代表無評價)", style=drop_down_title),
                    dcc.RangeSlider(id='slider-3', value=[1, max(data['review_rate_number'])], step=1, min=1, max=max(data['review_rate_number']))
                ], style = drop_down_2 ),
            ], style=top_block),
            dbc.Row([
                dbc.Col([
                    html.H5("查詢ID", style=drop_down_title),
                    dcc.Input(
                        id='search-1',
                        type='text',
                        value="",  # 預設值為空值
                        style={'margin': '15px'}
                    )
                ], style = drop_down_2 ),
            ], style=top_block),
            # 動態顯示搜索成果
            dbc.Row([
                dbc.Col([
                    # 搜索筆數顯示
                    html.Div(id="result-count", style=drop_down_title),
                    html.Div(
                        children=[
                            html.Button("上一頁", id="prev-page", n_clicks=0, style=button_set),
                            html.P(id="page-info", style=page_info),
                            html.Button("下一頁", id="next-page", n_clicks=0, style=button_set),
                        ], style = page_set
                    )
                ]),
            ], style=top_block),
            dbc.Row([
                dbc.Col([
                    # 儲存當前頁面的組件
                    dcc.Store(id="current-page", data=1),
                    dcc.Loading([
                        # 顯示篩選結果的容器
                        html.Div(id="item-container"),
                    ]),
                    html.Div(
                        children=[
                            html.Button("上一頁", id="prev-page", n_clicks=0, style=button_set),
                            html.P(id="page-info", style=page_info), # 當前頁面及搜索筆數顯示
                            html.Button("下一頁", id="next-page", n_clicks=0, style=button_set),
                        ], style=page_set
                    )
                ]),
            ], style=middle_block_2),
        ])
    # 清單
    elif tab == 'hotel_list':
        return html.Div([
             dbc.Row([
                dbc.Col([
                   html.H3("清單", style=list_title), 
                ], style=list_title_block),
            ]),
            # 加入清單的旅館資訊會顯示在這邊
            dbc.Row([
                dbc.Col([
                    dcc.Loading([
                        html.Div(id="saved-list"),
                    ]),
                ], style={'padding': '0px'}),
            ]),
            # 這是一個固定的區塊，放置總價
            dbc.Row([
                dbc.Col([
                    dcc.Loading([
                        html.Div(id="all-hotel-price"),
                    ]),
                ], style={'padding': '0px'}),
            ], style={'padding': '0px'}),
        ])
    else:
        return html.Div("選擇的標籤頁不存在。", style=drop_down_title)
    
#----------------------------------------------------------------------------------------------------------------
#---------------------------------------------CALLBACK-----------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
# ------第一頁--------
# 地圖散點圖回調函數
@app.callback(
    [Output('tabs-content-1', 'children'),  # 更新地圖區域內容
     Output('three-content', 'children')],  # 更新推薦住宿區域內容
    [Input('dropdown-group-1', 'value'),    # 地區選擇下拉選單的值
     Input('slider-1', 'value'),           # 價格範圍滑塊的值
     Input('graph-tabs', 'value')]         # 當前選擇的標籤頁
)
def update_map(dropdown_value_1, slider_value_1, tab):
    # 如果當前標籤頁不是 "all_hotel"，則不更新
    if tab != 'all_hotel':
        return no_update
    
    # 獲取原始數據
    df = data
    
    # 調用地圖散點生成函數生成圖表
    fig1 = generate_map_plot(df, dropdown_value_1, slider_value_1)
    
    # 如果選擇了具體的地區，過濾數據
    if dropdown_value_1:
        df = df[data["neighbourhood_group"] == dropdown_value_1]
    
    # 根據價格範圍進一步過濾數據，並按照評論數降序排列
    df = df[(df["price_sum"] >= slider_value_1[0]) & (df["price_sum"] <= slider_value_1[1])].sort_values(by='number_of_reviews', ascending=False)

    # 構建推薦住宿資訊卡片
    items = [
        html.Div(
            children=[
                html.Img(src="./assets/no_pic.jpg", style=no_pic_img),
                html.H5(item["name"], style=hotel_title),
                html.P(f"地區: {item['neighbourhood_group']}"),
                html.P(f"評價: {item['review_rate_number']}分"),
                html.P(f"房型: {item['room_type']}"),
                html.P(f"房東認證: {item['host_identity_verified']}"),  # 房東認證狀態
                html.P(f"價格: ${item['price_sum']}"),
                html.Button("加入清單", id={"type": "add-btn", "index": item["id"]}, style=button_set)  # 加入清單按鈕
            ],
            style=hotel_three_card
        )
        for _, item in df.head(3).iterrows()  # 取前三個推薦住宿
    ]
    
    # 返回更新的地圖圖表和推薦住宿卡片
    return html.Div([
        dcc.Graph(id='graph1', figure=fig1),  # 地圖圖表
    ], style=map_plot_graph), items


# ------第一頁--------
# 更新選單回調
@app.callback(
    Output('dropdown-group-5', 'children'),  # 更新第二個選單的內容
    [Input('dropdown-group-2', 'value'),     # 從第一個選單獲取選中的值
     Input('graph-tabs', 'value')]          # 當前選中的標籤頁
)
def update_dropdown(dropdown_value, tab):
    # 如果當前標籤頁不是"hotel_compare"，則不進行更新
    if tab != 'hotel_compare':
        return no_update
    
    # 如果第一個選單未選擇任何值，返回包含所有景點的下拉選單
    if dropdown_value is None:
        return dcc.Dropdown(
            id='dropdown-group-3',
            placeholder='選擇景點',
            options=[{'label': str(i), 'value': str(i)} for i in data['neighbourhood'].unique()],
            style=drop_down_2
        )

    # 根據第一個選單的值過濾數據並返回相應的下拉選單
    df = data[data["neighbourhood_group"] == dropdown_value]
    return dcc.Dropdown(
        id='dropdown-group-3',
        placeholder='選擇景點',
        options=[{'label': str(i), 'value': str(i)} for i in df['neighbourhood'].unique()],
        style=drop_down_2
    )

# 價格分布圖回調
@app.callback(
    Output('tabs-content-2', 'children'),  # 更新第一個圖表的內容
    [Input('dropdown-group-3', 'value'),   # 從第二個選單獲取選中的值
     Input('graph-tabs', 'value')]        # 當前選中的標籤頁
)
def update_price_hist(dropdown_value, tab):
    # 如果當前標籤頁不是"hotel_compare"，則不進行更新
    if tab != 'hotel_compare':
        return no_update

    # 獲取原始數據
    df = data
    
    # 根據選中的值生成價格分布直方圖
    fig2 = generate_hist_price(df, dropdown_value)

    return html.Div([
        dcc.Graph(id='graph2', figure=fig2),  # 渲染價格分布直方圖
    ], style=graph_left)

# 評價分布圖回調
@app.callback(
    Output('score-content', 'children'),  # 更新第二個圖表的內容
    [Input('dropdown-group-3', 'value'),  # 從第二個選單獲取選中的值
     Input('graph-tabs', 'value')]       # 當前選中的標籤頁
)
def update_score_bar(dropdown_value, tab):
    # 如果當前標籤頁不是"hotel_compare"，則不進行更新
    if tab != 'hotel_compare':
        return no_update

    # 獲取原始數據
    df = data
    
    # 根據選中的值生成評價分布圖
    fig3 = generate_hist_score(df, dropdown_value)

    return html.Div([
        dcc.Graph(id='graph3', figure=fig3),  # 渲染評價分布直方圖
    ], style=graph_right)

# 旅館類型長條圖回調
@app.callback(
    Output('type-content', 'children'),   # 更新第三個圖表的內容
    [Input('dropdown-group-3', 'value'),  # 從第二個選單獲取選中的值
     Input('graph-tabs', 'value')]       # 當前選中的標籤頁
)
def update_bar(dropdown_value, tab):
    # 如果當前標籤頁不是"hotel_compare"，則不進行更新
    if tab != 'hotel_compare':
        return no_update

    # 獲取原始數據
    df = data
    
    # 根據選中的值生成旅館類型長條圖
    fig4 = generate_bar(df, dropdown_value)

    return html.Div([
        dcc.Graph(id='graph4', figure=fig4),  # 渲染旅館類型長條圖
    ], style=graph_left)

# 房東認證與否圓餅圖回調
@app.callback(
    Output('host-content', 'children'),   # 更新第四個圖表的內容
    [Input('dropdown-group-3', 'value'),  # 從第二個選單獲取選中的值
     Input('graph-tabs', 'value')]       # 當前選中的標籤頁
)
def update_pie(dropdown_value, tab):
    # 如果當前標籤頁不是"hotel_compare"，則不進行更新
    if tab != 'hotel_compare':
        return no_update

    # 獲取原始數據
    df = data

    # 根據選中的值生成房東認證與否圓餅圖
    fig5 = generate_pie(df, dropdown_value)

    return html.Div([
        dcc.Graph(id='graph5', figure=fig5),  # 渲染房東認證與否圓餅圖
    ], style=graph_right)

# ------第三頁--------
# 搜尋結果回調
@app.callback(
    [Output("item-container", "children"),
     Output("result-count", "children"),
     Output("page-info", "children"),
     Output("current-page", "data")],
    [Input('dropdown-group-5', 'value'),
     Input('slider-2', 'value'),
     Input('slider-3', 'value'),
     Input("prev-page", "n_clicks"),
     Input("next-page", "n_clicks"),
     Input("search-1", "value"),
     Input('graph-tabs', 'value')],
     State("current-page", "data")
)
def update_result(dropdown_value_1, slider_value_1, slider_value_2, prev_page, next_page, search_value, tab, current_page):
    # 如果當前標籤頁不是"choose_hotel"，則不進行更新
    if tab != 'choose_hotel':
        return no_update

    # 根據價格範圍過濾數據
    filtered_df = data[(data["price_sum"] >= slider_value_1[0]) & (data["price_sum"] <= slider_value_1[1])]
    # 根據評價範圍過濾數據
    filtered_df = filtered_df[(filtered_df["review_rate_number"] >= slider_value_2[0]) & (filtered_df["review_rate_number"] <= slider_value_2[1])]
    # 如果選擇了特定地區，進一步過濾數據
    if dropdown_value_1 and dropdown_value_1 != 'All':
        filtered_df = filtered_df[filtered_df["neighbourhood_group"] == dropdown_value_1]
    # 如果有查詢值，直接抓取資料(第一筆)
    if search_value:
        filtered_df = data[data["id"] == search_value].head(1)

    # 計算結果數量
    result_num = len(filtered_df)
    ITEMS_PER_PAGE = 10  # 每頁顯示的項目數
    total_pages = max(1, -(-result_num // ITEMS_PER_PAGE))  # 總頁數，向上取整

    # 更新當前頁碼
    triggered_id = ctx.triggered_id
    if triggered_id == "prev-page" and current_page > 1:
        current_page -= 1
    elif triggered_id == "next-page" and current_page < total_pages:
        current_page += 1

    # 計算顯示範圍
    start_idx = (current_page - 1) * ITEMS_PER_PAGE
    end_idx = start_idx + ITEMS_PER_PAGE

    # 篩選出範圍內的資料
    page_data = filtered_df.iloc[start_idx:end_idx]

    # 生成當前頁面的項目列表
    items = [
        html.Div(
            children=[
                html.Img(src="./assets/no_pic.jpg"),
                html.Div(
                    children=[
                        html.H4(item["name"], style=hotel_title_2),
                        html.H5(f"地區: {item['neighbourhood_group']}"),
                        html.H5(f"評價: {item['review_rate_number']}分"),
                        html.H5(f"房型: {item['room_type']}"),
                        html.H5(f"房東認證: {item['host_identity_verified']}"),
                        html.H3(f"USD${item['price_sum']}", style=hotel_price)], style=hotel_content
                ),
                html.Button("加入清單", id={"type": "add-btn", "index": item["id"]}, style=button_set_2)
            ], style=hotel_info_block
        )
        for _, item in page_data.iterrows()
    ]

    # 更新頁面信息
    page_info = f"第{current_page}頁 / 共{total_pages}頁 "

    return items, html.P(f"總共搜尋到 {result_num} 筆資料"), page_info, current_page

# 處理加入清單的邏輯
@app.callback(
    Output("saved-items", "data", allow_duplicate=True),
    [Input({"type": "add-btn", "index": ALL}, "n_clicks"),
     Input('graph-tabs', 'value')],
    State("saved-items", "data"),
    prevent_initial_call=True
)
def add_to_list(n_clicks, tab, saved_items):
    # 檢查是否點擊過按鈕
    if all(click is None for click in n_clicks):  # 如果所有按鈕都沒有被點擊
        return saved_items

    # 確保有按鈕被點擊
    if not any(click is not None for click in n_clicks):
        return saved_items
    
    # 獲取觸發的按鈕 ID
    triggered = ctx.triggered_id

    # 確保觸發的是新增按鈕
    if not triggered or triggered == "graph-tabs" or triggered.get("type") != "add-btn":
        return saved_items

    # 獲取按鈕的 index
    item_id = triggered.get("index")

    # 獲取對應的數據項目
    item = data[data["id"] == item_id].iloc[0].to_dict()
    
    # 檢查是否已存在於清單中
    if item not in saved_items:
        saved_items.append(item)
    
    return saved_items

# 更新紅點狀態
@app.callback(
    [Output("red-dot-text", "children"), 
     Output("red-dot", "style"), ],
    [Input("saved-items", "data"),
     Input('graph-tabs', 'value')]
)
def update_red_dot(saved_items, tab):
    # 如果清單為空，初始化為空列表
    if not saved_items:
        saved_items = []
    count = len(saved_items)  # 獲取清單中項目的數量
    updated_style = red_dot_style.copy()

    # 當 count > 0 且 tab != "hotel_list" 時顯示紅點
    if count > 0 and tab != "hotel_list":
        updated_style["visibility"] = "visible"
        updated_style["opacity"] = "1"
        updated_style["display"] = "block"
    
    return str(count), updated_style

# ------第四頁--------
# 更新清單
@app.callback(
    Output("saved-list", "children"),
    [Input("saved-items", "data"),
     Input('graph-tabs', 'value')]
)
def update_hotel_list(saved_items, tab):
    # 如果當前標籤頁不是"hotel_list"，則不進行更新
    if tab != 'hotel_list':
        return no_update

    # 計算平均價格
    mean_price = round(data["price_sum"].mean())

    # 更新保存列表
    saved_list = [
        html.Div(
            children=[
                html.Img(src="./assets/no_pic.jpg"),
                html.Div(
                    children=[
                        html.H4(item["name"], style=hotel_title_2),
                        html.H5(f"地區: {item['neighbourhood_group']}"),
                        html.H5(f"評價: {item['review_rate_number']}分"),
                        html.H5(f"房型: {item['room_type']}"),
                        html.H5(f"房東認證: {item['host_identity_verified']}"),
                        html.H3(f"USD${item['price_sum']}", style=hotel_price),
                        html.P(f"比平均價格優惠USD${mean_price - item['price_sum']}")], style=hotel_content
                ),
                html.Button("X", id={"type": "del-btn", "index": item["id"]}, style=button_set_3)
            ], style=hotel_info_block
        )
        for item in saved_items
    ]
    return saved_list

# 更新總價
@app.callback(
    Output("all-hotel-price", "children"),
    [Input("saved-items", "data"),
     Input('graph-tabs', 'value')]
)
def update_hotel_list(saved_items, tab):
    # 如果當前標籤頁不是"hotel_list"，則不進行更新
    if tab != 'hotel_list':
        return no_update

    # 計算總價
    price = 0
    for item in saved_items:
        price += item["price_sum"]

    # 更新總價顯示
    all_hotel_price = [
        html.Div(
            children=[html.H3(f"總金額{price}元", style={'fontWeight': 'bold'})
        ], style=all_price_block)
    ]
    return all_hotel_price

# 處理刪除清單項目的邏輯
@app.callback(
    Output("saved-items", "data", allow_duplicate=True),
    Input({"type": "del-btn", "index": ALL}, "n_clicks"),
    State("saved-items", "data"),
    prevent_initial_call=True
)
def del_list(n_clicks, saved_items):
    # 如果沒有按鈕被點擊，則返回原清單
    if not any(n_clicks):
        return saved_items
    
    # 獲取觸發的按鈕 ID
    triggered = ctx.triggered_id

    # 確保觸發的是刪除按鈕
    if not triggered or triggered.get("type") != "del-btn":
        return saved_items

    # 獲取按鈕的 index
    item_id = triggered.get("index")
    
    # 返回移除對應項目的清單
    return [item for item in saved_items if item["id"] != item_id]

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)
