# Copyright 2018-2021 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def register():
    import streamlit as st

    st.sidebar.success("請選擇功能頁")
    new_username = st.text_input('請輸入註冊用戶名:', '您的名子')
    new_password = st.text_input('請輸入新用戶密碼:','abc')
    new_password_again = st.text_input('請再次確認新用戶密碼:')  
    if new_password == new_password_again:
        new_gender = st.selectbox(
    '請輸入性別:', ('男', '女'))
        new_age = st.slider('請輸入芳齡:', 0, 120,30, step= 1)
        new_cellphone = st.text_input('請輸入手機號碼:')
        #st.write("特惠活動滿八千免運，請輸入您的總預算:")
        moeny = st.slider('特惠活動滿八千免運，請輸入您的總預算:', 0, 50000, step= 1000)
        st.write('你的預算:', moeny)
    else: 
        st.text('請再確認你的密碼')
    st.markdown("""  """
    )


# Turn off black formatting for this function to present the user with more
# compact code.
# fmt: off
def checkout():
    import streamlit as st
    import pandas as pd
    import pydeck as pdk

    from urllib.error import URLError

    @st.cache
    def from_data_file(filename):
        url = (
            "http://raw.githubusercontent.com/streamlit/"
            "example-data/master/hello/v1/%s" % filename)
        return pd.read_json(url)

    try:
        
        st.sidebar.markdown('### Map Layers')

        st.sidebar.checkbox('A', True)

    except URLError as e:
        st.error("""
            **This demo requires internet access.**

            Connection error: %s
        """ % e.reason)
# fmt: on

# Turn off black formatting for this function to present the user with more
# compact code.
# fmt: off


def product_list():
    import streamlit as st
    products_list = {
    "蘭蔻": 1500,
    "'SK-II'": 1400,
    "'OLAY'": 1300,
    "歐姬兒": 1300,
    "雅詩蘭黛": 1300,
    "綠茶水平衡面霜": 1400,
    "綠茶籽保濕霜": 1500,
    "黛珂": 1500,
    "蜂王乳保濕凝露": 1600,
    "蜂王乳潤白QQ凝露": 1600,
    "資生堂": 1300
    }
    buy_number = [0]*len(products_list)
    for i,(product, price) in enumerate(products_list.items()):
        buy_number[i] = st.number_input(f"商品:{product}, 價格:{price}",step = 1)
    #st.write('The current number is ', number)


    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


# fmt: on

# Turn off black formatting for this function to present the user with more
# compact code.
# fmt: off
def cart():
    import streamlit as st
    def discount(money):
            #如果消費1500元到1999元是不會有折扣的(Bug)
        if(money >= 8000):
            money = money * 0.8
            conclusion = "恭喜達到免運活動，商品滿三千打8折共 %d 元"%(money) 
        elif(money >= 3000):
            money = money * 0.8 + 250
            conclusion = "恭喜商品滿三千打8折，運費250，含運共 %d 元"%(money) 
        elif(money >= 2500):
            money = money * 0.85 + 250
            conclusion = "恭喜商品滿兩千五打8折，運費250，含運共 %d 元"%(money) 
        elif(money >= 2000):
            money = money * 0.9 + 250
            conclusion = "恭喜商品滿兩千打9折，運費250，含運共 %d 元"%(money) 
        else:
            money = money + 250
        return money, conclusion
    products_list = {
    "蘭蔻": 1500,
    "'SK-II'": 1400,
    "'OLAY'": 1300,
    "歐姬兒": 1300,
    "雅詩蘭黛": 1300,
    "綠茶水平衡面霜": 1400,
    "綠茶籽保濕霜": 1500,
    "黛珂": 1500,
    "蜂王乳保濕凝露": 1600,
    "蜂王乳潤白QQ凝露": 1600,
    "資生堂": 1300
    }
    buy_number = [0, 0, 3, 0, 0, 4, 10, 0, 2, 0, 0]
    buy_product_list = [[p]*buy_number[i] for i, p in enumerate(products_list.keys())]
    buy_product_list_flatten = [j for i in buy_product_list for j in i]

    try:
        final_buy_product_list = st.multiselect(
            "選擇產品",buy_product_list_flatten, buy_product_list_flatten
        )
        st.text(discount(sum([products_list[p] for p in final_buy_product_list])))
        1+''
    except Exception as e:
        st.error(e)
    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


# fmt: on

# Turn off black formatting for this function to present the user with more
# compact code.
# fmt: off
def statistics():
    import streamlit as st
    import time
    import numpy as np

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

# fmt: on
