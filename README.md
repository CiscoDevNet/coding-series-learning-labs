# Cisco DevNet Learning Lab: git-intro

**Description**:  This is a tutorial that provides an introduction to coding.  It is written to be displayed within the [Cisco DevNet Learning Labs system](https://learninglabs.cisco.com).

  - **Technology stack**: Built using Markdown.
  - **Status**:  Beta status.

## Dependencies

* None

## Installation

1. Clone (or fork then clone) this project

## Configuration

No configuration necessary.

## Usage

* You can view these files using a Markdown editor.

## Link checking

You can run a link checker such as the Node-based [markdown-link-check](https://github.com/tcort/markdown-link-check) recursively through all labs by running:

```
$ cd labs
$ find . -name \*.md -exec echo "File: {}" \; -exec markdown-link-check {} \;
```

## Known issues

* None

These learning modules are for public consumption, so you must ensure that you have the rights to any content that you contribute.

Write your content in Markdown. DevNet staff reviews content according to the [Cisco Style Guide](http://www-author.cisco.com/c/en/us/td/docs/general/style/guide/Latest/stylegd.html). (Link available on Cisco VPN only.)

#### Publishing Requirements

To create and publish a new lab, take the following steps:
- Add a new folder under `labs`.
- Create a JSON file with the same name as the `labs/`_folder_ name.
- Create markdown files named 1.md, 2.md, and so on; refer to those files in the `labs/`_folder_ JSON file.
- Ensure that the JSON file contains appropriate page titles and file references.
- Send a pull request to get the files commited and merged to `master` by a DevNet reviewer.

A DevNet reviewer then creates a release on the repository with the latest `master` and publishes through the admin interface.

#### Editors

You can write Markdown in a plain text editor, but there are many desktop and Web-based options that allow you to write and preview your work at the same time. We recommend Visual Studio Code [Download](https://code.visualstudio.com/) for several reasons:
- Lightweight environment for coding (or writing Markdown)
- Available on Mac OS, Linux or Windows
- Github Client integration
- Great Markdown preview features native in the editor
- Intuitive operation and structure

You can validate a JSON file by using the [online formatter and validator](https://jsonformatter.curiousconcept.com).

## Getting help

If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker.

## License
[LICENSE](LICENSE)

## Getting involved

* If you'd like to make contributions, feel free to make a request in the issue tracker.  If you're interested in creating a Cisco DevNet Learning Lab, contact Ashley Roach (asroach at cisco.com).

## Credits and references

* [Cisco DevNet Learning Labs](https://learninglabs.cisco.com)
