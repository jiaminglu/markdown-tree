## Install
`pip install markdown-tree`

## Usage

```
Usage: markdown_tree [OPTIONS] [DIRECTORY]

Options:
  --ignore TEXT         Ignored files or dirs, comma separated, default=.*
  --header TEXT         Header
  --footer TEXT         Footer
  --emoji / --no-emoji  Enable file/folder emoji
  --prefixes TEXT       Prefixes, default='## {},- {}', which means, top level
                        entries are <h2> and the rest are <ul>

  -c, --config PATH     Load all configs from a json file if exists,
                        default=.mdtreeconfig.json

  -o, --output PATH     Output filename, default is stardard output
  --help                Show this message and exit.
```
