# Jupyter Book Tutorial

(Last updated: May 22, 2023)

In this tutorial, we will teach you how to create a Jupyter book and deploy it online.
This page is written in markdown, which also serves as an example.

:::{note}
This tutorial only mentions the basics.
For more advanced usage of Jupyter Book, such as this special content block, check [the Jupyter Book documentation](https://jupyterbook.org/en/stable/content/index.html) for more information.
:::

## Table of contents
- [Prerequisites](#pre)
- [Step 1: Install conda](#s1)
- [Step 2: Install Jupyter Book](#s2)
- [Step 3: Create a new repository](#s2)
- [Step 4: Build the book locally](#s4)
- [Step 5: Deploy the book online](#s5)

## Prerequisites
<a name="pre"></a>

We will use [GitHub Pages](https://pages.github.com) to deploy your compiled book, which means that you need to [register a GitHub account](https://github.com/signup).

We assume that you have installed the environment that can edit and run Jupyter Notebook files.
If you have not done so, check the [Jupyter website](https://jupyter.org) for how to install the user interface and environment.

You need a terminal (e.g., [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) or [Zsh](https://en.wikipedia.org/wiki/Z_shell)) to work with Jupyter Book.
If you are on Windows, install [the git tool](https://git-scm.com/), which should come with a terminal.
If you are on Mac or Linux, the git tool is already installed, so you can just open the terminal and start typing commands.

We expect that you have some basic understanding of using `git` for version control.
If you are new to this idea, check [the git guide](https://github.com/git-guides).

## Step 1: Install conda
<a name="s1"></a>

The first step is installing the conda virtual environment using [miniconda](https://docs.conda.io/en/main/miniconda.html) or [anaconda](https://www.anaconda.com/).
Pick either one of them and follow the instructions on the website to install conda so that you can use the `conda` command on your terminal.

We recommend using miniconda since it is light-weighted, and you can avoid waiting for a long time to install many packages that may not be necessary.
If you already have the conda environment ready on your machine, you can skip this step.

For Mac users, you can also install miniconda using the [Homebrew](https://brew.sh/) package manager:
```sh
brew cask install miniconda
echo 'export PATH="/usr/local/Caskroom/miniconda/base/bin:$PATH"' >> ~/.bash_profile
echo '. /usr/local/Caskroom/miniconda/base/etc/profile.d/conda.sh' >> ~/.bash_profile
source ~/.bash_profile
```

## Step 2: Install Jupyter Book
<a name="s2"></a>

Now, create a new conda environment using the command below. We need to install Jupyter Book in the conda environment.
```sh
conda create -n jupyterbook
```
After you have the environment ready, activate it.
```sh
conda activate jupyterbook
```
Then, install Python in the environment. You need to be careful here if you are using Windows.
According to [the documentation](https://jupyterbook.org/en/stable/advanced/windows.html#working-on-windows), Python 3.8 has some problems when being used for building Jupyter Book.
So, if you are a Windows user, install Python 3.7 specifically instead.
```sh
# For Mac and Linux users
conda install python

# For Windows users
conda install python=3.7
```
Next, install `pip` and check if the path of `pip` is correct.
```sh
conda install pip
which pip # make sure this is the pip inside the jupyterbook environment, which means the path should contains the "jupyterbook" string
```
Finally, install the packages that are needed for building and compiling notebooks.
```sh
pip install -U jupyter-book
```
Check if Jupyter Book is installed correctly using the following command.
Having no error messages means that Jupyter Book is installed correctly.
```sh
jupyter-book --help
```

## Step 3: Create a new repository
<a name="s3"></a>

Next, we need to create a new repository to host your website and code using this tutorial as the template.
Clone our tutorial repository (which downloads the code to your local machine):
```sh
git clone https://github.com/yenchiah/jupyter-book-template
```
The cloned tutorial repository has the template files that you need to build your website.
We are only using the template for reference.

To have your repository that can host your website and code, [create a new repository](https://github.com/new) and work from there.
Make sure that your repository is public, and do not add a README file.
You also do not need to add the `.gitignore` file and `license`.

Then, clone your newly created (and currently empty) repository to your local machine.
Remember to use the proper account (i.e., replacing `[my-account-name]`) and repository name (i.e., replacing `[my-repository-name]`) in the URL that you want to clone.
```sh
git clone https://github.com/[my-account-name]/[my-repository-name]
```
Now, copy all the template files and folders from the tutorial repository to this newly created repository.
Again, remember to use the correct repository name (i.e., replacing `[my-repository-name]`).
```sh
cp -r jupyter-book-template/* [my-repository-name]/
```
Finally, delete the old `git` history from the template that you just copied since we do not need them.
```sh
rm -rf .git
```

:::{warning}
Notice that you need to use a terminal to copy all the files (but not drag/drop or copy/paste files with the user interface).
Otherwise, you will fail to copy the hidden files, such as the `.gitignore` or `.gitmodules` files.
:::

## Step 4: Build the book locally
<a name="s4"></a>

Now we are going to compile and build your book on your local machine.
Inside your conda environment, we need to install some required Python packages:
```sh
pip install -U numpy
pip install -U plotly
pip install -U pandas
pip install -U matplotlib
pip install -U seaborn
```
To build the book, run the following command.
Remember that you must go to the repository folder  (i.e., replacing `[my-repository-name]`) that you just cloned.
```sh
cd [my-repository-name]
jupyter-book build .
```
The above command only builds the newly-updated files since the last time you built the book.
Sometimes you may want to build the entire book from scratch, and you can use the following:
```sh
jupyter-book build --all .
```
After building the book, all the html files in the "_build/html/" directory will be updated.
You can then use your browser to open the files locally on your machine to view the compiled notebooks and markdown files.
You can also install a [local Apache HTTP Server](https://httpd.apache.org/) to view the files since the html files are sometimes incorrectly displayed if opened using a browser.

:::{important}
Notice that every time you add new files or update existing files, you need to re-build the book using the commands provided above.
:::

We also already set up the configuration file (`_config.yml`) and table of content file (`_toc.yml`) for you.
For more information about how to edit them, check [this documentation](https://jupyterbook.org/en/stable/start/create.html).

## Step 5: Deploy the book online
<a name="s5"></a>

Now, we have the compiled website files ready, and we can move on to deploy the website.
We will do this using the [GitHub Pages](https://pages.github.com).

First, push your code and files on your local machine to your remote repository.
Replace `[my-repository-name]` with your repository name.
```sh
cd [my-repository-name]
git add .
git commit -m "Add my first book!"
git push
```
The above commands push your code to the main branch.
However, we need to use the [ghp-import](https://github.com/c-w/ghp-import) package to push your website code to a separate branch.
To use the package, run the following to install it:
```sh
pip install -U ghp-import
```
Then, run the following command to push your html files to the `gh-pages` branch.
```sh
ghp-import -n -p -f _build/html
```

:::{important}
Remember that every time you build some new files (or updated files), you need to run the above commands again to update your website code in the remote GitHub repository.
:::

After this, go to the URL that points to your GitHub repository, click "Settings" -> "Pages" to go to the page settings.
You should see a message similar to "Your site is live at [XXX]", where "[XXX]" is your website URL that is publicly accessible.

Also, sometimes it will take a while for GitHub to update your webpage content.
You can check the "Action" page to check the status.
For example, here is the [action page for our tutorial repository](https://github.com/yenchiah/jupyter-book-template/actions).

You can now publish this URL online, such as on your personal website.
More information about how to publish your book can be found on [this documentation](https://jupyterbook.org/en/stable/start/publish.html).