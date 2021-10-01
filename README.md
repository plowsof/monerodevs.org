
People can have Multiple tags.
Projects should only have One tag

looks something like:    
(avatar can be empty - i will get your twitter profile pic automatically - failing that - your github.. failing that.. a default icon

```
{
    "name": "",
    "github": "",
    "reddit": "",
    "matrix": "",
    "twitter": "",
    "youtube": "",
    "website": "",
    "donate": "",
    "avatar": "",
    "description": "",
    "tags": [
        "Monero",
        "OptOut",
        "Events"
    ]
}
```

example:

```
{
    "name": "Seth Simmons",
    "github": "sethforprivacy",
    "reddit": "fort3hlulz",
    "matrix": "sethsimmons:monero.social",
    "twitter": "sethforprivacy",
    "youtube": "OptOutPodcast",
    "website": "https://sethforprivacy.com/",
    "donate": "86JzKKyZvtEC98y6zJxCCVfcA3r75XngPBjpYDE6zRR36keNGMHwZomDjMCv1oCYB2j9myiFqEJQF3JtnhKdfX546T91eaY",
    "avatar": "https://pbs.twimg.com/profile_images/1353846945291370496/E8JJq2d0.jpg",
    "description": "I like Monero [getmonero.org](www.getmonero.org)",
    "tags": [
        "Monero",
        "OptOut",
        "Events"
    ]
}
```

the corresponding 'OptOut' project:
```
{
    "name": "OptOut Podcast",
    "github": "",
    "twitter": "optoutpod",
    "donate": "https://www.optoutpod.com/support/",
    "type": "project",
    "website": "https://www.optoutpod.com/",
    "youtube": "OptOutPodcast",
    "avatar": "https://pbs.twimg.com/profile_images/1403070707320430599/uK2eSM-s.jpg",
    "description": "Welcome to Opt Out, where I sit down with passionate people to learn why privacy matters to them, the tools and techniques they\u2019ve found and leveraged, and where we encourage and inspire others towards personal privacy and data-sovereignty.",
    "tags": [
        "Monero",
        "OptOut"
    ]
}
```

### using the src

Install git on your os
create a folder on your machine / open terminal there
set up ssh key access for github ...
git clone git@github.com:plowsof/monerodevs.org.git
git remote add devlist git@github.com:plowsof/monerodevs.org.git
place the python and template files in the same dir as the people/projects folders
a cronjob can call the script with "shuffle" as an arg to reshuffle the main page
a human must view pull requests. merge them. then run the script to generate the new html files
