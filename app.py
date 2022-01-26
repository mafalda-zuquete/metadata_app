import dash
import dash_core_components as dcc
#import dash as dcc
import dash_html_components as html
#from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import pandas as pd
from bs4 import BeautifulSoup
import plotly.graph_objs as go
import json
from datetime import datetime

#external_stylesheets = [
    #'https://codepen.io/Lewitje/pen/doJRBX.css',
    #{
        #'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        #'rel': 'stylesheet',
        #'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        #'crossorigin': 'anonymous'
    #}
#]

#data theme
data_theme_df = pd.read_csv("data-theme.csv")

theme_zip = zip(data_theme_df["code"],data_theme_df["label"])

theme_options = []

for theme in theme_zip:
    theme_dict = {"label":theme[1],"value":theme[0]}
    theme_options.append(theme_dict)

#access right
access_right_df = pd.read_csv("access-right.csv")

access_right_zip = zip(access_right_df["code"],access_right_df["name"])

access_right_options = []

for access in access_right_zip:
    access_right_dict = {"label":access[1],"value":access[0]}
    access_right_options.append(access_right_dict)

#frequencies
frequencies_df = pd.read_csv("frequencies.csv")

frequencies_zip = zip(frequencies_df["code"],frequencies_df["name"])

frequencies_options = []

for frequency in frequencies_zip:
    frequencies_dict = {"label":frequency[1],"value":frequency[0]}
    frequencies_options.append(frequencies_dict)

#languages
languages_df = pd.read_csv("languages.csv")

languages_zip = zip(languages_df["code"],languages_df["name"])

languages_options = []

for language in languages_zip:
    languages_dict = {"label":language[1],"value":language[0]}
    languages_options.append(languages_dict)

#filetypes
filetypes_df = pd.read_csv("filetypes.csv")

filetypes_zip = zip(filetypes_df["code"],filetypes_df["name"])

filetypes_options = []

for filetype in filetypes_zip:
    filetypes_dict = {"label":filetype[1],"value":filetype[0]}
    filetypes_options.append(filetypes_dict)

filetypes_zip_2 = zip(filetypes_df["code"],filetypes_df["mediaType"])

file_mediatypes = {}

for filetype in filetypes_zip_2:
    file_mediatypes[filetype[0]] = filetype[1]

#licenses
licenses_df = pd.read_csv("licenses.csv")

licenses_zip = zip(licenses_df["code"],licenses_df["name"])

licenses_options = []

for license in licenses_zip:
    licenses_dict = {"label":license[1],"value":license[0]}
    licenses_options.append(licenses_dict)

#countries
countries_df = pd.read_csv("countries.csv")

countries_zip = zip(countries_df["code"],countries_df["name"])

countries_options = []

for country in countries_zip:
    countries_dict = {"label":country[1],"value":country[0]}
    countries_options.append(countries_dict)

#continents
continents_df = pd.read_csv("continents.csv")

continents_zip = zip(continents_df["code"],continents_df["name"])

continents_options = []

for continent in continents_zip:
    continents_dict = {"label":continent[1],"value":continent[0]}
    continents_options.append(continents_dict)

#places
places_df = pd.read_csv("places.csv")

places_zip = zip(places_df["code"],places_df["name"])

places_options = []

