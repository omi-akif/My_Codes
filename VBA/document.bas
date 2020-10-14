Option Explicit

Sub ConvertWordtoExcel()
    Dim t1 As Single, t2 As Single
    Dim DataFile As String
    Dim DataPath As String
    Dim SavePath As String
    Dim SavePathFolder As String
    Dim rw As Long
    Dim ws As Worksheet
    Dim WordApp As Word.Application
    Dim FD As FileDialog

    On Error GoTo EH

    'identify sheet to take results
    Set ws = ActiveSheet

    t1 = Timer() '<~~ only used to report run time

    ' Create an instance of Word
    Set WordApp = New Word.Application
    WordApp.Visible = False

    ' Set up path to data files
    Set FD = Application.FileDialog(msoFileDialogFolderPicker) 'Open Folder Picker
    FD.Show
    DataPath = FD.SelectedItems(1) & "\"
    Debug.Print "Folder", DataPath
    SavePath = DataPath & "Txt\" '<~~ save text files to a separate subfolder called Txt
    SavePathFolder = Dir(SavePath, vbDirectory) ' If the Txt subfolder does not exist, create it
        If SavePathFolder = vbNullString Then
            VBA.FileSystem.MkDir (SavePath)
        End If

    ' Get first word file in directory
    DataFile = Dir(DataPath & "*.docx")
    Do While DataFile <> vbNullString
        Debug.Print "Convert ", DataFile
        ' Open in word, save as text
        ConvertToText WordApp, DataPath, DataFile, SavePath
        DoEvents

        ' Get next file
        DataFile = Dir
    Loop

    ' Tidy up
    WordApp.Quit
    Set WordApp = Nothing

    t2 = Timer

    Debug.Print "Convert Time", t2 - t1


    t1 = Timer()
    ' Get first text file in directory
    DataFile = Dir(SavePath & "*.txt")
    rw = 1
    Do While DataFile <> vbNullString
        Debug.Print "Read ", DataFile
        ' process the file
        ReadFile ws, SavePath, DataFile, rw
        DoEvents
        ' Get next file
        DataFile = Dir
    Loop


    t2 = Timer

    Debug.Print "Read Time", t2 - t1

Exit Sub
EH:
    On Error Resume Next
    ' Tidy up
    If Not WordApp Is Nothing Then WordApp.Quit
    Set WordApp = Nothing

End Sub

Sub ConvertToText(WordApp As Word.Application, ByVal FilePath As String, ByVal FileName As String, ByVal SavePath As String)
    Dim WordDoc As Word.Document
    Dim i As Long

    ' ensure file is closed if Sub errors
    On Error GoTo EH

    ' Open the file
    Set WordDoc = WordApp.Documents.Open(FilePath & FileName)

    With WordDoc.Range
  With .Find
    .ClearFormatting
    .Replacement.ClearFormatting
    .Wrap = wdFindContinue
    .Forward = True
    .Format = False
    .MatchWildcards = True
    .Text = "[ ]{2,}[^13]{1,}(REPORT NUM   :)" 'Clean header on each page
    .Replacement.Text = "\1"
    .Execute Replace:=wdReplaceAll
    .Text = "REPORT NUM   : * CTRY OF ORIGIN^13" 'Clean header on each page
    .Replacement.Text = ""
    .Execute Replace:=wdReplaceAll
    .Text = "[ ]{2,}ACTUAL SHP TOTAL*[ ]{20,}^13^m" 'Clean footer on some pages
    .Replacement.Text = ""
    .Execute Replace:=wdReplaceAll
    .Text = "[ ]{2,}TOTAL FOR DUTY*[ ]{20,}^13^m" 'Clean more footers
    .Replacement.Text = ""
    .Execute Replace:=wdReplaceAll
    .Text = "REPORT NUM   :*SUMMARY*[\*] [\*][ ]{20,}[^13]{1,}" 'Clean last page
    .Replacement.Text = ""
    .Execute Replace:=wdReplaceAll
    .Text = "^13^m" ' Clean all page breaks
    .Replacement.Text = "^13"
    .Execute Replace:=wdReplaceAll
    .Text = "[^13]{2,}" ' Clean empty paragraphs
    .Replacement.Text = "^13"
    .Execute Replace:=wdReplaceAll
    .Text = "(*)^13(*)^13(*)^13" ' Combine 3 paragraphs into one and add file name at the end
    .Replacement.Text = "\1 \2 \3 " + FileName + "^13"
    .Execute Replace:=wdReplaceAll
  End With
  End With


    ' generate Text file name
    i = InStrRev(FileName, ".")
    FileName = Left$(FileName, i) & "txt"

    ' Save as text
    WordDoc.SaveAs2 _
        FileName:=SavePath & FileName, _
        FileFormat:=wdFormatText, _
        AddToRecentFiles:=False, _
        EmbedTrueTypeFonts:=False, _
        SaveNativePictureFormat:=False, _
        SaveFormsData:=False, _
        SaveAsAOCELetter:=False, _
        Encoding:=1252, _
        InsertLineBreaks:=False, _
        AllowSubstitutions:=False, _
        LineEnding:=0, _
        CompatibilityMode:=0

EH:
    On Error Resume Next
    ' Close file
    WordDoc.Close False

End Sub

Sub ReadFile(ws As Worksheet, FilePath As String, FileName As String, ByRef rw)
    'parse text file
    Dim Ln As String
    Dim FileNum As Integer

    Dim ExtractedData() As Variant
    Dim idx As Long

    ' ensure file is closed if Sub errors
    On Error GoTo EH

    ' Text file handling
    FileNum = FreeFile
    Open FilePath & FileName For Input As FileNum

    ' Restults array.
    ReDim ExtractedData(1 To 1000000, 1 To 1) ' Excel sheet can hold at most 1048576 rows
    idx = 0
    Do While Not EOF(FileNum)
        ' Read a line from file
        Line Input #FileNum, Ln

        ' Add your code to extract required data here
        'If Ln Like " [A-Z][A-Z][A-z]########*" Then
            If Ln Like " *" Then
            idx = idx + 1
            ExtractedData(idx, 1) = Ln
        End If
        'End If
        '============================================
    Loop
    ' Place extracted data onto sheet
    ws.Cells(rw, 1).Resize(idx, 1) = ExtractedData
    ' Update row num for next file
    rw = rw + idx

EH:
    On Error Resume Next
    ' Clean Up
    Close #FileNum
End Sub
