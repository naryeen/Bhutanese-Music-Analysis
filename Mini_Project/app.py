from itertools import count
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('minidata.xlsx')
df.head()
#This columns will be deleted as it doesnot take part in the analysis and the new dataframe (df1) will store the new dataset.
df1 = df.drop(['description', 'thumbnailUrl', 'videoOwnerTitle', 'videoId', 'videotags', 'videoAddedToPlaylistAt', 'videoOwnerChannelId'], axis = 1) 

df1 = df1.dropna()  # Remove rows and columns with Null/NaN values
df1.isna().sum()  #checking if all the null values are removed or not
df1.loc[df1['favoriteCount'] == 0] #Access the column 'favorite count' consisting of value 0 
s = df1['favoriteCount']  #this column gives no meaning to analyze the dataset since all the values are zero (0) 
del df1['favoriteCount']  #Delete the column favouriteCount
df1.duplicated() # Return boolean Series denoting duplicate rows

df1.duplicated().sum()
df1.loc[df1.duplicated(), :]
df1.drop_duplicates(keep='last')


#column title consist of many information along with the title, so have splited the column title and taken only the title name and artist (is any)
#created object name url and printed one value from the column title 
url = df1.title[9]                 
url
#used split method to split the values based on (|) for one value in the column title
split_title = url.split("|")[0]
split_title

#Function that accepts url and returns the title name based on your experimentation above
def get_title(url):
   title_name = url.split("|")[0]
   return title_name
   
#Apply the get_title function to the 'url' column using '.map' 
#and add a new column 'title_name' to store the names
df1['Title_name'] = df1.title.map(get_title)
del df1['title']  #Delete the column title after creating new column Title_name

#column videoPublishedAt consist of many information along with the year, so have splited the column videoPubllishedAt and taken only year
#created object name url_year and printed one value from the column videoPublishedAt 
url_year = df1.videoPublishedAt[9]
#used split method to split the values based on (-) for one value in the column videopublishedAt
split_year = url_year.split("-")[0]

#Function that accepts url_year and returns only the year based on your experimentation above
def get_year(url_year):
    year = url_year.split("-")[0]
    return year
#Apply the get_year function to the 'url_year' column using '.map' 
#and add a new column 'year' to store the names
df1['year'] = df1.videoPublishedAt.map(get_year)

del df1['videoPublishedAt']  #Delete the column videoPublishedAt after creating column year to store the released year of each MV

df1.year = df1.year.astype('int') #converting the data type of year from float to int



#Created a new dataframe name channeldf and used groupby function (It allows you to split your data into separate groups to perform computations for better analysis)) to group the data in the column playlistHostedChannelName
channeldf = df1.groupby('playlistHostedChannelName', sort=False)
channeldf
channeldf.size() #display the different channel along with the total number of values in each channel
channeldf.first() #bring the column playlistHostedChannelName at first as first column


channeldf.get_group('Yeshi Lhendup Films') #get_group() to get a group from a GroupBy object
yeshidf = channeldf.get_group('Yeshi Lhendup Films') #creaetd new dataframe yeashidf to get the grouped data from the group yeshi lhendup flim
#will dsiplay the name of the music video along with the year and videoUrl based on the highest viewcount
yeshidf[yeshidf.viewCount == yeshidf.viewCount.max()][['Title_name', 'year', 'videoUrl', 'viewCount']]
# three largest values (highest view count) in column viewCount
g1 = yeshidf.nlargest(3, ['viewCount'])[['Title_name', 'year', 'videoUrl', 'viewCount']]
g1
plt.scatter(yeshidf.year,yeshidf.viewCount)
plt.title("year Vs viewCount")
plt.xlabel("year")
plt.ylabel("ViewCount")
# plt.show()
import plotly.express as px #Displays the top 3 music video based on viewCount
px.bar(data_frame = g1, x = 'Title_name', y = 'viewCount', color = 'viewCount', orientation = 'v', width=800, height=400)

