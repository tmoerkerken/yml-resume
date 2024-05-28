render:
	poetry run python scripts/render.py

parse:
	poetry run python scripts/parse.py

open:
	open "output/resume.pdf"

hotreload_init:
	watchman watch .
	watchman -- trigger . recompile "**/*.yml" "templates/**/*" -- "${PWD}/scripts/hot_reload.sh"
create: parse render