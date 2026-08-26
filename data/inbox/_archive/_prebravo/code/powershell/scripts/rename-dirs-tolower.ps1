#---
# hashtags: 
#  - #powershell
#  - #get-childitem
#  - #recursion
#---

#Get the directories / sub directories and rename to lowercase
Get-ChildItem -recurse |
    ?{ $_.PSIsContainer -And $_.Name -CMatch "[A-Z]" } |
    %{
        $NName = $_.Name.ToLowerInvariant()

        # Set temporary name to enable rename to the same name; Windows is not case sensitive
        $TempItem = Rename-Item -Path $_.FullName -NewName "x$NName" -PassThru

        Rename-Item -Path $TempItem.FullName -NewName $NName
    }