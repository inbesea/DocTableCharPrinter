# This is a sample Python script.
import requests
from bs4 import BeautifulSoup

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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

    table = getTableFromURL(request)
    simpleTable = simplifyTable(table)
    groupedTable = groupTableByY(simpleTable)
    print("grouped ",groupedTable)
    for row in groupedTable:
        print(" -> ",row)
    sortedArr = sorted(simpleTable, key=lambda x: x[2])

    print(sortedArr)
    for row in sortedArr:
        print(row)

    for r in sortedArr:
        print(r[1])

    # for row in table.find_all('tr'):
    #     columns = row.find_all(['th', 'td'])
    #     print([column.text for column in columns])
    #
    # for row in table.find_all('tr'):
    #     columns = row.find_all(['td'])
    #     print([column.text for column in columns])

    # Collect and return the first table (assuming the first table is what you want)
    return sorted
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def test():
    array_2d = [
        [3, 1, 2],
        [1, 3, 4],
        [2, 2, 1]
    ]

    # Sort by the second column (index 1)
    sorted_array = sorted(array_2d, key=lambda x: x[1])
    print(sorted_array)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    getTable()