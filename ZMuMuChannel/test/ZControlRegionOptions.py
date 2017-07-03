#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "ZControlRegion_cfg.py"

# choose luminosity used for MC normalization
intLumi = 35863.308

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

    # DY
    'DYJetsToLL',
#    'DYBBJetsToLL',

    # TTbar
    'TTJets_DiLept',

    # tW
    'SingleTop',

    # Diboson
    'Diboson',
    #'WWToLNuLNu',
    #'ZZToLLNuNu',
    #'ZG',

    # QCD
#    'QCD_MuEnriched',
    
    # Signal
    #'DisplacedSUSYSignal',
    
    # Data
    'DoubleMu_2016',

]

InputCondorArguments = {}
