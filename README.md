# Simulador Blockchain

Es una aplicación P2P desarrollada en Python que simula el comportamiento de una red Blockchain simplificada. Este prototipo usa las definiciones de bloques y transacciones como las usadas por la red Bitcoin.

Estado del proyecto: Incompleto 😭

Video explicativo de lo que sí funciona y los errores actuales: https://youtu.be/J7Ll3LQFyo0

## 🔥 Instalación

```shell
virtualenv venv
source venv/bin/activate
make requirements
pip install -e .
```

## 💡 Cómo usarlo

`genIdenti -i < NumIdentidades > −n < NumNodos >`

Este comando crea una nueva red con identidades genericas y de nodos.

> No se pueden llamar nodos sin identidad.

`nodo -n <nombre nodo> -d <dir> -f <archivo red> -c <archivo config>`

Este comando lo que hace es activar un nodo en la red en donde:

< nombre nodo > : el nombre que usará el nodo para identficarse. Debe ser `nodo<num>`
< dir > : Directorio dónde el nodo colocará el archivo de nombre < nombre nodo > .log
< archivo red > : es el nombre del archivo que tendrá la información de la red virtual. Ejemplo: file_example/network_file.txt
< archivo config > : Archivo que tendrá un conjunto de variables. Ejemplo: file_example/node_config.txt

> Nota: los nodos referenciados que no tengan identidad asociada van a ser ignorados. Para evitar esto cree con el comando genIdenti suficientes nodos.

`genTransac -f <archivo config> -n <archivo nodo> -d <dir>`

Este comando genera transacciones a partir de los archivos de configuración suministrados.

< archivo config > será el nombre de un archivo que cumplirá la especificación
siguiente:
- frecuencia: Número de transacciones por minuto
- NumEntradasMin: Número de entradas Mínimo
- NumEntradasMax: Número de entradas Máximo
- NumSalidasMin: Número de salidas Mínimo
- NumSalidasMax: Número de salidas Máximo

< archivo nodo > es el nombre de un archivo que tendrá los nombres y puertos de
los nodos a los que se le puede enviar la transacción. Recuerde que en este caso, los nombres no corresponden con el nombre internet (ip) sino con el identficador en la red P2P. Ejemplo: file_example/node_file.txt

< dir > : Directorio dónde el nodo colocará el archivo de nombre < nombre nodo > .log

`exploradorBloque {-a <altura del bloque> | -h <hash del bloque>}`

Muestra un resumen de la información en un bloque.

`exploradorTransac -h <hash de la transacción>`

Muestra un resumen de la información en una transacción.

## Detalles de implementación

- Las identididades tienen seguridad asimetrica (tienen clave pública y privada)
- La comunicación entre los nodos es mediante unos protocolos (Ingresar Transacción, Presentación, Propagar Transacción, Propagar bloque candidato), y usa P2SH (Pay to public key hash), que no está implementado en lenguaje de pila pero funciona similar.
- Toda actividad de los nodos esta registrada en archivos logs.
- Se usa PoW como mecanismo de consenso.

## Tests

```shell
make test
make quality
```
