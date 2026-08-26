# excel

## convert epoch milliseconds to date
```
=(A2/86400000)+DATE(1970,1,1) + TIME(0,0,0)
=(A2/86400/1000)+25569
```

## convert utc time to excel
```
=DATEVALUE(LEFT(G9,10))+TIMEVALUE(MID(G9,12,8))
```

## add zero to empty fields in pivot table
pivot table options
![alt text](assets/attachments/kb/htb/redteam/assets/tools/excel/Replace-Blank-Cells-with-Zeros-Pivot-Tables-Enter-0.png)


## split string on char and get last instance
`=CHOOSECOLS(TEXTSPLIT(B2, "\"), -1)`

## replace in string
`=SUBSTITUTE(B2, "\Device\HarddiskVolume6\", "")`


## time format
`dd/mm/yyyy h:mm:ss.000`