for place in places_zip:
    places_dict = {"label":place[1],"value":place[0]}
    places_options.append(places_dict)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])#, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([

    html.H1("Metadata JSON Generator"),
    html.Div("Fill out all the fields with information related with the file that you want to generate a metadata file for. When you are done, name the metada file and download the information."),
    html.Div("Write the name of the metadata file"),
    dcc.Input(
        id="filename",
        placeholder="File name",
        type="text",
        value=""
    ),
    html.Button("Download file", id="button_download"),
    dcc.Download(id="download"),
    dcc.Tabs(
        id="tabs",
        value="agent",
        children=[
            dcc.Tab(
                label="Agent",
                value="agent",
                children=[
                    html.Div("Write the name of the entitiy responsible for making the dataset available"),
                    dcc.Input(
                        id="agent",
                        placeholder="Agent",
                        type="text",
                        value=""
                    ),
                    html.Button("Submit",id="button_agent",n_clicks=0),
                    html.Div(id="div_agent")
                ]
            ),
            dcc.Tab(
                label="Contact Point",
                value="contact_point",
                children=[
                    html.Div("Write a contact e-mail in case there are comments or doubts regarding the dataset"),
                    dcc.Input(
                        id="contact_point",
                        placeholder="Contact point",
                        type="email",
                        value=""
                    ),
                    html.Button("Submit",id="button_contact_point",n_clicks=0),
                    html.Div(id="div_contact_point")
                ]
            ),
            dcc.Tab(
                label="Dataset",
                value="dataset",
                children=[
                    html.Div("Dataset title"),
                    dcc.Input(
                        id="title_dataset",
                        placeholder="Title",
                        type="text",
                        value=""
                    ),
                    html.Div("Dataset description"),
                    dcc.Textarea(
                        id="description_dataset",
                        placeholder="Description",
                        value=""
                    ),
                    html.Div("Write keywords related to the dataset (separated by commas)"),
                    dcc.Textarea(
                        id="keywords",
                        placeholder="Keywords",
                        value=""
                    ),
                    html.Div("Select the dataset's theme"),
                    dcc.Dropdown(
                        id="theme",
                        options=theme_options,
                        placeholder="Theme"
                    ),
                    html.Div("Select the dataset's access rights"),
                    dcc.Dropdown(
                        id="access_right",
                        options=access_right_options,
                        placeholder="Acess"
                    ),
                    html.Div("Select the dataset's update frequency"),
                    dcc.Dropdown(
                        id="frequency",
                        options=frequencies_options,
                        placeholder="Frequency"
                    ),
                    html.Div("Select the dataset's language"),
                    dcc.Dropdown(
                        id="language_dataset",
                        options=languages_options,
                        placeholder="Langugage"
                    ),
                    html.Div("Date when the dataset was issued"),
                    dcc.DatePickerSingle(
                        id="issued_dataset",
                        date=datetime.today(),
                    ),
                    html.Div("Date when the dataset was most recently modified"),
                    dcc.DatePickerSingle(
                        id="modified_dataset",
                        date=datetime.today(),
                    ),
                    html.Button("Submit",id="button_dataset",n_clicks=0),
                    html.Div(id="div_dataset")
                ]
            ),
            dcc.Tab(
                label="Distribution",
                value="distribution",
                children=[
                    html.Div("Distribution title"),
                    dcc.Input(
                        id="title_distribution",
                        placeholder="Title",
                        type="text",
                        value=""
                    ),
                    html.Div("Distribution description"),
                    dcc.Textarea(
                        id="description_distribution",
                        placeholder="Description",
                        value=""
                    ),
                    html.Div("URL to access the distribution"),
                    dcc.Input(
                        id="accessURL",
                        placeholder="Access URL",
                        type="url",
                        value=""
                    ),
                    html.Div("URL to download the distribution"),
                    dcc.Input(
                        id="downloadURL",
                        placeholder="Download URL",
                        type="url",
                        value=""
                    ),
                    html.Div("Select the distribution's format"),
                    dcc.Dropdown(
                        id="format",
                        options=filetypes_options,
                        placeholder="Format"
                    ),
                    html.Div("Distribution size in bytes"),
                    dcc.Input(
                        id="byteSize",
                        placeholder="Byte size",
                        type="number",
                        value=""
                    ),
                    html.Div("Select the dataset's language"),
                    dcc.Dropdown(
                        id="language_distribution",
                        options=languages_options,
                        placeholder="Language"
                    ),
                    html.Div("Date when the distribution was issued"),
                    dcc.DatePickerSingle(
                        id="issued_distribution",
                        date=datetime.today(),
                    ),
                    html.Div("Date when the distribution was most recently modified"),
                    dcc.DatePickerSingle(
                        id="modified_distribution",
                        date=datetime.today(),
                    ),
                    html.Button("Submit",id="button_distribution",n_clicks=0),
                    html.Div(id="div_distribution")
                ]
            ),
            dcc.Tab(
                label="License Document",
                value="license_document",
                children=[
                    html.Div("Select the dataset's license type"),
                    dcc.Dropdown(
                        id="license",
                        options=licenses_options,
                        placeholder="License"
                    ),
                    html.Button("Submit",id="button_license",n_clicks=0),
                    html.Div(id="div_license")
                ]
            ),
            dcc.Tab(
                label="Location",
                value="location",
                children=[
                    html.Div("Select the dataset's location type"),
                    dcc.Tabs(
                        id="location_tabs",
                        value="coordinates",
                        children=[
                            dcc.Tab(
                                label="Coordinates",
                                value="coordinates",
                                children=[
                                    html.Div("Write the coordinates of the bounding box of the location described by the dataset"),
                                    dcc.Textarea(
                                        id="bbox",
                                        placeholder="Bounding box coordinates",
                                        value=""
                                    ),
                                    html.Div("Write the coordinates of the centroid of the location described by the dataset"),
                                    dcc.Input(
                                        id="centroid",
                                        placeholder="Centroid coordinates",
                                        value="",
                                        type="text"
                                    ),
                                    html.Div(id="div_location_coordinates")
                                ]
                            ),
                            dcc.Tab(
                                label="Continent",
                                value="continents",
                                children=[
                                    html.Div("Select the continent that the dataset refers to"),
                                    dcc.Dropdown(
                                        id="continent",
                                        options=continents_options,
                                        placeholder="Continent"
                                    ),
                                    html.Div(id="div_location_continents")
                                ]
                            ),
                            dcc.Tab(
                                label="Country",
                                value="countries",
                                children=[
                                    html.Div("Select the country that the dataset refers to"),
                                    dcc.Dropdown(
                                        id="country",
                                        options=countries_options,
                                        placeholder="Country"
                                    ),
                                    html.Div(id="div_location_countries")
                                ]
                            ),
                            dcc.Tab(
                                label="Place",
                                value="places",
                                children=[
                                    html.Div("Select the place that the dataset refers to"),
                                    dcc.Dropdown(
                                        id="place",
                                        options=places_options,
                                        placeholder="Place"
                                    ),
                                    html.Div(id="div_location_places")
                                ]
                            ),
                        ],
                    ),
                    html.Button("Submit",id="button_location",n_clicks=0),
                ]
            ),
            dcc.Tab(
                label="Period of Time",
                value="period_of_time",
                children=[
                    html.Div("Start of the period of time described by the dataset"),
                    dcc.DatePickerSingle(
                        id="startDate",
                        date=datetime.today(),
                    ),
                    html.Div("End of the period of time described by the dataset"),
                    dcc.DatePickerSingle(
                        id="endDate",
                        date=datetime.today(),
                    ),
                    html.Button("Submit",id="button_period_of_time",n_clicks=0),
                    html.Div(id="div_period_of_time")
                ]
            )
        ]
    ),
    dbc.Row(
        id='images',
        children=[
            html.Img(src='/assets/nova_ims.png',style={'width':'10%'}),
            html.Img(src='/assets/CML.jpg',style={'width':'10%'}),
            html.Img(src='/assets/ama.jpg',style={'width':'10%'}),
            html.Img(src='/assets/nec.png',style={'width':'10%'}),
            html.Img(src='/assets/bsc.png',style={'width':'10%'})
        ],
        #style={'display':'inline-block','vertical-align':'bottom'}
    )
])

