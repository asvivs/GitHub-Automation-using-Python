from github import Github
from github import Auth

# authentication
access_token = "YOUR_GITHUB_ACCESS_TOKEN"
auth = Auth.Token(access_token)
g = Github(auth=auth)

# repo name
repo_name = "LeetCode-SQL-Problems"
base_directory = "LeetCode SQL Challenge"

day = 8
question = "Number of Unique Subjects Taught by Each Teacher (#2356)"
blog_url = "https://medium.com/@asvithavs/day-8-leetcode-sql-challenge-89bdbcb5277d"

# get your github username
user = g.get_user()

# file name and file content in Markdown format
file_name = f"Day {day} LeetCode SQL Challenge.md"
file_content = f"# Day {day} LeetCode SQL Challenge: {question}\n\n## Read the Full Solution\n\nYou can find the " \
               f"detailed solution to this problem in my Medium blog post:\n\n[Medium Blog]({blog_url}) "

# checking if file already exists
try:
    repo = user.get_repo(repo_name)
    contents = repo.get_contents(f"{base_directory}/{file_name}")

    # If file exists update it
    repo.update_file(contents.path, f"Updated file {file_name}", file_content, contents.sha)
    print(f"Hey {user.login},\n Your file {file_name} is Updated Successfully!!!")
except Exception as e:
    # If file doesn't exist create it
    repo.create_file(f"{base_directory}/{file_name}", f"{file_name} Created", file_content)
    print(f"Hey {user.login},\n\n Your file {file_name} is Created Successfully!!!")

print(" ")
print("Automation Completed :)")
