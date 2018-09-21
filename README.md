#gitkeep

Sometimes when working with Git you require the folder structure of your project
to be part of your repository. Maybe because you want to underline the
importance of certain directories. Maybe some part of the logic depends on
certain directories being there.

However, [Git is not currently capable of versioning directories](https://git.wiki.kernel.org/index.php/GitFaq#Can_I_add_empty_directories.3F).
It only versions files. So if your directories are empty, they won't be versioned.

One well known hack to get around this problem is to create a dummy file inside
the empty directories you wish to version, in order to force them into source
control.

Gitkeep is a tiny command line utility written in Python that makes it easy to
use this hack, by creating `.gitkeep` files in the directories of your choosing.

In the Bash command line it is the equivalent of running:

    find . -type d -empty -exec touch {}/.gitkeep \;

However, using the Bash command above forces you to do the same for each directory
path you wish to version, and then to manually delete any exceptions.

Also, Windows users do not have the luxury of the Bash command line unless they
install Cygwin.

# Use

To create a `.gitkeep` file in a specific directory called 'foo':

    gitkeep path/to/foo

To remove it:

	gitkeep --let-go path/to/foo

To create a `.gitkeep` file in a directory called 'foo' and all its
sub-directories:

    gitkeep --recursive path/to/foo

To remove all `.gitkeep` files from a directory called 'foo' and all its
sub-directories:

    gitkeep --recursive --let-go path/to/foo

There are also short-hand options that can be combined. Most notably to remove
all `.gitkeep` files recursively

	gitkeep -lr path/to/foo

# Implementation Notes

Gitkeep is powered by [Click](http://click.pocoo.org/6/).

##Install for Development

First prepare a virtual environment to install your local copy. From the root of
your project run:

    virtualenv venv
    New python executable in venv/bin/python
    Installing setuptools, pip............done.

Activate the corresponding environment. On OS X and Linux, do the following:

    . venv/bin/activate

Notice the prompt of your shell has changed to show the active environment.

Get Click installed in your virtual environment:

    pip install Click

To go back to the real world, run:

    deactivate
