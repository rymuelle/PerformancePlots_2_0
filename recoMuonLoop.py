for counter, event in enumerate(recoMuons):	

	if counter % 1000 == 0: print counter, (counter +0.0)/event.GetEntries()
	if counter > 10000: break
	if verbosity > 10:
		print "event eta " , event.glb_eta
		print "event pt " , event.glb_pt

	##
	## barrel
	##

	if abs(event.glb_eta) < 0.9 :
		TH1F_sta_nChi2_barrel.Fill(event.sta_nchi2)
		TH1F_glb_nChi2_barrel.Fill(event.glb_nchi2)

	##
	## endcape
	##

	if abs(event.glb_eta) > 0.9 :
		TH1F_sta_nChi2_endcap.Fill(event.sta_nchi2)
		TH1F_glb_nChi2_endcap.Fill(event.glb_nchi2)
	
	##
	## ptres
	##


	if 1==1: #event.glb_pt > 0: #thresholdPt: #and event.glb_pt and event.sta_pt:
		ptResGLBSTA = event.q*(1.0/event.sta_pt-1.0/event.glb_pt)
		#ptResGLBSTA = (event.sta_pt-event.glb_pt)/event.glb_pt
		TH2F_glb_sta_eta_ptRes.Fill(event.glb_eta, ptResGLBSTA)
		TH2F_glb_sta_phi_ptRes.Fill(event.glb_phi, ptResGLBSTA)
		

	##
	## is mc
	##


	if isMC:
		ptResGLB = (event.glb_pt-event.glb_gen_pt)/event.glb_gen_pt
		ptResSTA = (event.sta_pt-event.glb_gen_pt)/event.glb_gen_pt

		TH2F_glb_gen_pt_ptRes.Fill(event.glb_gen_pt, ptResGLB)
		TH2F_glb_gen_eta_ptRes.Fill(event.glb_gen_eta, ptResGLB)

		TH2F_sta_gen_pt_ptRes.Fill(event.glb_gen_pt, ptResSTA)
		TH2F_sta_gen_eta_ptRes.Fill(event.glb_gen_eta, ptResSTA)

	