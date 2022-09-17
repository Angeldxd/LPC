Write-Host "Este script mostrará los valores desde el 1 hasta el valor que tu le ingreses, aumentando de 1 en 1"
Function error {
Write-Host "Número no válido"
}

[int]$numero = Read-Host "Ingresa un número entero entre el 1 y 100, inclúyendolos"


if($numero -le 100 ){
    if($numero -gt 0){
    $numero += 1
for($i=1; $i -lt $numero; $i++) {
    Write-Host $i
 }
 }else {
    error
 }}
 else {
    error}
 