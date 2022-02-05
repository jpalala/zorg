# Zorg

Basically some python scripts to parse domain in a directory `~/.zorg.d`

## Usage 

`python domains.py google.com`

## Files


`domains.py` looks up via argument if it doesnt then it will try to get some details if found in your `.zorg.d/list.domains.yaml` file

See `examples/` for how your `list.domains.yaml` should look like

## TODO

Handle errors. The script `domains.py` was designed to be simple and  does not handle file not found or other parsing issues  as of now.

## Future plans

1. Check domain IP via ping if its not in list.

2. Show notes about a server in `.zorg.d/servers/ip-hash.md`



