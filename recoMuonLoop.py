for counter, event in enumerate(recoMuons):	

	if counter % 1000 == 0: print counter, (counter +0.0)/event.GetEntries()
	if counter > 10000: break

	
	##
	## barrel
	##

	if abs(event.glb_eta) < 0.9 :
		print event.glb_eta


	##
	## endcape
	##

	
	##
	## ptres
	##

	if event.glb_pt > thresholdPt and event.glb_pt and event.sta_pt:
		print event.glb_pt

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

	