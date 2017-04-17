#import ROOT
from ROOT import TFile, TTree, TH1F, TCanvas, TProfile, TH2F,  TCollection, TLegend
#import histograms
import  math, sys, os

execfile("functions.py")
execfile("constants.py")

#c1 = TCanvas("c1", "c1", 600, 400)



#open files

fileList = ["out_500_200k_ideal_APEcov.root", "out_500_200k_ideal_diag.root"]
fileListName = ["Cov", "Diag"]
colors = [1,4]

files = []
TH2F_temp = []

for count, file in enumerate(fileList):
	files.append( TFile.Open(file, "read"))


########################################################################################
##
## Draw Profiles
##
########################################################################################


makeProfile("glb_gen_pt_v_ptRes",nBins, "gaus", drawBinPlots,ptResMeanRange,ptResSigmaRange)
makeProfile("glb_gen_pt_v_ptRes",nBins, "mean", drawBinPlots, ptResMeanRange,ptResSigmaRange)


