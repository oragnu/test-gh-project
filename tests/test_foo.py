from test_gh_project.foo import foo


def test_foo():
    assert foo("foo") == "foo"
