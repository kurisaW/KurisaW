import os
import re
import requests
import base64


# 替换为你的GitHub用户名和仓库名
github_username = 'kurisaW'
github_repo = 'kurisaW.github.io'

# 从GitHub Secrets中获取Token
github_token = os.environ.get('GH_TOKEN')

# 获取博客目录的内容
github_url = f'https://api.github.com/repos/{github_username}/{github_repo}/contents/content/post'
headers = {
    'Authorization': f'Bearer {github_token}',
    'Accept': 'application/vnd.github.v3+json'
}
response = requests.get(github_url, headers=headers)
response.raise_for_status()
content = response.json()

# 从每个博客目录的index.md文件中提取日期和标题
blog_posts = []
for item in content:
    if item['type'] == 'dir':
        dir_name = item['name']
        index_url = f'https://api.github.com/repos/{github_username}/{github_repo}/contents/content/post/{dir_name}/index.md'
        response = requests.get(index_url, headers=headers)
        response.raise_for_status()
        index_content = response.json()
        if 'content' in index_content:
            content_str = base64.b64decode(index_content['content']).decode('utf-8')
            date_match = re.search(r'date:\s*(\d{4}-\d{2}-\d{2})', content_str)
            title_match = re.search(r'title:\s*(.+)', content_str)
            summary_match = re.search(r'description:\s*(.+)', content_str)
            date = date_match.group(1) if date_match else 'N/A'
            title = title_match.group(1) if title_match else 'Untitled'
            summary = summary_match.group(1).strip() if summary_match else 'Untitled'
            link = f'https://github.com/{github_username}/{github_repo}/blob/master/content/post/{dir_name}/index.md'
            blog_posts.append({'date': date, 'title': title, 'link': link, 'summary': summary})

# 排序博客文章并选择最近的10篇
sorted_posts = sorted(blog_posts, key=lambda x: x['date'], reverse=True)[:10]

# 生成Markdown表格
markdown_table = "\n| UpdateTime | Title | Summary |\n| ---------- | ----- | ------- |\n" + \
    "\n".join([f"| {post['date']} | [{post['title']}]({post['link']}) | {post['summary']} |" for post in sorted_posts])

# 更新README.md文件
readme_path = 'README.md'  # 替换为你的README.md路径
with open(readme_path, 'r', encoding='utf-8') as file:
    readme_content = file.read()
    # 使用正则表达式替换部分
    updated_readme = re.sub(r'(### `✍️ Recent Posts`)([\s\S]*?)(\n##)', rf'\1{markdown_table}\3', readme_content)

with open(readme_path, 'w', encoding='utf-8') as file:
    file.write(updated_readme)

