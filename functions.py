def returnValues(name):
	nameSplit = name.split("-")
	varName = [nameSplit[0]+"_"+nameSplit[2],nameSplit[1]+"_"+nameSplit[2]]
	exec("etaValue = event." + nameSplit[1]+"_eta")
	exec("phiValue = event." +nameSplit[1]+"_phi")
	exec("firstValue = event." + varName[0])
	exec("secondValue = event." + varName[1])
	return etaValue, phiValue, firstValue, secondValue



def getFitParams(hist):
    fit = hist.GetFunction("pol1")
    
    p0 = fit.GetParameter(0) # offset from x axis
    p0e = fit.GetParError(0) # offset from x axis
    
    p1 = fit.GetParameter(1) # slope
    p1e = fit.GetParError(1) # slope


def getFitParamsGauss(hist):
    fit = hist.GetFunction("gaus")
    
    p0 = fit.GetParameter(0) # const
    p0e = fit.GetParError(0) # const
    
    p1 = fit.GetParameter(1) # mean
    p1e = fit.GetParError(1) # mean error

    p2 = fit.GetParameter(2) # sigma?
    p2e = fit.GetParError(2) # sigma error?

    #print p0, p0e, p1, p1e
    return p0, p0e, p1, p1e, p2, p2e

def fitCut(hist, sigmas, opts):
    lower, upper = hist.GetMean()-sigmas*hist.GetRMS(), hist.GetMean()+sigmas*hist.GetRMS()
    hist.Fit("gaus",opts, "", lower, upper)



def makeProfile(TH2F_name, lnBins, fitType, drawBinPlots):
	TH2F_temp_input = []
	TH1F_fit_mean_output = []
	TH1F_fit_sigma_output = []

	

	widthType = "RMS"
	meanType = "mean"
	if fitType == "gaus":  
		widthType = "fit #sigma"
		meanType = "fit center"

	for fileCount, file in enumerate(files):
		TH2F_temp_input.append(file.Get(TH2F_name))
	
	

	for histoCount, histo in enumerate(TH2F_temp_input):
		histoBounds = histo.GetXaxis().GetXmin(), histo.GetXaxis().GetXmax()
		TH1F_fit_mean_output.append(TH1F("{}_{}_mean".format(histo.GetName(),histoCount) , "{} {} ;{};{} fit mean".format(histo.GetTitle(),meanType,histo.GetXaxis().GetTitle(), histo.GetYaxis().GetTitle()), lnBins, histoBounds[0], histoBounds[1])) #,  histo.GetYaxis().GetXmin(),histo.GetYaxis().GetXmax()  )
		TH1F_fit_sigma_output.append(TH1F("{}_{}_sigma".format(histo.GetName(),histoCount) , "{} {} ;{};{} fit #sigma".format(histo.GetTitle(),widthType ,histo.GetXaxis().GetTitle(), histo.GetYaxis().GetTitle()), lnBins, histoBounds[0], histoBounds[1])) 
	
	for bins in range(lnBins):
		for fileCount, histo in enumerate(TH2F_temp_input):
				histoBounds = histo.GetXaxis().GetXmin(), histo.GetXaxis().GetXmax()
				length = histoBounds[1] -  histoBounds[0] + 0.0
				lengthBins = histo.GetNbinsX() #-  histo.GetlNbinsX() + 0.0
				width = length/lnBins
				widthBins = lengthBins/lnBins
				minValue = histo.GetXaxis().GetXmin()
				boundsBins = bins*widthBins, (bins+1)*widthBins
				bounds = minValue + bins*width, minValue + (bins+1)*width
	#
				boundsValue = histoBounds[0]+ (lnBins+.0)/length*bins, histoBounds[0]+ (lnBins+.0)/length*(bins+1)

				temp = histo.ProjectionY("temp",boundsBins[0], boundsBins[1], "")
				temp.SetLineColor(fileCount)
				if fitType == "gaus":
					#temp.Fit("gaus","QC")
					fitCut(temp, nGausFit, "QC")
					values = getFitParamsGauss(temp)
					#print values[2], values[3], getFitParamsGauss
					TH1F_fit_mean_output[fileCount].SetBinContent(bins, values[2])
					TH1F_fit_mean_output[fileCount].SetBinError(bins, values[3])
					TH1F_fit_sigma_output[fileCount].SetBinContent(bins, values[4])
					TH1F_fit_sigma_output[fileCount].SetBinError(bins, values[5])
				if fitType != "gaus":
					#fitCut(temp, nGausFit, "")
					#temp.Fit("gaus","QC")
					values = temp.GetMean(), temp.GetMeanError(), temp.GetRMS(), temp.GetRMSError()
					#print values[2], values[3], getFitParamsGauss
					TH1F_fit_mean_output[fileCount].SetBinContent(bins, values[0])
					TH1F_fit_mean_output[fileCount].SetBinError(bins, values[1])
					TH1F_fit_sigma_output[fileCount].SetBinContent(bins, values[2])
					TH1F_fit_sigma_output[fileCount].SetBinError(bins, values[3])

				if drawBinPlots: 
					temp.Draw()
					c1.SaveAs('{}_from_{}_to_{}_{}.png'.format(TH2F_name,boundsValue[0],boundsValue[1],histo.GetXaxis().GetTitle()))
				
	
	for TH2FCount, histo in enumerate(TH1F_fit_mean_output):
		#print TH2FCount, histo.GetBinContent(3)
		histo.SetLineColor(colors[TH2FCount])
		#for i in range(histo.GetlNbinsX())
		#	print histo.GetBinContent()
		if TH2FCount == 0: histo.Draw()
		if TH2FCount > 0: histo.Draw("same")

	legend =  TLegend(0.1,0.7,0.48,0.9)
	for TH2FCount, histo in enumerate(TH1F_fit_mean_output):
		legend.AddEntry(histo,fileListName[TH2FCount],"lep")
	legend.Draw()
	
	c1.SaveAs('{}_{}_mean.png'.format(TH2F_name, fitType))

	for TH2FCount, histo in enumerate(TH1F_fit_sigma_output):
		#print TH2FCount, histo.GetBinContent(3)
		histo.SetLineColor(colors[TH2FCount])
		#for i in range(histo.GetlNbinsX())
		#	print histo.GetBinContent()
		if TH2FCount == 0: histo.Draw()
		if TH2FCount > 0: histo.Draw("same")

	legendRMS =  TLegend(0.1,0.7,0.48,0.9)
	for TH2FCount, histo in enumerate(TH1F_fit_mean_output):
		legendRMS.AddEntry(histo,fileListName[TH2FCount],"lep")
	legendRMS.Draw()
	
	c1.SaveAs('{}_{}_sigma.png'.format(TH2F_name, fitType))



