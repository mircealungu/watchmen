from watchmen.watchmen import Watchmen


def test_broken_url():
    """Assert if the constructor works correctly. """
    watch = Watchmen();
    watch.add_potential_urls('iambroken')
    assert 'iambroken' not in watch.good_urls()
