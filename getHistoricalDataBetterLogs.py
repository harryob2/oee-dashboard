from java.util import Calendar
from historical import duration, sum, maximum
from java.text import SimpleDateFormat
import java.lang.System as System
import system
from com.inductiveautomation.ignition.client.util.gui import OutputConsole
from java.awt.event import ActionEvent
import sys

# Function to clear the Ignition console
def clear_ignition_console():
    console = OutputConsole.getInstance()
    action_event = ActionEvent(console, ActionEvent.ACTION_PERFORMED, "clear")
    console.actionPerformed(action_event)

# Function to parse 'cell', 'area', and 'machine' identifiers from a machine tag
def extract_info_from_tag(tag):
    parts = tag.split('/')
    if len(parts) >= 5:
        return parts[1], parts[2], parts[3]
    else:
        return "Unknown", "Unknown", "Unknown"
    
# Function to create a loading bar
def create_loading_bar(percentage, length=30):
    filled_length = int(length * percentage)
    return '#' * filled_length + '-' * (length - filled_length)

# Function to estimate time left
def estimate_time_left(start_time, total_days, days_processed):
    elapsed_time = (System.currentTimeMillis() - start_time) / 1000  # in seconds
    if days_processed > 0:
        seconds_per_day = elapsed_time / days_processed
        return (total_days - days_processed) * seconds_per_day
    return 0


