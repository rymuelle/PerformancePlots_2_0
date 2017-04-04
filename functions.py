def returnValues(name):
	nameSplit = name.split("-")
	varName = [nameSplit[0]+"_"+nameSplit[2],nameSplit[1]+"_"+nameSplit[2]]
	exec("etaValue = event." + nameSplit[1]+"_eta")
	exec("phiValue = event." +nameSplit[1]+"_phi")
	exec("firstValue = event." + varName[0])
	exec("secondValue = event." + varName[1])
	return etaValue, phiValue, firstValue, secondValue