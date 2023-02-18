import pandas as pd
from sqlalchemy import create_engine,text

#First, create a pg database npiProviders.  Update username/password as necessary

#Connect to database
url = 'postgresql+psycopg2://postgres:password@localhost/npiProviders'  
engine = create_engine(url)

#Read in file to populate DB
matches = pd.read_csv('prepared_data_for_db.csv',index_col=0)  #this file has all information formatted and prepared

#Put dataframe contents into database
matches.to_sql('npi_registry',url,if_exists='replace',index=False)

#IN PGADMIN/PSQL, RUN:
# ALTER TABLE npi_registry ADD COLUMN geom GEOMETRY(point, 4326); ##Create geom column
# UPDATE npi_registry SET geom = ST_SETSRID(ST_MakePoint(cast("LON" as float), cast("LAT" as float)),4326); ## create geom from coordinates
# alter table npi_registry alter column "LAT" type numeric using ("LAT"::numeric); 
# alter table npi_registry alter column "LON" type numeric using ("LON"::numeric);