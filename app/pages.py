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

#Copyright 2022 Chi-Chun Chiu

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

product_dict = {
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


def register():
    import streamlit as st
    import datetime
    import pickle
    st.sidebar.success("請選擇功能頁")
    new_username = st.text_input('請輸入註冊用戶名:')
    new_password = st.text_input('請輸入新用戶密碼:','')
    if new_password!='' :
        new_password_again = st.text_input('請再次確認新用戶密碼:')  
        if new_password == new_password_again:
            new_gender = st.selectbox(
        '請輸入性別:', ('男', '女'))
            birth_day = st.date_input( "請輸入生日:",value = datetime.date(1990, 1, 1),max_value=datetime.datetime.now())
            new_cellphone = st.text_input('請輸入手機號碼:')
            #st.write("特惠活動滿八千免運，請輸入您的總預算:")
            moeny = st.slider('特惠活動滿八千免運，請輸入您的總預算:', 0, 50000, step= 1000)
            st.write('你的預算:', moeny)
            if st.button('提交'):
                with open('register_info.pickle', 'wb') as f:
                    pickle.dump((new_username, new_gender, birth_day, moeny), f, pickle.HIGHEST_PROTOCOL)           
                return new_username, new_gender, birth_day, moeny
        else: 
            st.text('請再確認你的密碼')
        st.markdown("""  """
        )



def checkout(checkout_dic, birthday_month):
    import streamlit as st
    import pandas as pd
    import datetime
    import pickle
    
    def birthday_discount_check(birthday_month, purchase_amount):
        now = datetime.datetime.now()
        current_month = now.month
        if current_month == birthday_month:
            discounted_amount = int(purchase_amount * 0.9)
            st.write('祝您生日快樂!打九折')
            return discounted_amount
        else:
            return purchase_amount    

    try:
        price = [product_dict[i] for i in checkout_dic.keys()]
        total_price = [checkout_dic[i]*product_dict[i] for i in checkout_dic.keys()]


        st.sidebar.checkbox('A', True)

        df = pd.DataFrame.from_dict(checkout_dic, orient='index')
        df['價格'] = price
        df['總額'] = total_price
        
        df = df.rename(columns={0:'數量'})
        st.dataframe(df)
        #st.dataframe(df.style.highlight_max(axis=0))
        total_price = sum(total_price)
        total_price = birthday_discount_check(birthday_month.month,total_price)
        st.write('### 應付$:' ,total_price)
        if st.button('確定購買'):
            with open('total_price.pickle', 'wb') as f:
                pickle.dump(total_price, f, pickle.HIGHEST_PROTOCOL)           
            return total_price
    except Exception as e:
        st.error(e)



def product_list(birth_day, new_gender, buy_number_list = [0]*len(product_dict)):
    import streamlit as st
    import datetime
    import pickle
    def product_recommendation(birth_day,sex):
        sex = (lambda x: 'female' if sex == '女' else 'man')(sex)
        now = datetime.date.today()
        age = int((now - birth_day).days)/365
            
        if age < 30 and sex == 'female':
            st.write('## 猜妳也喜歡保濕及乳液產品')
        elif age >= 30 and age < 50 and sex == 'female':
            st.write('## 除了保濕、乳液產品，也推薦妳使用我們的隔離霜、淡妝產品')
        else:
            st.write('## 本月各式化妝品都有促銷，歡迎選購')

    product_recommendation(birth_day, new_gender)
    buy_number_list = [0]*len(product_dict)
    for i,(product, price) in enumerate(product_dict.items()):
        buy_number_list[i] = st.number_input(f"商品:{product}, 價格:{price}",step = 1)

    if st.button('提交'):
        with open('buy_number_list.pickle', 'wb') as f:
            pickle.dump(buy_number_list, f, pickle.HIGHEST_PROTOCOL) 
        return buy_number_list


def cart(buy_number_list):
    import streamlit as st
    from collections import Counter
    import pickle
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
        elif(money >= 1500):
            money = money * 0.9 + 250
            conclusion = "恭喜商品滿兩千打9折，運費250，含運共 %d 元"%(money) 
        else:
            money = money + 250
            conclusion = "本次消費金額未滿$1500元無折扣，含運共 %d 元"%(money) 
        return money, conclusion

    buy_product_list = [[p]*buy_number_list[i] for i, p in enumerate(product_dict.keys())]
    buy_product_list_flatten = [j for i in buy_product_list for j in i]

    try:
        final_buy_product_list = st.multiselect(
            "更改產品:",buy_product_list_flatten, buy_product_list_flatten
        )
        st.write(f'### {discount(sum([product_dict[p] for p in final_buy_product_list]))[1]}')
        checkout_dict = Counter(final_buy_product_list)
        if st.button('正確無誤'):
            with open('checkout_dict.pickle', 'wb') as f:
                pickle.dump(checkout_dict, f, pickle.HIGHEST_PROTOCOL)      
            return checkout_dict
    except Exception as e:
        st.error(e)


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





def create_reciept(total_price):
    import streamlit as st
    st.write('# 開發中')
    