@app.callback(
    Output("div_agent","children"),
    [
        Input("agent","value"),
        Input("button_agent","n_clicks")
    ]
)
def agent_json(agent,n_clicks):
    changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
    if "button_agent" in changed_id:
        agent_meta = {
            "@id":"_:b0",
            "@type":"foaf:Agent",
            "name":{
                "@language":"pt",
                "@value":agent
            }
        }

        with open("agent.json", "w") as outfile:
            json.dump(agent_meta, outfile)

        return "Submitted"
        #return str(agent_meta)

@app.callback(
    Output("div_contact_point","children"),
    [
        Input("contact_point","value"),
        Input("button_contact_point","n_clicks")
    ]
)
def contact_point_json(contact_point,n_clicks):
    changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
    if "button_contact_point" in changed_id:
        contact_point_meta = {
            "@id":"_:b1",
            "@type":"http://www.w3.org/2006/vcard/ns#Kind",
            "hasEmail":contact_point
        }

        with open("contact_point.json", "w") as outfile:
            json.dump(contact_point_meta, outfile)

        return "Submitted"
        #return str(contact_point_meta)

@app.callback(
    Output("div_dataset","children"),
    [
        Input("title_dataset","value"),
        Input("description_dataset","value"),
        Input("keywords","value"),
        Input("theme","value"),
        Input("access_right","value"),
        Input("frequency","value"),
        Input("language_dataset","value"),
        Input("issued_dataset","date"),
        Input("modified_dataset","date"),
        Input("button_dataset","n_clicks")
    ]
)
def dataset_json(title,description,keywords,theme,access_right,frequency,language,issued,modified,n_clicks):
    changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
    if "button_dataset" in changed_id:
        if (theme is not None) and (access_right is not None) and (frequency is not None) and (language is not None):
            dataset_meta = {
                "@id":"dataset_id",
                "@type":"dcat:Dataset",
                "description":description,
                "title":title,
                "keyword":keywords.split(","),
                "theme":"http://publications.europa.eu/resource/authority/data-theme/" + theme,
                "accessRights":"http://publications.europa.eu/resource/authority/access-right/" + access_right,
                "accuralPeriodicity":"http://publications.europa.eu/resource/authority/frequency/" + frequency,
                "language":"http://publications.europa.eu/resource/authority/language/" + language,
                "issued":issued,
                "modified":modified
            }

            with open("dataset.json", "w") as outfile:
                json.dump(dataset_meta, outfile)
        
            return "Submitted"
            #return str(dataset_meta)

