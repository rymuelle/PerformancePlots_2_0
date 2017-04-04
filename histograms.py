from ROOT import TH1F, TCanvas, TProfile, TProfile2D, TProfile3D, TH2F
from array import array

c1 = TCanvas("c1", "c1", 600, 400)

print "opening file: ", fileIn
print "creating file: ", fileOut

outFile = TFile(fileOut, "recreate")


#leadingMuonPt = TH1F("leadingMuonPt", "leading #mu p_{T}; p_{T}; counts", 100, 0, 1000)

isMC = True

ptBins = 50
ptMin = 0
ptMax = 3000 

phiBins = 50
phiMin = -3.1415
phiMax = 3.1415

etaBins = 50
etaMin = -3
etaMax = 3

ptResBins = 50
ptResMin = -0.5
ptResMax = 0.5

muonTypes = ["sta","glb_trk","glb","glb_pic","glb_gen"]
if not isMC: del muonTypes[-1] 

#generic comparision plots
#TProfile_ptRes = []
TH2F_pt_ptRes = []
TH2F_eta_ptRes = []
TH2F_phi_ptRes = []

for counter, types in enumerate(muonTypes):
	for counter2, types2 in enumerate(muonTypes):
		if counter2 > counter:
			prefix = '{}-{}-'.format(types,types2)
			title = '{} vs {} '.format(types,types2)
			#print prefix
			#TProfile_ptRes.append( TProfile3D(prefix + "pt-ptRes",  title + "p_{T} ;p_{T};counts",  ptBins, ptMin, ptMax, phiBins, phiMin, phiMax, etaBins, etaMin, etaMax))
			#TProfile_ptRes.append( TProfile2D(prefix + "pt-ptRes",  title + "p_{T}Res ;#phi;#eta", phiBins, phiMin, phiMax, etaBins, etaMin, etaMax))

			TH2F_pt_ptRes.append( TH2F( prefix + "pt-pt_v_ptRes",title + "p_{T}Res ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResMin, ptResMax ))
			TH2F_phi_ptRes.append( TH2F( prefix + "phi-phi_v_ptRes",title + "p_{T}Res ;#phi;pTRes",phiBins, phiMin, phiMax ,ptResBins, ptResMin, ptResMax  ))
			TH2F_eta_ptRes.append( TH2F( prefix + "eta-eta_v_ptRes",title + "p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResMin, ptResMax  ))
