# Description
Data from a `low-density polyethylene` production process. There are 14 process variables and 5 quality variables.

# Dataset
This is simulated data. Two tubular reactors are connected in series. The first 50 observations are from common-cause (normal) operation, while the last 4 show a process fault developing: the impurity level in the ethylene feed in both zones is increasing. The dataset consists of:

- `Tin` : inlet temperature to zone 1 of the reactor [K]
- `Tmax1` : maximum temperature along zone 1 [K]
- `Tout1` : outlet temperature from zone 1 [K]
- `Tmax2` : maximum temperature along zone 2 [K]
- `Tout2` : outlet temperature from zone 2 [K]
- `Tcin1` : temperature of inlet coolant to zone [K]
- `Tcin2` : temperature of inlet coolant to zone 2 [K]
- `z1` : percentage along zone 1 where Tmax1 occurs [%]
- `z2` : percentage along zone 2 where Tmax2 occurs [%]
- `Fi1` : flow rate of initiators to zone 1 [g/s]
- `Fi2` : flow rate of initiators to zone 2 [g/s]
- `Fs1` : flow rate of solvent to zone 1 [% of ethylene]
- `Fs2` : flow rate of solvent to zone 2 [% of ethylene]
- `Press` : pressure in the reactor [atm]
- `Conv` : quality variable: cumulative conversion
- `Mn` : quality variable: number average molecular weight
- `Mw` : quality variable: weight average molecular weight
- `LCB` : quality variable: long chain branching per 1000 C atoms
- `SCB` : quality variable: short chain branching per 1000 C atoms

# Preparation
Python version: 3.6 

# License
Please follow [this]("https://creativecommons.org/licenses/by-sa/4.0/") for License information