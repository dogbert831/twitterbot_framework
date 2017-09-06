with open("results.txt") as f:
    for line in f:
        if "trump" in line:
        	lastmatch = line
    if lastmatch is not None:
    	print(lastmatch)