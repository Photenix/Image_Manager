Write-Host "1. Compilar proyecto"
Write-Host "2. Remover compilado"
Write-Host "3. Salir"
$option = Read-Host "Ingresa una opcion: "

if ( $option -eq "1" ) {
    pyinstaller.exe -F -w .\main.py
}
elseif ( $option -eq "2" ) {
    Remove-Item -Recurse .\dist
    Remove-Item -Recurse .\build
    Remove-Item .\main.spec
}
elseif ( $option -eq "3" ) {
    Write-Host "Saliendo :3"
}