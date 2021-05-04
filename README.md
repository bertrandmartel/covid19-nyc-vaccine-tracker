# Covid19 NYC Vaccine Tracker

[![CI](https://github.com/bertrandmartel/covid19-nyc-vaccine-tracker/workflows/Report/badge.svg)](https://github.com/bertrandmartel/covid19-nyc-vaccine-tracker/actions)

This runs every day and extracts data from Tableau from [NYC Vaccine Tracker](https://public.tableau.com/profile/integrated.data.team#!/vizhome/COVID-19VaccineTrackerDashboard_16153822244270/DosesAdministered) public Tableau website

This project uses [Tableau scraper python library](https://github.com/bertrandmartel/tableau-scraping)

latest data: https://github.com/bertrandmartel/covid19-nyc-vaccine-tracker/tree/master/deploy/latest

## Update 08/04/2021

From 08/04/2021, tableau data has added age filters to some sheets: `18+` and `All`. Thus, the format has changed in the directories and sheets name (maybe format) has changed as well :

```
├── Administered (2).csv
├── coverage
│   ├── adults
│   │   ├── Demographics % (V2) (2).csv
│   │   ├── NYC Unknown RE 1 dose.csv
│   │   └── Sheet 22.csv
│   └── all
│       ├── Demographics % (V2) (2).csv
│       └── Sheet 22.csv
├── Cumulative trends (2).csv
├── Daily trends (2).csv
├── Delivered (2).csv
├── Doses on hand.csv
├── geography
│   ├── at least one dose
│   │   ├── adults
│   │   │   ├── AgePriority_RaceEth.csv
│   │   │   ├── Map ZIP.csv
│   │   │   ├── RacePriority_RaceEth.csv
│   │   │   └── SexPriority_RaceEth.csv
│   │   └── all
│   │       ├── AgePriority_RaceEth.csv
│   │       ├── Map ZIP.csv
│   │       ├── RacePriority_RaceEth.csv
│   │       └── SexPriority_RaceEth.csv
│   └── fully vaccinated
│       ├── adults
│       │   ├── AgePriority_RaceEth.csv
│       │   ├── Map ZIP.csv
│       │   ├── RacePriority_RaceEth.csv
│       │   └── SexPriority_RaceEth.csv
│       └── all
│           ├── AgePriority_RaceEth.csv
│           ├── Map ZIP.csv
│           ├── RacePriority_RaceEth.csv
│           └── SexPriority_RaceEth.csv
├── Known At Least 1.csv
├── NYC v NON NYC overall.csv
└── Unknown RE 1 dose.csv
```

# Archive

## Update 04/05/2021

In worksheet NYC vax, default filter is now set at `All` instead of `18+`

## Update 26/03/2021

```
├── Administered (2).csv
├── Cumulative trends (2).csv
├── Daily trends (2).csv
├── Delivered (2).csv
├── Demographics % (V2) (2).csv
├── Doses on hand.csv
├── geography
│   ├── at least one dose
│   │   ├── AgePriority_RaceEth.csv
│   │   ├── RacePriority_RaceEth.csv
│   │   └── SexPriority_RaceEth.csv
│   ├── fully vaccinated
│   │   ├── AgePriority_RaceEth.csv
│   │   ├── RacePriority_RaceEth.csv
│   │   └── SexPriority_RaceEth.csv
│   └── Map ZIP.csv
├── Known At Least 1.csv
├── NYC Unknown RE 1 dose.csv
├── NYC v NON NYC overall.csv
├── NYC vs Non NYC (2).csv
├── NYC vs Non NYC.csv
├── Sheet 28.csv
└── Unknown RE 1 dose.csv
```
