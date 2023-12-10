# import io
# import pandas as pd 
# import streamlit as st 
# import mysql.connector
# import ydata_profiling 
# from streamlit_player import st_player
# from streamlit_pandas_profiling import st_profile_report
# from streamlit_extras.metric_cards import style_metric_cards
# from streamlit_extras.add_vertical_space import add_vertical_space

# # Data Preparation
# mysql_credentials = st.secrets["mysql"]; host = mysql_credentials["host"]; user = mysql_credentials["user"]
# password = mysql_credentials["password"]; database = mysql_credentials["database"]

# conn = mysql.connector.connect(
#             host = host,
#             user = user, 
#             password = password,
#             database = database
# )

# cursor = conn.cursor()

# def get_dataframs(table_name):
#     query = f'select * from {table_name}'
#     cursor.execute(query)
#     data = cursor.fetchall()
#     df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
#     df['year'] = df['year'].astype(str)
#     return df
#     # print(df.info())

# add_trans_df = agg_user_df = map_trans_df = map_user_df = \
# top_trans_dist_df = top_trans_pin_df = top_user_dist_df = top_user_pin_df = None 

# table_names = [
#     'agg_trans', 'agg_user', 'map_trans', 'map_user', 'top_trans_dist',
#     'top_trans_pin', 'top_user_dist', 'top_user_pin'
# ]

# for table_name in table_names:
#     var_name = f'{table_name}_df'
#     globals()[var_name] = get_dataframs(table_name)

# cursor.close()
# conn.close()


# if 'options' not in st.session_state:
#     st.session_state['options'] = {
#         'Aggregate Transaction': 'agg_trans_df',
#         'Aggregate User': 'agg_user_df',
#         'Map Transaction': 'map_trans_df',
#         'Map User': 'map_user_df',
#         'Top Transaction Districtwise': 'top_trans_dist_df',
#         'Top Transaction Pincodewise': 'top_trans_pin_df',
#         'Top User Districtwise': 'top_user_dist_df',
#         'Top User Pincodewise': 'top_user_pin_df'
#     }

# df_names = [
#             var_name for var_name in globals() 
#             if isinstance(globals()[var_name], pd.core.frame.DataFrame) and var_name.endswith('_df')
#             ]
# print('df_names : ', df_names)

# if 'df_list' not in st.session_state:
#     st.session_state['df_list'] = []
    
#     for var_name in df_names:
#         st.session_state[var_name] = globals()[var_name]
#         st.session_state['df_list'].append(var_name)

#         print('var_name : ', var_name)


# if 'options' not in st.session_state:
#     st.session_state['options'] = {
#         'Aggregate Transaction': 'agg_trans_df',
#         'Aggregate User': 'agg_user_df',
#         'Map Transaction': 'map_trans_df',
#         'Map User': 'map_user_df',
#         'Top Transaction Districtwise': 'top_trans_dist_df',
#         'Top Transaction Pincodewise': 'top_trans_pin_df',
#         'Top User Districtwise': 'top_user_dist_df',
#         'Top User Pincodewise': 'top_user_pin_df'
#     }



# df_names = [
#     var_name for var_name in globals()
#     if isinstance(globals()[var_name], pd.core.frame.DataFrame) and var_name.endswith('_df')
# ]

# for df_name in df_names:
#     print(df_name)
# Add DataFrame variable names to df_list if they are not already present

# if 'df_list' not in st.session_state:
#     st.session_state['df_list'] = []

    # for var_name in df_names:
    #     print(var_name)
    #     if var_name not in st.session_state['df_list']:
    #         st.session_state['df_list'].append(var_name)

    # Update or add DataFrame to session state
# st.session_state[var_name] = globals()[var_name]



# # App


# st.set_page_config(
#                 page_title = 'PhonePe Data Visualization', layout = 'wide',
#                 page_icon = 'Related Images and Videos/Logo.png'
#                 )

# st.title(':blue[PhonePe Data Visualization]')

# add_vertical_space(2)

# phonepe_description = """PhonePe has launched PhonePe Pulse, a data analytics platform that provides insights into
#                         how Indians are using digital payments. With over 30 crore registered users and 2000 crore 
#                         transactions, PhonePe, India's largest digital payments platform with 46% UPI market share,
#                         has a unique ring-side view into the Indian digital payments story. Through this app, you 
#                         can now easily access and visualize the data provided by PhonePe Pulse, gaining deep 
#                         insights and interesting trends into how India transacts with digital payments."""

