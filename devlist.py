import time
import os
import requests
import json
import jinja2
import glob 
import pprint
from bs4 import BeautifulSoup
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import markdown
import sys
import shutil
import random
from github import Github
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""
auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

'''
If this is running on a web server
the 'changed html' files do not have to be uploaded
as they are already on the web server
'''
git_username = "plowsof"
repo_name =  "plowsof.github.io"
repo_dir = "monerodevs"

git_token = ""



default_avatar = "icons/default-avatar.jpg"

def uploadtogit(infile,outfile):
    global repo_name 
    global repo_dir
    global git_token
    g = Github(git_token)

    repo = g.get_user().get_repo(repo_name)

    with open(infile, 'r') as file:
        content = file.read()
    ##print(outfile)
    # Upload to github
    git_file = repo_dir + "/" + outfile
    contents = repo.get_contents(git_file)
    repo.update_file(contents.path, "committing files", content, contents.sha, branch="main")
    #print(git_file + ' UPDATED')


def setAvatar(person):
    global default_avatar
    try:
        if person["avatar"]:
            return(person["avatar"])
    except Exception as e:
        pass
    try:
        if person["twitter"]:
            return(getTwitterImage(person["twitter"]))
    except Exception as e:
        pass

    try:
        if person["github"]:
            return(getGithubImage(person["github"]))
    except Exception as e:
        pass

    return default_avatar

def getGithubImage(username):
    url = f"https://github.com/{username}"
    scrape = requests.get(url)
    soup = BeautifulSoup(scrape.text, 'html.parser')
    #print(soup.prettify())
    get = soup.find(property="og:image")
    avatar = get['content']
    return avatar
    
def getTwitterImage(username):
    user = api.get_user(username)
    return (user.profile_image_url_https.replace("_normal",""))


def makeProjectPage(people,data,project_fname,tag_link_to):
    people_for_project = []
    tag = data["tags"][1]

    for person in people:
        if tag in person["tags"]:
            people_for_project.append(person)

    project_list = [data]
    #project_list.append(data)
    project_html = createCard(project_list,tag_link_to)

    #print(project_html)
    people_html = createCard(people_for_project,tag_link_to)

    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "project_template.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(people=people_html,project=project_html)  # this is where to put args to the template renderer
    
    
    with open(project_fname,"w+") as f:
        f.write(outputText)
    

#pprint.pprint(projects)
#pprint.pprint(people)
def createCard(data_list,tag_link_to,nested="./"):
    people_html = []
    inline = 0
    thestring = ""
    people = data_list
    for person in people:
        if inline == 0:
            thestring = ""
            thestring += "<div class='container'>"
        if person["avatar"] == "":
            avatar = setAvatar(person)
        else:
            avatar = person["avatar"] 
            #print({markdown.markdown(person['description'])})
        thestring += f'''<div class="card"> 
                        <p id="title">{person['name']}</p>
                        <p id="description">{markdown.markdown(person['description'])}</p>
                        <img class="avatar" src="{avatar}">
                    '''
        try:
            if person["twitter"] != "":
                thestring +=    f'''
                            <a href="https://twitter.com/{person["twitter"]}">
                                <img class="twitter" src="{nested}icons/twitter.png">
                            </a>
                            '''
        except:
            pass
        try:
            if person["reddit"] != "":
                thestring += f'''
                                <a href="https://reddit.com/u/{person["reddit"]}">
                                    <img class="reddit" src="{nested}icons/reddit.png">
                                </a>
                            '''
            pass
        except:
            pass

        if person["github"] != "":
            if "/git." in person["github"]:
                git_url = person["github"]
            else:
                git_url = f'https://github.com/{person["github"]}'


            thestring += f'''
                            <a href="{git_url}">
                                <img class="github" src="{nested}icons/github.png">
                            </a>
                        '''
        try:
            if person["matrix"] != "":
                thestring += f'''
                                <a href='https://matrix.to/#/@{person["matrix"]}'>
                                    <img class="matrix" src="{nested}icons/matrix.png">
                                </a>
                            '''
            pass
        except:
            pass
        try:
            if person["youtube"] != "":
                thestring += f'''
                                <a href="https://youtube.com/c/{person["youtube"]}">
                                    <img class="youtube" src="{nested}icons/youtube.png">
                                </a>
                            '''
            pass
        except:
            pass
        try:
            if person["website"] != "":
                thestring += f'''
                                <a href="{person["website"]}">
                                    <img class="www" src="{nested}icons/www.png">
                                </a>
                            '''
            pass
        except:
            pass


        thestring += "<div class='tags'>"
        for tag in person["tags"]:
            if tag != "Monero":
                try:
                    tag_url = "./" + tag_link_to[tag]
                    pass
                except Exception as e:
                    print(f"error: {person['name']} has a tag: {tag} which has no Project")
                    sys.exit(1)
                    pass
                
                thestring += f'''
                            <a href='{tag_url}'>
                            <div class='tag'>{tag}  </div>
                            </a>
                        '''
        thestring += "</div>"
        try:
            if person["donate"] != "":
                if "http" in person["donate"]:
                    #its a web url link
                    thestring += f'''
                    <div>
                    <button><a href='{person['donate']}'>Donate</a></button>
                    </div>
                                '''
                else:
                    thestring += f'''
                    <div>
                    <button class='dono'>Donate</button>
                    <span class='dono'><a href='monero:{person['donate']}'>{person['donate']}</a></span>
                    </div>
                                '''
                    #it should be an address
            pass
        except Exception as e:
            pass
        thestring += "</div>"

        inline += 1
        if inline == 3:
            thestring += "</div>"
            #print(thestring)
            #print("****************************")
            people_html.append(thestring)
            inline = 0
    if inline != 0:
        thestring += "</div>"
        people_html.append(thestring)

    return people_html