"""@app.callback(
    Output("div_n_distribution","children"),
    Input("n_distributions","value")
)
def many_distributions(n_distributions):
    tabs = []

    if n_distributions is None:
        n_distributions = 0

    for i in range(n_distributions):
        j = i+1
        tab = dcc.Tab(
            label=str(j),
            value=str(j)
        )
        tabs.append(tab)

    dist_tab = dcc.Tabs(
        id="dist_tabs",
        value="1",
        children=tabs
    )

    return dist_tab"""

@app.callback(
    Output("div_distribution","children"),
    [
        Input("title_distribution","value"),
        Input("description_distribution","value"),
        Input("accessURL","value"),
        Input("downloadURL","value"),
        Input("format","value"),
        Input("byteSize","value"),
        Input("language_distribution","value"),
        Input("issued_distribution","date"),
        Input("modified_distribution","date"),
        Input("button_distribution","n_clicks")
    ]
)
def distribution_json(title,description,accessURL,downloadURL,format,byteSize,language,issued,modified,n_clicks):
    print(n_clicks)
    changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
    if "button_distribution" in changed_id:
        if (format is not None) and (language is not None):
            distribution_id = "distribution_" + str(n_clicks)
            distribution_meta = {
                "@id":distribution_id,
                "@type":"dcat:Distribution",
                "accessURL":accessURL,
                "description":description,
                "format":"http://publications.europa.eu/resource/authority/file-type/" + format,
                "byteSize":byteSize,
                "downloadURL":downloadURL,
                "language":"http://publications.europa.eu/resource/authority/language/" + language,
                "mediaType":file_mediatypes[format],
                "title":title,
                "issued":issued,
                "modified":modified
            }

            filename = 'distribution_' + str(n_clicks) + '.json'

            with open(filename, "w") as outfile:
                json.dump(distribution_meta, outfile)
        
            return "Submitted"
            #return str(distribution_meta)

