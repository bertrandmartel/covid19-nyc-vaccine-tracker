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

url = 'https://public.tableau.com/views/COVID-19VaccineTrackerDashboard_16153822244270/Dosesadministered'

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

allAdults = rootWb.goToSheet("All Adults")
for t in allAdults.worksheets:
    print(f"worksheet name : {t.name}")
    if not t.data.empty:
        t.data.to_csv(buildFilePath(
            currentFolder, f'{t.name}.csv'), index=False)

nycAdults = rootWb.goToSheet("NYC Adults")
for t in nycAdults.worksheets:
    print(f"worksheet name : {t.name}")
    if not t.data.empty:
        t.data.to_csv(buildFilePath(
            currentFolder, f'{t.name}.csv'), index=False)

geography = rootWb.goToSheet("Geography")

os.makedirs(os.path.join(currentFolder, "geography"), exist_ok=True)

geography.getWorksheet("Map ZIP").data.to_csv(
    buildFilePath(os.path.join(currentFolder, "geography"), 'Map ZIP.csv'), index=False)

os.makedirs(os.path.join(currentFolder, "geography",
                         "at least one dose"), exist_ok=True)
os.makedirs(os.path.join(currentFolder, "geography",
                         "fully vaccinated"), exist_ok=True)


def processRaceSex(wb, dir, sheetName):
    currentPath = buildFilePath(os.path.join(
        currentFolder, "geography", dir), f"{sheetName}.csv")
    wb.getWorksheet(sheetName).data.to_csv(
        currentPath, index=False)


processRaceSex(geography, "at least one dose", "AgePriority_RaceEth")
processRaceSex(geography, "at least one dose", "SexPriority_RaceEth")
processRaceSex(geography, "at least one dose", "RacePriority_RaceEth")

wb = geography.setParameter("Select Vaccine Indicator", "Fully Vaccinated")

processRaceSex(wb, "fully vaccinated", "AgePriority_RaceEth")
processRaceSex(wb, "fully vaccinated", "SexPriority_RaceEth")
processRaceSex(wb, "fully vaccinated", "RacePriority_RaceEth")
