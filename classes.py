# I'm not sure if this will be a useful way of reorganizing,
# but it can't hurt for now to have this skeleton set up,
# in case we want to object-ify the pipeline later

from os import path
import pandas as pd
import numpy as np

class OriginalStudy():
    def __init__(self, sourcedata, name):
        self.df = pd.DataFrame()
        self.name = name
    
    def validate(self):
        pass
    
    def clean(self):
        pass
        
class ReversalStudy(OriginalStudy):
    def __init__(self, sourcedata, name):
        OriginalStudy.__init__(self, sourcedata, name)
        
class EyetrackStudy(OriginalStudy):
    def __init__(self):
        pass
    
    def validate(self):
        pass
    
    def clean(self):
        pass
    
class FullStudy():
    def __init__(self):
        pass
    
    def validate(self):
        pass