machine_tags = [
    'limerick/baseplates/makino/makino 2/global tags/run',
    'limerick/baseplates/makino/makino 3/global tags/run',
    'limerick/baseplates/makino/makino 4/global tags/run',
    'limerick/baseplates/makino/makino 5/global tags/run',
    'limerick/baseplates/makino/makino 6/global tags/run',
    'limerick/baseplates/makino/makino 7/global tags/run',
    'limerick/baseplates/makino/makino 8/global tags/run',
    'limerick/baseplates/makino/makino 9/global tags/run',
    'limerick/baseplates/wheelabrator/wheelabrator 1/global tags/run',
    'limerick/foundry/apas/apas 1/global tags/run',
    'limerick/foundry/gate cut/gate cut 1/global tags/run',
    'limerick/foundry/pusher furnace/pusher furnace 1/global tags/run',
    'limerick/foundry/rollover/rollover 1/global tags/run',
    'limerick/foundry/rollover/rollover 2/global tags/run',
    'limerick/foundry/rollover/rollover 3/global tags/run',
    'limerick/foundry/rollover/rollover 4/global tags/run',
    'limerick/foundry/shell/shell 1/global tags/run',
    'limerick/foundry/vacuum furnace/vacuum furnace 2/global tags/run',
    'limerick/foundry/vacuum furnace/vacuum furnace 3/global tags/run',
    'limerick/foundry/wax injection/wax injection 1/global tags/run',
    'limerick/foundry/xray/xray 1/global tags/run',
    'limerick/hdp/inserts/inserts 1/global tags/run',
    'limerick/hdp/inserts/inserts 2/global tags/run',
    'limerick/hdp/inserts/inserts 3/global tags/run',
    'limerick/hdp/inserts/inserts 4/global tags/run',
    'limerick/hdp/inserts/inserts 5/global tags/run',
    'limerick/hdp/patellas/patellas 1/global tags/run',
    'limerick/pa/coating/coating 3/global tags/run',
    'limerick/pa/coating/coating 4/global tags/run',
    'limerick/pa/coating/coating 5/global tags/run',
    'limerick/pa/washing/washing 3/global tags/run',
    'limerick/pa/washing/washing 4/global tags/run',
    'limerick/pa/washing/washing 5/global tags/run',
    'limerick/packaging metals/illig/illig 2/global tags/run',
	'limerick/packaging metals/nelipak/nelipak 10/global tags/run',
    'limerick/packaging metals/nelipak/nelipak 7/global tags/run',
    'limerick/packaging metals/nelipak/nelipak 8/global tags/run',
    'limerick/packaging metals/nelipak/nelipak 9/global tags/run',
    'limerick/packaging plastics/blister pack auto/blister pack auto 1/global tags/run',
    'limerick/passivation/amsonic/amsonic 1/global tags/run',
    'limerick/tfa/bending/bending 1/global tags/run',
    'limerick/tfa/bending/bending 2/global tags/run',
    'limerick/tfa/blast/blast 1/global tags/run',
    'limerick/tfa/blast/blast 2/global tags/run',
    'limerick/tfa/blast/blast 3/global tags/run',
    'limerick/tfa/blast/blast 4/global tags/run',
    'limerick/tfa/blast/laser/global tags/run',
    'limerick/tfa/fic/fic 1/global tags/run',
    'limerick/tfa/gantry/gantry 1/global tags/run',
    'limerick/tfa/gantry/gantry 2/global tags/run',
    'limerick/tfa/gantry/gantry 3/global tags/run',
    'limerick/tfa/gantry/gantry 5/global tags/run',
    'limerick/tfa/gantry/gantry 6/global tags/run',
    'limerick/tfa/gantry/gantry 7/global tags/run',
    'limerick/tfa/gantry/gantry 8/global tags/run',
    'limerick/tfa/gantry/gantry 9/global tags/run',
    'limerick/tfa/gantry/gantry 10/global tags/run',
    'limerick/tfa/gantry/gantry 11/global tags/run',
    'limerick/tfa/gantry/gantry 12/global tags/run',
    'limerick/tfa/haas/haas 1/global tags/run',
    'limerick/tfa/haas/haas 10/global tags/run',
    'limerick/tfa/haas/haas 2/global tags/run',
    'limerick/tfa/haas/haas 3/global tags/run',
    'limerick/tfa/haas/haas 4/global tags/run',
    'limerick/tfa/haas/haas 6/global tags/run',
    'limerick/tfa/haas/haas 7/global tags/run',
    'limerick/tfa/haas/haas 8/global tags/run',
    'limerick/tfa/haas/haas 9/global tags/run',
    'limerick/tfa/linish/linish 1/global tags/run',
    'limerick/tfa/linish/linish 2/global tags/run',
    'limerick/tfa/linish/linish 3/global tags/run',
    'limerick/tfa/linish/linish 4/global tags/run',
    'limerick/tfa/linish/linish 5/global tags/run',
    'limerick/tfa/linish/linish 6/global tags/run',
    'limerick/tfa/polish/polish 1/global tags/run',
    'limerick/tfa/polish/polish 2/global tags/run',
    'limerick/tfa/polish/polish 3/global tags/run',
    'limerick/tfa/polish/polish 4/global tags/run',
    'limerick/tfa/polish/polish 5/global tags/run',
    'limerick/tfa/zeiss/laser/global tags/run',
    'limerick/tfa/zeiss/zeiss 1/global tags/run',
    'limerick/tfa/zeiss/zeiss 2/global tags/run',
    'limerick/tfa/zeiss/zeiss 3/global tags/run',
    'limerick/tfa/zeiss/zeiss 4/global tags/run',
    'limerick/tfa/zeiss/zeiss 5/global tags/run',
    'limerick/tfa/zeiss/zeiss 6/global tags/run',
    'limerick/tfa/zeiss/zeiss 7/global tags/run',
    'limerick/tfa/zeiss/zeiss 8/global tags/run',
    'limerick/tfa/zeiss/zeiss 9/global tags/run',
    'limerick/thk/chiron/chiron 1/global tags/run',
    'limerick/triathlon cementless/cellro/cellro 1/global tags/run',
    'limerick/triathlon cementless/haas/haas 1/global tags/run',
    'limerick/triathlon cementless/haas/haas 2/global tags/run',
    'limerick/triathlon cementless/haas/haas 3/global tags/run',
    'limerick/triathlon cementless/haas/haas 4/global tags/run',
    'limerick/triathlon cementless/haas/haas 5/global tags/run',
    'limerick/triathlon cementless/haas/haas 6/global tags/run',
    'limerick/triathlon cementless/laser/laser 1/global tags/run',
    'limerick/triathlon cementless/laser/laser 2/global tags/run',
    'limerick/triathlon cementless/linish/linish 2/global tags/run',
    'limerick/triathlon cementless/linish/linish 3/global tags/run',
    'limerick/triathlon cementless/linish/linish 4/global tags/run',
    'limerick/triathlon cementless/makino/makino 1/global tags/run',
    'limerick/triathlon cementless/makino/makino 2/global tags/run',
    'limerick/triathlon cementless/polish/polish 1/global tags/run',
    'limerick/triathlon cementless/polish/polish 3/global tags/run'
    ]

