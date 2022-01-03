import json
import os   
import pandas as pd

def referenceDocuments(embedIntoFile,embedFromFile,embedIntoKey,embedFromKey,collectionName):
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
    #go through each item in the embedInto and compare the key colunns of both the files. From the matched json, get the _id.
    for embedIntoItem in embedIntoData:
        for emdedFromItem in embedFromData:
            isEmbedIntoExist = True
            #if the key column in not present in any of the two files, then skip adding the reference for that data
            for index in range(len(embedIntoKey)):
                if embedFromKey[index] not in emdedFromItem:
                    isEmbedIntoExist = False
                    break
                if embedIntoKey[index] not in embedIntoItem:
                    isEmbedIntoExist = False
                    break
                if embedIntoItem[embedIntoKey[index]] != emdedFromItem[embedFromKey[index]]:
                    isEmbedIntoExist = False
                    break
            #if there is a match, then add the reference
            if isEmbedIntoExist:
                if collectionName not in embedIntoItem:
                        embedIntoItem[collectionName] = []
                embedIntoItem[collectionName].append(emdedFromItem["_id"])
        embeddedList.append(embedIntoItem)
    embeddedJson = json.dumps(embeddedList,indent=4,ensure_ascii=False)
    f = open(absFilePath,'w')
    
    f.write(embeddedJson)

    f.close()

if __name__=="__main__":
    referenceDocuments("city.json","airport.json",['name','country','province'],['city','country_code','airport_province'],"airports")

    referenceDocuments("country.json","ethnicgroup.json",['code'],['country_code'],"ethnicgroups")
    referenceDocuments("country.json","religion.json",['code'],['country'],"religion")
    referenceDocuments("country.json","ismember.json",['code'],['country'],"member")
    referenceDocuments("country.json","language.json",['code'],['country'],"languages")

    referenceDocuments("organization.json","ismember.json",['abbreviation'],['organization'],"members")
