

c1 = TCanvas("c1", "c1", 600, 600)



########################################################################################
##
## Make Profile Constants
##
########################################################################################

nBins = 10
nGausFit = 1.5
drawBinPlots = False
nBins = 16

ptResMeanRange = -.001,.002
ptResSigmaRange = .00, .008

ptResGLBMeanRange = -.01,.01
ptResGLBSigmaRange = .00, .2


ptResSTAMeanRange = -.5,.5
ptResSTASigmaRange = 0, .6

ptResType2STAMeanRange = -.5,.5
ptResType2STASigmaRange = 0, .6

ptPullSTAMeanRange = -10,10
ptPullSTASigmaRange = 0, 30

ptPullGLBMeanRange = -.3,.3
ptPullGLBSigmaRange = 0, 3


massMeanRange = 0, 4000
massSigmaRange = 0, 200


nChi2MeanRange = .5, 2
nChi2RMSRange = 0, 1


nHitsMeanRange = 30, 60
nHitsRMSRange = 8, 12

isMC = True

verbose = 5