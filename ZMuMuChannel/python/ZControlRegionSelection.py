import FWCore.ParameterSet.Config as cms
import copy
import string
from OSUDisplacedHiggs.ZMuMuChannel.CutDefinitions import *

##########################################################################
###### Set up the Z control region for the displaced SUSY analysis #######
##########################################################################

##########################################################################
#Selections without triggers

ZControlRegion = cms.PSet(
    name = cms.string("ZControlRegion"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
ZControlRegion.cuts.append(jet_eta_cut)
ZControlRegion.cuts.append(jet_pt_20_cut)
ZControlRegion.cuts.append(jet_id_cut)
### at least two good muons
ZControlRegion.cuts.append(muon_eta_cut)
ZControlRegion.cuts.append(muon_pt_30_cut)
ZControlRegion.cuts.append(muon_global_cut)
ZControlRegion.cuts.append(muon_id_cut)
ZControlRegion.cuts.append(muon_iso_cut)
ZControlRegion.cuts.append(muonjet_deltaR_veto)
ZControlRegion.cuts.append(muon_2muon_cut)
### invMass in Z range
ZControlRegion.cuts.append(diMuon_invMass_Z_cut)
### we don't take kindly to b-jets around these parts
#ZControlRegion.cuts.append(jet_csvm_veto)
