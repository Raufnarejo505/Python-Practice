import requests
import plotly.express as px

# make an api call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers = headers)
print(f"Status code : {r.status_code}")

# convert the response object to a dictionary.
response_dict = r.json()

# process results
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")
repo_dicts = response_dict['items']
repo_names, stars = [], []
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the firstt repository
# repo_dict = repo_dicts[0]
# print(f"\nkeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)
print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    # print(f"Name: {repo_dict['name']}")
    # print(f"Owner: {repo_dict['owner']['login']}")
    # print(f"Stars: {repo_dict['stargazers_count']}")
    # print(f"Repository: {repo_dict['html_url']}")
    # print(f"Created: {repo_dict['created_at']}")
    # print(f"Updated: {repo_dict['updated_at']}")
    # print(f"Description: {repo_dict['description']}")


# make visualization
fig = px.bar(x=repo_names, y=stars)
fig.show()
