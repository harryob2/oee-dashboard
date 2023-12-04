# OEE Dashboard Guide

## Overview

This document provides an overview of the OEE Dashboard, detailing how live data is transferred from Ignition to our On-Premises MariaDB server and then to the Power BI dashboard.

## Background

- **Development Date**: Late November 2023
- **Team**:
  - **Lead Developer**: Harry O’Brien
  - **Support and Guidance**: David Higgins
  - **Initial Design and Concept**: Ante Tolusic
  - **Project Lead**: Ante Tolusic

## What is OEE?

OEE (Overall Equipment Effectiveness) is a measure of manufacturing productivity and is calculated as follows:

$$\text{OEE} = \text{Availability} \times \text{Performance} \times \text{Quality}$$

Where:

$$\text{Availability} = \frac{\text{Run Time of Machine}}{\text{Total Available Time}}$$

$$\text{Performance} = \frac{\text{Total Output}}{\text{Target Output}}$$

$$\text{Quality} = \frac{\text{Parts Started}}{\text{Parts Finished}}$$
**Note** Quality is currently set to 1 as it's not measured, however this function shows how it should ideally be measured. 


## Data Flow

Data is sent from Ignition to the MariaDB server every 24 hours, where it's stored in a table. The Power BI dashboard connects to this database and refreshes every 24 hours as well.

### Accessing the Data Script in Ignition

1. Open the Ignition Designer Launcher desktop app.
2. Navigate to `Gateway Events` under `Scripting`.
3. Find the `OEE Data` script under `Scheduled`.

### OEE Data Script Details

- **Execution Time**: Runs daily at 3:20 AM.
- **Functions Used**: From the `historical` script in Ignition - `duration`, `sum`, and `max`.
- **Data Points Collected**:
  - `cell`, `area`, `machine`: Extracted from the tag name using `extract_info_from_tag()` function.
  - `date`: Set to `Today’s Date - 1`.
  - `run_minutes`, `idle_minutes`, `fault_minutes`: Calculated using `duration()` function.
  - `run_time_percent`, `idle_time_percent`, `fault_time_percent`: Calculated as `Data Point / 1440`.
  - `output`: Derived using `sum()` function on the `dhr_recorded` tag.
  - `target`: Similar to `output`, but using the `target` tag.
  - `performance`: Calculated as `output / target`.
  - `oee`: Calculated as `run_time_percent * performance`.
- **Additional Column**:
  - `id`: Auto-incremented, requires no manual input.
