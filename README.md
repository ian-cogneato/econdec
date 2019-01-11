# Economic Decision Study

## Reversal Fix
`0.reversal_fix.ipynb`

Describes and applies the fix for Study-2 Reversal Calculations in early subjects.

## Raw EyeLink Data Extraction

Data should already be transferred from the EyeLink computer into `../sourcedata/.staging/`.

1. `TrialReport`
   1. `Analysis` => `Reports` => `Trial Report`
2. `Choice`
   1. Pre-configure Interest Period according to: {choice.yml}
      1. **this file still needs to be written**
   2. `Analysis` => `Reports` => `InterestArea Report`
3. `StockOutcome`
   1. Pre-configure Interest Period according to: {stock-outcome.yml}
      1. **this file still needs to be written**
   2. `Analysis` => `Reports` => `InterestArea Report`

## Individual Data Extraction

Data Being Pulled from Display Computer:

- Use USB port farthest from wall; the right when looking directly at the computer

Open the folder “Kylie” on desktop: `Kylie/RunThis2018EconDecEyeTracking/.`

Then select folder for the participant range for which you want to backup the data for (inclusive): `./iEconDec_374_397/`

Need to backup from BOTH:

- `./results/_ssid_/*`
- `./runtime/dataviewer/_ssid_/*`

On the external

- `2017_2018integration/RunThisED3backup_ResultsWork/iEconDec3/.`
   - `./results/`
   - `./runtime/dataviewer/`

and then save to the corresponding folder (i.e. results saved to results)

Note: if you cannot find the ss files on the Display Computer, then ask Dr. Joe Schmidt how to pull from the Host Computer

Once these files are copied to `/r/experiments/econdec/sourcedata/.staging`:

`raw2bids.py` module then finds all the new subjects' data files and copies them into `../sourcedata/ds3/` under `sub-xxx` directories.
Converts `RESULTS_FILE.txt` into `sub-xxx_task-eye_beh.csv`.

## EconDec-1 & EconDec-2 Merge

`1.econdec-12_merge.ipynb`

## EconDec-3 Conversion

`1.econdec-3_convert.ipynb`

## Realign Columns and Homogenize DataTypes

`2.realign_homogenize_all.ipynb`

## Import Gaze Data

`3.gaze-data_import.ipynb`

## Binarize, Median Split, Normalize Data

`4.trial_bin_split_znorm.ipynb`

## Merge into Subject-Level Transformation

`5.subject_level_merge.ipynb`
