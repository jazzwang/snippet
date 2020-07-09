import os
from github import Github

try:
    github_id        = os.environ["GITHUB_ID"]
    github_password  = os.environ["GITHUB_PASSWORD"]
except:
    print("Please define environment variable 'GITHUB_ID' and 'GITHUB_PASSWORD'.")
    exit(1)

g = Github(github_id, github_password)

## https://stackoverflow.com/questions/3167494/how-often-does-python-flush-to-a-file
## defaul buffer size = 8192 (8 KB)
## change to 512 Bytes
reactions = open('datacon2020_reactions.csv','w+', 512)
## Write CSV headers
print("issue_id,issue_title,user_id,reaction_type,timestamp",file=reactions)

## https://pygithub.readthedocs.io/en/latest/examples/Repository.html#get-list-of-open-issues
repo = g.get_repo("datacon2020/proposal")
for issue in repo.get_issues():
    ## https://pygithub.readthedocs.io/en/latest/github_objects/Issue.html#github.Issue.Issue.get_reactions
    for reaction in issue.get_reactions():
        ## - issue.number: Type: integer
        ## https://pygithub.readthedocs.io/en/latest/github_objects/Issue.html#github.Issue.Issue.number
        ## - reaction.user: Type: github.NamedUser.NamedUser
        ## https://pygithub.readthedocs.io/en/latest/github_objects/Reaction.html#github.Reaction.Reaction.user
        ## - reaction.user.login: Type: string
        ## https://pygithub.readthedocs.io/en/latest/github_objects/NamedUser.html#github.NamedUser.NamedUser.login
        ## - reaction.user.name: Type: string
        ## https://pygithub.readthedocs.io/en/latest/github_objects/NamedUser.html#github.NamedUser.NamedUser.name
        ## - reaction.created_at: Type:	datetime.datetime
        ## https://pygithub.readthedocs.io/en/latest/github_objects/Reaction.html#github.Reaction.Reaction.created_at
        print(str(issue.number) + ",\"" + issue.title + "\"," + reaction.user.login + "," + reaction.content + "," + str(reaction.created_at), file=reactions)
        print(str(issue.number) + ",\"" + issue.title + "\"," + reaction.user.login + "," + reaction.content + "," + str(reaction.created_at))
