import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(1,11):
    sheet['A' + str(i)] = i

#Reference requires 3 arguments:
    # The Worksheet object containing your chart data.
    # A tuple of two integers, representing the top-left cell (starts at 1)
    # A tuple of two integers, representing the bottom-right cell
refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1,max_row=10)

seriesObj = openpyxl.chart.Series(refObj, title='First series')

chartObj = openpyxl.chart.BarChart()
chartObj.title = 'My Chart'

#Append series object to chart object
chartObj.append(seriesObj)

#Add the Chart object to the Worksheet object, optionally specifying which cell should be the top-left corner of the chart.
sheet.add_chart(chartObj, 'C5')
wb.save('sampleChart.xlsx')
