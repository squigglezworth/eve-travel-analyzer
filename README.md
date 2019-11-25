# eve-travel-analyzer
Quick and dirty script to parse EVE Online local chat logs for jumps to new systems and output JSON


# Usage
(Requires Python 3)

Edit the `listeners` line at the top of the script to your character name. You can also provide a list of names.

Run the script, passing your chat logs as a list of arguments to the script.

On (most) Linux systems, you can do so with:
```
python analyzer.py /path/to/EVE/logs/Chatlogs/Local*
```

Do whatever you want with the JSON output:
```
python analyzer.py Local* > results.json
```
