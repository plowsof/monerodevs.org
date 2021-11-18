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
        "Monero"
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

## I want to be on the list 
[how to make a PR on github](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

Lets say my name is 'John Doe'. I am a member of the 'Monero Policy Workgroup' and i want to be added on the devlist website.
I fork this repo, then i create a new file in 'people' called (name does not matter) johndoe.json. The 'tag' for the MPW is, "MPW" so i need to add that as a tag.
```
~ Contents of people/johndoe.json ~
{
    "name": "John Doe",
    "github": "", <- just provide the username for this and reddit/matrix
    "reddit": "",
    "matrix": "",
    "twitter": "",
    "youtube": "", <- The /c/ channel name (not the uid or the link wont work)
    "website": "",
    "donate": "", <- A web url can be used to take people to your page OR put an address/openalias here to display on the site
    "avatar": "", <- If you leave this empty, your twitter / or github / of default icon will be auto filled in because i like saving people time.
    "description": "", <- this will default to "I like monero getmonero.org" if left empty
    "tags": [
        "Monero",
        "MPW" <- We've added the tag
    ]
}

```

Then submit a PR and wait for the 'human' (probably me) to review it.     

John Doe now wants to create a new project! called 'cyberpunks'! so he needs to create a file in the projects folder, using the same template:

```
~ Contents of projects/cyberpunks.json~
{
    "name": "Cyber Punks",
    "github": "",
    "reddit": "",
    "matrix": "",
    "twitter": "",
    "youtube": "",
    "website": "",
    "donate": "",
    "avatar": "",
    "description": "We are a team of CyberPunks!",
    "tags": [
        "Monero",
        "Punk" <- anyone who wants to be shown in this group can add a PR with "Punk" added to their tags.
    ]
}
```

John Doe can then , edit his people/johndoe.json and add the "Punk" to his tags as shown below:
```
~ Contents of people/johndoe.json ~
{
    "name": "John Doe",
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
        "MPW",
        "Punks" <- We've added the new tag (notice no comma after the last tag)
    ]
}
```

### using the src

- Install git on your os
- create a folder on your machine / open terminal there
- set up ssh key access for github ...
- git clone git@github.com:plowsof/monerodevs.org.git
- git remote add devlist git@github.com:plowsof/monerodevs.org.git
- place the python and template files in the same dir as the people/projects folders
- a cronjob can call the script with "shuffle" as an arg to reshuffle the main page
- a human must view pull requests. merge them. then run the script to generate the new html files
- when running on a vps - changes to the save dir of the html files need to be made and uploading to git not needed

### what it looks like when in use

For this example, i deleted the avatar links for Justin and FluffyPony (as they where not working anymore). I also added a quick start guide link to the p2pool project and updated a youtube url for the monero-guides project.
```
root@Box:/home/human/monerodevs# python3 devlist_2.py
remote: Enumerating objects: 23, done.
remote: Counting objects: 100% (23/23), done.
remote: Compressing objects: 100% (16/16), done.
remote: Total 16 (delta 12), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (16/16), done.
From github.com:plowsof/monerodevs.org
   1c94901..26904af  main       -> devlist/main
Already on 'main'
Your branch is ahead of 'origin/main' by 25 commits.
  (use "git push" to publish your local commits)
Updating 1c94901..26904af
Fast-forward
 people/fluffypony.json      | 4 ++--
 people/justin.json          | 2 +-
 projects/monero-guides.json | 4 ++--
 projects/p2pool.json        | 4 ++--
 4 files changed, 7 insertions(+), 7 deletions(-)
avatar not set
avatar not set
dir exists
people/fluffypony.json
people/justin.json
projects/monero-guides.json
projects/p2pool.json
['monero-public-events.html', 'monero-policy-workgroup.html', 'magic-monero-fund
.html', 'monero-space-workgroup.html', 'monero-guides-.html', 'p2pool.html']
root@eeeBox:/home/human/monerodevs# python3 devlist_2.py update
upload :monero-policy-workgroup.html
upload :magic-monero-fund.html
upload :monero-guides-.html
upload :monero-public-events.html
upload :index.html
upload :p2pool.html
upload :monero-space-workgroup.html
root@Box:/home/human/monerodevs#
```
