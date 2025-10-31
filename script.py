# This is a sample Python script.
from contextlib import nullcontext

import requests
from bs4 import BeautifulSoup

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

blank = '▁'
largestXvalue: int

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


def getTableFromURL(request):
    # Make request
    html_response = requests.get(url=request)

    # Parse html into a BeautifulSoup object
    soup = BeautifulSoup(html_response.text, 'html.parser')

    # print(soup.find('table'))
    table = soup.find('table')

    return table


def simplifyTable(table):
    resultArray = []
    columns = table.find_all('tr')
    for row in columns[1:]:
        column = row.find_all(['th', 'td'])
        resultArray.append([int(column[0].text), column[1].text, int(column[2].text)])
    return resultArray

def largestX(table): 
    largestxvalue = 0
    for row in table:
        if row[0] > largestxvalue:
            largestxvalue = row[0]
    return largestxvalue

def groupTableByY(simpleTable):
    result = []

    for column in simpleTable:
        sorted = False
        for rcolumn in result:
            if rcolumn[0][2] == column[2]:
                rcolumn.append(column)
                sorted = True
                break
        if not sorted :
            result.append([[column[0], column[1], column[2]]])
    return result


def getTable():

    requestMain = 'https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub'
    request = 'https://docs.google.com/document/u/0/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub?pli=1'

    table = getTableFromURL(requestMain)
    simpleTable = simplifyTable(table)
    largestXvalue = largestX(simpleTable)
    print("largest X is - > ", largestXvalue)
    groupedTable = groupTableByY(simpleTable)

    print("grouped ",groupedTable)
    for row in groupedTable:
        print(" -> ",row)


    sortedArr = sorted(groupedTable, key=lambda x: x[0][2], reverse=True)

    resortedArr = []
    for list in sortedArr:
        list = sorted(list, key=lambda x: x[0])
        resortedArr.append(list)
        # print("sorted " , list)

    print("Sorted Array " , resortedArr)
    for row in resortedArr:
        print(row)

    for list in resortedArr:
        print("")
        for i in range(0,largestXvalue):
            if len(list) == 0:
                break
            if list[0][0] == i:
                value = list.pop(0)
                print(value[1], end='')
            else:
                print(blank, end='')

    return sorted

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    getTable()