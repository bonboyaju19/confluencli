# confluencli
A command line interface for [Atlassian Confluence](https://www.atlassian.com/software/confluence).

# Installation
For PYPI.
```
pip3 install confluencli
```

# How to use
Follow the steps below.
1. Set your environment values.
```
WIKI_USERNAME=YOUR_CONFLUENCE_USERNAME
WIKI_PASSWORD=YOUR_CONFLUENCE_PASSWORD
WIKI_URK=YOUR_CONFLUENCE_BASE_URL
```
2. Run command.
```
confluencli page download --id=YOUR_PAGE_ID --path=./output.zip
```

