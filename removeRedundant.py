import json 
import os
from typing_extensions import Required


def removeRedundantColumns(fileName,newFileName,columnsToInsert):
    #get the current directory name
    script_dir = os.path.dirname(__file__)

    #all the json files are under the folder datasets in the current directory
    rel_path = "datasets"

    #get the absolute path of the current directory and the dataset
    abs_file_path = os.path.join(script_dir, rel_path)
    absFilePath = os.path.join(abs_file_path,fileName)
    f = open(absFilePath,'r')
    # returns JSON object as a dictionary
    data = json.load(f) 
    f.close()

    #path of the modified files i.e. where the files will be
    rel_path = "modifiedDatasets"
    abs_file_path = os.path.join(script_dir, rel_path)
    absFilePath = os.path.join(abs_file_path,newFileName)
    f = open(absFilePath,'a')

    # Iterating through the json list
    for i in data['results']:
        for key,value in i.items():
            if key=="columns":
                columns = value
            else:
                items = value

    requiredItems = []

    #go through each item
    for item in items:
        redundantLessItem = {}
        #for the columns to be present in the file
        for column in columnsToInsert:
            column = column.lower()
            #if the value is present, then add it else dont add
            if item[column] != '':
                redundantLessItem[column] = item[column]
        #this is done to avoid duplicates eg: russia might be present twice in country.json with just country information
        if redundantLessItem not in requiredItems:
            requiredItems.append(redundantLessItem)

    id = 1
    #create _id for each object in MongoDB
    for item in requiredItems:
        item["_id"] = str(id)
        id = id + 1
    
    #convert list to json and write to file
    redundantLessJson = json.dumps(requiredItems,indent=4,ensure_ascii=False)
    f.write(redundantLessJson)


if __name__=="__main__":
    #airport
    removeRedundantColumns('airport.json','airport.json',['IATACODE','NAME','COUNTRY_CODE','CITY','AIRPORT_PROVINCE','ISLAND','LATITUDE','LONGITUDE','ELEVATION','GMTOFFSET'])

    #borders
    removeRedundantColumns('borders.json','borders.json',['COUNTRY1','COUNTRY2','LENGTH'])

    #city
    removeRedundantColumns('city.json','city.json',['NAME','COUNTRY','PROVINCE','LATITUDE','LONGITUDE','ELEVATION'])

    #citylocalname
    removeRedundantColumns('citylocalname.json','citylocalname.json',['CITY','COUNTRY','PROVINCE','LOCALNAME'])

    #cityothername
    removeRedundantColumns('cityothername.json','cityothername.json',['CITY','COUNTRY','PROVINCE','OTHERNAME'])

    #citypopulations
    removeRedundantColumns('citypopulations.json','citypopulations.json',['CITY','COUNTRY','PROVINCE','YEAR','POPULATION'])

    #country
    removeRedundantColumns('country.json','country.json',['NAME','CODE','CAPITAL','PROVINCE','AREA'])

    #countrycontinent
    removeRedundantColumns('country.json','countrycontinent.json',['CODE','ENCOMPASSES_CONTINENT','ENCOMPASS_PERCENTAGE','CONTINENT_AREA'])

    #continent
    #removeRedundantColumns('country.json','continent.json',['ENCOMPASSES_CONTINENT','CONTINENT_AREA'])

    #countryothernamelocalname
    removeRedundantColumns('country-other-localname.json','country-other-localname.json',['COUNTRY','LOCALNAME','OTHERNAME'])

    #countrypopulations
    removeRedundantColumns('countrypopulations.json','countrypopulations.json',['COUNTRY','YEAR','POPULATION'])

    #economy
    removeRedundantColumns('economy.json','economy.json',['COUNTRY','GDP','AGRICULTURE','SERVICE','INDUSTRY','INFLATION','UNEMPLOYMENT'])

    #ethnicgroup
    removeRedundantColumns('ethnicgroup.json','ethnicgroup.json',['COUNTRY_CODE','ETHNIC_GROUP_NAME','ETHNIC_GROUP_PERCENTAGE'])

    #ismember
    removeRedundantColumns('ismember.json','ismember.json',['COUNTRY','ORGANIZATION','TYPE'])

    #language
    removeRedundantColumns('language.json','language.json',['COUNTRY','LANGUAGE','PERCENTAGE'])

    #island
    removeRedundantColumns('located-on.json','located-on.json',['CITY','PROVINCE','COUNTRY','ISLAND'])

    #organization
    removeRedundantColumns('organization.json','organization.json',['ABBREVIATION','NAME','CITY','COUNTRY','PROVINCE','ESTABLISHED'])

    #politics
    removeRedundantColumns('politics.json','politics.json',['COUNTRY','INDEPENDENCE','WASDEPENDENT','DEPENDENT','GOVERNMENT'])

    #population
    removeRedundantColumns('population.json','population.json',['COUNTRY_CODE','POPULATION_GROWTH','INFANT_MORTALITY'])

    #province
    removeRedundantColumns('province.json','province.json',['NAME','COUNTRY','AREA','CAPITAL','CAPPROV'])

    #provincelocalname
    removeRedundantColumns('provincelocalname.json','provincelocalname.json',['PROVINCE','COUNTRY','LOCALNAME'])

    #provinceothername
    removeRedundantColumns('provinceothername.json','provinceothername.json',['PROVINCE','COUNTRY','OTHERNAME'])

    #provincepopulation
    removeRedundantColumns('provincepopulation.json','provincepopulation.json',['PROVINCE','COUNTRY','YEAR','POPULATION'])

    #religion
    removeRedundantColumns('religion.json','religion.json',['COUNTRY','NAME','PERCENTAGE'])