#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "FSUSelection_cfg.py"

# choose luminosity used for MC normalization
intLumi = 35863.308 # full 2016 data
#intLumi = 5784.596 # 2016B 
#intLumi = 2573.399 # 2016C 
#intLumi = 4248.384 # 2016D 
#intLumi = 4009.132 # 2016E 
#intLumi = 3101.618 # 2016F 
#intLumi = 7540.488 # 2016G 
#intLumi = 8605.69  # 2016H 

systematics_file = "OSUDisplacedHiggs.Configuration.systematicsDefinitions"
external_systematics_directory = "OSUDisplacedHiggs/Configuration/data/"

# create list of datasets to process


datasets = [
    'ggZH_HSSbbbb_MS_40_ctauS_0',
    'ggZH_HSSbbbb_MS_40_ctauS_0p05',
    'ggZH_HSSbbbb_MS_40_ctauS_1',
    'ggZH_HSSbbbb_MS_40_ctauS_10',
    'ggZH_HSSbbbb_MS_40_ctauS_100',
    'ggZH_HSSbbbb_MS_40_ctauS_1000',
    'ggZH_HSSbbbb_MS_40_ctauS_10000',
    'DYJetsToLL',
]



InputCondorArguments = {}
