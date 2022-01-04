# MongoDB-Embedding-And-References-JSON-Data-Creation
The scripts provided are used to generate the embedded and reference json files for inserting into the MongoDB database.


There are three python scripts in this project.

1. removeRedundant.py
2. embedDocuments.py
3. referenceDocuments.py

================================

The first script removeRedundant.py is used to remove the columns that are redundant in the json file i.e. the column can be derived from some other doucment. It also removes the data points with no values. It also creates an id for each record in the json file which is to be used for referencing.

The function takes in three arguments : input json file, output json file, list of columns to be kept in the new json.

================================

The second script is embedDocuments.py. This takes in two json files and embeds the latter json document into the former json document. 

It takes in six arguments : embedInto Json File, embedFrom Json File, columns of first file which act as key, columns of second file which acts as key for embedding, columns of second file to be embedded into first, collection name to be had in first file

================================

The third script is referenceDocuments.py. This takes in two json files and add the references(or document/entry id) instead of embedding the whole data.

It takes in five arguments : embedInto Json File, embedFrom Json File, columns of first file which act as key, columns of second file which acts as key for embedding, collection name to be had in first file

Only the "\_id " value is added into the first file.

After running these scripts, the newly created json files can be directly loaded into MongoDB.
