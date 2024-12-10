# T1D Change Point Detection Benchmark
An open source benchmark for semi-supervised change point detection of type 1 diabetic meals from continuous glucose monitor time series data. Originally created to present to PyData Global 2024 in association with [sktime](https://www.sktime.net/en/stable/) and [skchange](https://skchange.readthedocs.io/en/latest/).

**NOTE: The benchmark is still under heavy development and is subject to change. Consider its current state as alpha v.0.0.1**


# Dataset Metadata

| property    | value                                                                         |
|-------------|-------------------------------------------------------------------------------|
| name        | T1D Semi-Supervised Change Point Detection Benchmark                          |
| url         | https://github.com/Blood-Glucose-Control/t1d-change-point-detection-benchmark |
| sameAs      | https://github.com/Blood-Glucose-Control/t1d-change-point-detection-benchmark |
| description |                                                                               |
| citation    |                                                                               |
| license     |                                                                               |



# Data Directory Structure

## Overview
This repository contains three main data directories: `raw`, `processed`, and `obfuscated`, each serving different purposes in the data pipeline.

## Directory Details
### 1. data/raw

Contains data generated directly from `simglucose` simulator.

**Characteristics:**
- Duration per patient: 90 days
- 30 patients (10 adults, 10 children and 10 adolescents)
- Source: Jinyu Xie. Simglucose v0.2.1 (2018)
- Reference: https://github.com/jxx123/simglucose

### 2. data/processed

Contains processed data derived from `data/raw`.

#### File Naming Convention

Pattern: `{patientNum}_{cgmName}_{insulinPumpName}_{startDate}_{endDate}.csv`

Example: `ado001_Dexcom_Cozmo_2024-02-01_2024-04-30`

| Component       | Description                                                      | Example                   |
|-----------------|------------------------------------------------------------------|---------------------------|
| patientNum      | Concatenation of first 3 and last 3 characters from patient name | `ado001` (adolescent#001) |
| cgmName         | CGM device name                                                  | `Dexcom`                  |
| insulinPumpName | Insulin pump device name                                         | `Cozmo`                   |
| startDate       | First day of generated data                                      | `2024-02-01`              |
| endDate         | Last day of generated data                                       | `2024-04-30`              |

### 3. data/obfuscated

Contains data obfuscated from `data/processed` to simulate human behavior.

#### File Naming Convention

Pattern: `{patientNum}_{cgmName}_{insulinPumpName}_{startDate}_{endDate}_{loggingBehaviour}_{loggingTiming}.csv`

Example: `ado001_Dexcom_Cozmo_2024-02-01_2024-04-30_all_normal.csv`

| Component       | Description                                                      | Example                   |
|-----------------|------------------------------------------------------------------|---------------------------|
| patientNum      | Concatenation of first 3 and last 3 characters from patient name | `ado001` (adolescent#001) |
| cgmName         | CGM device name                                                  | `Dexcom`                  |
| insulinPumpName | Insulin pump device name                                         | `Cozmo`                   |
| startDate       | First day of generated data                                      | `2024-02-01`              |
| endDate         | Last day of generated data                                       | `2024-04-30`              |

#### Logging Behavior Types

| Filename Indicator | Type                   | Description                                      | Distribution |
|--------------------|------------------------|--------------------------------------------------|--------------|
| all                | All meals              | Logs every meal                                  | 20%          |
| top2               | Multiple meals per day | Logs 1-2 largest meals (on average 1.8 logs/day) | 25%          |
| once               | Once per day           | Logs largest meal only                           | 20%          |
| weekly             | A few times per week   | Irregular logging (on average 3 logs/week)       | 20%          |
| none               | Never                  | No logging                                       | 15%          |

*Note: Distribution percentages are subject to change*

#### Logging Timing Patterns

| Filename Indicator  | Pattern             | Description                            | Distribution |
|---------------------|---------------------|----------------------------------------|--------------|
| late                | Left skewed         | Forgetful loggers (gamma distribution) | 38%          |
| early               | Right skewed        | Hasty loggers (gamma distribution)     | 23%          |
| average             | Normal Distribution | Centered around meal start time        | 28%          |
| punctual            | Unchanged           | Logs exactly at meal start             | 11%          |

*Note: Distribution percentages are subject to change*

*Note: Parameters for gamma/distribution are subject to change*


#### Gamma/normal distribution for loggingTiming
Each graph contains 50 randomly generated curves
Average logger:
![Normal Distribution](data/distribution/average_logger.png)

Late logger:
![Gamma Distribution](data/distribution/late_logger.png)

Early logger:
![Gamma Distribution](data/distribution/early_logger.png)