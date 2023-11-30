# generate_script
Python script command generator for stambia

Usage:

usage: generate_command.py [-h] [-c COMMAND] [-f FROMDATE] [-t TODATE] [-b BU] [-s STEP] [-w WAIT]

options:
  -h, --help            show this help message and exit

  -c COMMAND, --command COMMAND The prefix command to launch

  -f FROMDATE, --fromdate FROMDATE From date dd/mm/yyyy format

  -t TODATE, --todate TODATE To date dd/mm/yyyy format

  -b BU, --bu BU        Business unit

  -s STEP, --step STEP  Step in days

  -w WAIT, --wait WAIT  Wait in minutes between each command

Example:

./startdelivery.sh -name FIT-VSTOCK.ST-GCP.GEN -var '~/cod_flux' reprise_hmv -var '~/num_bu' 003 -var '~/from' 01/01/2023 -var '~/to' 01/01/2024

