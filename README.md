# ignition-runtime-script

A collection of scripts for getting OEE data from ignition and saving it to MariaDB. 

`runtime.py` and `getHistoricalData.py` are the 2 important scripts.

`runtime.py` runs everyday at 3:30am to update the table. `getHistoricalData.py` was used to populate the table with historical data, which went as far back as the 14th of August 2023, around the time the plant reopened from the 2 week shutdown.

The other scripts were used by myself to analyze and understand the data.

The table with all of this data in MariaDB looks like this:

| cell                | area             | machine          | date       | run_minutes | run_time_percent | idle_minutes | idle_time_percent | fault_minutes | fault_time_percent | performance | output | target | id   |
|---------------------|------------------|------------------|------------|-------------|------------------|--------------|-------------------|---------------|--------------------|-------------|--------|--------|------|
| baseplates          | makino           | makino 8         | 2023-09-22 | 1279.00     | 88.0             | 160          | 11.00             | 0             | 0.00               | 87.0000     | 193    | 220    | 4141 |
| baseplates          | makino           | makino 7         | 2023-09-22 | 1308.00     | 90.0             | 131          | 9.00              | 0             | 0.00               | 92.0000     | 203    | 220    | 4140 |
| baseplates          | makino           | makino 6         | 2023-09-22 | 1358.00     | 94.0             | 81           | 5.00              | 0             | 0.00               | 133.0000    | 253    | 190    | 4139 |
| baseplates          | makino           | makino 5         | 2023-09-22 | 1333.00     | 92.0             | 106          | 7.00              | 0             | 0.00               | 81.0000     | 179    | 220    | 4138 |
| ...                 | ...              | ...              | ...        | ...         | ...              | ...          | ...               | ...           | ...                | ...         | ...    | ...    | ...  |