@app.callback(
    Output("div_license","children"),
    [
        Input("license","value"),
        Input("button_license","n_clicks")
    ]
)
def license_json(license,n_clicks):
    changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
    if "button_license" in changed_id:
        if (license is not None):
            license_meta = {
                "@id":"_:b2",
                "@type":"dct:license",
                "type":"http://publications.europa.eu/resource/authority/licence/" + license
            }

            with open("license.json", "w") as outfile:
                json.dump(license_meta, outfile)

            return "Submitted"
            #return str(license_meta)

@app.callback(
    Output("div_period_of_time","children"),
    [
        Input("startDate","date"),
        Input("endDate","date"),
        Input("button_period_of_time","n_clicks")
    ]
)
def period_of_time_json(startDate,endDate,n_clicks):
    changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
    if "button_period_of_time" in changed_id:
        period_of_time_meta = {
            "@id":"_:b3",
            "@type":"dct:PeriodOfTime",
            "startDate":startDate,
            "endDate":endDate
        }

        with open("period_of_time.json", "w") as outfile:
            json.dump(period_of_time_meta, outfile)

        return "Submitted"
        #return str(period_of_time_meta)

@app.callback(
    Output("div_location_coordinates","children"),
    [
        Input("bbox","value"),
        Input("centroid","value"),
        Input("button_location","n_clicks")
    ]
)
def location_coordinates_json(bbox,centroid,n_clicks):
    changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
    if "button_location" in changed_id:
        location_meta = {
            "@id":"_:b4",
            "@type":"dct:Location",
            "bbox":bbox,
            "centroid":centroid
        }

        with open("location.json", "w") as outfile:
            json.dump(location_meta, outfile)

        return "Submitted"
        #return str(location_meta)

@app.callback(
    Output("div_location_continents","children"),
    [
        Input("continent","value"),
        Input("button_location","n_clicks")
    ]
)
def location_coordinates_json(continent,n_clicks):
    changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
    if "button_location" in changed_id:
        if (continent is not None):
            location_meta = {
                "@id":"_:b4",
                "@type":"dct:Location",
                "geometry":"http://publications.europa.eu/resource/authority/continent/" + continent
            }

            with open("location.json", "w") as outfile:
                json.dump(location_meta, outfile)

            return "Submitted"
            #return str(location_meta)

@app.callback(
    Output("div_location_countries","children"),
    [
        Input("country","value"),
        Input("button_location","n_clicks")
    ]
)
def location_countries_json(country,n_clicks):
    changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
    if "button_location" in changed_id:
        if (country is not None):
            location_meta = {
                "@id":"_:b4",
                "@type":"dct:Location",
                "geometry":"http://publications.europa.eu/resource/authority/country/" + country
            }

            with open("location.json", "w") as outfile:
                json.dump(location_meta, outfile)

            return "Submitted"
            #return str(location_meta)

@app.callback(
    Output("div_location_places","children"),
    [
        Input("place","value"),
        Input("button_location","n_clicks")
    ]
)
def location_places_json(place,n_clicks):
    changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
    if "button_location" in changed_id:
        if (place is not None):
            location_meta = {
                "@id":"_:b4",
                "@type":"dct:Location",
                "geometry":"http://publications.europa.eu/resource/authority/place/" + place
            }

            with open("location.json", "w") as outfile:
                json.dump(location_meta, outfile)

            return "Submitted"
            #return str(location_meta)

