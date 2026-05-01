import pandas as pd
import ssl

# Bypass SSL for the classroom
ssl._create_default_https_context = ssl._create_unverified_context

# Dataset 1: Airports
air_url = "https://raw.githubusercontent.com/datasets/airport-codes/refs/heads/main/data/airport-codes.csv"
df_air = pd.read_csv(air_url)

# Dataset 2: Country Metadata (for merging)
country_url = "https://raw.githubusercontent.com/datasets/country-codes/master/data/country-codes.csv"
df_countries = pd.read_csv(country_url)

# AM_ports = df_air[df_air['iso_country']=='AM'] 
# GE_ports = df_air[df_air['iso_country']=='GE'] 

# caucasus_airports = pd.concat([AM_ports, GE_ports])
# print(caucasus_airports.head())

# df_countries = df_countries[['ISO3166-1-Alpha-2', 'official_name_en', 'ISO4217-currency_name']]


# df_countries = pd.merge(
#     df_countries,
#     df_air,
#     left_on="ISO3166-1-Alpha-2",
#     right_on="icao_code",
# )

# print(df_countries.head())

