## Install
`pip install markdown-tree`

## Usage

```
$ markdown_tree --help
Usage: markdown_tree [OPTIONS] [DIRECTORY]

Options:
  --ignore TEXT    Ignored files or dirs, comma separated, default=.*
  --header TEXT    Header
  --footer TEXT    Footer
  --prefixes TEXT  Prefixes, default='## {},- {}', which means, top level
                   entries are <h2> and the rest are <ul>
  --config PATH		 Load all configs from a json file if exists,
                   default=.mdtreeconfig.json
  --help           Show this message and exit.
```
