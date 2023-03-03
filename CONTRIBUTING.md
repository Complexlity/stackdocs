# Who Can Contribute

All stackies are free to contribute to the project in any way including opening an issue, requesting a feature, fixing a bug, adding a feature, adding new campaigns and quests on the page, updating the docs etc,

# How To Update Quest and Campaign Documentation

At the moment, All Campaign and Quest pages contain a `Brief Overview Here` text. This is a dummy text which represents a simple summary of what the StackUp Campaign or Quest Teaches.

At the base of the campaign page, you would see and button `edit this page`.
![Edit Page Screen Shot](static/img/edit-screenshot.png)

This takes you to the exact file to edit the document in the repo. Make the updates and pull a request

Optionally, you could navigate to the [docs](/docs/) folder and find the folder for the quest and update it

**IMPORTANT!!**: Ensure the `Brief Overview` is indeed brief(3 lines at most). The main purpose of StackDocs is to provide links to the particular stackup page

# How To Create A New Campaign Or Quest On The Docs

In the root folder of the project, run this simple

```
python3 <campaign-name> <quest one name> <quest two name> .....
```

You can use as many arguments as the number of quest for the particular campaign
Then , go into the newly created folder and update the links
Refer to the [scripts README](/scripts/README.md) for me detailed guide

<!--Issues URL-->

[issues-url]: https://github.com/Complexlity/stackdocs/issues
