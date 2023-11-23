# ignition-runtime-script
A script that will get the total runtime of each machine in a 24hr period and send it straight to MariaDB. 

runtime.py and getHistoricalData.py are the 2 important scripts. 

runtime.py runs everyday at 3:30am to update the table. getHistoricalData.py was used to populate the table with historical data, which went as far back as the 14th of August 2023, around the time the plant reopened from the 2 week shutdown. 

The other scripts were used by myself to analyze and understand the data. 

The table with all of this data looks like this:
cell                |area             |machine            |date      |run_minutes|run_time_percent|idle_minutes|idle_time_percent|fault_minutes|fault_time_percent|performance|output|target|id  
--------------------+-----------------+-------------------+----------+-----------+----------------+------------+-----------------+-------------+------------------+-----------+------+------+----
baseplates          |makino           |makino 8           |2023-09-22|    1279.00|            88.0|         160|            11.00|            0|              0.00|    87.0000|   193|   220|4141
baseplates          |makino           |makino 7           |2023-09-22|    1308.00|            90.0|         131|             9.00|            0|              0.00|    92.0000|   203|   220|4140
baseplates          |makino           |makino 6           |2023-09-22|    1358.00|            94.0|          81|             5.00|            0|              0.00|   133.0000|   253|   190|4139
baseplates          |makino           |makino 5           |2023-09-22|    1333.00|            92.0|         106|             7.00|            0|              0.00|    81.0000|   179|   220|4138
baseplates          |makino           |makino 4           |2023-09-22|    1383.00|            96.0|          56|             3.00|            0|              0.00|   120.0000|   229|   190|4137
baseplates          |makino           |makino 3           |2023-09-22|    1309.00|            90.0|         124|             8.00|            0|              0.00|    86.0000|   190|   220|4136
baseplates          |makino           |makino 2           |2023-09-22|       0.00|             0.0|        1440|           100.00|            0|              0.00|     9.0000|    17|   175|4135
triathlon cementless|polish           |polish 3           |2023-09-21|    1210.00|            84.0|         218|            15.00|           10|              0.00|    92.0000|   311|   336|4134
triathlon cementless|polish           |polish 1           |2023-09-21|    1161.00|            80.0|         121|             8.00|          156|             10.00|    91.0000|   309|   336|4133
triathlon cementless|makino           |makino 2           |2023-09-21|    1121.00|            77.0|         318|            22.00|            0|              0.00|    74.0000|    63|    85|4132
triathlon cementless|makino           |makino 1           |2023-09-21|     998.00|            69.0|         393|            27.00|            2|              0.00|    69.0000|    59|    85|4131
triathlon cementless|linish           |linish 4           |2023-09-21|     396.00|            27.0|        1044|            72.00|            0|              0.00|    23.0000|    78|   336|4130
triathlon cementless|linish           |linish 3           |2023-09-21|     702.00|            48.0|         736|            51.00|            0|              0.00|    28.0000|    96|   336|4129
triathlon cementless|linish           |linish 2           |2023-09-21|     625.00|            43.0|         814|            56.00|            0|              0.00|    38.0000|   128|   336|4128
triathlon cementless|laser            |laser 2            |2023-09-21|     795.00|            55.0|         644|            44.00|            0|              0.00|    80.0000|  2420|  3000|4127
triathlon cementless|laser            |laser 1            |2023-09-21|     239.00|            16.0|        1199|            83.00|            1|              0.00|    23.0000|   692|  3000|4126