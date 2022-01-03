import json
import os   
import pandas as pd

def embedDocuments(embedIntoFile,embedFromFile,embedIntoKey,embedFromKey,columnsToBeEmbedded,collectionName):
    script_dir = os.path.dirname(__file__)
    rel_path = "modifiedDatasets"
    abs_file_path = os.path.join(script_dir, rel_path)


    absFilePath = os.path.join(abs_file_path,embedFromFile)
    f = open(absFilePath,'r')
    # returns JSON object as a dictionary
    embedFromData = json.load(f) 
    f.close()

    absFilePath = os.path.join(abs_file_path,embedIntoFile)
    f = open(absFilePath,'r')
    # returns JSON object as a dictionary
    embedIntoData = json.load(f) 
    f.close()

    embeddedList = []

    #go through each item in the embedInto and compare the key colunns of both the files. From the matched json, get the required columsn from the second file.
    for embedIntoItem in embedIntoData:
        for emdedFromItem in embedFromData:
            isEmbedIntoExist = True

            for index in range(len(embedIntoKey)):
                if embedIntoItem[embedIntoKey[index]] != emdedFromItem[embedFromKey[index]]:
                    isEmbedIntoExist = False
                    break
            
            if isEmbedIntoExist:
                #if there is only one field required, create an array
                if len(columnsToBeEmbedded) == 1:
                    if collectionName not in embedIntoItem:
                        embedIntoItem[collectionName] = []
                    embedIntoItem[collectionName].append(emdedFromItem[columnsToBeEmbedded[0]])
                else:
                    #else create a dictionary which will be json inside json
                    embeddedDictionary = {}

                    for column in columnsToBeEmbedded:
                        if column in emdedFromItem:
                            embeddedDictionary[column] = emdedFromItem[column]
                    
                    if len(embeddedDictionary) > 0:
                        if collectionName not in embedIntoItem:
                            embedIntoItem[collectionName] = []
                        embedIntoItem[collectionName].append(embeddedDictionary)
        embeddedList.append(embedIntoItem)
    embeddedJson = json.dumps(embeddedList,indent=4,ensure_ascii=False)
    
    f = open(absFilePath,'w')
    
    f.write(embeddedJson)

    f.close()

if __name__=="__main__":
    embedDocuments("city.json","citylocalname.json",['name','country','province'],['city','country','province'],['localname'],"citylocalname")

    embedDocuments("city.json","cityothername.json",['name','country','province'],['city','country','province'],['othername'],"cityothernames")

    embedDocuments("city.json", "citypopulations.json", ["name","country","province"], ["city", "country", "province"], ["year", "population"], "population")

    embedDocuments("city.json", "located-on.json", ["name","country","province"], ["city", "country", "province"], ["island"], "island")

    embedDocuments("country.json", "economy.json", ["code"], ["country"], ["gdp", "agriculture","service","industry","inflation","unemployment"], "economy")

    embedDocuments("country.json", "politics.json", ["code"], ["country"], ["independence", "wasdependent","dependent","government"], "politics")

    embedDocuments("country.json", "countrycontinent.json", ["code"], ["code"], ["encompasses_continent", "encompass_percentage","continent_area"], "continent")

    embedDocuments("country.json", "country-other-localname.json", ["code"], ["country"], ["localname", "othername"], "localnameothername")

    embedDocuments("country.json", "countrypopulations.json", ["code"], ["country"], ["year", "population"], "population")
    
    embedDocuments("country.json", "population.json", ["code"], ["country_code"], ["population_growth", "infant_mortality"], "population_growth")

    embedDocuments("province.json", "provincelocalname.json", ["name","country"], ["province","country"], ["localname"], "localname")

    embedDocuments("province.json", "provinceothername.json", ["name","country"], ["province","country"], ["othername"], "othername")

    embedDocuments("province.json", "provincepopulation.json", ["name","country"], ["province","country"], ["year","population"], "population")