# Fetching and storing office location data

This repo contains a collection of scripts that fetches, cleans and saves data on searchable private provider offices (providers of the labor market program "Rusta och Matcha") on the Swedish Public Employment Service [website](https://arbetsformedlingen.se/for-arbetssokande/extra-stod/stod-a-o/rusta-och-matcha/sok-leverantor-inom-rusta-och-matcha/).

The data is fetched and stored automatically under `/data/raw` before being cleaned and combined under `/data/clean`

## How to use

The program is run by executing `run.sh` (as executable):
```
# Make file executable
chmod +x run.sh

# Execute program
./run.sh
```
`run.sh` checks Python and pip versions, checks/installs necessary dependencies as stated in `requirements.txt` and runs `main.py`, which in turn imports modules from `/scripts`

### Example raw data:
```
[
    {
        "total_count": 1070,
        "leverantorer": [
            {
                "id": 10072088,
                "namn": "Trim tab AB",
                "rating": "3",
                "nyval_tillatet": false,
                "adresser": [
                    {
                        "adressid": "331616",
                        "adressrad": "Odinsgatan 13",
                        "postnummer": "41103",
                        "postort": "Göteborg",
                        "koordinater": {
                            "latitud": "57.70879",
                            "longitud": "11.981139",
                            "north": "6400296",
                            "east": "320147"
                        }
                    }
                ]
            },
```
### Example clean data:

|id|namn|rating|nyval_tillatet|adressid|adressrad|postnummer|postort|koordinater.latitud|koordinater.longitud|koordinater.north|koordinater.east|observerad_datum|
| ------------- |:-------------:| ------------- |:-------------:| ------------- |:-------------:| ------------- |:-------------:| ------------- |:-------------:| ------------- |:-------------:| ------------- |
|10072088|Trim tab AB|3|False|331616|Odinsgatan 13|41103|Göteborg|57.70879|11.981139|6400296|320147|2025-02-19|
|10072090|Jobbmaskinen DistansMatchning AB|3|False|331636|Lisa Sass gata 1|42253|Hisings Backa|57.75021|11.989525|6404883|320851|2025-02-19|
|10072095|Cleverex Jobbförmedling & Utbildning AB|3|False|331656|Radiatorvägen 15|70227|Örebro|59.25923|15.179742|6568932|510249|2025-02-19|
