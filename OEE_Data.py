import system
from java.util import Calendar
from historical import duration, sum, maximum

# Function to parse 'cell', 'area', and 'machine' identifiers from a machine tag
def extract_info_from_tag(tag):
    parts = tag.split('/')
    if len(parts) >= 5:
        return parts[1], parts[2], parts[3]
    else:
        return "Unknown", "Unknown", "Unknown"

# Calculate start and end times
calendar = Calendar.getInstance()
calendar.add(Calendar.DATE, -1)
yesterday = calendar.getTime()
startTime = system.date.midnight(yesterday)
endTime = system.date.addDays(startTime, 1)

machine_tags = [
    '[Main]limerick/baseplates/makino/makino 2/global tags/run',
    '[Main]limerick/baseplates/makino/makino 3/global tags/run',
    '[Main]limerick/baseplates/makino/makino 4/global tags/run',
    '[Main]limerick/baseplates/makino/makino 5/global tags/run',
    '[Main]limerick/baseplates/makino/makino 6/global tags/run',
    '[Main]limerick/baseplates/makino/makino 7/global tags/run',
    '[Main]limerick/baseplates/makino/makino 8/global tags/run',
    '[Main]limerick/baseplates/makino/makino 9/global tags/run',
    '[Main]limerick/baseplates/wheelabrator/wheelabrator 1/global tags/run',
    '[Main]limerick/foundry/apas/apas 1/global tags/run',
    '[Main]limerick/foundry/gate cut/gate cut 1/global tags/run',
    '[Main]limerick/foundry/pusher furnace/pusher furnace 1/global tags/run',
    '[Main]limerick/foundry/rollover/rollover 1/global tags/run',
    '[Main]limerick/foundry/rollover/rollover 2/global tags/run',
    '[Main]limerick/foundry/rollover/rollover 3/global tags/run',
    '[Main]limerick/foundry/rollover/rollover 4/global tags/run',
    '[Main]limerick/foundry/shell/shell 1/global tags/run',
    '[Main]limerick/foundry/vacuum furnace/vacuum furnace 2/global tags/run',
    '[Main]limerick/foundry/vacuum furnace/vacuum furnace 3/global tags/run',
    '[Main]limerick/foundry/wax injection/wax injection 1/global tags/run',
    '[Main]limerick/foundry/xray/xray 1/global tags/run',
    '[Main]limerick/hdp/inserts/inserts 1/global tags/run',
    '[Main]limerick/hdp/inserts/inserts 2/global tags/run',
    '[Main]limerick/hdp/inserts/inserts 3/global tags/run',
    '[Main]limerick/hdp/inserts/inserts 4/global tags/run',
    '[Main]limerick/hdp/inserts/inserts 5/global tags/run',
    '[Main]limerick/hdp/patellas/patellas 1/global tags/run',
    '[Main]limerick/pa/coating/coating 3/global tags/run',
    '[Main]limerick/pa/coating/coating 4/global tags/run',
    '[Main]limerick/pa/coating/coating 5/global tags/run',
    '[Main]limerick/pa/washing/washing 3/global tags/run',
    '[Main]limerick/pa/washing/washing 4/global tags/run',
    '[Main]limerick/pa/washing/washing 5/global tags/run',
    '[Main]limerick/packaging metals/illig/illig 2/global tags/run',
    '[Main]limerick/packaging metals/nelipak/nelipak 10/global tags/run',
    '[Main]limerick/packaging metals/nelipak/nelipak 7/global tags/run',
    '[Main]limerick/packaging metals/nelipak/nelipak 8/global tags/run',
    '[Main]limerick/packaging metals/nelipak/nelipak 9/global tags/run',
    '[Main]limerick/packaging plastics/blister pack auto/blister pack auto 1/global tags/run',
    '[Main]limerick/passivation/amsonic/amsonic 1/global tags/run',
    '[Main]limerick/tfa/bending/bending 1/global tags/run',
    '[Main]limerick/tfa/bending/bending 2/global tags/run',
    '[Main]limerick/tfa/blast/blast 1/global tags/run',
    '[Main]limerick/tfa/blast/blast 2/global tags/run',
    '[Main]limerick/tfa/blast/blast 3/global tags/run',
    '[Main]limerick/tfa/blast/blast 4/global tags/run',
    '[Main]limerick/tfa/blast/laser/global tags/run',
    '[Main]limerick/tfa/fic/fic 1/global tags/run',
    '[Main]limerick/tfa/gantry/gantry 1/global tags/run',
    '[Main]limerick/tfa/gantry/gantry 2/global tags/run',
    '[Main]limerick/tfa/gantry/gantry 3/global tags/run',
    '[Main]limerick/tfa/gantry/gantry 5/global tags/run',
    '[Main]limerick/tfa/gantry/gantry 6/global tags/run',
    '[Main]limerick/tfa/gantry/gantry 7/global tags/run',
    '[Main]limerick/tfa/gantry/gantry 8/global tags/run',
    '[Main]limerick/tfa/gantry/gantry 9/global tags/run',
    '[Main]limerick/tfa/gantry/gantry 10/global tags/run',
    '[Main]limerick/tfa/gantry/gantry 11/global tags/run',
    '[Main]limerick/tfa/gantry/gantry 12/global tags/run',
    '[Main]limerick/tfa/haas/haas 1/global tags/run',
    '[Main]limerick/tfa/haas/haas 10/global tags/run',
    '[Main]limerick/tfa/haas/haas 2/global tags/run',
    '[Main]limerick/tfa/haas/haas 3/global tags/run',
    '[Main]limerick/tfa/haas/haas 4/global tags/run',
    '[Main]limerick/tfa/haas/haas 6/global tags/run',
    '[Main]limerick/tfa/haas/haas 7/global tags/run',
    '[Main]limerick/tfa/haas/haas 8/global tags/run',
    '[Main]limerick/tfa/haas/haas 9/global tags/run',
    '[Main]limerick/tfa/linish/linish 1/global tags/run',
    '[Main]limerick/tfa/linish/linish 2/global tags/run',
    '[Main]limerick/tfa/linish/linish 3/global tags/run',
    '[Main]limerick/tfa/linish/linish 4/global tags/run',
    '[Main]limerick/tfa/linish/linish 5/global tags/run',
    '[Main]limerick/tfa/linish/linish 6/global tags/run',
    '[Main]limerick/tfa/polish/polish 1/global tags/run',
    '[Main]limerick/tfa/polish/polish 2/global tags/run',
    '[Main]limerick/tfa/polish/polish 3/global tags/run',
    '[Main]limerick/tfa/polish/polish 4/global tags/run',
    '[Main]limerick/tfa/polish/polish 5/global tags/run',
    '[Main]limerick/tfa/zeiss/laser/global tags/run',
    '[Main]limerick/tfa/zeiss/zeiss 1/global tags/run',
    '[Main]limerick/tfa/zeiss/zeiss 2/global tags/run',
    '[Main]limerick/tfa/zeiss/zeiss 3/global tags/run',
    '[Main]limerick/tfa/zeiss/zeiss 4/global tags/run',
    '[Main]limerick/tfa/zeiss/zeiss 5/global tags/run',
    '[Main]limerick/tfa/zeiss/zeiss 6/global tags/run',
    '[Main]limerick/tfa/zeiss/zeiss 7/global tags/run',
    '[Main]limerick/tfa/zeiss/zeiss 8/global tags/run',
    '[Main]limerick/tfa/zeiss/zeiss 9/global tags/run',
    '[Main]limerick/thk/chiron/chiron 1/global tags/run',
    '[Main]limerick/triathlon cementless/cellro/cellro 1/global tags/run',
    '[Main]limerick/triathlon cementless/haas/haas 1/global tags/run',
    '[Main]limerick/triathlon cementless/haas/haas 2/global tags/run',
    '[Main]limerick/triathlon cementless/haas/haas 3/global tags/run',
    '[Main]limerick/triathlon cementless/haas/haas 4/global tags/run',
    '[Main]limerick/triathlon cementless/haas/haas 5/global tags/run',
    '[Main]limerick/triathlon cementless/haas/haas 6/global tags/run',
    '[Main]limerick/triathlon cementless/laser/laser 1/global tags/run',
    '[Main]limerick/triathlon cementless/laser/laser 2/global tags/run',
    '[Main]limerick/triathlon cementless/linish/linish 2/global tags/run',
    '[Main]limerick/triathlon cementless/linish/linish 3/global tags/run',
    '[Main]limerick/triathlon cementless/linish/linish 4/global tags/run',
    '[Main]limerick/triathlon cementless/makino/makino 1/global tags/run',
    '[Main]limerick/triathlon cementless/makino/makino 2/global tags/run',
    '[Main]limerick/triathlon cementless/polish/polish 1/global tags/run',
    '[Main]limerick/triathlon cementless/polish/polish 3/global tags/run'
    ]

