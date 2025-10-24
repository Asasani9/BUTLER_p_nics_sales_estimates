# About
Redivis doesn't have the concept of scheduling notebooks to run. This is a bummer for datasets that we want to update with any kind of frequency. It does, however, let you run a notebook via its API. That's what this program does, and it can be used on any notebook.

In the future, whenever Redivis implements scheduled runs, we can hopefully discontinue these — though we'll still need to update the dataset pages in WordPress 

Coming soon: Once WordPress updating is available via API, this program will do that too — Nass is working on it.

## Usage
1. Fork this repo.
2. Rename the repo following this convention `BUTLER_[name_of_dataset]`. So for the `r_gva` dataset it's `BUTLER_r_gva`.
3. Change the following variables in the [`get.py`](get.py) file. 
```
username = "[YOUR_USERNAME]"  # Replace with your Redivis username
workflow_name = "[WORKFLOW_NAME]"  # Replace with your workflow name
notebook_name = "[NOTEBOOK_NAME]"  # Replace with your notebook name
```
4. Lastly, set the time that the notebook should run in the [`dataset-butler.yml`](.github/workflows/dataset-butler.yml) file. If you don't wanna think too hard about crontab time formatting here's a [helpful resource](https://crontab.guru/).
```
# This schedules the workflow to run automatically
schedule:
# cron format is: MINUTE HOUR DAY-OF-MONTH MONTH DAY-OF-WEEK
# This runs at 10:00 UTC, which is 6:00 AM ET (during Daylight Saving)
# or 5:00 AM ET (during Standard Time). GitHub Actions uses UTC time.
# For 6 AM ET year-round, you'd typically use 11:00 UTC.
# 11:00 UTC = 6 AM EST (UTC-5) and 7 AM EDT (UTC-4). Let's stick with 10:00 UTC for 6 AM EDT.
- cron: '0 10 * * *'
```