if savePng:

	if isMC:	
		TH2F_glb_gen_pt_ptRes.Draw("colz")
		c1.SaveAs("TH2F_glb_gen_pt_ptRes.png")
		TH2F_glb_gen_eta_ptRes.Draw("colz")
		c1.SaveAs("TH2F_glb_gen_eta_ptRes.png")
	
		#sta gen
		TH2F_sta_gen_pt_ptRes.Draw("colz")
		c1.SaveAs("TH2F_sta_gen_pt_ptRes.png")
	
		TH2F_sta_gen_eta_ptRes.Draw("colz")
		c1.SaveAs("TH2F_sta_gen_eta_ptRes.png")

	##
	##hybrid mass
	##
	
	TH2F_sta_glb_pt_HybridSTA_Mass.Draw("colz")
	c1.SaveAs("TH2F_sta_glb_pt_HybridSTA_Mass.png")
	TH2F_sta_glb_eta_HybridSTA_Mass.Draw("colz")
	c1.SaveAs("TH2F_sta_glb_eta_HybridSTA_Mass.png")
	TH2F_sta_glb_phi_HybridSTA_Mass.Draw("colz")
	c1.SaveAs("TH2F_sta_glb_phi_HybridSTA_Mass.png")


	##
	##	nChi2
	##

	TH1F_sta_nChi2_barrel.Draw()
	c1.SaveAs("TH1F_sta_nChi2_barrel.png")
	TH1F_sta_nChi2_endcap.Draw()
	c1.SaveAs("TH1F_sta_nChi2_endcap.png")
	TH1F_glb_nChi2_endcap.Draw()
	c1.SaveAs("TH1F_glb_nChi2_endcap.png")
	TH1F_glb_nChi2_barrel.Draw()
	c1.SaveAs("TH1F_glb_nChi2_barrel.png")


	##
	##	ptRes
	##

	TH2F_glb_sta_eta_ptRes.Draw("colz")
	c1.SaveAs("TH2F_glb_sta_eta_ptRes.png")
	TH2F_glb_sta_phi_ptRes.Draw("colz")
	c1.SaveAs("TH2F_glb_sta_phi_ptRes.png")