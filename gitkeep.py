import click

@click.command()
@click.option('--recursive', '-r', default=False, is_flag=True,
	help='Add/remove the .gitkeep files recursively for all sub-directories in the specified path.')
@click.option('--letgo', '-l', default=False, is_flag=True,
	help='Removes the .gitkeep files from the specified path.')
@click.argument('path')
def gitkeep(recursive, letgo, path):
	"""Add a .gitkeep file to a directory in order
	to push them into a Git repo even if they're empty.\n
	Read more about why this is necessary at:
	https://git.wiki.kernel.org/index.php/Git_FAQ#Can_I_add_empty_directories.3F"""

	click.echo('recursive: %r' % recursive)
	click.echo('Let go: %r' % letgo)
	click.echo('Path: %s' % path)
