$variable = @("tache_1", "tache_2")
foreach ($element in $variable){
    if ($element -eq "tache_1"){
        Write-Host "premiere tache"

    }
    else {
        Write-Host "deuxieme tache terminee"
    }
}