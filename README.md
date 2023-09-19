# Template directory maker

This program creates a brand new local directory with the following structure:

![Directory structure](https://i.imgur.com/PSyRyln.png)

Then creates a git repository and pushes the local changes to https://github.com/uribalb/versioning_dev_output

The pathlib module was used to create the directory (in ["directory.py"](./directory.py) )
We used gitpython in the main script to initialize and commit changes to the repository and our github token was hidden within a [".env"](./.env) file that was then "gitignored".

To test the code, we recommend creating a brand new output repo as well as a git token with appropriate permissions, create your own .env file with the line "GITHUB_TOKEN=YOUR_TOKEN" then edit the variables 'username', 'remote' and 'token' in ["main.py"](./main.py) to match your github username, repo url and token respectively.

Have fun !
