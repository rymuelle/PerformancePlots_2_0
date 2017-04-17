#import ROOT
from ROOT import TFile, TTree, TH1F, TCanvas, TProfile, TH2F,  TCollection, TLegend
#import histograms
import  math, sys, os

execfile("functions.py")

c1 = TCanvas("c1", "c1", 600, 400)

nBins = 10
nGausFit = 1.8
drawBinPlots = False

#open files

fileList = ["out_500_200k_ideal_APEcov.root", "out_500_200k_ideal_diag.root"]
fileListName = ["Cov", "Diag"]
colors = [1,3]

files = []
TH2F_temp = []

for count, file in enumerate(fileList):
	files.append( TFile.Open(file, "read"))


#TH2F_name = "glb_gen_pt_v_ptRes"
nBins = 10

makeProfile("glb_gen_pt_v_ptRes",nBins, "gaus", drawBinPlots)
makeProfile("glb_gen_pt_v_ptRes",nBins, "mean", drawBinPlots)

#TH2F_temp_input = []
#TH1F_temp_output = []
#for fileCount, file in enumerate(files):
#	TH2F_temp_input.append(file.Get(TH2F_name))
#
#
#for histoCount, histo in enumerate(TH2F_temp_input):
#	TH1F_temp_output.append(TH1F("{}_{}".format(histo.GetName(),histoCount) , histo.GetTitle(), nBins, histo.GetXaxis().GetXmin(), histo.GetXaxis().GetXmax())) #,  histo.GetYaxis().GetXmin(),histo.GetYaxis().GetXmax()  )
#	
#
#for bins in range(nBins):
#	for fileCount, histo in enumerate(TH2F_temp_input):
#	
#			length = histo.GetXaxis().GetXmax() -  histo.GetXaxis().GetXmin() + 0.0
#			lengthBins = histo.GetNbinsX() #-  histo.GetNbinsX() + 0.0
#			width = length/nBins
#			widthBins = lengthBins/nBins
#			minValue = histo.GetXaxis().GetXmin()
#			boundsBins = bins*widthBins, (bins+1)*widthBins
#			bounds = minValue + bins*width, minValue + (bins+1)*width
##
#			temp = histo.ProjectionY("temp",boundsBins[0], boundsBins[1], "")
#			temp.SetLineColor(fileCount)
#			temp.Fit("gaus","QC")
#			values = getFitParamsGauss(temp)
#			#print values[2], values[3], getFitParamsGauss
#			TH1F_temp_output[fileCount].SetBinContent(bins, values[2])
#			TH1F_temp_output[fileCount].SetBinError(bins, values[3])
#			
#
#for TH2FCount, histo in enumerate(TH1F_temp_output):
#	#print TH2FCount, histo.GetBinContent(3)
#	histo.SetLineColor(colors[TH2FCount])
#	#for i in range(histo.GetNbinsX())
#	#	print histo.GetBinContent()
#	if TH2FCount == 0: histo.Draw()
#	if TH2FCount > 0: histo.Draw("same")
#
#	c1.SaveAs("bleh.png")
#	#if TH2FCount > 0: histo.Draw("same")
#c1.SaveAs("bleh.png")


#TH1F_temp = [[0 for x in range(nBins)] for y in range(len(files)) ] 
#TH1F_temp = []





#os.mkdir("output")
#os.chdir("./output")
#get histos from file 1
#for key in files[0].GetListOfKeys():
	##print key.GetName()
	#TH2F_temp.append( key.ReadObj())
	##TH1F_temp.append([]) 
##get rest of histos from other files with same name
	#for count, file in enumerate(files):
		##print count
		#if count > 0: 
			#TH2F_temp.append( file.Get(key.ReadObj().GetName() ))
		##	TH1F_temp.append([]) 
	##for count, histo in enumerate(TH2F_temp):
##create plain histograms
	##for fileCount, histo in enumerate(TH2F_temp):
#
		##TH1F_temp[fileCount].append
#
		##print histo.GetName()
		#
	##fitValues = [[0 for x in range(nBins)] for y in range(len(files)) ]
