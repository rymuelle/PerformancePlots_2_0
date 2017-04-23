from ROOT import TH1F, TCanvas, TProfile, TProfile2D, TProfile3D, TH2F
from array import array

c1 = TCanvas("c1", "c1", 600, 400)

print "opening file: ", fileIn
print "creating file: ", fileOut

outFile = TFile(fileOut, "recreate")


#leadingMuonPt = TH1F("leadingMuonPt", "leading #mu p_{T}; p_{T}; counts", 100, 0, 1000)

isMC = False

ptBins = 50
ptMin = 0
ptMax = 250

thresholdPt = 30.0

phiBins = 50
phiMin = -3.1415
phiMax = 3.1415

etaBins = 50
etaMin = -3
etaMax = 3

ptResBins = 50
ptResMin = -0.7
ptResMax = 0.7



massBins = 50
massMin = 60
massMax = 120

hydridMassCut = 5.
hybridMassValue = 91.


nChi2Bins = 50
nChi2Min = 0
nChi2Max = 3


#glb gen 

TH2F_glb_gen_pt_ptRes = TH2F("glb_gen_pt_v_ptRes"," glb vs gen p_{T}Res ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResMin, ptResMax )
TH2F_glb_gen_eta_ptRes = TH2F("glb_gen_eta_v_ptRes"," glb vs gen p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResMin, ptResMax )

#sta gen
TH2F_sta_gen_pt_ptRes = TH2F("sta_gen_pt_v_ptRes"," sta vs gen p_{T}Res ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResMin, ptResMax )
TH2F_sta_gen_eta_ptRes = TH2F("sta_gen_eta_v_ptRes"," sta vs gen p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResMin, ptResMax )


##
## nchi2
##

TH1F_sta_nChi2_barrel = TH1F("TH1F_sta_nChi2_barrel", "sta n#chi^{2} |#eta| < 0.9; n#chi^2",nChi2Bins, nChi2Min, nChi2Max )
TH1F_sta_nChi2_endcap = TH1F("TH1F_sta_nChi2_endcap", "sta n#chi^{2} |#eta| > 0.9; n#chi^2",nChi2Bins, nChi2Min, nChi2Max )
TH1F_glb_nChi2_endcap = TH1F("TH1F_glb_nChi2_endcap", "glb n#chi^{2} |#eta| > 0.9; n#chi^2",nChi2Bins, nChi2Min, nChi2Max )
TH1F_glb_nChi2_barrel = TH1F("TH1F_glb_nChi2_barrel", "glb n#chi^{2} |#eta| < 0.9; n#chi^2",nChi2Bins, nChi2Min, nChi2Max )


##
## ptRes
##

TH2F_glb_gen_eta_ptRes = TH2F("glb_gen_eta_v_ptRes"," glb vs gen p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResMin, ptResMax )
TH2F_glb_gen_phi_ptRes = TH2F("glb_gen_phi_v_ptRes"," glb vs gen p_{T}Res ;#phi;pTRes",phiBins, phiMin, phiMax ,ptResBins, ptResMin, ptResMax )






# recoDimuon plots
#glb gen 

TH2F_sta_glb_pt_HybridSTA_Mass = TH2F("sta_glb_pt_HybridSTA_Mass"," sta glb Hydrid Z' Mass ;p_{T};GeV",ptBins, ptMin, ptMax ,massBins, massMin, massMax )
TH2F_sta_glb_eta_HybridSTA_Mass = TH2F("sta_glb_eta_HybridSTA_Mass"," sta glb Hydrid Z' Mass ;#eta;GeV",etaBins, etaMin, etaMax ,massBins, massMin, massMax )
TH2F_sta_glb_phi_HybridSTA_Mass = TH2F("sta_glb_phi_HybridSTA_Mass"," sta glb Hydrid Z' Mass ;#phi;GeV",phiBins, phiMin, phiMax ,massBins, massMin, massMax )

#TH2F_sta_glb_pt_HybridSTA_Mass = TH2F("sta_glb_pt_HybridSTA_Mass"," sta Hydrid Z' Mass ;p_{T};GeV",ptBins, ptMin, ptMax ,massBins, massMin, massMax )

#muonTypes = ["sta","glb_trk","glb","glb_pic","glb_gen"]
#if not isMC: del muonTypes[-1] 




#generic comparision plots
#TProfile_ptRes = []
#TH2F_pt_ptRes = []
#TH2F_eta_ptRes = []
#TH2F_phi_ptRes = []



#for counter, types in enumerate(muonTypes):
#	for counter2, types2 in enumerate(muonTypes):
#		if counter2 > counter:
#			prefix = '{}-{}-'.format(types,types2)
#			title = '{} vs {} '.format(types,types2)
			#print prefix
			#TProfile_ptRes.append( TProfile3D(prefix + "pt-ptRes",  title + "p_{T} ;p_{T};counts",  ptBins, ptMin, ptMax, phiBins, phiMin, phiMax, etaBins, etaMin, etaMax))
			#TProfile_ptRes.append( TProfile2D(prefix + "pt-ptRes",  title + "p_{T}Res ;#phi;#eta", phiBins, phiMin, phiMax, etaBins, etaMin, etaMax))

			#TH2F_pt_ptRes.append( TH2F( prefix + "pt-pt_v_ptRes",title + "p_{T}Res ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResMin, ptResMax ))
			#TH2F_phi_ptRes.append( TH2F( prefix + "phi-phi_v_ptRes",title + "p_{T}Res ;#phi;pTRes",phiBins, phiMin, phiMax ,ptResBins, ptResMin, ptResMax  ))
			#TH2F_eta_ptRes.append( TH2F( prefix + "eta-eta_v_ptRes",title + "p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResMin, ptResMax  ))
