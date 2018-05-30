import urllib.request
import json
import os
import csv

class Wrapper(object):

    def __init__(self):
        self.path_archive = "../archive"
        self.path_dp = "../datapackage.json"
        self.path_data = "../data"

        # Resolved to absolute path for debugging in vscode
        self.path_archive = os.path.abspath(self.path_archive)
        self.path_dp = os.path.abspath(self.path_dp)
        self.path_data = os.path.abspath(self.path_data)

        self.setup()

        # Retrieving meta data from datapackage.json
        with open(self.path_dp) as dp:
            self.meta = json.load(dp)
        
        # Retrieving all resources
        self.resources_dp = self.meta["resources"]
        self.data = []
        self.resources = []

    def setup(self):
        # Creates the directory for archive if they don't exist        
        if not os.path.exists(self.path_archive):
            os.mkdir(self.path_archive)
    
    def retrieveFiles(self):

        # Iterating through all resources and retrieving remote files
        for resource_dp in self.resources_dp:
            path_archive = os.path.join(self.path_archive,resource_dp["name"]) + "." + resource_dp["format"]
            urllib.request.urlretrieve(resource_dp["path"],path_archive)
            fields = resource_dp["schema"]["fields"]
            fields = tuple([field["name"] for field in fields])
            fileType = path_archive.rsplit(".",1)[-1]

            # Setting up resources for creating CSVs
            self.resources.append(
                {
                    "path_archive":path_archive,
                    "fields":fields,
                    "fileType":fileType,
                    "path_data":os.path.join(self.path_data,resource_dp["name"] + ".csv")
                }
            )
    
    def createCSV(self,path):
        with open(path, "w",newline='',encoding="utf-8") as f:
            fieldnames = [*self.data[0]]     
            writer = csv.DictWriter(f,fieldnames = fieldnames)
            writer.writeheader()
            for row in self.data:                                        
                writer.writerow(row)
            
            # Empty self.data variable so it can be set with the next files data
            self.data[:] = []
    
    def createDataSet(self):
        self.retrieveFiles()
        for self.resource in self.resources:
            self.setData()
            self.createCSV(self.resource["path_data"])
    
    def setData(self):
        raise NotImplementedError