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

'detailed' output will give a bunch of JSON, formatted like so:
```
{
	# Date
	"2019.04.26": {
		# Session start (No jumps this session)
		"10:16:44": [],
		"11:48:31": [
			{
				# Jump time, and desetination
				"12:00:40": "Urlen"
			},
			{
				"12:01:44": "Perimeter"
			},
			...
		]
	},
	"2019.04.27": {
		...
	}
}
```
