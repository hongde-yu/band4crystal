import sys
name = sys.argv[1]
Hart_ev = 27.21

# with open(name) as f:
# 	line = f.readline()
# 	while(line):
# 		line = f.readline()
# 		if "# EFERMI (HARTREE)" in line:
# 			fermi = float(line.split()[-1]) * Hart_ev
num = 0
breaker = []
with open (name) as f:
	fout = open("OUT_"+name, "w")
	for i in range(30):
		line = f.readline()	
	while (line):
		line = f.readline()
		num = num +1
		if "# EFERMI (HARTREE)" in line:
			fermi = float(line.split()[-1]) * Hart_ev
			break
		line_s = line.split()
		k = line_s [0]
		energy = ["%.5f" %(i*Hart_ev) for i in list(map(float, line_s [1:150]))]
		fout.write(str(k)+" "+" ".join(energy)+"\n")
		if num in [12,18,30]:
			breaker.append(k)
			print (k, -3)
			print (k, 3)
			print ()
	print (fermi)
	# for each in breaker:
	# 	fout.write(" \n")
	# 	fout.write(each+" "+"-3\n")
	# 	fout.write(each+" "+"3\n")
	# 	fout.write(" \n")
	fout.close()

	if "afm" in name or "fm" in name:
		fout2 = open("OUT2_"+name, "w")
		for i in range(24):
			line = f.readline()
		while (line):
			line = f.readline()
			if "# EFERMI (HARTREE)" in line:
				fermi = float(line.split()[-1]) * Hart_ev
				break
			line_s = line.split()
			k = line_s [0]
			energy = ["%.5f" %(i*Hart_ev) for i in list(map(float, line_s [1:150]))]
			fout2.write(str(k)+" "+" ".join(energy)+"\n")
		print (fermi)
		# for each in breaker:
		# 	fout2.write(" \n")
		# 	fout2.write(each+" "+"-3\n")
		# 	fout2.write(each+" "+"3\n")
		# 	fout2.write(" \n")
		fout2.close()
