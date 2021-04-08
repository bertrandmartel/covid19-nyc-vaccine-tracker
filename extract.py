from tableauscraper import TableauScraper as TS
import os
import time
import sys

currentPath = os.path.dirname(os.path.abspath(__file__))

if len(sys.argv) > 1:
    currentPath = os.path.join(currentPath, sys.argv[1])

if len(sys.argv) > 2:
    currentFolder = os.path.join(currentPath, sys.argv[2])
else:
    currentFolder = os.path.join(currentPath, time.strftime("%Y-%m-%d"))

url = 'https://public.tableau.com/views/COVID-19VaccineTrackerDashboard_16153822244270/DosesAdministered'

ts = TS()
ts.loads(url)

os.makedirs(currentFolder, exist_ok=True)

rootWb = ts.getWorkbook()


def buildFilePath(currentFolder, name):
    return os.path.join(currentPath, currentFolder, name)


for t in rootWb.worksheets:
    print(f"worksheet name : {t.name}")
    if not t.data.empty:
        t.data.to_csv(buildFilePath(
            currentFolder, f'{t.name}.csv'), index=False)

dailyWb = rootWb.setParameter("Cumulative + Daily", "Daily trends")

ws = dailyWb.getWorksheet("Daily trends (2)")
if not ws.data.empty:
    ws.data.to_csv(buildFilePath(
        currentFolder, "Daily trends (2).csv"), index=False)

allPeople = rootWb.goToSheet("All People Vaccination")
for t in allPeople.worksheets:
    print(f"worksheet name : {t.name}")
    if not t.data.empty:
        t.data.to_csv(buildFilePath(
            currentFolder, f'{t.name}.csv'), index=False)

nycVaxCoverage = rootWb.goToSheet("NYC Vax Coverage")

os.makedirs(os.path.join(currentFolder, "coverage"), exist_ok=True)
os.makedirs(os.path.join(currentFolder, "coverage", "adults"), exist_ok=True)
os.makedirs(os.path.join(currentFolder, "coverage", "all"), exist_ok=True)

# adults covrage
for t in nycVaxCoverage.worksheets:
    print(f"worksheet name : {t.name}")
    if not t.data.empty:
        t.data.to_csv(buildFilePath(
            os.path.join(currentFolder, "coverage", "adults"), f'{t.name}.csv'), index=False)

# all coverage
vaxCoverageAll = nycVaxCoverage.getWorksheet(
    "Sheet 22").setFilter("Age Group", "All")
for t in vaxCoverageAll.worksheets:
    print(f"worksheet name : {t.name}")
    if not t.data.empty:
        t.data.to_csv(buildFilePath(
            os.path.join(currentFolder, "coverage", "all"), f'{t.name}.csv'), index=False)

geography = rootWb.goToSheet("Geography")

os.makedirs(os.path.join(currentFolder, "geography"), exist_ok=True)

os.makedirs(os.path.join(currentFolder, "geography",
                         "at least one dose"), exist_ok=True)
os.makedirs(os.path.join(currentFolder, "geography",
                         "at least one dose", "adults"), exist_ok=True)
os.makedirs(os.path.join(currentFolder, "geography",
                         "at least one dose", "all"), exist_ok=True)
os.makedirs(os.path.join(currentFolder, "geography",
                         "fully vaccinated"), exist_ok=True)
os.makedirs(os.path.join(currentFolder, "geography",
                         "fully vaccinated", "adults"), exist_ok=True)
os.makedirs(os.path.join(currentFolder, "geography",
                         "fully vaccinated", "all"), exist_ok=True)


def processRaceSex(wb, dir, sheetName):
    currentPath = buildFilePath(os.path.join(
        currentFolder, "geography", dir), f"{sheetName}.csv")
    wb.getWorksheet(sheetName).data.to_csv(
        currentPath, index=False)


# 1) at least one dose - adults
processRaceSex(geography, os.path.join(
    "at least one dose", "adults"), "AgePriority_RaceEth")
processRaceSex(geography, os.path.join(
    "at least one dose", "adults"), "SexPriority_RaceEth")
processRaceSex(geography, os.path.join(
    "at least one dose", "adults"), "RacePriority_RaceEth")
processRaceSex(geography, os.path.join(
    "at least one dose", "adults"), "Map ZIP")

# 2) fully vaccinated - adults
wb = geography.setParameter("Select Vaccine Indicator", "% Fully Vaccinated")

processRaceSex(wb, os.path.join("fully vaccinated",
                                "adults"), "AgePriority_RaceEth")
processRaceSex(wb, os.path.join("fully vaccinated",
                                "adults"), "SexPriority_RaceEth")
processRaceSex(wb, os.path.join("fully vaccinated",
                                "adults"), "RacePriority_RaceEth")

#  at least one dose - zip map
wb = geography.setParameter("Select Indicator - Map", "% Fully Vaccinated")
processRaceSex(wb, os.path.join(
    "fully vaccinated", "adults"), "Map ZIP")

# all
wb = geography.getWorksheet("AgePriority_RaceEth").setFilter("AGE", "All")
processRaceSex(wb, os.path.join(
    "fully vaccinated", "all"), "AgePriority_RaceEth")
processRaceSex(wb, os.path.join(
    "fully vaccinated", "all"), "SexPriority_RaceEth")
processRaceSex(wb, os.path.join(
    "fully vaccinated", "all"), "RacePriority_RaceEth")

wb = geography.setParameter("Select Vaccine Indicator", "% At Least 1 Dose")
processRaceSex(wb, os.path.join(
    "at least one dose", "all"), "AgePriority_RaceEth")
processRaceSex(wb, os.path.join(
    "at least one dose", "all"), "SexPriority_RaceEth")
processRaceSex(wb, os.path.join(
    "at least one dose", "all"), "RacePriority_RaceEth")

wb = geography.getWorksheet("Map ZIP").setFilter("AGE_GROUP", "All")
processRaceSex(wb, os.path.join(
    "fully vaccinated", "all"), "Map ZIP")
wb = geography.setParameter("Select Indicator - Map", "% At Least 1 Dose")
processRaceSex(wb, os.path.join(
    "at least one dose", "all"), "Map ZIP")
