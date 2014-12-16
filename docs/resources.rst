=========
Resources
=========

The following Resources are supported by the Diablo3API wrapper


Career Profile
==============
The Profile resource takes one argument, the Battletag of the user in the form of Battletag-1234 ::

    from diablo3api import Diablo3API

    api = Diablo3API()
    api.profile.get("battletag-1234")

Hero Profile
============
The Hero Profile resource takes 2 arguments, the Battletag and the Hero ID. The Career Profile resource will list all of the heroes for a given profile. ::

    from diablo3api import Diablo3API

    api = Diablo3API()
    api.profile.hero.get("battletag-1234", 5678)

Item Information
================
The Item Information resource takes 1 argument, the Item ID. The Hero Profile will list all of the items equipped by a Hero. ::

    from diablo3api import Diablo3API

    api = Diablo3API()
    api.item.get("item-id")

Follower Information
====================
The Follower Information resource takes 1 argument, the Follower Type. The only valid Follower types are "templar", "scoundrel", and "enchantress". ::

    from diablo3api import Diablo3API

    api = Diablo3API()
    api.follower.get("templar")

Alternatively there are specific methods for each of the followers. ::

    api.follower.templar()
    api.follower.scoundrel()
    api.follower.enchantress()

Artisan Information
===================
The Artisan Information resource takes 1 argument, the Artisan Type. The only valid Artisan types are "blacksmith", "jeweler", and "mystic". ::

    from diablo3api import Diablo3API

    api = Diablo3API()
    api.artisan.get("blacksmith")

Alternatively there are specific methods for each of the artisans. ::

    api.artisan.blacksmith()
    api.artisan.jeweler()
    api.artisan.mystic()
