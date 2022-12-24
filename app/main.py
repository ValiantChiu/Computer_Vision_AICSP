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

# Copyright 2022 Chi-Chun Chiu

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


import inspect
import textwrap
from collections import OrderedDict

import streamlit as st
from streamlit.logger import get_logger
import pages
import pickle

LOGGER = get_logger(__name__)

# Dictionary of
# demo_name -> (demo_function, demo_description)
PAGES = OrderedDict(
    [
        ("註冊", (pages.register, None)),
        (
            "商品頁",
            (
                pages.product_list,
                """呈列所有商品
                """,
            ),
        ),
        (
            "購物車",
            (
                pages.cart,
                """已經購買的項目
                """,
            ),
        ),
        (
            "結帳",
            (
                pages.checkout,
                """付款並產生發票
                """,
            ),
        ),
        (
            "發票及貨運單",
            (
                pages.create_reciept,
                """發票
                """,
            ),
        ),
        (
            "流量統計(bonus)",
            (
                pages.statistics,
                """來客統計
                """,
            ),
        ),
    ]
)


def run():
    page_name = st.sidebar.selectbox("選擇頁面", list(PAGES.keys()), 0)
    show_code = st.sidebar.checkbox("Show code", False)

    if page_name == "註冊":
        page = PAGES[page_name][0]
        st.write("# 歡迎來到寶香齡美妝^-^")
        register_info = page()
        if register_info:
            new_username, new_gender, birth_day, moeny = register_info
            st.write(f"### {new_username}貴賓, 請前往商品頁")

    if page_name == "商品頁":
        page = PAGES[page_name][0]
        try:
            with open(f"register_info.pickle", "rb") as f:
                new_username, new_gender, birth_day, moeny = pickle.load(f)
            buy_number_list = page(birth_day, new_gender)
            if buy_number_list:
                st.write(f"### {new_username}貴賓, 請前往購物車")
        except Exception as e:

            st.write("# 尚未完成註冊")

    if page_name == "購物車":
        page = PAGES[page_name][0]
        try:
            with open(f"buy_number_list.pickle", "rb") as f:
                buy_number_list = pickle.load(f)
            checkout_dict = page(buy_number_list)
            if checkout_dict:
                st.write(f"### 請前往結帳")
        except Exception as e:
            st.write("# 尚未完成購買")

    if page_name == "結帳":
        page = PAGES[page_name][0]
        try:
            st.write(f"### 您的訂單")
            with open(f"register_info.pickle", "rb") as f:
                new_username, new_gender, birth_day, moeny = pickle.load(f)
            with open(f"checkout_dict.pickle", "rb") as f:
                checkout_dict = pickle.load(f)
            total_price = page(checkout_dict, birth_day)
            if total_price:
                st.write(f"### 請前往索取發票")
        except Exception as e:
            st.write("# 尚未確定購物車內容")
        pass

    if page_name == "發票及貨運單":
        page = PAGES[page_name][0]
        try:
            with open(f"total_price.pickle", "rb") as f:
                total_price = pickle.load(f)
            page(total_price)
        except Exception as e:
            st.write("# 尚未結帳")

    if page_name == "流量統計(bonus)":
        page = PAGES[page_name][0]
        page()

    try:
        if show_code:
            st.markdown("## Code")
            sourcelines, _ = inspect.getsourcelines(page)
            st.code(textwrap.dedent("".join(sourcelines[1:])))
    except Exception:
        pass


if __name__ == "__main__":
    run()
