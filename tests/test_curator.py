from watchmen import Watchmen


def test_broken_url():
    """Assert if the constructor works correctly. """
    watchmen = Watchmen()
    watchmen.addPotentialUrls('iambroken')
    assert 'iambroken' not in watchmen.goodURLs()
