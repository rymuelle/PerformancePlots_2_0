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
		##	ptPull
		##

		TH2F_gen_glb_eta_ptPull.Draw("colz")
		c1.SaveAs("TH2F_gen_glb_eta_ptPull.png")
		TH2F_gen_glb_pt_ptPull.Draw("colz")
		c1.SaveAs("TH2F_gen_glb_pt_ptPull.png")
		##
		##	ptRes
		##

		TH2F_gen_sta_eta_ptRes_type_2.Draw("colz")
		c1.SaveAs("TH2F_gen_sta_eta_ptRes_type_2.png")
		TH2F_gen_sta_phi_ptRes_type_2.Draw("colz")
		c1.SaveAs("TH2F_gen_sta_phi_ptRes_type_2.png")
		TH2F_gen_sta_pt_ptRes_type_2.Draw("colz")
		c1.SaveAs("TH2F_gen_sta_pt_ptRes_type_2.png") 

		TH2F_gen_glb_eta_ptRes.Draw("colz")
		c1.SaveAs("TH2F_gen_glb_eta_ptRes.png")
		TH2F_gen_glb_phi_ptRes.Draw("colz")
		c1.SaveAs("TH2F_gen_glb_phi_ptRes.png")
		TH2F_gen_glb_pt_ptRes.Draw("colz")
		c1.SaveAs("TH2F_gen_glb_pt_ptRes.png")

	##
	##	ptPull
	##

	TH2F_glb_sta_eta_ptPull.Draw("colz")
	c1.SaveAs("TH2F_glb_sta_eta_ptPull.png")
	TH2F_glb_sta_pt_ptPull.Draw("colz")
	c1.SaveAs("TH2F_glb_sta_pt_ptPull.png")

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

	TH2F_glb_eta_nChi2.Draw("colz")
	c1.SaveAs("TH2F_glb_eta_nChi2.png")
	TH2F_glb_pt_nChi2.Draw("colz")
	c1.SaveAs("TH2F_glb_pt_nChi2.png") 


	##
	##	ptRes
	##

	TH2F_glb_sta_eta_ptRes.Draw("colz")
	c1.SaveAs("TH2F_glb_sta_eta_ptRes.png")
	TH2F_glb_sta_phi_ptRes.Draw("colz")
	c1.SaveAs("TH2F_glb_sta_phi_ptRes.png")


	TH2F_glb_sta_eta_ptRes_type_2.Draw("colz")
	c1.SaveAs("TH2F_glb_sta_eta_ptRes_type_2.png")
	TH2F_glb_sta_phi_ptRes_type_2.Draw("colz")
	c1.SaveAs("TH2F_glb_sta_phi_ptRes_type_2.png")
	TH2F_glb_sta_pt_ptRes_type_2.Draw("colz")
	c1.SaveAs("TH2F_glb_sta_pt_ptRes_type_2.png") 



	##
	## nhits
	##
	TH2F_glb_eta_nHits.Draw("colz")
	c1.SaveAs("TH2F_glb_eta_nHits.png")
	TH2F_glb_pt_nHits.Draw("colz")
	c1.SaveAs("TH2F_glb_pt_nHits.png") 