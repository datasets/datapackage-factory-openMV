import urllib.request
import json
import os
import csv

class Process(object):

    def __init__(self):        
        self.path_dp = "../datapackage.json"
        self.path_data = "../data"
        
	# Resolving to absolute path for running with shell script from 
	# a parent directory and directly with python3 from current directory
        CURRENT_DIR = os.path.dirname(__file__)        
        self.path_dp = os.path.join(CURRENT_DIR,self.path_dp)
        self.path_data = os.path.join(CURRENT_DIR,self.path_data)
        
        # Creating data directory if it doesnot exists 
        self.setup()

        # Retrieving meta data from datapackage.json
        with open(self.path_dp) as dp:
            self.meta = json.load(dp)
        
        # Retrieving all resources
        self.resources_dp = self.meta["resources"]       
    
    def setup(self):
        if not os.path.exists(self.path_data):
            os.mkdir(self.path_data)   
    
    def dumpCSVs(self):

        # Iterating through all resources and retrieving remote files
        for resource_dp in self.resources_dp:
            path_data = os.path.join(self.path_data,resource_dp["name"]) + "." + resource_dp["format"]
            urllib.request.urlretrieve(resource_dp["path"],path_data)


if __name__ == "__main__":
    pr = Process()
    pr.dumpCSVs()