import plotly.express as px 
px.bar(data_frame = yeshidf, x = 'year', y = 'viewCount', color = 'viewCount', orientation = 'v', width=800, height=400) 
px.histogram(data_frame = yeshidf, x = 'year', width=800, height=400)
px.histogram(data_frame = yeshidf, x = 'viewCount', width=800, height=400)
#Most of the music video has the number of views less than 100K
#Only two music video has the number of views at around 1.5M which is the highest.



# ##4.2 Rigdrol Flims
# ####For visualizing the data, used scatter plot, bar graph and histogram.

channeldf.get_group('Rigdrol Films')
rigdroldf = channeldf.get_group('Rigdrol Films')
rigdroldf.head()
rigdroldf[rigdroldf.viewCount == rigdroldf.viewCount.max()][['Title_name', 'year', 'videoUrl', 'viewCount']]
# five largest values in column viewCount
g2 = rigdroldf.nlargest(3, ['viewCount'])[['Title_name', 'year', 'videoUrl', 'viewCount']]
g2
#Scatterplot graph to see the relationship between the viewcount and year
#Graph shows the highest viewcount in the year 2020
plt.scatter(rigdroldf.year, rigdroldf.viewCount)
plt.title("year Vs viewCount")
plt.xlabel("year")
plt.ylabel("viewCount")
# plt.show()
import plotly.express as px #Displays the top 3 music video based on viewCount
px.bar(data_frame = g2, x = 'Title_name', y = 'viewCount', color = 'viewCount', orientation = 'v', width=800, height=400)

import plotly.express as px
px.bar(data_frame = rigdroldf, x = 'year', y = 'viewCount', color = 'viewCount', orientation = 'v', width=800, height=400)
#highest number of music video released was in the year 2021.
px.histogram(data_frame = rigdroldf, x = 'year', width=800, height=400)

px.histogram(data_frame = rigdroldf, x = 'viewCount', width=800, height=400)
#There is not much differnece between the number of view Count for different music videos (number of views are less thn 400k)




# ##4.3 MStudio
# ####For visualizing the data, used scatter plot, bar graph and histogram.

channeldf.get_group('MStudioBhutan')
mstudiodf = channeldf.get_group('MStudioBhutan')
mstudiodf.head()
mstudiodf[mstudiodf.viewCount == mstudiodf.viewCount.max()][['Title_name', 'year', 'videoUrl', 'viewCount']]


# five largest values in column viewCount
g3 = mstudiodf.nlargest(3, ['viewCount'])[['Title_name', 'year', 'videoUrl', 'viewCount']]
g3

plt.scatter(mstudiodf.year, mstudiodf.viewCount)
plt.title("year Vs viewCount")
plt.xlabel("year")
plt.ylabel("viewCount")
# plt.show()

import plotly.express as px #Displays the top 3 music video based on viewCount
px.bar(data_frame = g3, x = 'Title_name', y = 'viewCount', color = 'viewCount', orientation = 'v', width=800, height=400)

import plotly.express as px
px.bar(data_frame = mstudiodf, x = 'year', y = 'viewCount', color = 'viewCount', orientation = 'v', width=800, height=400)

px.histogram(data_frame = mstudiodf, x = 'year', width=800, height=400)

px.histogram(data_frame = mstudiodf, x = 'viewCount', width=800, height=400)
#most of the videos have the views less than 100k.


# ##4.4 VMUSIC BHUTAN
channeldf.get_group('VMUSIC BHUTAN')
vmusicdf = channeldf.get_group('VMUSIC BHUTAN')
vmusicdf.head()
vmusicdf[vmusicdf.viewCount == vmusicdf.viewCount.max()][['Title_name', 'year', 'videoUrl', 'viewCount']]

# five largest values in column viewCount
g4 = vmusicdf.nlargest(3, ['viewCount'])[['Title_name', 'year', 'videoUrl', 'viewCount']]
g4

