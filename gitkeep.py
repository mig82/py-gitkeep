import click
import os
import time

@click.command()
@click.option("--recursive", "-r", default=False, is_flag=True,
	help="Add or remove the .gitkeep files recursively for all sub-directories in the specified path.")
@click.option("--letgo", "-l", default=False, is_flag=True,
	help="Remove the .gitkeep files from the specified path.")
@click.argument("path")
def gitkeep(recursive, letgo, path):
	"""Add a .gitkeep file to a directory in order
	to push them into a Git repo even if they"re empty.\n
	Read more about why this is necessary at:
	https://git.wiki.kernel.org/index.php/Git_FAQ#Can_I_add_empty_directories.3F"""

	click.echo("recursive: %r" % recursive)
	click.echo("Let go: %r" % letgo)

	# Add the path separator at the end of the path if missing.
	if(path[-1] != "/"):
		path = path + "/"

	click.echo("Path: %s" % path)

	if(os.path.exists(path)):
		if(os.path.isdir(path)):
			write_gitkeep(path)
		else:
			click.echo("Path is NOT a directory!")
	else:
		click.echo("Path does NOT exist!")

def write_gitkeep(path):
	file = open(path + ".gitkeep", "w")
	file.write("Created %s\n" % time.strftime("%Y-%m-%d %H:%M:%S"))
	file.write("By https://github.com/mig82/py-gitkeep\n\n")
	file.write(".gitkeep files are a cool hack to push empty directories to Git.")
	file.close()
