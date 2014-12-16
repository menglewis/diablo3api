# -*- coding: utf-8 -*-


class Diablo3APIError(Exception):
    pass


class Resource(object):
    """
    Base Class for a Diablo 3 Resource
    """

    def __init__(self, api_host, session):
        self.api_host = api_host
        self.session = session

    def get(self, *args, **kwargs):
        """
        Makes a request to the URL and returns the response as a Python object
        :param args:
        :param kwargs:
        :return:
        """
        r = self.response(*args, **kwargs)
        if r.status_code == 200:
            return r.json()

        raise(Diablo3APIError(r.reason))

    def response(self, *args, **kwargs):
        """
        Returns the full Requests response for the Resource
        :param args:
        :param kwargs:
        :return:
        """
        url = self.build_url(*args, **kwargs)
        return self.session.get(url)

    def build_url(self, resource):
        """
        Builds the URL using the base API host and the resource
        :param resource:
        :return:
        """
        url = "%s/%s" % (self.api_host, resource)
        return url


class Profile(Resource):
    """
    A Resource for the Diablo Career Profile. See http://blizzard.github.io/d3-api-docs/#career-profile/career-profile-example
    """
    resource = "profile"

    def __init__(self, *args, **kwargs):
        """
        Call the Super __init__ method and add an instantiation of the Hero resource
        :param args:
        :param kwargs:
        :return:
        """
        super(Profile, self).__init__(*args, **kwargs)
        self.hero = Hero(*args, **kwargs)

    def build_url(self, battletag, resource=resource):
        """
        Builds a URL of the form: /api/d3/profile/<battletag>/
        :param battletag:
        :param resource:
        :return:
        """
        url = super(Profile, self).build_url(resource=self.resource)
        return "%s/%s/" % (url, battletag)


class Hero(Resource):
    """
    A Resource for the Diablo Hero Profile. A Hero Profile is within a Career profile which is why this class is
    instantiated under the Profile class. See http://blizzard.github.io/d3-api-docs/#hero-profile/hero-profile-example
    """
    parent_resource = "profile"
    resource = "hero"

    def build_url(self, battletag, hero):
        """
        Builds a URL of the form: /api/d3/profile/<battletag>/hero/<heroId>
        :param args: There should be 2 positional Arguments for Battletag and Hero ID.
        :return:
        """
        return "%s/%s/%s/%s/%s" % (self.api_host, self.parent_resource, battletag, self.resource, hero)


class Item(Resource):
    """
    A Resource for a Diablo Item. See http://blizzard.github.io/d3-api-docs/#item-information/item-information-example
    """
    resource = "data/item"

    def build_url(self, item, resource=resource):
        """
        Builds a URL of the form: /api/d3/data/item/<itemId>
        :param item:
        :param resource:
        :return:
        """
        url = super(Item, self).build_url(resource=self.resource)
        return "%s/%s" % (url, item)


class Follower(Resource):
    """
    A Resource for a Diablo Follower. See http://blizzard.github.io/d3-api-docs/#follower-information/follower-information-example
    Currently only "templar", "scoundrel", and "enchantress" are valid Followers
    """
    resource = "data/follower"

    def build_url(self, follower, resource=resource):
        """
        Builds a URL of the form: /api/d3/data/follower/<follower-type>
        :param follower:
        :param resource:
        :return:
        """
        url = super(Follower, self).build_url(resource=self.resource)
        return "%s/%s" % (url, follower)

    def templar(self):
        """
        Wrapper method to get data for the Templar
        """
        return self.get(follower="templar")

    def scoundrel(self):
        """
        Wrapper method to get data for the Scoundrel
        """
        return self.get(follower="scoundrel")

    def enchantress(self):
        """
        Wrapper method to get data for the Templar
        """
        return self.get(follower="enchantress")


class Artisan(Resource):
    """
    A Resource for the Diablo Artisan. See http://blizzard.github.io/d3-api-docs/#artisan-information/artisan-information-example
    Currently only "blacksmith", "jeweler", and "mystic" are valid Artisans.
    """
    resource = "data/artisan"

    def build_url(self, artisan, resource=resource):
        """
        Builds a URL of the form: /api/d3/data/artisan/<artisan-type>
        """
        url = super(Artisan, self).build_url(resource=self.resource)
        return "%s/%s" % (url, artisan)

    def blacksmith(self):
        """
        Wrapper method to get data for the Blacksmith
        """
        return self.get(artisan="blacksmith")

    def jeweler(self):
        """
        Wrapper method to get data for the Jeweler
        """
        return self.get(artisan="jeweler")

    def mystic(self):
        """
        Wrapper method to get data for the Mystic
        """
        return self.get(artisan="mystic")
