# Utility function to clean a string
def stripspaces(s):
	"""
	Remove whitespace chars from both ends of the string
	returns a new string with whitespace chars removed from both ends of the string
	converts multiple whitespace chars into 1 space char
	returns an empty string if input is None or anything else than a string or unicode
	TODO: change the re expression to strip the start and end whitespace as well and remove the strip() call
	"""
	import re
	if s == None or not isinstance(s, basestring):
		return ''
	else:
		t = s.strip()   # trip whitespaces chars from both ends
		r = re.sub(r'[\s\s]+', ' ', t)  # convert multiple whitespace chars into one
	return r

#to run the tests:
#python stripspaces.py
if __name__ == "__main__":
    print "running stripspaces tests..."
    assert '' == stripspaces(None)
    assert '' == stripspaces(1)
    assert '' == stripspaces('')
    assert 'a' == stripspaces('   a   ')
    assert 'a b' == stripspaces(' \t  \t\ta\t\t   \t b  \t ')
    print "stripspaces tests passed!"