@app.callback(
    #Output("div_final","children"),
    Output("download","data"),
    [
        Input("button_distribution","n_clicks"),
        Input("filename","value"),
        Input("button_download","n_clicks")
        #Input("button_submit","n_clicks")
    ]
)
def submit(n_dist,file_name,n_clicks):
    changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
    if "button_download" in changed_id:
        with open("agent.json") as agent_file:
            agent = json.load(agent_file)
        with open("contact_point.json") as contact_point_file:
            contact_point = json.load(contact_point_file)
        with open("dataset.json") as dataset_file:
            dataset = json.load(dataset_file)

        dists = []
        for i in range(1,n_dist+1):
            file = 'distribution_' + str(i) + '.json'
            with open(file) as distribution_file:
                distribution = json.load(distribution_file)
                dists.append(distribution)

        with open("license.json") as license_file:
            license = json.load(license_file)
        with open("location.json") as location_file:
            location = json.load(location_file)
        with open("period_of_time.json") as period_of_time_file:
            period_of_time = json.load(period_of_time_file)

        dataset["contactPoint"] = contact_point["@id"]

        dists_id = []
        for d in dists:
            dists_id.append(d['@id'])

        dataset["distribution"] = dists_id
        dataset["publisher"] = agent["@id"]
        dataset["spatial"] = location["@id"]
        dataset["temporal"] = period_of_time["@id"]

        distribution["licenseDocument"] = license["@id"]

        metadata = {
            "@context":{
                "name":{
                    "@id":"http://xmlns.com/foaf/spec/name"
                },
                "type":{
                    "@id":"http://purl.org/dc/terms/type"
                },
                "dataset":{
                    "@id":"http://www.w3.org/ns/dcat#dataset",
                    "@type":"@id"
                },
                "description":{
                    "@id":"http://purl.org/dc/terms/description"
                },
                "publisher":{
                    "@id":"http://purl.org/dc/terms/publisher",
                    "@type":"@id"
                },
                "title":{
                    "@id":"http://purl.org/dc/terms/title"
                },
                "homepage":{
                    "@id":"http://xmlns.com/foaf/0.1/homepage",
                    "@type":"@id"
                },
                "language":{
                    "@id":"http://purl.org/dc/terms/language",
                    "@type":"@id"
                },
                "license":{
                    "@id":"http://purl.org/dc/terms/license",
                    "@type":"@id"
                },
                "issued":{
                    "@id":"http://purl.org/dc/terms/issued",
                    "@type":"http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "spatial":{
                    "@id":"http://purl.org/dc/terms/spatial",
                    "@type":"@id"
                },
                "themeTaxonomy":{
                    "@id":"http://www.w3.org/ns/dcat#themeTaxonomy",
                    "@type":"@id"
                },
                "modified":{
                    "@id":"http://purl.org/dc/terms/modified",
                    "@type":"http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "hasPart":{
                    "@id":"http://purl.org/dc/terms/hasPart",
                    "@type":"@id"
                },
                "isPartOf":{
                    "@id":"http://purl.org/dc/terms/isPartOf",
                    "@type":"@id"
                },
                "record":{
                    "@id":"http://www.w3.org/ns/dcat#record",
                    "@type":"@id"
                },
                "rights":{
                    "@id":"http://purl.org/dc/terms/rights",
                    "@type":"@id"
                },
                "service":{
                    "@id":"http://www.w3.org/ns/dcat#service",
                    "@type":"@id"
                },
                "catalog":{
                    "@id":"http://www.w3.org/ns/dcat#catalog",
                    "@type":"@id"
                },
                "creator":{
                    "@id":"http://purl.org/dc/terms/creator",
                    "@type":"@id"
                },
                "contactPoint":{
                    "@id":"http://www.w3.org/ns/dcat#contactPoint",
                    "@type":"@id"
                },
                "distribution":{
                    "@id":"http://www.w3.org/ns/dcat#distribution",
                    "@type":"@id"
                },
                "keyword":{
                    "@id":"http://www.w3.org/ns/dcat#keyword"
                },
                "temporal":{
                    "@id":"http://purl.org/dc/terms/temporal",
                    "@type":"@id"
                },
                "theme":{
                    "@id":"http://www.w3.org/ns/dcat#theme",
                    "@type":"@id"
                },
                "accessRights":{
                    "@id":"http://purl.org/dc/terms/accessRights",
                    "@type":"@id"
                },
                "conformsTo":{
                    "@id":"http://purl.org/dc/terms/conformsTo",
                    "@type":"@id"
                },
                "page":{
                    "@id":"http://xmlns.com/foaf/0.1/page",
                    "@type":"@id"
                },
                "accuralPeriodicity":{
                    "@id":"http://purl.org/dc/terms/accuralPeriodicity",
                    "@type":"@id"
                },
                "hasVersion":{
                    "@id":"http://purl.org/dc/terms/hasVersion",
                    "@type":"@id"
                },
                "identifier":{
                    "@id":"http://purl.org/dc/terms/identifier",
                    "@type":"@id"
                },
                "isReferencedBy":{
                    "@id":"http://purl.org/dc/terms/isReferencedBy",
                    "@type":"@id"
                },
                "isVersionOf":{
                    "@id":"http://purl.org/dc/terms/isVersionOf",
                    "@type":"@id"
                },
                "landingPage":{
                    "@id":"http://www.w3.org/ns/dcat#landingPage",
                    "@type":"@id"
                },
                "otherIdentifier":{
                    "@id":"http://purl.org/dc/terms/identifier",
                    "@type":"@id"
                },
                "provenance":{
                    "@id":"http://purl.org/dc/terms/provenance",
                    "@type":"@id"
                },
                "qualifiedAttribution":{
                    "@id":"https://www.w3.org/ns/prov#qualifiedAttribution",
                    "@type":"@id"
                },
                "qualifiedRelation":{
                    "@id":"http://www.w3.org/ns/dcat#qualifiedRelation",
                    "@type":"@id"
                },
                "relation":{
                    "@id":"http://purl.org/dc/terms/relation",
                    "@type":"@id"
                },
                "sample":{
                    "@id":"http://www.w3.org/ns/adms#sample",
                    "@type":"@id"
                },
                "source":{
                    "@id":"http://purl.org/dc/terms/source",
                    "@type":"@id"
                },
                "spatialResolutionInMeters":{
                    "@id":"http://www.w3.org/ns/dcat#spatialResolutionInMeters",
                    "@type":"http://www.w3.org/2001/XMLSchema#decimal"
                },
                "temporalResolution":{
                    "@id":"http://www.w3.org/ns/dcat#temporalResolution",
                    "@type":"http://www.w3.org/2001/XMLSchema#duration"
                },
                "versionInfo":{
                    "@id":"http://www.w3.org/2002/07/owl#versionInfo"
                },
                "versionNotes":{
                    "@id":"http://www.w3.org/ns/adms#versionNotes"
                },
                "wasGeneratedBy":{
                    "@id":"http://www.w3.org/ns/prov#wasGeneratedBy",
                    "@type":"@id"
                },
                "primaryTopic":{
                    "@id":"http://xmlns.com/foaf/0.1/primaryTopic",
                    "@type":"@id"
                },
                "status":{
                    "@id":"http://www.w3.org/ns/adms#status",
                    "@type":"@id"
                },
                "endpointURL":{
                    "@id":"http://www.w3.org/ns/dcat#endpointURL",
                    "@type":"@id"
                },
                "endpointDescription":{
                    "@id":"http://www.w3.org/ns/dcat#endpointDescription",
                    "@type":"@id"
                },
                "servesDataset":{
                    "@id":"http://www.w3.org/ns/dcat#servesDataset",
                    "@type":"@id"
                },
                "accessURL":{
                    "@id":"http://www.w3.org/ns/dcat#accessURL",
                    "@type":"@id"
                },
                "availability":{
                    "@id":"http://data.europa.eu/r5r/availability",
                    "@type":"@id"
                },
                "format":{
                    "@id":"http://purl.org/dc/terms/format",
                    "@type":"@id"
                },
                "accessService":{
                    "@id":"http://www.w3.org/ns/dcat#accessService",
                    "@type":"@id"
                },
                "byteSize":{
                    "@id":"http://www.w3.org/ns/dcat#byteSize",
                    "@type":"http://www.w3.org/2001/XMLSchema#decimal"
                },
                "checksum":{
                    "@id":"http://spdx.org/rdf/terms#checksum",
                    "@type":"@id"
                },
                "compressFormat":{
                    "@id":"http://www.w3.org/ns/dcat#compressFormat",
                    "@type":"@id"
                },
                "downloadURL":{
                    "@id":"http://www.w3.org/ns/dcat#downloadURL",
                    "@type":"@id"
                },
                "hasPolicy":{
                    "@id":"http://www.w3.org/ns/odrl/2/hasPolicy",
                    "@type":"@id"
                },
                "mediaType":{
                    "@id":"http://www.w3.org/ns/dcat#mediaType",
                    "@type":"@id"
                },
                "packageFormat":{
                    "@id":"http://www.w3.org/ns/dcat#packageFormat",
                    "@type":"@id"
                },
                "prefLabel":{
                    "@id":"http://www.w3.org/2004/02/skos/core#prefLabel"
                },
                "algorithm":{
                    "@id":"http://spdx.org/rdf/terms#algorithm",
                    "@type":"@id"
                },
                "checksumValue":{
                    "@id":"http://spdx.org/rdf/terms#checksumValue",
                    "@type":"http://www.w3.org/2001/XMLSchema#hexBinary"
                },
                "notation":{
                    "@id":"http://www.w3.org/2004/02/skos/core#notation",
                    "@type":"@id"
                },
                "bbox":{
                    "@id":"http://www.w3.org/ns/dcat#bbox"
                },
                "centroid":{
                    "@id":"http://www.w3.org/ns/dcat#centroid"
                },
                "geometry":{
                    "@id":"http://www.w3.org/ns/locn#geometry"
                },
                "startDate":{
                    "@id":"http://www.w3.org/ns/dcat#startDate",
                    "@type":"http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "endDate":{
                    "@id":"http://www.w3.org/ns/dcat#endDate",
                    "@type":"http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "hadRole":{
                    "@id":"http://www.w3.org/ns/dcat#hadRole",
                    "@type":"@id"
                },
                "mbox":{
                    "@id":"http://xmlns.com/foaf/0.1/mbox"
                },
                "adms":"http://www.w3.org/ns/adms#",
                "dcat":"http://www.w3.org/ns/dcat#",
                "dcatap":"http://data.europa.eu/r5r/",
                "dct":"http://purl.org/dc/terms/",
                "foaf":"http://xmlns.com/foaf/0.1/",
                "locn":"http://www.w3.org/ns/locn#",
                "owl":"http://www.w3.org/2002/07/owl#",
                "odrl":"http://www.w3.org/ns/odrl/2/",
                "rdfs":"http://www.w3.org/2000/01/rdf-schema#",
                "schema":"http://schema.org/",
                "skos":"http://www.w3.org/2004/02/skos/core#",
                "spdx":"http://spdx.org/rdf/terms#",
                "xsd":"http://www.w3.org/2001/XMLSchema#",
                "vann":"http://purl.org/vocab/vann/",
                "voaf":"http://purl.org/vocommons/voaf#",
                "vcard":"http://www.w3.org/2006/vcard/ns#"
            },
            "@graph":[
                agent,
                contact_point,
                dataset,
                license,
                location,
                period_of_time
            ] + dists
        }

        #with open(filename + ".jsonld", "w") as outfile:
            #json.dump(metadata, outfile)

        metadata_str = str(metadata).replace("'",'"')

        return dict(content=metadata_str,filename=file_name + ".jsonld")
        #return str(metadata)

if __name__ == "__main__":
    app.run_server(debug=True)