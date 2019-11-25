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

Do whatever you want with the output:
```
python analyzer.py Local* > results
```

The output is a simple list of tab-separated strings
```
2019.11.25      20:50:29        Ashab
2019.11.25      20:51:51        Madirmilire
2019.11.25      20:53:12        Niarja
2019.11.25      20:54:28        Kaaputenen
2019.11.25      20:56:03        Inaro
2019.11.25      20:57:35        Sirppala
2019.11.25      20:58:53        Urlen
2019.11.25      20:59:54        Perimeter
```
