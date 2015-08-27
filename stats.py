def mean(vals):
	total = float(sum(vals))
	length = len(vals)
	return total/length


# print mean([2,4])

def std(vals):
	n = len(vals)
	if n == 0:
		return 0.0
	mu = mean(vals)
	var = 0.0
	for val in vals:
		var = var + (val-mu)**2
	return (var/n)**.5
	