#Highest view count in the year 2021 and lowest in the year 2016 and no videos uploaded in between
plt.scatter(vmusicdf.year, vmusicdf.viewCount)
plt.title("year Vs viewCount")
plt.xlabel("year")
plt.ylabel("viewCount")
# plt.show()

import plotly.express as px #Displays the top 3 music video based on viewCount
px.bar(data_frame = g4, x = 'Title_name', y = 'viewCount', color = 'viewCount', orientation = 'v', width=800, height=400)

import plotly.express as px
px.bar(data_frame = vmusicdf, x = 'year', y = 'viewCount', color = 'viewCount', orientation = 'v', width=800, height=400)
#Highest view count in between the 2020 and 2022

px.histogram(data_frame = vmusicdf, x = 'year', width=800, height=400)
#Less number of videos uploaded and there is not much difference in count of videos uploaded in each year

px.histogram(data_frame = vmusicdf, x = 'viewCount', width=800, height=400)
#Most videos consist of view counts below 1M


# ##4.5 Tandin Phubz
channeldf.get_group('Tandin Phubz')
phubdf = channeldf.get_group('Tandin Phubz')
phubdf[phubdf.viewCount == phubdf.viewCount.max()][['Title_name', 'year', 'videoUrl', 'viewCount']]

# five largest values in column viewCount
g5 = phubdf.nlargest(3, ['viewCount'])[['Title_name', 'year', 'videoUrl', 'viewCount']]
g5

#Highest video along with the highest number of views are released between the year 2017 to  2021
plt.scatter(phubdf.year, phubdf.viewCount)
plt.title("year Vs viewCount")
plt.xlabel("year")
plt.ylabel("viewCount")
# plt.show()

import plotly.express as px #Displays the top 3 music video based on viewCount
px.bar(data_frame = g5, x = 'Title_name', y = 'viewCount', color = 'viewCount', orientation = 'v', width=800, height=400)

import plotly.express as px
px.bar(data_frame = phubdf, x = 'year', y = 'viewCount', color = 'viewCount', orientation = 'v', width=800, height=400)
#Highest total number of views in the year 2020
#Total number of views in each year is around 0.5M

px.histogram(data_frame = phubdf, x = 'year', width=800, height=400)
#Highest number of the videos are uploaded in the year 2020
px.histogram(data_frame = phubdf, x = 'viewCount', width=800, height=400)
#Most of the videos have less than 200k number of views


# ##4.6 Lhendup Audio Visual
channeldf.get_group('Lhendup Audio Visual')
lhendupdf = channeldf.get_group('Lhendup Audio Visual')

lhendupdf[lhendupdf.viewCount == lhendupdf.viewCount.max()][['Title_name', 'year', 'videoUrl', 'viewCount']]
# five largest values in column viewCount
g6 = lhendupdf.nlargest(3, ['viewCount'])[['Title_name', 'year', 'videoUrl', 'viewCount']]
g6

plt.scatter(lhendupdf.year, lhendupdf.viewCount)
plt.title("year Vs viewCount")
plt.xlabel("year")
plt.ylabel("viewCount")
# plt.show()
#videos released in the year 2020 has less than 100k and year 2021 has the highest viewcount with around 200k
import plotly.express as px #Displays the top 3 music video based on viewCount
px.bar(data_frame = g6, x = 'Title_name', y = 'viewCount', color = 'viewCount', orientation = 'v', width=800, height=400)

import plotly.express as px
px.bar(data_frame = lhendupdf, x = 'year', y = 'viewCount', color = 'viewCount', orientation = 'v', width=800, height=400)
px.histogram(data_frame = lhendupdf, x = 'year', width=800, height=400)
#More numeber of videos was released in the year around 2020
px.histogram(data_frame = lhendupdf, x = 'viewCount', width=800, height=400)
#Almost all the video have the view count below 50K


