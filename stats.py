def mean(vals):
	total = float(sum(vals))
	length = len(vals)
	return total/length


# print mean([2,4])


def std(vals):
	if len(vals) == 0:
		return 0.0
	return vals[-1] / 2.
