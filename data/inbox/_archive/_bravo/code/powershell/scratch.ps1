





  Add-Type -AssemblyName System.Core 
    function Run-Server() 
    { 
      param([string]$h); 
      $b = New-Object byte[] 8; 
      $p = New-Object System.IO.Pipes.AnonymousPipeClientStream -ArgumentList @([System.IO.Pipes.PipeDirection]::In, $h); 
      if ($p) { $l = $p.Read($b, 0, 8); 
        while ($l -gt 7) 
        { 
          $c = [System.BitConverter]::ToInt32($b, 0); 
          $l = [System.BitConverter]::ToInt32($b, 4); 
          $t = $null; 
          if ($l -gt 0) { 
            $t1 = New-Object byte[] $l; 
            $l = $p.Read($t1, 0, $t1.Length); 
            $t = [System.Text.Encoding]::UTF8.GetString($t1, 0, $l) 
          } 
          if ($c -eq 1){ 
            Invoke-Expression $t 
          } elseif ($c -eq 9) { 
            break 
          } 
          $l = $p.Read($b, 0, 8) 
        } 
        $p.Dispose() } 
      } 
      Run-Server -h 1404
    }

    