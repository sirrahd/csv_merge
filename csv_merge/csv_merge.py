import csv
import tkinter
from collections import deque
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def main():
    # By default Tk shows an empty window, remove it
    tkinter.Tk().withdraw()

    input('Press enter to select the base file')
    baseFilePath = askopenfilename(title='Select the base file to read')
    print('Base file: ' + baseFilePath)

    input('Press enter to select the merge file')
    mergeFilePath = askopenfilename(title='Select the merge file to read')
    print('Merge file: ' + mergeFilePath)
    
    input('Press enter to select the save file')
    saveFilePath = asksaveasfilename()
    print('Save file: ' + saveFilePath)

    baseFile = csv.reader(open(baseFilePath, 'r', encoding='utf-8'))
    mergeFile = deque(csv.reader(open(mergeFilePath, 'r', encoding='utf-8')))
    saveFile = csv.writer(open(saveFilePath, 'w', encoding='utf-8'), delimiter=';', quoting=csv.QUOTE_NONE)

    mergeRow = mergeFile.popleft()
    for baseRow in baseFile:
        if mergeRow[0] == baseRow[0]:
            mergeCol = mergeRow[1]
            try:
                mergeRow = mergeFile.popleft()
            except:
                pass
        else:
            mergeCol = ''

        saveFile.writerow([baseRow[0], mergeCol, baseRow[1]])
        
main()