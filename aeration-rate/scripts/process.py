from wrapper import Wrapper,os
import xml.etree.ElementTree as ET

class Process(Wrapper):
    
    def __init__(self):
        Wrapper.__init__(self)

    def setData(self):
        path = self.resource["path_archive"]
        fields = self.resource["fields"]
        fileType = self.resource["fileType"]

        if fileType == "txt":
            with open(path,'r',encoding="utf-8") as f:                
                for line in f:
                    if line[0] != "#" and line != "" and line != "\n":
                        values,comment = line.split("#",1)
                        values = values.split(";")
                        values.append(comment) 
                        # Row constructed as a list of dict
                        row = dict(zip(fields,tuple([v.strip(' \n\r\t') for v in values])))
                        self.data.append(row)

        elif fileType == "xml":    
            tree = ET.parse(path)            
            annotations = tree.findall(".//annotations/annotation")

            prevCodepoint = ""
            for annotation in annotations:                
                codepoint = annotation.attrib["cp"]

                # Every couple of consecutive annotation tags contain the data for keywords and name for every codepoint,
                # therefore, a single row is constructed from two consecutive tags
                if codepoint != prevCodepoint:
                    keywords = annotation.text
                else:
                    name = annotation.text
                    row = dict(zip((fields),(codepoint,keywords,name)))
                    self.data.append(row)
                    
                prevCodepoint = codepoint

if __name__ == "__main__":
    pr = Process()
    pr.createDataSet()