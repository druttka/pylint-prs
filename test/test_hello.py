import pytest
from pylintprs.hello import get_greeting as g

def test_get_greeting_includes_name():
    result = g('python')
    assert result == 'Hello python'