# ##4.7 Galey Visual Production
channeldf.get_group('Galey Visual Production')
galeydf = channeldf.get_group('Galey Visual Production')
galeydf[galeydf.viewCount == galeydf.viewCount.max()][['Title_name', 'year', 'videoUrl', 'viewCount']]
# five largest values in column viewCount
g7 = galeydf.nlargest(3, ['viewCount'])[['Title_name', 'year', 'videoUrl', 'viewCount']]
g7

### based on year
# yeardf = df1.groupby('year', sort=False)
# yeardf.get_group(2016)
# year1 = yeardf.get_group(2016)
# year1[year1.viewCount == year1.viewCount.max()][['Title_name', 'year', 'videoUrl', 'viewCount']]
# # five largest values in column viewCount
# y2016 = year1.nlargest(5, ['viewCount'])[['Title_name', 'year', 'videoUrl', 'viewCount']]


# yeardf.get_group(2017)
# year2 = yeardf.get_group(2017)
# year2[year2.viewCount == year2.viewCount.max()][['Title_name', 'year', 'videoUrl', 'viewCount']]
# # five largest values in column viewCount
# y2017 = year2.nlargest(10, ['viewCount'])[['Title_name', 'year', 'videoUrl', 'viewCount']]


# yeardf.get_group(2018)
# year3 = yeardf.get_group(2018)
# year3[year3.viewCount == year3.viewCount.max()][['Title_name', 'year', 'videoUrl', 'viewCount']]
# # five largest values in column viewCount
# y2018 = year3.nlargest(10, ['viewCount'])[['Title_name', 'year', 'videoUrl', 'viewCount']]


# yeardf.get_group(2019)
# year4 = yeardf.get_group(2019)
# year4[year4.viewCount == year4.viewCount.max()][['Title_name', 'year', 'videoUrl', 'viewCount']]
# # five largest values in column viewCount
# y2019 = year4.nlargest(10, ['viewCount'])[['Title_name', 'year', 'videoUrl', 'viewCount']]

# yeardf.get_group(2020)
# year5 = yeardf.get_group(2020)
# year5[year5.viewCount == year5.viewCount.max()][['Title_name', 'year', 'videoUrl', 'viewCount']]
# # five largest values in column viewCount
# y2020 = year5.nlargest(10, ['viewCount'])[['Title_name', 'year', 'videoUrl', 'viewCount']]


# yeardf.get_group(2021)
# year6 = yeardf.get_group(2021)
# year6[year6.viewCount == year6.viewCount.max()][['Title_name', 'year', 'videoUrl', 'viewCount']]
# # five largest values in column viewCount
# y2021 = year6.nlargest(10, ['viewCount'])[['Title_name', 'year', 'videoUrl', 'viewCount']]

# yeardf.get_group(2022)
# year7 = yeardf.get_group(2022)
# year7[year7.viewCount == year7.viewCount.max()][['Title_name', 'year', 'videoUrl', 'viewCount']]
# # five largest values in column viewCount
# y2022 = year7.nlargest(10, ['viewCount'])[['Title_name', 'year', 'videoUrl', 'viewCount']]


plt.scatter(galeydf.year, galeydf.viewCount)
plt.title("year Vs viewCount")
plt.xlabel("year")
plt.ylabel("viewCount")
# plt.show()
#Highest total number of Views in the year 2022

import plotly.express as px #Displays the top 3 music video based on viewCount
px.bar(data_frame = g7, x = 'Title_name', y = 'viewCount', color = 'viewCount', orientation = 'v', width=800, height=400)

import plotly.express as px
px.bar(data_frame = galeydf, x = 'year', y = 'viewCount', color = 'viewCount', orientation = 'v', width=800, height=400)
#Highest total number of views and video with highest view was released in the year 2022

