# Utility function to clean a string
def stripspaces(s):
    """Remove whitespace chars from both ends of the string returns a new
    string with whitespace chars removed from both ends of the string
    converts multiple whitespace chars into 1 space char returns an empty
    string if input is None or anything else than a string or unicode.
    """
    if s == None or not isinstance(s, basestring):
        return ""
    return " ".join(s.strip().split())

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


