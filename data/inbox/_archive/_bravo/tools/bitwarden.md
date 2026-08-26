# bitwarden


## secrets manager setup

### set path at machine level 
```sh
#add bw path to machine path
$bw = 'C:\Program Files\BitwardenCLI\;'; $currpath = [Environment]::GetEnvironmentVariable('path', 'machine');$combined = $bw + $currpath;[Environment]::SetEnvironmentVariable('path', $combined,'Machine');
```

### setx BWS_ACCESS_TOKEN
```sh
runas /user:int\svc_int_cybertsk_prd c:\windows\system32\cmd.exe
setx BWS_ACCESS_TOKEN 0.903c5a6a-693b-491a-876f-b0a0003dd305.k4Jtx5Vz7LUtDef526sjaEpmUtULPG:VCyKqsrxV0HMTiGB2vcSYw==

```

### get secret
```sh
(bws -t $env:BWS_ACCESS_TOKEN secret get a2f062a0-5969-4b44-b6a7-b0a0003d2f88) | convertfrom-json | select-object value
```

