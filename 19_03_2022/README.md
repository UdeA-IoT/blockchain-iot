
# Apuntes del articulo

> Articulo analizado: 

El paper describe y analiza las tecnicas control de acceso en IoT basadas en blockchain. Para ello explora casos de uso en dos escenarios principales; el control de acceso para IoT y otros casos de uso como vehicular had hot networks, healcare aund supply chains. Aqui se discute por que puede ser usada una Blockchain para implementar de manera eficiente el control de acceso en IoT.


## Sobre las blockchain 

El paper principal Bitcoin: A Peer-to-Peer Electronic Cash System ([link](https://bitcoin.org/bitcoin.pdf)) y es la base de todo. Sin embargo en https://bitcoin.org ([vocabulary](https://bitcoin.org/en/vocabulary) / [vocabulario](https://bitcoin.org/es/vocabulario)). Adicionalmente en  https://bitcoiner.guide/ hay información muy útil, pero si lo que se quiere es empezar a explorar el desarrollo se puede consultar: https://developer.bitcoin.org/devguide/index.html.

En todo caso, a continuación se muestran algunos de los conceptos mencionados en el paper:
* Blockchain: Es una secuencia de transacciones fijas, registradas en el tiempo (time staped sequence) por un grupo de maquinas mediante el uso de algoritmos especiales.
* Node: Cada una de las maquina que participa. Cada nodo guarda la misma copia de datos.

![bloque](https://www.dummies.com/wp-content/uploads/cryptocurrency-blockchain.jpg)

* Ledger: Copia de datos distribuida. Cada nodo tiene una copia del legder.
* Block basic componets: Version information, nonce value, hash value of previus block, timestamp, merkle root and transactions.
  *  Version number of blockain: Usado para mantener los cambios y actualizaciones durante la toda la duración del protocolo.
  *  Nonce: es un numero arbitrario (asociado al problema matematico) al cual se enfrentaran los mineros. 
  *  Hash: Funcion criptografica usada para asegurar la cadena.
  *  Timestamp: Usado para indicar cuando ocurre una transacción particular.
  *  Merkle root: Se obtiene mediante el hash de la transacción nuevamente.
  *  Transaction List: Se refiere a las transaciones asociadas a un bloque particular. 

### Como trabaja una blockchain

El proceso se resume en la siguiente figura:

![Figura](https://kilroyblockchain.com/media/how_does_blockchain_work.png)

En el paper se hablan de conceptos importantes como:
* Asimetric criptography ([link util](https://toughnickel.com/personal-finance/Unblocking-The-Blockchain-Public-Key-Encryption)).
  * private key.
  * public key.

![Critografia asimetrica](https://hackernoon.com/hn-images/1*RnbSEDRnWKkLOroN9hz7mg.png)

* Consensus algorithm ([link 1](https://devopedia.org/blockchain-consensus), [link 2](https://blockgeeks.com/guides/blockchain-consensus/))

* miner.

### Consensus Algorithms

Su función principal es mantener la integridad de la blockchain. Los concensos mas pupulares se muestran a continuación:
1. **Proof of Work (PoW)**: Administración de la red basada en la potencia de computo.
2. **Proof of Stake (PoS)**: La administración la tienen los nodos con mas money.
3. **Proof of Authority (PoA)**: arbitrary chosen trustworthy nodes administers the network.
4. **Proof of Elapsed Time (PoET)**: nodes who have fonished specifc waiting period administers the network.
5. **Delegated Proof of Stake (DPoS)**: Nodes elected by delegates through voting administers the network.

La siguiente figura resume ([link](https://www.affde.com/es/blockchain-consensus-algorithms-guide.html)) algunos casos:

![consensos](https://www.affde.com/uploads/article/180780/qG4PnERNcZsFa4G7.png)

En el articulo **Cryptographic consensus mechanisms** ([link](aggarwal2020.pdf)) se muestran mas detalles al respecto.

### Algunos simuladores

Aunque esto no se habla en el articulo, se agregó esta parte para comprender un poco mejor el funcionamiento de blockchain.

1. https://blockchaindemo.io/
2. http://blockchain.mit.edu/
3. https://andersbrownworth.com/blockchain/
4. https://hackernoon.com/blockchain-simulators-ui2030z0

## Blockchain Based IoT Access Control Methods

**Problema - Estructura centralizada (client-server model) de IoT**: La falta de confianza (trust) entre los diferentes dispositivos participantes puede causar en la red completa.

**Posible solución**: Dentro de las propuestas, el uso de blockchains ha ganado fuerza debido a su estructura descentralizada, segura e inmutable.

En el documento se exploran los siguientes metodos:

1. **Attribute Based Access Control (ABAC)**: Simplifica el access management en IoT. Se mencionan los siguientes articulos.
   * [A Novel Attribute-Based Access Control Scheme Using Blockchain for IoT](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8668769). En la blockchain se preservan atributos como user atributes, resource atributes y object atributes based on users' requeriments. El ABAC extrae las singularidades o representaciones en un conjunto de atributos los cuales son publicados por el attribute authority.
   * [An Attribute-Based Collaborative Access Control Scheme Using Blockchain for IoT Devices](https://www.mdpi.com/2079-9292/9/2/285/htm): El control basado en atributos se basa en cinco componentes principales llamados Consortium Blockchain Network, Authority Nodes (AN), IoT Devices, Chaincode and Public Ledger and Access Tree.

2. **Fair Access - Acceso justo**: Facilita el control de los usuarios sobre sus propios datos al introducir una tecnologia no centralizada **completely pseudonymus**. Se menciona el articulo **FairAccess: a new Blockchain-based access control framework for the Internet of Things** ([link](https://asset-pdf.scinapse.io/prod/2588585573/2588585573.pdf)).
3. **Distributed Access Control**: Se proporciona control de acceso descentralizado enlazando redes de sensores geograficamente distribuidas (combination of Wire-
less Sensor Networks, Manager Nodes, Agent node, Smart contract, Blockchain network and Management hubs.). Esta es una combinación de . Se resume el articulo **Blockchain Meets IoT: An Architecture for Scalable Access Management in IoT** ([link](https://www.ericsson.com/en/reports-and-papers/research-papers/blockchain-meets-iot-an-architecture-for-scalable-access-management-in-iot)). Tambien se analiza el articulo **Dynamic Access Control Scheme for IoT Devices using Blockchain** ([link](https://ieeexplore.ieee.org/abstract/document/8539659))
4. **Distributed Key Management**
5. **Token Based Access Control**
6. **Control Chain**
7. **Attribute Update Oriented Access Control**
8. **Ripple Protocol Consensus Algorithm (RPCA) Based Access Control**
9.  **Multiple Smart Contracts Based Access Control**

## Terminos importantes por topico

Son palabras claves conocidas y desconocidas mencionadas a lo largo del texto.

### Seguridad

1. Control de acceso

### Blockchain

1. Ledger
2. hash.
3. Concenso.
4. Miner




## Preguntas
1. ¿Que caso de uso vamos a usar en nuestro caso?




# Referencias

1. https://libroblockchain.com/wp-content/uploads/2018/07/Libro-de-Satoshi-Blockchain-Espana-v1-junio-2018.pdf ([link](https://libroblockchain.com/wp-content/uploads/2018/07/Libro-de-Satoshi-Blockchain-Espana-v1-junio-2018.pdf))
2. Bitcoin: un sistema de dinero en efectivo electrónico peer­to­peer([link](https://nakamotoinstitute.org/static/docs/bitcoin-es.pdf))
3. Bitcoin: A Peer-to-Peer Electronic Cash System ([link](https://bitcoin.org/bitcoin.pdf))
4. Blockchain and Money ([link](https://ocw.mit.edu/courses/sloan-school-of-management/15-s12-blockchain-and-money-fall-2018/index.htm))
5. https://blockchain.cse.iitk.ac.in/slides-NPTEL-BlockchainTechnologyApplications.pdf
6. https://www.ibm.com/cloud/architecture/architectures/blockchainArchitecture/reference-architecture
7. https://www.mdpi.com/2076-3417/10/19/6749/htm
8. https://gobiernodigital.mintic.gov.co/692/articles-179085_recurso_3.pdf
9. https://decbc.com/blog/what-is-asymmetric-cryptography/
10. https://hackernoon.com/
11. https://www.sciencedirect.com/science/article/pii/S240595951930164X#:~:text=The%20consensus%20of%20blockchain%20is,be%20aligned%20with%20the%20server.
12. https://itnext.io/pulling-the-blockchain-apart-the-transaction-life-cycle-381b76842c6
13. https://www.ibm.com/topics/what-is-blockchain
14. https://www.simplilearn.com/tutorials/blockchain-tutorial/blockchain-technology
15. https://arxiv.org/pdf/2106.04808.pdf
16. https://www.dummies.com/article/business-careers-money/personal-finance/cryptocurrency/what-is-a-blockchain-and-how-does-it-work-262432
17. https://hackernoon.com/asymmetric-cryptography-in-blockchains-d1a4c1654a71