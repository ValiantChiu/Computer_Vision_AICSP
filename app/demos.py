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

    st.markdown(
        """

    """
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
    import numpy as np



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
    import pandas as pd
    import altair as alt

    from urllib.error import URLError

    @st.cache
    def get_UN_data():
        AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
        df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
        return df.set_index("Region")

    try:
        df = get_UN_data()
        countries = st.multiselect(
            "選擇產品",["China", "United States of America"], ["China"]
        )

    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )
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