for machine_tag in machine_tags:
    # Replace run with idle
    machine_tag_idle = machine_tag.replace("run", "idle")

    # Replace run with fault
    machine_tag_fault = machine_tag.replace("run", "fault")

    # Replace run with dhr recorded
    machine_tag_dhr_recorded = machine_tag.replace('run', 'dhr recorded')
    
    # Replace run with target per day
    machine_tag_target_per_day = machine_tag.replace('run', 'target per day')

    # Calculate run, idle, and fault minutes
    runMinutes, idleMinutes, faultMinutes = duration(machine_tag, startTime, endTime, 1) // 60, duration(machine_tag_idle, startTime, endTime, 1) // 60, duration(machine_tag_fault, startTime, endTime, 1) // 60

    # Calculate run, idle, and fault time %
    runTimePercent, idleTimePercent, faultTimePercent  = round(float(runMinutes) / 1440, 4), round(float(idleMinutes) / 1440, 4), round(float(faultMinutes) / 1440, 4)

    # Calculate output
    # Must be converted to float, because it is returned in a weird format
    output = float(sum(machine_tag_dhr_recorded, startTime, endTime))
    
    # Calculate target
    target = float(maximum(machine_tag_target_per_day, startTime, endTime))

    # Calculate adjusted target
    adjustedTarget = round(target * runTimePercent, 4)

    # Calculate performance
    if adjustedTarget != 0:
        performance = output / adjustedTarget
    else:
        performance = 0

    # Calculate OEE
    oee = runTimePercent * performance

    # Extract cell, area, and machine info
    cell, area, machine = extract_info_from_tag(machine_tag)

    # Prepare SQL query
    sql_query = "INSERT INTO analysis_connect.oee_data (cell, area, machine, date, run_minutes, run_time_percent, idle_minutes, idle_time_percent, fault_minutes, fault_time_percent, output, target, performance, oee, adjusted_target) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

    # Attempt to insert data into the database and log the outcome
    try:
        affectedRows = system.db.runPrepUpdate(sql_query, [cell, area, machine, startTime, runMinutes, runTimePercent, idleMinutes, idleTimePercent, faultMinutes, faultTimePercent, output, target, performance, oee, adjustedTarget], "PowerBI2")
    except Exception as e:
        print("Error inserting data for {}: {}".format(machine_tag, e))

# Update timestamp
truncate_query = "TRUNCATE TABLE analysis_connect.oee_update_timestamp"
system.db.runUpdateQuery(truncate_query, "PowerBI2")
insert_query = "INSERT INTO analysis_connect.oee_update_timestamp (timestamp) VALUES (?)"
system.db.runPrepUpdate(insert_query, [system.date.now()], "PowerBI2")
print("Updated OEE Data successfully.")