# eve-travel-analyzer
Quick and dirty script to parse EVE Online local chat logs for jumps to new systems and output JSON


# Usage
(Requires Python 3)

Edit the `listeners` line at the top of the script to your character name. You can also provide a list of names.

Run the script, passing your chat logs as a list of arguments.

On (most) Linux systems, you can do so with:
```
python analyzer.py /path/to/EVE/logs/Chatlogs/Local*
```

By default it will use the 'simple' output format (see below.) You can specify other formats with `--output-format`. Call the script with `-h` to see available formats.


Do whatever you want with the output:
```
python analyzer.py Local* > results
```

'simple' output:
```
2019.11.25      20:50:29        Ashab
2019.11.25      20:51:51        Madirmilire
2019.11.25      20:53:12        Niarja
2019.11.25      20:54:28        Kaaputenen
...
```

'totals' output:
```
2019.11.22      320
2019.11.23      206
2019.11.24      281
2019.11.25      247
...
```
