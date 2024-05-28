# Engineering Take-Home Exercise
## Running The Project
To use the script, run the following from your command line while within the project directory:

```
python check_drug_interactions.py <interactions.json> <input.txt> <output.txt> 
```

Where:
- ` check_drug_interactions.py ` is the script
- ` <interactions.json> ` is the provided interactions data
- ` <input.txt> ` is the text file with the drugs that need to be checked, organized the way the original README designated
- ` <output.txt> ` is the text file where the output of running the script will be stored, organized the way the original README designated

### Notes
Within the ` interactions.json ` file, the second object was:

```
  {
    "drugs": [
      "sildenafil", 
      "nitroglycerin"
    ],
    "severity": "contraindication",
    "description": "Phosphodiesterase-5 (PDE5) inhibitors may potentiate the hypotensive effect of organic nitrates."
  },
```
I've changed the `severity` from `contraindication` to `major` since `contraindication` was not designated within the original README.