#
#
#
#### we have an object (TH2F_temp)	which stores a th2f across all the files
#
	#temp_profile = []
	#for fileCount, histo in enumerate(TH2F_temp):
		#temp_profile.append(TH2F("{}_{}".format(histo.GetName(),fileCount) , histo.GetTitle(), nBins, histo.GetXaxis().GetXmin(), histo.GetXaxis().GetXmax(), 50, histo.GetYaxis().GetXmin(),histo.GetYaxis().GetXmax()  )) 
#
	#for bins in range(nBins):
		#for fileCount, histo in enumerate(TH2F_temp):
			#if type(histo) is  TH2F: 
#
				#length = histo.GetXaxis().GetXmax() -  histo.GetXaxis().GetXmin() + 0.0
				#lengthBins = histo.GetNbinsX() #-  histo.GetNbinsX() + 0.0
				#width = length/nBins
				#widthBins = lengthBins/nBins
				#minValue = histo.GetXaxis().GetXmin()
				#boundsBins = bins*widthBins, (bins+1)*widthBins
				#bounds = minValue + bins*width, minValue + (bins+1)*width
	#
				#temp = histo.ProjectionY("temp",boundsBins[0], boundsBins[1], "")
				#temp.SetLineColor(fileCount)
				#temp.Fit("gaus","QC")
				#values = getFitParamsGauss(temp)
				#print values[0], values[1]
				#temp_profile[fileCount].SetBinContent(bins, values[0])
				#temp_profile[fileCount].SetBinError(bins, values[1])
				##print bins, fileCount, temp.GetEntries(), getFitParamsGauss(temp)
				##if fileCount == 0: temp.Draw()
				##if fileCount > 0: temp.Draw("same")
				##fitValues[fileCount][bins] = (getFitParamsGauss(temp))
#
	#for fileCount, histo in enumerate(TH2F_temp):
		#temp_profile[fileCount].Draw()
		#c1.SaveAs('{}_{}.png'.format(histo.GetName(), fileCount) )
#
#
#
	#
	#
		##c1.SaveAs('{}_{}_{}_{}.png'.format(histo.GetName(),  bins,bounds[0],bounds[1]) )
#
			##print '{}_{}_{}_{}.png'.format(histo.GetName(), bins,bounds[0],bounds[1])
			##TH1F_temp[fileCount].append(histo.ProjectionY("temp",boundsBins[0], boundsBins[1], ""))
			##TH1F_temp[fileCount][bins] = histo.ProjectionY("temp",boundsBins[0], boundsBins[1], "")
			##print fileCount, bins,bounds[0],bounds[1], histo.ProjectionY("temp",boundsBins[0], boundsBins[1], "").GetEntries(), TH1F_temp[fileCount][bins].GetEntries()
			##TH1F_temp[fileCount][bins].SetLineColor(fileCount)
#
			##if fileCount == 0: tTH1F_temp[fileCount][bins].Draw()
			##if fileCount > 0:  TH1F_temp[fileCount][bins].Draw("same")	
#
	##for bins in range(nBins):
	##	for fileCount in range(len(fileList)):
	##		if fileCount == 0: TH1F_temp[fileCount][bins].Draw()
	##		if fileCount > 0: TH1F_temp[fileCount][bins].Draw("same")
#
	##c1.SaveAs("wahtever.png")
	##c1.SaveAs('{}_{}_{}_{}.png'.format(histo.GetName(),  bins,bounds[0],bounds[1]) )
#
	##TH1F_temp = [[0 for x in range(nBins)] for y in range(len(files)) ] 
		#
		##c1.SaveAs('{}_{}_{}_{}.png'.format(histo.GetName(),  bins,bounds[0],bounds[1]) )
#
#
	##	for count3, files2 in enumerate(TH1F_temp):
	##		count4 = 0
			##print len(files2)
	##		for count4, binHisto in enumerate(files2):
	##			bounds = minValue + count4*width, minValue +  (count4+1)*width
	##			files2.ProjectionY("temp",bounds[0], bounds[1], "").Draw()
	##			c1.SaveAs(files2.GetName() + "_" + count4 + ".png")
	#print count

#TH2F_temp = []


#for histo in TH2F_list:
#	print histo.GetName()

#go histogram by histogram producing profiles
