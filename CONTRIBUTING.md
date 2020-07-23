# Bionitio Contributing Guidelines

Hi there! Many thanks for taking an interest in improving Bionitio.

## Contribution workflow

If you'd like to help out with this package, the standard workflow is as follows:

1. Check that there isn't [already an issue](https://github.com/BIONITIO_GITHUB_USERNAME/bionitio/issues) about your idea to avoid duplicating work.
    * If there isn't one already, please create one so that others know you're working on this
2. Fork the [bionitio repository](https://github.com/BIONITIO_GITHUB_USERNAME/bionitio) to your GitHub account
3. Make the necessary changes / additions within your forked repository
4. Submit a Pull Request and wait for the code to be reviewed and merged.

If you're not used to this workflow with git, you can start with some [basic docs from GitHub](https://help.github.com/articles/fork-a-repo/).

## Installing dev requirements

If you want to work with developing the Bionitio code, you'll need a couple of extra Python packages.
These are listed in `requirements-dev.txt` and can be installed as follows:

```bash
pip install --upgrade -r requirements-dev.txt
```

Then install your local fork of Bionitio:

```bash
pip install -e .
```

## Code formatting with Black

All Python code in Bionitio must be passed through the [Black Python code formatter](https://black.readthedocs.io/en/stable/).
This ensures a harmonised code formatting style throughout the package, from all contributors.

You can run Black on the command line (it's included in `requirements-dev.txt`) - eg. to run recursively on the whole repository:

```bash
black .
```

Alternatively, Black has [integrations for most common editors](https://black.readthedocs.io/en/stable/editor_integration.html)
to automatically format code when you hit save.
You can also set it up to run when you [make a commit](https://black.readthedocs.io/en/stable/version_control_integration.html).

There is an automated CI check that runs when you open a pull-request to Bionitio that will fail if
any code does not adhere to Black formatting.

## Tests

When you create a pull request with changes, [GitHub Actions](https://github.com/features/actions) will run automatic tests.
Typically, pull-requests are only fully reviewed when these tests are passing, though of course we can help out before then.
