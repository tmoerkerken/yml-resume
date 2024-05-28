Hot reload:
https://gist.github.com/ryan-williams/f9a7fb5ceb17d44e0284892d5a923e5d

Logging:
```
logfile="$(ps aux | grep watchman | grep -o -- '--logfile=\S*' | awk -F= '{ print $2 }')"
tail -f "${logfile}"
```

Rename example_resume.yml to resume.yml and run `make create`