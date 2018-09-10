import click

@click.command()
@click.option('--recursive', '-r', default=False,
	help='Whether to do this recursively for all sub-directories in the path')
@click.option('--letgo', '-l', default=False,
	help='Whether to remove the .gitkeep file instead of adding it.')
@click.argument('path')
def gitkeep(recursive, letgo, path):
	"""A command line utility that adds .gitkeep files to directories in order
	to force them into a Git repo even if they're empty.\n
	Read more about why this is necessary at:
	https://git.wiki.kernel.org/index.php/Git_FAQ#Can_I_add_empty_directories.3F"""

	click.echo('Path: %s' % path)
