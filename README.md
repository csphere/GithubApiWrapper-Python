*Github API Wrapper - Python*
=================================================
-------------------------------------------------
A minimal Python wrapper created for making interaction with the Github API(v3) easy and predictable.

http://developer.github.com/v3/

*Basic Authentication*
-------------------------------------------------
Use a username and password associated with a Github account.

Example:
<pre>
from github import github
g = github.Github( username, password )
</pre>

*Making Requests*
=================================================
-------------------------------------------------
Use the API documentation as a reference.  The library is structured exactly like the API v3 documentation.

*Example Request for Authenticated User's Data*
-------------------------------------------------
<pre>
response = g.users.getUser()
</pre>
<h4>The response...</h4>
<pre>
{
    "headers": {
        "url": "https://api.github.com/user",
        "content_type": "application/json; charset=utf-8",
        "http_code": 200,
        "header_size": 347,
        "request_size": 111,
        "filetime": -1,
        "ssl_verify_result": 0,
        "redirect_count": 0,
        "total_time": 0.110919,
        "namelookup_time": 0.00618,
        "connect_time": 0.014401,
        "pretransfer_time": 0.054725,
        "size_upload": 0,
        "size_download": 817,
        "speed_download": 7365,
        "speed_upload": 0,
        "download_content_length": 817,
        "upload_content_length": 0,
        "starttransfer_time": 0.110853,
        "redirect_time": 0
    },
    "body": {
        "type": "User",
        "url": "https://api.github.com/users/username",
        "private_gists": 2,
        "created_at": "2011-07-07T22:20:48Z",
        "email": "example@gmail.com",
        "html_url": "https://github.com/username",
        "gravatar_id": "123123123123123123123123123",
        "collaborators": 1,
        "hireable": false,
        "disk_usage": 13348,
        "total_private_repos": 3,
        "following": 4,
        "blog": "http://www.yoursitename.com/",
        "bio": null,
        "avatar_url": "https://www.avatar.com/pathtoyouravatar.png",
        "login": "username",
        "owned_private_repos": 3,
        "followers": 1,
        "name": "Your Name",
        "plan": {
            "private_repos": 10,
            "collaborators": 3,
            "space": 614400,
            "name": "micro"
        },
        "location": "Your City, NY",
        "id": 902312,
        "public_repos": 0,
        "public_gists": 17,
        "company": "Your Company Name, LLC"
    }
}
</pre>


*Example Request Creating a New Repository*
-------------------------------------------------
<pre>
# Using just the new Repo name
response = g.repos.createUserRepo( "MyNewRepo" )

# Using some other parameters
name = "MyNewRepo"
desc = "Some description."
page = "www.homepage.com"
private = True
has_issues = True
has_wiki = True
has_downloads = True
response = g.repos.createUserRepo( name, desc, page, private, has_issues, has_wiki, has_downloads )
</pre>

<h4>The response...</h4>
<pre>
{
    "headers": {
        "url": "https://api.github.com/user/repos?access_token=[YOUR_TOKEN]",
        "content_type": "application/json; charset=utf-8",
        "http_code": 201,
        "header_size": 413,
        "request_size": 358,
        "filetime": -1,
        "ssl_verify_result": 0,
        "redirect_count": 0,
        "total_time": 0.280588,
        "namelookup_time": 0.014798,
        "connect_time": 0.023159,
        "pretransfer_time": 0.065582,
        "size_upload": 170,
        "size_download": 975,
        "speed_download": 3474,
        "speed_upload": 605,
        "download_content_length": 975,
        "upload_content_length": 170,
        "starttransfer_time": 0.280533,
        "redirect_time": 0
    },
    "body": {
        "url": "https://api.github.com/repos/username/MyNewRepo",
        "watchers": 1,
        "has_issues": true,
        "created_at": "2012-02-14T03:40:49Z",
        "html_url": "https://github.com/username/MyNewRepo",
        "has_downloads": true,
        "ssh_url": "git@github.com:username/MyNewRepo.git",
        "svn_url": "https://github.com/username/MyNewRepo",
        "description": "Some description.",
        "mirror_url": null,
        "clone_url": "https://github.com/username/MyNewRepo.git",
        "forks": 1,
        "fork": false,
        "has_wiki": true,
        "private": True,
        "homepage": "www.homepage.com",
        "size": 0,
        "updated_at": "2012-02-14T03:40:49Z",
        "owner": {
            "url": "https://api.github.com/users/username",
            "avatar_url": "https://secure.gravatar.com/avatar/someimage.png",
            "gravatar_id": "948f18791231231231231231231",
            "login": "username",
            "id": 901650
        },
        "name": "MyNewRepo",
        "open_issues": 0,
        "master_branch": null,
        "pushed_at": null,
        "id": 3436770,
        "git_url": "git://github.com/username/MyNewRepo.git",
        "language": null
    }
}
</pre>