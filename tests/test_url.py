# -*- coding: utf-8 -*-
import unittest
from diablo3api import Diablo3API


class URLBuildTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Diablo3API()

    def test_profile_url(self):
        cases = ("testuser-2255", "username-1234", "battletag-8527")

        for case in cases:
            self.assertEqual(self.api.profile.build_url(case), "https://us.battle.net/api/d3/profile/%s/" % case)

    def test_hero_url(self):
        cases = (
            ("testuser-2255", 1529),
            ("username-1234", 25822124),
            ("battletag-8527", 2525291),
        )
        for (battletag, hero) in cases:
            self.assertEqual(self.api.profile.hero.build_url(battletag, hero),
                             "https://us.battle.net/api/d3/profile/%s/hero/%s" % (battletag, hero))

    def test_item_url(self):
        cases = ("item", "test-item")
        for case in cases:
            self.assertEqual(self.api.item.build_url(case), "https://us.battle.net/api/d3/data/item/%s" % case)

    def test_follower(self):
        cases = ("templar", "scoundrel", "enchantress")
        for case in cases:
            self.assertEqual(self.api.follower.build_url(case), "https://us.battle.net/api/d3/data/follower/%s" % case)

    def test_artisan(self):
        cases = ("blacksmith", "jeweler", "mystic")
        for case in cases:
            self.assertEqual(self.api.artisan.build_url(case), "https://us.battle.net/api/d3/data/artisan/%s" % case)
