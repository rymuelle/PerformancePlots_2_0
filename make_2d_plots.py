#import ROOT
from ROOT import TFile, TTree, TH1F
#import histograms
import  math, sys



fileIn = sys.argv[1]
fileOut = sys.argv[2]

execfile("histograms.py")
execfile("functions.py")



f = TFile.Open(fileIn, "read")
td = f.Get("muAlAnalyzer")
Events = td.Get("Events")
genMuons = td.Get("genMuons")
recoMuons = td.Get("recoMuons")
recoDimuons = td.Get("recoDimuons")

#Events.Print()
#genMuons.Print()
#recoMuons.Print()
#recoDimuons.Print()



for counter, event in enumerate(recoMuons):
	refPt = event.glb_pt
	refEta = event.glb_eta
	refPhi = event.glb_phi
	if isMC:
		refPt = event.glb_gen_pt
		refEta = event.glb_gen_eta
		refPhi = event.glb_gen_phi		

	if counter % 1000 == 0: print counter, (counter +0.0)/event.GetEntries()
	if counter > 10000: break
	for counter2, types in enumerate(TH2F_pt_ptRes):

		name = TH2F_pt_ptRes[counter2].GetName()
		values = returnValues(name)
		TH2F_pt_ptRes[counter2].Fill(refPt,(values[2]-values[3])/values[3] )

		name = TH2F_eta_ptRes[counter2].GetName()
		values = returnValues(name)
		TH2F_eta_ptRes[counter2].Fill(refEta,(values[2]-values[3])/values[3] )

		name = TH2F_phi_ptRes[counter2].GetName()
		values = returnValues(name)
		TH2F_phi_ptRes[counter2].Fill(refPhi,(values[2]-values[3])/values[3] )





	#	name =  TProfile_ptRes[counter2].GetName()
	#	values = returnValues(name)
	#	TProfile_ptRes[counter2].Fill(values[0],values[1],(values[2]-values[3])/values[3])

	#	name =  TProfile_pt_ptRes[counter2].GetName()
	#	values = returnValues(name)
	#	TProfile_ptRes[counter2].Fill(values[0],values[1],(values[2]-values[3])/values[3])

	#print counter, values[0], values[1],values[2], values[3]








for counter, types in enumerate(TH2F_pt_ptRes):
	TH2F_pt_ptRes[counter].Draw("colz")
	c1.SaveAs(TH2F_pt_ptRes[counter].GetName()+".png")

	TH2F_phi_ptRes[counter].Draw("colz")
	c1.SaveAs(TH2F_phi_ptRes[counter].GetName()+".png")

	TH2F_eta_ptRes[counter].Draw("colz")
	c1.SaveAs(TH2F_eta_ptRes[counter].GetName()+".png")
#	TProfile_ptRes[counter].Draw("colz")
#	c1.SaveAs(TProfile_ptRes[counter].GetName()+".png")
#leadingMuonPt.Draw()
#1.SaveAs("leadingMuonPt.root")

outFile.Write()
outFile.Close()