px.histogram(data_frame = galeydf, x = 'year', width=800, height=400)
#Most video were released around the year 2020 to 2021
px.histogram(data_frame = galeydf, x = 'viewCount', width=800, height=400)
#Alomost all the videos has high numeber of views which is in million.
channeldf.size() #display the different channel along with the total number of videos in each channel



dfmean = channeldf['Title_name'].count() #new dataframe created to count the numeber of videos uploaded in each channel
dfmean.plot(kind = 'pie', title = 'Total count of Videos in each Channel', ylabel = 'Numbers of videos uploaded', xlabel = 'Channel Name', figsize = (10,6))
#Among seven MV Channel, M studio Flims has the highest number of videos

h1 = df1.nlargest(5, ['viewCount'])[['Title_name', 'year', 'playlistHostedChannelName', 'videoUrl', 'viewCount']] #Top 5 Music Video
px.bar(data_frame = h1, x = 'Title_name', y = 'viewCount', color = 'Title_name', orientation = 'v', width=800, height=400)
#Top five music video along with the number of views in each video


import plotly.express as px #Shows that the videos released in the year around 2019 to 2021 has the videos with the highest viewcount
px.line(data_frame = df1, x = 'year', y = 'viewCount', color = 'year', orientation = 'v', width=800, height=400)

import plotly.express as px #Shows that total number of view count in each channel
px.bar(data_frame = df1, x = 'playlistHostedChannelName', y = 'viewCount', color = 'playlistHostedChannelName', orientation = 'v', width=800, height=400)


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
server=app.server

tabs_styles = {
    'height': '34px',
    'align-items': 'center'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'border-radius': '15px',
    'color': 'white',
    'background-color': '#0a0a0a',
    'box-shadow': '4px 4px 4px 4px lightgrey',

}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#2577ba',
    'color': '#0a0a0a',
    'padding': '6px',
    'border-radius': '15px',
}

app.layout = html.Div((

    html.Div([
        html.Div([
            html.Div([
                html.H2('Bhutanese Music Video Analysis', style = {'margin-bottom': '0px', 'color': 'black', 'textAlign': 'center'}),
            ])
        ], className = "create_container1 four columns", id = "title"),

    ], id = "header", className = "row flex-display", style = {"margin-bottom": "25px"}),

html.Div([
    html.Div([
        dcc.Tabs(id = "tabs-styled-with-inline", value = 'tab-1', children = [
            dcc.Tab(label = 'Top 3 most viewed MV based on Selected Channel', value = 'tab-1', style = tab_style, selected_style = tab_selected_style),
            dcc.Tab(label = 'Comparison of different MV and MV Channel', value = 'tab-2', style = tab_style, selected_style = tab_selected_style),
            dcc.Tab(label = 'Music Video released based on Selected Year', value = 'tab-3', style = tab_style, selected_style = tab_selected_style),
            dcc.Tab(label = 'Conclusion from Visualization of Bhutanese MV Analysis', value = 'tab-4', style = tab_style, selected_style = tab_selected_style),
        ], style = tabs_styles),
        html.Div(id = 'tabs-content-inline')
    ], className = "create_container3 eight columns", ),
    ], className = "row flex-display"),

    html.Div([
        html.Div([

            html.P('Select Channel', className = 'fix_label', style = {'color': 'black', 'margin-top': '2px', 'display': 'None'}),
            dcc.Dropdown(id = 'select_channels',
                         multi = False,
                         clearable = True,
                         disabled = False,
                         style = {'display': 'None'},
                         value = 'Yeshi Lhendup Films',
                         placeholder = 'Select Channel',
                         options = [{'label': 'Yeshi Lhendup Films', 'value': 'Yeshi Lhendup Films'},
                                   {'label': 'Rigdrol Films', 'value': 'Rigdrol Films'},
                                   {'label': 'MStudio Bhutan', 'value': 'MStudio Bhutan'},
                                   {'label': 'VMUSIC BHUTAN', 'value': 'VMUSIC BHUTAN'},
                                   {'label': 'Tandin Phubz', 'value': 'Tandin Phubz'},
                                   {'label': 'Lhendup Audio Visual', 'value': 'Lhendup Audio Visual'},
                                   {'label': 'Galey Visual Production', 'value': 'Galey Visual Production'}],
                         className = 'dcc_compon'),

        ], className = "create_container3 four columns", style = {'margin-bottom': '20px'}),
    ], className = "row flex-display"),

        html.Div([
          html.Div([

            dcc.Graph(id = 'top3_chart',
                      style = {'display': 'None'},
                      config = {'displayModeBar': 'hover'}),
        ], className = "create_container3 six columns"),
    ], className = "row flex-display"),

), id= "mainContainer", style={"display": "flex", "flex-direction": "column"})


