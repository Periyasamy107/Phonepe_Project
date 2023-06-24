import io
import pandas as pd
import streamlit as st
import ydata_profiling
from streamlit_player import st_player
from streamlit_pandas_profiling import st_profile_report
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.add_vertical_space import add_vertical_space

visual = st.container()

# Data Prep
# Reading from csv so as to make it work for everyone in streamlit cloud app...
# Otherwise there's another file named Home_with_SQL_Part.py in Miscellaneous directory in this same repo...

agg_trans_df = pd.read_csv(r'Miscellaneous/agg_trans.csv')
agg_user_df = pd.read_csv(r'Miscellaneous/agg_user.csv')
map_trans_df = pd.read_csv(r'Miscellaneous/map_trans.csv')
map_user_df = pd.read_csv(r'Miscellaneous/map_user.csv')
top_trans_dist_df = pd.read_csv(r'Miscellaneous/top_trans_dist.csv')
top_trans_pin_df = pd.read_csv(r'Miscellaneous/top_trans_pin.csv')
top_user_dist_df = pd.read_csv(r'Miscellaneous/top_user_dist.csv')
top_user_pin_df = pd.read_csv(r'Miscellaneous/top_user_pin.csv')

visual:
