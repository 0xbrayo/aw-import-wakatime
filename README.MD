# Wakatime importer for activitywatch

This script imports data from the Wakatime heartbeats json file into activitywatch.
You can download your Wakatime data from the [Wakatime website](https://wakatime.com/settings/account). Make sure to select the "Heartbeats" option. 

## Usage
This script replicates how wakatime tracks time but in activitywatch. It merges all heartbeats within 5 minutes of each other into one event. It uses a naive approach to throttling the events sent to avoid overloading the activitywatch server. This can be improved in the future.