@app.callback(Output('tabs-content-inline', 'children'),
              Input('tabs-styled-with-inline', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.Div([
                html.Div([
                    html.P('Select Channel', className = 'fix_label', style = {'color': 'black', 'margin-top': '2px'}),
                    dcc.Dropdown(id = 'select_channels',
                                 multi = False,
                                 clearable = True,
                                 disabled = False,
                                 style = {'display': True},
                                 value = 'VMUSIC BHUTAN',
                                 placeholder = 'Select Channel',
                                 options = [{'label': 'Yeshi Lhendup Films', 'value': 'Yeshi Lhendup Films'},
                                           {'label': 'Rigdrol Films', 'value': 'Rigdrol Films'},
                                           {'label': 'MStudio Bhutan', 'value': 'MStudio Bhutan'},
                                           {'label': 'VMUSIC BHUTAN', 'value': 'VMUSIC BHUTAN'},
                                           {'label': 'Tandin Phubz', 'value': 'Tandin Phubz'},
                                           {'label': 'Lhendup Audio Visual', 'value': 'Lhendup Audio Visual'},
                                           {'label': 'Galey Visual Production', 'value': 'Galey Visual Production'}], 
                                 className = 'dcc_compon'),

                ], className = "create_container2 six columns", style = {'margin-top': '20px'}),
            ], className = "row flex-display"),
            
            html.Div([
                html.Div([
                    dcc.Graph(id = 'top3_chart',
                              config = {'displayModeBar': 'hover'}),
                ], className = "create_container2 twenty columns", style = {'margin-top': '10px'}),
            ], className = "row flex-display"),
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.Div([
                html.Div([
                    html.P('Click on the radio button for more information', className = 'fix_label', style = {'color': 'black'}),
                    dcc.RadioItems(id = 'radio_items',
                                   labelStyle = {"display": "inline-block"},
                                   options = [
                                       {'label': 'Top five music video along with the number of views in each video', 'value': 'line'},
                                       {'label': 'Total No of MV uploaded by each Channel till now', 'value': 'line1'},
                                       {'label': 'Total number of view count in each channel', 'value': 'line2'}],
                                   value = 'line',
                                   style = {'text-align': 'center', 'color': 'black'}, className = 'dcc_compon'),

                ], className = "create_container2 six columns", style = {'margin-top': '20px'}),
            ], className = "row flex-display"),

            html.Div([
                html.Div([


                    dcc.Graph(id = 'multi_chart1',
                              config = {'displayModeBar': 'hover'}),

                ], className = "create_container2 ten columns", style = {'margin-top': '10px'}),

            ], className = "row flex-display"),
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('MV Released Based on Year', style = {'text-align': 'center', 'margin-top': '50px', 'font-family':'courier;', 'color':'black'}),
            dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018},
                     {"label": "2019", "value": 2019},
                     {"label": "2020", "value": 2020},
                     {"label": "2021", "value": 2021},
                     {"label": "2022", "value": 2022}],
                 multi=False,
                 value=2017,
                 style={'width': "100%", 'textAlign': 'center'}
                 ),
            html.Div(id='output_container', children=[]),
            html.Br(),

            dcc.Graph(id='my_bee_map', figure={})
        ]) 
    
    elif tab == 'tab-4':
        return html.Div(children=[
            html.H1(children='Conclusion', style={'textAlign': 'center'}),

            html.Div(children='''
                1. MStudio Bhutan has the highest number of videos released so far with 92 videos uploaded followed by the Yeshi Lhendup Flims with 89 videos.

            ''',style={'textAlign': 'center','margin-top': '50px'}),

            html.Div(children='''
                2. The number of views in each music video does not depends on the year it was released as some of the latest videos has higher number of view counts compared to the old videos.
                
            ''',style={'textAlign': 'center','margin-top': '50px'}),

            html.Div(children='''
                3. Most of the music videos are released in the year between 2019 to 2021.
                
            ''',style={'textAlign': 'center','margin-top': '50px'}),

            html.Div(children='''
                4. The music video "YA TARU MA TARU " released in the year 2019 by Yeshi Lhendup Flims has the highest number of views with around 1.7 million.
                
            ''',style={'textAlign': 'center','margin-top': '50px'}),

            html.Div(children='''
                5. Yeshi Lhendup Flims has the highest total number of view with around 25 million.
                
            ''',style={'textAlign': 'center','margin-top': '50px'}),

             html.Div(children='''
                6. Thus, the Music Video Channel 'Yeashi Lhendup Flims' is most popular in Bhutan.
                
            ''',style={'textAlign': 'center','margin-top': '50px'}),
            ])
            
            

            
    
                
        
    
