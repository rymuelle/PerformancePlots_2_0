#import ROOT
from ROOT import TFile, TTree, TH1F, TCanvas, TProfile, TH2F,  TCollection
#import histograms
import  math, sys

execfile("functions.py")

nBins = 10
#open files

fileList = ["out.root", "out2.root"]
files = []
TH2F_temp = []

for count, file in enumerate(fileList):
	files.append( TFile.Open(file, "read"))

TH1F_temp = [[0 for x in range(nBins)] for y in range(len(files)) ] 

#nextKey =  TIter(files[0].GetListOfKeys())
for key in files[0].GetListOfKeys():
	#print key.GetName()
	TH2F_temp.append( key.ReadObj())

	for count, file in enumerate(files):
		#print count
		if count > 0: 
			TH2F_temp.append( file.Get(key.ReadObj().GetName() ))

	#for count, histo in enumerate(TH2F_temp):
	for count2, histo in enumerate(TH2F_temp):
		print histo.GetName()
		length = histo.GetXaxis().GetXmax() -  histo.GetXaxis().GetXmin() + 0.0
		width = length/nBins
		for count3, files2 in enumerate(TH1F_temp):
			count4 = 0
			#print len(files2)
			for count4, binHisto in enumerate(files2):
				print count4#*width  - length/2, (count4 + 1)*width - length/2


	TH2F_temp = []


#for histo in TH2F_list:
#	print histo.GetName()

#go histogram by histogram producing profiles




