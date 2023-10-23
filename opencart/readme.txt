$Env:OPENCART_PORT=8081; $Env:PHPADMIN_PORT=8888; $Env:LOCAL_IP=$(Get-NetIPAddress -AddressFamily IPv4 -InterfaceAlias 'Беспроводная сеть' | Where-Object {$_.AddressFamily -eq 'IPv4'}).IPAddress; docker-compose up -d

$Env:OPENCART_PORT, $Env:PHPADMIN_PORT, $Env:LOCAL_IP

docker volume rm opencart_mariadb_data opencart_opencart_data opencart_opencart_storage_data