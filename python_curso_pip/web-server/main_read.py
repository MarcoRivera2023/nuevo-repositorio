import pandas as pd

def run():
    df = pd.read("data.csv")
    df=df[df["Continent"]=="Africa"]
    
    countries = df["Country"].values
    percentages=df["World Population Percentage"].values
    charts.generate_pie_chart(countries, percentages)
    
    data=read_csv.read_csv("data.csv")
    country = input ("Type Cpuntry =>")
    print (country)
    
    results=utils.population_by_country(data, country)
     if len(results)>0:
         
         