def main():
    found = 1
    people = []
    project_list = []
    tag_link_to = {}

    if found == 1:
        #generate the static html page
        inline = 1
        for x in glob.glob("people/*json"):
            with open(x,"r") as f:
                data = json.load(f)
            try:
                modified = 0
                if data["avatar"] == "":
                    print("avatar not set")
                    data["avatar"] = setAvatar(data)
                    modified = 1
                if data["description"] == "":
                    data["description"] = "I like Monero [getmonero.org](www.getmonero.org)"
                    modified = 1
                #if modified, save the file and push it.



                if modified == 1:
                    with open(x, "w") as f:
                        json.dump(data, f,indent=4)
                    os.system(f"git add {x}")
            except Exception as e:
                pass

            people.append(data)
        #we changed a description/avatar - push the new files so we dont have to do it again

    
    
    if found == 1:
        #generate the static html page
        inline = 1
        for x in glob.glob("projects/*json"):
            with open(x,"r") as f:
                data = json.load(f)
                project_list.append(data)
                #tag links to projects name (different than tag).html
                tag_link_to[data["tags"][1]] =  (data["name"]).lower().replace(" ","-") + ".html"
                if "http" not in data["website"]:
                    data["website"] = "https://www.getmonero.org/"
                    modified = 1
                if data["avatar"] == "":
                    print("avatar not set")
                    data["avatar"] = setAvatar(data)
                    modified = 1
                if data["description"] == "":
                    data["description"] = "I like Monero [getmonero.org](www.getmonero.org)"
                    modified = 1
                    
                if modified == 1:
                    with open(x, "w") as f:
                        json.dump(data, f,indent=4)
                    os.system(f"git add {x}")

        with open("tag_link_to.json", "w+") as f:
            json.dump(tag_link_to, f,indent=4)
        for data in project_list:
            project_fname = (data["name"]).lower().replace(" ","-") + ".html"
            makeProjectPage(people,data,project_fname,tag_link_to)



        if modified == 1:
            os.system(f"git commit -m 'changes'")
            os.systen(f"git push devlist main")

    random.shuffle(people)
    random.shuffle(project_list)

    people_html = createCard(people,tag_link_to)
    projects_html = createCard(project_list,tag_link_to)

    #print(projects_html)
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "template.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(people=people_html,projects=projects_html)  # this is where to put args to the template renderer

    #the main page
    with open("index.html","w+") as f:
        f.write(outputText)


def checkDiff():

    os.chdir("/home/human/Documents/xmr-btc-wishlist/watchgit/deployed/monerodevs.org")
    os.system("git fetch devlist")
    stream = os.popen("git diff main devlist/main").read()
    os.system("git checkout main")
    os.system("git merge devlist/main")
    new_json_files = []
    new_html_files = []
    #print(stream.splitlines())
    changes = 0
    for line in stream.splitlines():
        if "diff" in line:
            if "json" in line:
                changes = 1
                fname = line.split("b/")[1]
                new_json_files.append(fname)

    if changes == 1:
        #build new files
        main()
        #see which ones actually changes
        if os.path.isdir("uploadme"):
            print("dir exists")
            files = glob.glob('uploadme/*.html')
            
            for x in files:
                os.remove(x)
        else:
            os.mkdir("uploadme")
        #if its a project,  its just the index page and the project page
        with open("tag_link_to.json", 'r') as f:
            tag_link_to = json.load(f)
        #the persons card will change (index.html) by default
        #all of the persons tags pages will change
        for changed in new_json_files:
            with open(changed,"r") as f:
                print(changed)
                data = json.load(f)
            for tag in data["tags"]:
                if tag != "Monero":
                    try:
                        new_html_files.append(tag_link_to[tag])
                        pass
                    except Exception as e:
                        print(f"Project: {tag} doesnt exist")
                

        print(new_html_files)
        for file in new_html_files:
            shutil.copyfile(file, os.path.join("uploadme",file))
        shutil.copyfile("index.html", os.path.join("uploadme","index.html"))





if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "shuffle":
            main()
            uploadtogit("index.html","index.html")
    else:
        checkDiff()
