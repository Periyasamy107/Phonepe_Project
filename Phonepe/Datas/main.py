
import mysql.connector
import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go
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
    col1.image('D:/Desktop/Projects/Phonepy/Datas/PhonePe-APK.png', width=350)
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






