# st.write(phonepe_description)

# add_vertical_space(2)

# st_player(url = "https://www.youtube.com/watch?v=c_1H6vivsiA", height = 480)

# add_vertical_space(2)

# st.image('Related Images and Videos/1.png')

# add_vertical_space(2)

# col1, col2, col3 = st.columns(3)

# total_reg_users = top_user_dist_df['Registered_User'].sum()
# col1.metric(
#             label = 'Total Registered Users',
#             value = '{:.2f} Cr'.format(total_reg_users/100000000),
#             delta = 'Forward Trend'
#             )

# total_app_opens = map_user_df['App_Opens'].sum()
# col2.metric(
#             label = 'Total App Opens', value = '{:.2f} Cr'.format(total_app_opens/100000000),
#             delta = 'Forward Trend'
#             )

# col3.metric(label = 'Total Transaction Count', value = '2000 Cr +', delta = 'Forward Trend')

# style_metric_cards()

# add_vertical_space(2)

# st.image('Related Images and Videos/pulse.gif', use_column_width = True)

# add_vertical_space(2)

# col, buff = st.columns([2, 4])

# option = col.selectbox(
#                         label='Data',
#                         options=list(st.session_state['options'].keys()),
#                         key='df'
#                         )

# tab1, tab2 = st.tabs(['Report and Dataset', 'Download Dataset'])

# with tab1:
    
#     column1, column2, buffer = st.columns([2, 2, 4])
    
#     show_profile = column1.button(label = 'Show Detailed Report', key = 'show')
#     show_df = column2.button(label = 'Show Dataset', key = 'show_df')
    
#     if show_profile:
#         df_name = st.session_state['options'][option]
#         df = globals()[df_name]
#         pr = df.profile_report()
#         st_profile_report(pr)
        
#     if show_df:
#         st.experimental_data_editor(
#                                     data = globals()[st.session_state['options'][option]],
#                                     use_container_width=True
#                                     )

# with tab2:
#     col1, col2, col3 = st.columns(3)
    
#     df_name = st.session_state['options'][option]
#     df = globals()[df_name]
    
#     csv = df.to_csv()
#     json = df.to_json(orient ='records')
#     excel_buffer = io.BytesIO()
#     df.to_excel(excel_buffer, engine ='xlsxwriter', index = False)
#     excel_bytes = excel_buffer.getvalue()
    
#     col1.download_button(
#                         "Download CSV file", data = csv,
#                         file_name = f'{option}.csv',
#                         mime = 'text/csv', key = 'csv'
#                         )
#     col2.download_button(
#                         "Download JSON file", data = json,
#                         file_name = f'{option}.json',
#                         mime = 'application/json', key = 'json'
#                         )
#     col3.download_button("Download Excel file", data = excel_bytes,
#                         file_name = f'{option}.xlsx',
#                         mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
#                         key = 'excel'
#                         )




import mysql.connector
import pandas as pd
import streamlit as st
import PIL 
from PIL import Image
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go
import requests
import json
import folium
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

conn = mysql.connector.connect(host='localhost',user='root',password='Samy@1007',database='phonepe_pulse')

cursor = conn.cursor()

SELECT = option_menu(
    menu_title = None, 
    options = ['Home', 'Barchart', 'Piechart'],
    icons = ['home', 'bar-chart', 'pie-chart'],
    default_index = 2, 
    orientation = 'horizontal'
)

if SELECT == 'Home':
    col1, col2 = st.columns(2)
    col1.image('PhonePe-APK.png', width=350)
    with col1:
        st.video('https://www.youtube.com/watch?v=OfXbp7hPno0')
        st.download_button('Download the app', 'https://www.phonepe.com/app-download/')
    with col2:
        st.subheader('PhonePe is a payments app that allows you to use BHIM UPI, your credit card and debit card or wallet to recharge your mobile phone, pay all your utility bills and to make instant payments at your favourite offline and online stores. You can also invest in mutual funds and buy insurance plans on PhonePe.')

    