# Calculate yesterday's date
calendar = Calendar.getInstance()
calendar.add(Calendar.DATE, -1)
yesterday = calendar.getTime()

# Set the start date to August 14, 2023
startCalendar = Calendar.getInstance()
startCalendar.set(2023, Calendar.AUGUST, 14)  # Calendar.AUGUST is equivalent to 7

# Create a date formatter for displaying the date
date_formatter = SimpleDateFormat("yyyy-MM-dd")

# Calculate total number of days to process
total_days = (yesterday.getTime() - startCalendar.getTimeInMillis()) // (24 * 60 * 60 * 1000) + 1
days_processed = 0

# Start time for the whole process
start_time = System.currentTimeMillis()

# Loop over each day from the start date to yesterday
while startCalendar.getTimeInMillis() <= yesterday.getTime():

    # Calculate the progress
    progress_percentage = days_processed / float(total_days)
    loading_bar = create_loading_bar(progress_percentage)

    # Estimate time left
    time_left_seconds = estimate_time_left(start_time, total_days, days_processed)
    time_left = "Time left: {:.2f} minutes".format(time_left_seconds / 60)

    # Midnight of the current day in the loop
    loopDayStart = system.date.midnight(startCalendar.getTime())
    # Format the date for display
    formatted_date = date_formatter.format(loopDayStart)

    # One day after the start, which is the end of the current day in the loop
    loopDayEnd = system.date.addDays(loopDayStart, 1)

    # Now loop over each machine tag for the current day
    for machine_tag in machine_tags:

        # Extract cell, area, and machine info
        cell, area, machine = extract_info_from_tag(machine_tag)
        
        # Clear the line before printing
        sys.stdout.write('\r' + ' ' * 80)
        sys.stdout.flush()
        # Print the current status with cell, area, machine, and date
        sys.stdout.write('\rDate: {}\nCell: {}\nArea: {}\nMachine: {}\nProgress: {} {:.1f}%\n{}\n'.format(
            formatted_date, cell, area, machine, loading_bar, progress_percentage * 100, time_left))
        sys.stdout.flush()

        # Replace run with idle
        machine_tag_idle = machine_tag.replace("run", "idle")

        # Replace run with fault
        machine_tag_fault = machine_tag.replace("run", "fault")

        # Replace run with dhr recorded
        machine_tag_dhr_recorded = machine_tag.replace('run', 'dhr recorded')
        
        # Replace run with target per day
        machine_tag_target_per_day = machine_tag.replace('run', 'target per day')

        # Calculate run, idle, and fault minutes
        runMinutes, idleMinutes, faultMinutes = duration(machine_tag, loopDayStart, loopDayEnd, 1) // 60, duration(machine_tag_idle, loopDayStart, loopDayEnd, 1) // 60, duration(machine_tag_fault, loopDayStart, loopDayEnd, 1) // 60
    
        # Calculate run, idle, and fault time %
        runTimePercent, idleTimePercent, faultTimePercent  = round(runMinutes*100 / 1440, 14), round(idleMinutes*100 / 1440, 14), round(faultMinutes*100 / 1440, 14)

        # Calculate output
        output = sum(machine_tag_dhr_recorded, loopDayStart, loopDayEnd)
        
        # Calculate target
        target = maximum(machine_tag_target_per_day, loopDayStart, loopDayEnd)

        # Calculate performance
        performance = round(output*100 / target, 14) if target != 0 else 0
    
        # Prepare SQL query
        sql_query = "INSERT INTO analysis_connect.oee_data (cell, area, machine, date, run_minutes, run_time_percent, idle_minutes, idle_time_percent, fault_minutes, fault_time_percent, output, target, performance) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    
        # Attempt to insert data into the database and log the outcome
        try:
            affectedRows = system.db.runPrepUpdate(sql_query, [cell, area, machine, loopDayStart, runMinutes, runTimePercent, idleMinutes, idleTimePercent, faultMinutes, faultTimePercent, output, target, performance], "PowerBI2")
        except Exception as e:
            print("Error inserting data for {}: {}".format(machine_tag, e))


    # Move to the next day
    days_processed += 1
    startCalendar.add(Calendar.DATE, 1)
    print('\n')  # Move to the next line for clarity in the terminal

print("\nAll runtimes added to MariaDB.")
