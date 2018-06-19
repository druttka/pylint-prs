"""The hello module for testing pylint and tox integration in PRs"""

def get_greeting(name):
    """Returns a formatted greeting given a name"""
    return 'Hello {0}!'.format(name)