@app.callback(Output('multi_chart1', 'figure'),
              [Input('radio_items', 'value')])
def update_graph(radio_items):
    if radio_items == 'line':
        h1 = df1.nlargest(5, ['viewCount'])[['Title_name', 'year', 'playlistHostedChannelName', 'videoUrl', 'viewCount']]
        fig = px.bar(
        data_frame = h1, 
        x = 'Title_name', 
        y = 'viewCount', 
        color = 'Title_name',
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark',
        orientation = 'v')

        return fig

    if radio_items == 'line1':
        dfmean = channeldf['Title_name'].count()
        fig = px.pie(labels = ['Yeshi Lhendup Flims', 'Rigdrol Films', 'MStudio Bhutan','VMUSIC BHUTAN', 'Tandin Phubz','Lhendup Audio Visual','Galey Visual Production' ],
                        values = [89,9,92,6,22,14,7],
                        # marker = dict(colors = colors'),
                        # hoverinfo = 'label+value+percent',
                        # textinfo = 'label+value',
                        # textfont = dict(size = 13),
                        # texttemplate = '%{label}: %{value:,f} <br>(%{percent})',
                        # textposition = 'auto',
                        hole = .5,
                        template='plotly_dark',
                        title = 'Label: Yeshi Lhendup Flims = Orange  MStudio Bhutan = Blue Tandin Phubz = Green (Top 3 Channel with highest number of MV)',
                       )
        return fig

    if radio_items == 'line2':
        fig = px.bar(
        data_frame = df1, 
        x = 'playlistHostedChannelName', 
        y = 'viewCount', 
        color = 'playlistHostedChannelName',
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark',
        orientation = 'v')

        return fig


@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))
    yeardf = df1[['Title_name', 'year', 'viewCount']]
    yeardf = yeardf.sort_values(by='viewCount', ascending=False)
    dff = yeardf[yeardf["year"] == option_slctd]
    
    container = "The year chosen by user was: {}".format(option_slctd)

    fig = px.bar(
        data_frame=dff,
        x='viewCount',
        y='Title_name',
        hover_data=['viewCount', 'Title_name'],
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark',
        orientation = 'h'
    )

    return container, fig

