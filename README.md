Syncing Your Local Repo with GitHub (Pulling Changes)
Once you've cloned the repository, you'll want to keep your local copy updated with any changes that might happen on GitHub (e.g., if you or a collaborator push new code). This is done using git pull.
To pull changes:
Open your project in VS Code.
Open the Integrated Terminal (Ctrl + `` (backtick) orTerminal > New Terminal`).
Make sure you are in the root directory of your project.
Run the following command:

## To download from GitHub

* **git pull**: This command does two things:
Fetches changes from the remote repository (downloads new commits and updates from GitHub).
Merges those fetched changes into your current local branch.
If there are any new changes on GitHub, git pull will download them and integrate them into your local files. If your local repository is already up-to-date, it will simply say "Already up to date."

Recommended Workflow for Collaborating / Keeping Sync:
Before you start working each day (or before making significant changes): git pull to get the latest changes from GitHub.
When you finish a set of changes locally:

## To upload to GitHub

* **git add . **(to stage your changes)
* **git commit -m "Your descriptive commit message" **(to record your changes locally)
* **git push **(to send your committed changes to GitHub)

This ensures your local copy is always aligned with the remote, and your contributions are sent back up.
