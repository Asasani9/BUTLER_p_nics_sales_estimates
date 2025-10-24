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
Sticking with the `r_gva` example that would be:
```
    username = "glevines"
    workflow_name = "gva:kgtn"
    notebook_name = "gva_updater:x4bf"
```
**Note**: The URL format for a notebook https://redivis.com/workflows/kgtn-7vy84cvbr/notebooks/x4bf-9jy3tv2tp is the easiest way to grab the 'qualified reference' information required after the `:` above. This is the URL grabbed from the `gva` workflow with the `gva_updater` notebook selected in the workflow's lefthand tree diagram.

4. Lastly, set the time that the notebook should run in the [`dataset-butler.yml`](.github/workflows/dataset-butler.yml) file. If you don't wanna think too hard about crontab time formatting here's a [helpful resource](https://crontab.guru/).
```
  # schedule: # Uncomment to enable scheduled runs
    # - cron: '0 10 * * *' # Uncomment to enable scheduled runs
```
5. Test that it works by clicking the `Actions` button above on the GitHub page. Click `Python application` in the left rail and then click the gray `Run workflow` button in the blue highlighted area.
