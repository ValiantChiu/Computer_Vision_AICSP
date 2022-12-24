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

import inspect
import textwrap
from collections import OrderedDict

import streamlit as st
from streamlit.logger import get_logger
import pages

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
        ),        (
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
    page = PAGES[page_name][0]

    if page_name == "註冊":
        show_code = True
        st.write("# 歡迎來到寶香齡美妝^-^")

    else:
        show_code = st.sidebar.checkbox("Show code", True)
        st.markdown("# %s" % page_name)
        description = PAGES[page_name][1]
        if description:
            st.write(description)
        # Clear everything from the intro page.
        # We only have 4 elements in the page so this is intentional overkill.
        #for i in range(10):
        #    st.empty()

    s = page()
    print(s)

    if show_code:
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(page)
        st.code(textwrap.dedent("".join(sourcelines[1:])))


if __name__ == "__main__":
    run()
