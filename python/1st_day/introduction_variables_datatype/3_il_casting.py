# Il casting è una tecnica per cambiare il tipo di dato di un dato
#
# linguaggi di programmazione TIPIZZATI
#
# Il tipo di una variabile va specificato al momento della dichiarazione
# e una volta definita la variabile potrà contenere solo quel tipo.
#
# ES. linguaggio C
#
# int age = 30;
# float height = 177.7;
# char gender = ‘M’;
#
# linguaggi di programmazione NON TIPIZZATI o DINAMICAMENTE TIPIZZATI
#
# Il tipo di una variabile non va specificato e una volta definita
# la variabile potrà contenere qualsiasi tipo.
# vantaggio - codice flessibile
# svantaggio - si creano disastri facilmente
#
# Python è NON TIPIZZATO
#
# ES. PYTHON
# weight = 80 # int
# weight = 80.5 # float
# weight = “80.5 Kg” # str
#
# meglio scrivere
#
# weight_int = 80 # int
# weight_float = 80.5 # float
# weight_str = “80.5 Kg” # str
#
# Anche lavorando con linguaggi non tipizzati,
# utilizza sempre uno stesso tipo per una variabile
#
#
# ALTRA DISTINZIONE DA FARE:
#
# TIPIZZAZIONE DEBOLE e TIPIZZAZIONE FORTE
#
# TIPIZZAZIONE DEBOLE
# Nel caso di tipizzazione debole, il linguaggio di programmazione potrebbe
# convertire implicitamente il contenuto della variabile da un tipo ad un altro
#
# ES. JavaScript
# var weightInt = 80 // int
# var weightStr = “80.5 Kg” // str
# weightInt + weightStr // “8080.5 Kg”
#
#
# TIPIZZAZIONE FORTE
# Nel caso di tipizzazione forte, il tipo di una variabile non viene mai modificato implicitamente,
# ma questo va fatto in maniera esplicita. (BISOGNA UTILIZZARE IL CASTING).
#
# ES. PYTHON
# weight_int = 80 # int
# weight_str = “80.5 Kg” # str
# weight_int + weight_str # TypeError
#
#
# Vediamo il CASTING
#
# weight = 80
# weight_float = float(weight) # 80.0
# weight_int = int(weight_float) # 80
#


