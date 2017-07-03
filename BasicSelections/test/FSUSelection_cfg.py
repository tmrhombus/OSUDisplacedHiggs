import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *
import OSUT3Analysis.DBTools.osusub_cfg as osusub
from OSUT3Analysis.Configuration.configurationOptions import *
import math
import os

################################################################################
##### Set up the 'process' object ##############################################
################################################################################

process = cms.Process ('OSUAnalysis')

# how often to print a log message
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.source = cms.Source ('PoolSource',
  fileNames = cms.untracked.vstring (
        'root://cmsxrootd.fnal.gov//store/mc/RunIISummer16MiniAODv2/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/54C6A127-05CA-E611-AAD2-0CC47A1DF1A4.root'
  )
)

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)

data_global_tag = '80X_dataRun2_2016SeptRepro_v3'
mc_global_tag = '80X_mcRun2_asymptotic_2016_miniAODv2_v1'

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, mc_global_tag, '')
if osusub.batchMode and (osusub.datasetLabel in types) and (types[osusub.datasetLabel] == "data"):
    print "using global tag " + data_global_tag + "..."
    process.GlobalTag = GlobalTag(process.GlobalTag, data_global_tag, '')
else:
    print "using global tag " + mc_global_tag + "..."


################################################################################
##### Set up the 'collections' map #############################################
################################################################################

# this PSet specifies which collections to get from the input files
miniAOD_collections = cms.PSet (
  electrons                   =  cms.InputTag  ('slimmedElectrons',                  ''),
  genjets                     =  cms.InputTag  ('slimmedGenJets',                    ''),
  jets                        =  cms.InputTag  ('slimmedJets',                       ''),
  bjets                       =  cms.InputTag  ('slimmedJets',                       ''),
  generatorweights            =  cms.InputTag  ('generator',                         ''),
  mcparticles                 =  cms.InputTag  ('packedGenParticles',                ''),
  hardInteractionMcparticles  =  cms.InputTag  ('prunedGenParticles',                ''),
  mets                        =  cms.InputTag  ('slimmedMETs',                       ''),
  muons                       =  cms.InputTag  ('slimmedMuons',                      ''),
  photons                     =  cms.InputTag  ('slimmedPhotons',                    ''),
  primaryvertexs              =  cms.InputTag  ('offlineSlimmedPrimaryVertices',     ''),
  pileupinfos                 =  cms.InputTag  ('slimmedAddPileupInfo',              ''),
  beamspots                   =  cms.InputTag  ('offlineBeamSpot',                   ''),
  superclusters               =  cms.InputTag  ('reducedEgamma', 'reducedSuperClusters'),
  taus                        =  cms.InputTag  ('slimmedTaus',                       ''),
  triggers                    =  cms.InputTag  ('TriggerResults',             '', 'HLT'),
  trigobjs                    =  cms.InputTag  ('selectedPatTrigger',                ''),
  pfCandidates                =  cms.InputTag  ('packedPFCandidates','',             ''),
)

collections = miniAOD_collections

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################

variableProducers = []
#variableProducers.append('DisplacedSUSYEventVariableProducer')

weights = cms.VPSet(
)

scalingfactorproducers = []

################################################################################
##### Import the channels to be run ############################################
################################################################################

from OSUDisplacedHiggs.BasicSelections.Selections import *

eventSelections = [FSUcut]

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from OSUT3Analysis.Configuration.histogramDefinitions import MuonHistograms, DiMuonHistograms
from OSUT3Analysis.Configuration.histogramDefinitions import JetHistograms, MuonJetHistograms
from OSUT3Analysis.Configuration.histogramDefinitions import MetHistograms, MuonMetHistograms
from OSUDisplacedHiggs.Configuration.histogramDefinitions import jetHistograms


histograms = cms.VPSet()
# histograms.append(MuonHistograms)
# histograms.append(DiMuonHistograms)
histograms.append(JetHistograms)
# histograms.append(MetHistograms)
# histograms.append(MuonJetHistograms)
# histograms.append(MuonMetHistograms)
# histograms.append(eventHistograms)
histograms.append(jetHistograms)

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################


add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collections, variableProducers, False)

################################################################################
### Configure variable and weight producers (must be done after add_channels) ##
################################################################################

# default values, altered automatically when using osusub.py

#process.DisplacedSUSYEventVariableProducer.type = cms.string("bgMC")
