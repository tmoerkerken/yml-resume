# YML-Resume
YML-Resume allows you to quickly and programmatically create beautiful resumes from structured YAML files. The package is in a very early development stage.

## Setting up
Make sure that `python` and `poetry` are installed on your system.
Then run `poetry install` to install the requirements.

## Creating resume
There is an example input folder called `example`. This folder can be renamed to `input` and then a resume can be created with:
- `poetry run python scripts/parse.py`, to parse input files and convert them to an html template via jinja.
- `poetry run python scripts/render.py`, to compile the html to pdf via playwright.

Note that additional context is provided with `--help`. For quick generation with defaults, use `make create`.

## Theming
Currently one theme is provided, called `graytopia`. Theme settings like accent colors can be configured via `themes/<theme_name>/defaults.cfg`.

## Development
### Hot reloading:
Run `make hotreload_init` to initialize `watchman` based hot reloading. For more information, see:
https://gist.github.com/ryan-williams/f9a7fb5ceb17d44e0284892d5a923e5d

### Logging:
To inspect hot reloading logs, run the following commands:

```
logfile="$(ps aux | grep watchman | grep -o -- '--logfile=\S*' | awk -F= '{ print $2 }')"
tail -f "${logfile}"
```
