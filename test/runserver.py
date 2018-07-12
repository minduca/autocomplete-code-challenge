import unittest

# I was considering to add pytest as test framework.  But I decided to only
# stay with 'unittest' because it integrates better with the IDE that I'm
# using.

# About the project structure, I found two main streams of thoughts :
    # (1) test files inside the src project and side-by-side to the content it
    # tests (with some name convention, like, 'test_foo.py' to test 'foo.py' or
    # 'test_foo_sufix1.py' if multiple test files are preferable)
    # (2) test project in a different module
    
    # I'm going with (2) the test project in a different module because I don't
    # like the idea of doubling the size of the deployable and send test code
    # mixed with production code.  The path to the tests is the same path of
    # the source element it tests in 'src'.
    
    # There is a somewhat hidden beauty however on the simplicity of (1) : you
    # keep phisically together things there are semantically related and
    # intuitively supposed to be close.  Maybe a decent solution to this would
    # be to go with (1) but skipping the compilation of every test related
    # content (including eventual external dependencies).

# All test methods have a 'test_' prefix.  This name convention is necessary
# for the IDE I'm using to find the tests on compilation time
if __name__ == '__main__':
    unittest.main()