if SELECT == 'Barchart':
    st.title('BarChart Visualization')
    st.subheader('Here are few insights about the data in bar chart visualization')
    options = [
        '--select--',
        'top 10 transaction based on district',
        'top 10 transaction based on state',
        'top 10 users based on district',
        'top 10 users based on state'
    ]
    
    select = st.selectbox('Select the option ', options)
    if select == 'top 10 transaction based on district': 
        cursor.execute("select distinct state, district,  sum(transaction_amount) as Total_Transaction_Amount from top_trans_dist group by state, district order by Total_Transaction_Amount desc limit 10;")
        dist = cursor.fetchall()
        df = pd.DataFrame(dist, columns=['state', 'district',  'transaction_amount'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader('Top 10 transaction in district wise')
            st.bar_chart(data=df, x = 'district', y='transaction_amount')


        json1 = 'D:\\Desktop\\Projects\\Phonepy\\Datas\\Miscellaneous\\states_india.geojson'
        mapp = folium.Map(location=[23.47,77.94], tiles='CartoDB positron', name='Light map',
                        zoom_start=5, attr = 'my data attribution')
        choice = ['transaction_amount']
        choice_selected = st.selectbox('select choice', choice)
        folium.Choropleth(
            geo_data = json1,
            name = 'choropleth',
            data = df,
            columns = ['state', choice_selected],
            key_on = 'feature.properties.st_nm',
            fill_color = 'YlOrRd',
            fill_opacity = 1,
            line_opacity = 10,
            legend_name = choice_selected
        ).add_to(mapp)
        folium.features.GeoJson('D:\\Desktop\\Projects\\Phonepy\\Datas\\Miscellaneous\\states_india.geojson',
                                name='state', popup = folium.features.GeoJsonPopup(fields=['st_nm'])).add_to(mapp)
        folium_static(mapp, width=700, height = 650)


    elif select == 'top 10 transaction based on state':
        cursor.execute("select distinct state,   sum(transaction_amount) as Total_Transaction_Amount from top_trans_pin group by state order by Total_Transaction_Amount desc limit 10;")
        dist = cursor.fetchall()
        df = pd.DataFrame(dist, columns=['state',  'transaction_amount'])

        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader('Top 10 transaction based on state wise')
            st.bar_chart(data=df, x = 'state', y='transaction_amount')

        json1 = 'D:\\Desktop\\Projects\\Phonepy\\Datas\\Miscellaneous\\states_india.geojson'
        mapp = folium.Map(location=[23.47,77.94], tiles='CartoDB positron', name='Light map',
                        zoom_start=5, attr = 'my data attribution')
        choice = ['transaction_amount']
        choice_selected = st.selectbox('select choice', choice)
        folium.Choropleth(
            geo_data = json1,
            name = 'choropleth',
            data = df,
            columns = ['state', choice_selected],
            key_on = 'feature.properties.st_nm',
            fill_color = 'YlOrRd',
            fill_opacity = 1,
            line_opacity = 10,
            legend_name = choice_selected
        ).add_to(mapp)
        folium.features.GeoJson('D:\\Desktop\\Projects\\Phonepy\\Datas\\Miscellaneous\\states_india.geojson',
                                name='state', popup = folium.features.GeoJsonPopup(fields=['st_nm'])).add_to(mapp)
        folium_static(mapp, width=700, height = 650)


    elif select == 'top 10 users based on district':
        cursor.execute("select distinct state, district,  sum(registered_user) as top_users from top_user_dist group by state, district order by top_users desc limit 10;")
        dist = cursor.fetchall()
        df = pd.DataFrame(dist, columns=['state', 'district',  'registered_user'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            plt.bar(df['district'], df['registered_user'])
            plt.xlabel('Districts', fontdict={'fontsize':30, 'fontstyle':'normal'})
            plt.ylabel('Users', fontdict={'fontsize':20})
            plt.title('Top 10 users based on district wise', fontdict={'fontsize':20})
            plt.xticks(rotation=90)
            plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
            st.pyplot(plt)

        df = df['registered_user'].astype('int64')
        json1 = 'D:\\Desktop\\Projects\\Phonepy\\Datas\\Miscellaneous\\states_india.geojson'
        mapp = folium.Map(location=[23.47,77.94], tiles='CartoDB positron', name='Light map',
                        zoom_start=5, attr = 'my data attribution')
        choice = ['registered_user']
        choice_selected = st.selectbox('select choice', choice)
        folium.Choropleth(
            geo_data = json1,
            name = 'choropleth',
            data = df,
            columns = ['state', choice_selected],
            key_on = 'feature.properties.st_nm',
            fill_color = 'YlOrRd',
            fill_opacity = 1,
            line_opacity = 10,
            legend_name = choice_selected
        ).add_to(mapp)
        folium.features.GeoJson('D:\\Desktop\\Projects\\Phonepy\\Datas\\Miscellaneous\\states_india.geojson',
                                name='state', popup = folium.features.GeoJsonPopup(fields=['st_nm'])).add_to(mapp)
        folium_static(mapp, width=700, height = 650)


    elif select == 'top 10 users based on state':
        cursor.execute("select distinct state, sum(registered_user) as top_users from top_user_pin group by state order by top_users desc limit 10;")
        dist = cursor.fetchall()
        df = pd.DataFrame(dist, columns=['state', 'registered_user'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            plt.bar(df['state'], df['registered_user'])
            plt.xlabel('States', fontdict={'fontsize':16, 'fontstyle':'italic'})
            plt.ylabel('Users', fontdict={'fontsize':12, 'fontstyle':'normal'})
            plt.title('Top 10 users based on state wise', fontdict={'fontsize':18, 'fontstyle':'italic'})
            plt.xticks(rotation=90)
            plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
            st.pyplot(plt)

        df = df['registered_user'].astype('int64')
        json1 = 'D:\\Desktop\\Projects\\Phonepy\\Datas\\Miscellaneous\\states_india.geojson'
        mapp = folium.Map(location=[23.47,77.94], tiles='CartoDB positron', name='Light map',
                        zoom_start=5, attr = 'my data attribution')
        choice = ['registered_user']
        choice_selected = st.selectbox('select choice', choice)
        folium.Choropleth(
            geo_data = json1,
            name = 'choropleth',
            data = df,
            columns = ['state', choice_selected],
            key_on = 'feature.properties.st_nm',
            fill_color = 'YlOrRd',
            fill_opacity = 1,
            line_opacity = 10,
            legend_name = choice_selected
        ).add_to(mapp)
        folium.features.GeoJson('D:\\Desktop\\Projects\\Phonepy\\Datas\\Miscellaneous\\states_india.geojson',
                                name='state', popup = folium.features.GeoJsonPopup(fields=['st_nm'])).add_to(mapp)
        folium_static(mapp, width=700, height = 650)




if SELECT == 'Piechart':
    st.title('Pie Chart Visualization')
    st.subheader('Here are few insights about the data in pie chart visualization')
    options = [
        '--select--',
        'top transaction based on transaction type',
        'which year having maximum transactions ?',
        'Which state is having maximum users ?',
        'Top 5 brands based on users hold'
    ]
    
    select = st.selectbox('Select the option ', options)
    if select == 'top transaction based on transaction type': 
        cursor.execute("select transaction_type, sum(transaction_amount) as total_transaction from agg_trans group by transaction_type;")
        dist = cursor.fetchall()
        df = pd.DataFrame(dist, columns=['transaction_type', 'transaction_amount'])

        labels = df['transaction_type']
        sizes = df['transaction_amount']

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.0f%%',  startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

    elif select == 'which year having maximum transactions ?': 
        cursor.execute("select year, sum(transaction_amount) as top_amounts from map_trans group by year order by top_amounts desc;")
        dist = cursor.fetchall()
        df = pd.DataFrame(dist, columns=['year', 'top_amounts'])

        labels = df['year']
        sizes = df['top_amounts']

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

    elif select == 'Which state is having maximum users ?': 
        cursor.execute("select state, sum(registered_user) as top_users from map_user group by state order by top_users desc limit 10;")
        dist = cursor.fetchall()
        df = pd.DataFrame(dist, columns=['state', 'top_users'])

        labels = df['state']
        sizes = df['top_users']

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)
    
    elif select == 'Top 5 brands based on users hold': 
        cursor.execute("select brand, sum(transaction_count) as top_user from agg_user group by brand order by top_user desc limit 5;")
        dist = cursor.fetchall()
        df = pd.DataFrame(dist, columns=['brand', 'top_user'])

        labels = df['brand']
        sizes = df['top_user']

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)






















