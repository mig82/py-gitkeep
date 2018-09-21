import click
import os
import time

@click.command()
@click.option("--recursive", "-r", default=False, is_flag=True,
	help="Add or remove the .gitkeep files recursively for all sub-directories "
	"in the specified path.")
@click.option("--let-go", "-l", default=False, is_flag=True,
	help="Remove the .gitkeep files from the specified path.")
@click.option("--message", "-m",
	help="A message to be included in the .gitkeep file, ideally used to "
	"explain why it's important to push the specified directory to source "
	"control even if it's empty.")
@click.argument("path")
def gitkeep(recursive, let_go, message, path):
	"""Add a .gitkeep file to a directory in order
	to push them into a Git repo even if they're empty.\n
	Read more about why this is necessary at:
	https://git.wiki.kernel.org/index.php/Git_FAQ#Can_I_add_empty_directories.3F"""

	click.echo("recursive: %r" % recursive)
	click.echo("Let go: %r" % let_go)

	# Add the path separator at the end of the path if missing.
	if(path[-1] != "/"):
		path = path + "/"

	click.echo("Path: %s" % path)

	#Execute only if the given path is for an existing directory.
	if(os.path.exists(path)):
		if(os.path.isdir(path)):
			content = get_gitkeep_content(message)
			walk_path(recursive, let_go, path, content)
		else:
			click.echo("Path is NOT a directory!")
	else:
		click.echo("Path does NOT exist!")

def get_gitkeep_content(message):
	content = """.gitkeep
	Created %s
	By https://github.com/mig82/py-gitkeep
	""" % time.strftime("%Y-%m-%d %H:%M:%S")

	if(not message):
		content += "Message: .gitkeep files are a simple hack to push empty directories to Git.\n"
	else:
		content += "Message: %s\n" % message

	return content

def walk_path(recursive, let_go, path, content):

	#Add or delete the .gitkeep file in the specified path.
	if(let_go):
		delete_gitkeep(path)
	else:
		write_gitkeep(path, content)

	#Add or delete the .gitkeep file recursively.
	if(recursive):
		for root, dirs, files in os.walk(path):
			for dir in dirs:

				gitkeep_path = os.path.join(root, dir) + "/"

				if(let_go):
					delete_gitkeep(gitkeep_path)
				else:
					write_gitkeep(gitkeep_path, content)


def write_gitkeep(path, content):
	file = open(path + ".gitkeep", "w")
	file.write(content)
	file.close()
	click.echo("	Created %s.gitkeep" % path)

def delete_gitkeep(path):
	gitkeep_path = path + ".gitkeep"
	if(os.path.exists(gitkeep_path)):
		os.remove(path + ".gitkeep")
		click.echo("	Removed %s.gitkeep" % path)
	else:
		click.echo("	No .gitkeep found at %s" % path)
