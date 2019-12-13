
Sub stock_data()
Dim ws As Worksheet
For Each ws In Worksheets

        
    'base variables
    Dim tickername As String
    Dim dates As String
    Dim openvalue As Double
    Dim highvalue As Integer
    Dim lowvalue As Integer
    Dim closevalue As Double
    Dim volume As Double
    Dim summary_table_row As Integer
    Dim i As Double
   
    'calculated values
    Dim ticker_count As Double
    Dim volume_count As Integer
    Dim totalvolume As Double
    Dim yearlychange As Double
    Dim percentchange As Double
    Dim LastRow As Long
    LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    'Summary tables creation
    ws.Range("J1").Value = "Ticker"
    ws.Range("K1").Value = "Yearly Change"
    ws.Range("L1").Value = "Percent Change"
    ws.Range("M1").Value = "Total Stock Volume"
    ws.Range("O2").Value = "Greatest % Increase"
    ws.Range("O3").Value = "Greatest % Decrease"
    ws.Range("O4").Value = "Greatest Total Volume"
    ws.Range("P1").Value = "Ticker"
    ws.Range("Q1").Value = "Value"
    summary_table_row = 2
    ticker_count = 0
    totalvolume = 0
 
    For i = 2 To LastRow
        If ticker_count = 0 Then
            openvalue = ws.Cells(i, 3).Value
        End If
        If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
            tickername = ws.Cells(i, 1).Value
            ws.Cells(summary_table_row, 10).Value = tickername
            ws.Cells(summary_table_row, 13).Value = (totalvolume + ws.Cells(i, 7).Value)
            closevalue = ws.Cells(i, 6).Value
            ticker_count = 0
            totalvolume = 0
            yearlychange = closevalue - openvalue
            If openvalue > 0 Then
                percentchange = yearlychange / openvalue
            Else
                percentchange = 0
            End If
            ws.Cells(summary_table_row, 11).Value = yearlychange
                If yearlychange > 0 Then
                    ws.Cells(summary_table_row, 11).Interior.Color = vbGreen
                Else
                    ws.Cells(summary_table_row, 11).Interior.Color = vbRed
                End If
            ws.Cells(summary_table_row, 12).Value = percentchange
                ws.Cells(summary_table_row, 12).NumberFormat = "0.00%"
            summary_table_row = summary_table_row + 1
        Else
            ticker_count = ticker_count + 1
            totalvolume = totalvolume + ws.Cells(i, 7).Value
        End If
    Next i
        
    Dim j As Long
    Dim greatest_increase_ticker As String
    Dim greatest_increase_value As Double
    Dim greatest_decrease_ticker As String
    Dim greatest_decrease_value As Double
    Dim greatest_volume_ticker As String
    Dim greatest_volume_value As Double
    Dim LastRow2 As Long
    LastRow2 = ws.Cells(Rows.Count, 10).End(xlUp).Row
        greatest_increase_ticker = 0
        greatest_increase_value = 0
        greatest_decrease_ticker = 0
        greatest_decrease_value = 0
        greatest_volume_ticker = 0
        greatest_volume_value = 0
        
    For j = 2 To LastRow2
    
        If ws.Cells(j + 1, 12).Value > greatest_increase_value Then
            greatest_increase_ticker = ws.Cells(2, 10).Value
            greatest_increase_value = ws.Cells(2, 12).Value
            greatest_increase_ticker = ws.Cells(j + 1, 10).Value
            greatest_increase_value = ws.Cells(j + 1, 12).Value
            ws.Range("P2").Value = greatest_increase_ticker
            ws.Range("Q2").Value = greatest_increase_value
                ws.Range("Q2").NumberFormat = "0.00%"
        Else
            greatest_increase_ticker = greatest_increase_ticker
            greatest_increase_value = greatest_increase_value
        End If
        
        If ws.Cells(j + 1, 12).Value < greatest_decrease_value Then
            greatest_decrease_ticker = ws.Cells(2, 10).Value
            greatest_decrease_value = ws.Cells(2, 12).Value
            greatest_decrease_ticker = ws.Cells(j + 1, 10).Value
            greatest_decrease_value = ws.Cells(j + 1, 12).Value
            ws.Range("P3").Value = greatest_decrease_ticker
            ws.Range("Q3").Value = greatest_decrease_value
                ws.Range("Q3").NumberFormat = "0.00%"
        Else
            greatest_decrease_ticker = greatest_decrease_ticker
            greatest_decrease_value = greatest_decrease_value
        End If
        
        If ws.Cells(j + 1, 13).Value > greatest_volume_value Then
            greatest_volume_ticker = ws.Cells(2, 10).Value
            greatest_volume_value = ws.Cells(2, 13).Value
            greatest_volume_ticker = ws.Cells(j + 1, 10).Value
            greatest_volume_value = ws.Cells(j + 1, 13).Value
            ws.Range("P4").Value = greatest_volume_ticker
            ws.Range("Q4").Value = greatest_volume_value
        Else
            greatest_volume_ticker = greatest_volume_ticker
            greatest_volume_value = greatest_volume_value
        End If

        Next j
    
Next ws

End Sub


