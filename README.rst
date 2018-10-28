gitkeep
=======

Sometimes when working with Git you require empty folders to be part of
your repository. Maybe because you want to underline the importance of
certain directories for storing certain files in the future. Maybe some
part of the logic depends on those directories being there.

However, because Git only versions files, it is `unable to add empty
directories <https://git.wiki.kernel.org/index.php/GitFaq#Can_I_add_empty_directories.3F>`__.

One well known hack to get around this problem is to version dummy files
inside the empty directories you wish to add to your repository, in
order to force the directory into source control.

Gitkeep is a tiny command line utility written in Python that makes it
easy to use this hack, by creating ``.gitkeep`` files in the directories
of your choosing.

In the Bash command line it is the equivalent of running:

::

   find . -type d -empty -exec touch {}/.gitkeep \;

However, using the Bash command above forces you to do the same for each
directory path you wish to version, and then to manually delete any
exceptions.

Also, Windows users do not have the luxury of the Bash command line
unless they install Cygwin.

Use
===

To create a ``.gitkeep`` file in a specific directory called ‘foo’:

::

   gitkeep path/to/foo

To add a message to your ``.gitkeep`` file in order to let fellow
developers understand why it’s important to keep the specified directory
in source control you can use the ``--message`` or ``-m`` flag:

::

   gitkeep path/to/foo -m "This is where we'll later add X stuff."

By default all ``.gitkeep`` files bear the date of creation, the URL to
this project and a default message. The idea here is to help others
maintaining your project in the future understand what these files are.
However, if you’d prefer to create empty ``.gitkeep`` files you can do
so with the ``--empty`` or ``-e`` flag:

::

   gitkeep path/to/foo -e

To remove a ``.gitkeep`` file from a specified path use the ``--let-go``
or ``-l`` flag:

::

   gitkeep --let-go path/to/foo

To create ``.gitkeep`` files recursively in a path and all its
sub-directories use the ``--recursive`` or ``-r`` flag:

::

   gitkeep --recursive path/to/foo

To remove all ``.gitkeep`` files recursively from a path and all its
sub-directories use a combination of the ``-r`` and ``-l`` flags above:

::

   gitkeep -lr path/to/foo

Implementation Notes
====================

Gitkeep is powered by `Click <http://click.pocoo.org/6/>`__.

Develop
-------

First prepare a virtual environment to install your local copy. From the
root of your project run:

::

   virtualenv venv
   New python executable in venv/bin/python
   Installing setuptools, pip............done.

Activate the corresponding environment. On OS X and Linux, do the
following:

::

   . venv/bin/activate

Notice the prompt of your shell has changed to show the active
environment.

Get Click installed in your virtual environment:

::

   pip3 install Click

To install gitkeep in your virtual environment:

::

   pip3 install --editable .

Then just try running gitkeep:

::

   gitkeep --help

To go back to the real world, run:

::

   deactivate
