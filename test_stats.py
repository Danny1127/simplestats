from stats import mean,std
from nose.tools import assert_equal,assert_almost_equal

def test_mean():
#	assert(mean([2,4]) == 3)
	assert_equal(mean([2,4]),3)
test_mean()

def test_float_mean():
#	assert(mean([1,2]) == 1.5)
	assert_equal(mean([1,2]),1.5)
#test_float_mean()

def ex_test():
#	assert(mean([-2,2,4])==4.0/3)
#	assert_equal(mean([-2,2,4]),4./3)
	assert_almost_equal(mean([-2,2,4]),1.33,places=2)	
#ex_test()


def test_std1():
	obs = std([0.0,2.])
	exp = 1.
	assert_equal(obs,exp)