@app.callback(
Output('top3_chart', 'figure'), 
[Input('select_channels', 'value')]
)
#graph plot and styling
def update_graph(channel):
    if channel == 'Yeshi Lhendup Films':
        return {'data':[go.Bar(
                                x = g1.viewCount,
                                y = g1.Title_name,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + g1['Title_name'].astype(str) + '<br>' +
                                    '<b>View Count</b>: ' + g1['viewCount'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#0a0a0a',
                            paper_bgcolor = '#0a0a0a',
                            title = {
                                    'text': 'Top 3 Music of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>View Count</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'white',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'white'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Title Name</b>',
                                autorange = 'reversed',
                                color = 'white',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'white',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'white'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Rigdrol Films':
        return {'data':[go.Bar(
                                x = g2.viewCount,
                                y = g2.Title_name,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + g2['Title_name'].astype(str) + '<br>' +
                                    '<b>View Count</b>: ' + g2['viewCount'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#0a0a0a',
                            paper_bgcolor = '#0a0a0a',
                            title = {
                                    'text': 'Top 3 Music of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'white',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>View Count</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'white',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'white'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Title Name</b>',
                                autorange = 'reversed',
                                color = 'white',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'white'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'MStudio Bhutan':
        return {'data':[go.Bar(
                                x = g3.viewCount,
                                y = g3.Title_name,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + g3['Title_name'].astype(str) + '<br>' +
                                    '<b>View Count</b>: ' + g3['viewCount'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#0a0a0a',
                            paper_bgcolor = '#0a0a0a',
                            title = {
                                    'text': 'Top 3 Music of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'white',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>View Count</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'white',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'white'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Title Name</b>',
                                autorange = 'reversed',
                                color = 'white',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'white',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'white'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'VMUSIC BHUTAN':
        return {'data':[go.Bar(
                                x = g4.viewCount,
                                y = g4.Title_name,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + g4['Title_name'].astype(str) + '<br>' +
                                    '<b>View Count</b>: ' + g4['viewCount'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#0a0a0a',
                            paper_bgcolor = '#0a0a0a',
                            title = {
                                    'text': 'Top 3 Music of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'white',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>View Count</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'white',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'white'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Title Name</b>',
                                autorange = 'reversed',
                                color = 'white',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'white',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'white'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Tandin Phubz':
        return {'data':[go.Bar(
                                x = g5.viewCount,
                                y = g5.Title_name,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + g5['Title_name'].astype(str) + '<br>' +
                                    '<b>View Count</b>: ' + g5['viewCount'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#0a0a0a',
                            paper_bgcolor = '#0a0a0a',
                            title = {
                                    'text': 'Top 3 Music of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'white',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>View Count</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'white',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'white'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Title Name</b>',
                                autorange = 'reversed',
                                color = 'white',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'white',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'white'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Lhendup Audio Visual':
        return {'data':[go.Bar(
                                x = g6.viewCount,
                                y = g6.Title_name,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + g6['Title_name'].astype(str) + '<br>' +
                                    '<b>View Count</b>: ' + g6['viewCount'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#0a0a0a',
                            paper_bgcolor = '#0a0a0a',
                            title = {
                                    'text': 'Top 3 Music of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'white',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>View Count</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'white',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'white'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Title Name</b>',
                                autorange = 'reversed',
                                color = 'white',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'white',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'white'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Galey Visual Production':
        return {'data':[go.Bar(
                                x = g7.viewCount,
                                y = g7.Title_name,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + g7['Title_name'].astype(str) + '<br>' +
                                    '<b>View Count</b>: ' + g7['viewCount'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#0a0a0a',
                            paper_bgcolor = '#0a0a0a',
                            title = {
                                    'text': 'Top 3 Music of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'white',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>View Count</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'white',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'white'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Title Name</b>',
                                autorange = 'reversed',
                                color = 'white',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'white',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'white'
                                )
                            ),                         
                        )    
               }


if __name__ == '__main__':
    app.run_server()