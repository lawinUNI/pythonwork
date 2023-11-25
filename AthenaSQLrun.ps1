####################################################
###
###  Athena レセプト抽出ツール
###
####################################################

$filename = "rece.txt"
$Recefolder = Split-Path $MyInvocation.MyCommand.path

#write-host $Rece

$filePath = $Recefolder + "/" + $filename

$file = New-Object System.IO.StreamReader($filePath, [System.Text.Encoding]::GetEncoding("sjis"))
$sqlpram = ""
while ($null -ne ($line = $file.ReadLine())) {
    if ($sqlpram -eq "") {
        $sqlpram = "'" + $line + "'"
    }else {
        $sqlpram = $sqlpram + ",'" + $line + "'"
    }
    #Write-Host($line)

}

Write-Host($sqlpram)