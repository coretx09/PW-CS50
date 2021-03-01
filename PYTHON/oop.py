#OOP
'''La programmation orientée objet (OOP) permet de créer des objets que l'on peut manipuler .
 La OOP est un paradigme de programmation qui fournit un moyen de structurer
 les programmes afin que les propriétés et les comportements soient regroupés dans des objets individuels .

 La OOP se concentre sur les objets que les développeurs souhaitent manipuler plutôt que sur
 la logique requise pour les manipuler.

 La première étape de la OOP consiste à collecter tous les objets qu'un programmeur souhaite manipuler 
 et à identifier comment ils sont liés les uns aux autres - un exercice souvent appelé modélisation de données .

 Une fois qu'un objet est connu, il est étiqueté avec une classe d'objets qui définit le type de données
 qu'il contient et toutes les séquences logiques qui peuvent le manipuler. Chaque séquence logique distincte
 est appelée méthode.
'''

#CLASS
'''Une classe est un plan ou un prototype défini par l'utilisateur à partir duquel des objets sont créés
 Une classe est comme un constructeur d'objet, ou un "plan" pour créer des objets.

 Un plan pour définir la manière dont quelque chose doit être défini. Il ne contient en fait aucune donnée. 
 Les classes définissent des fonctions appelées méthodes , qui identifient les comportements et les actions
 qu'un objet créé à partir de la classe peut effectuer avec ses données.

 ATTRIBUTS:
   Les attributs sont les variables appartenant à une classe
  ATTRIBUTS D'INSTANCE :
   La valeur d'un attribut d'instance est spécifique à une instance particulière de la classe.
   La fonction __init __ () pour attribuer des valeurs aux propriétés de l'objet ou à d'autres opérations nécessaires
   lors de la création de l'objet
   Les propriétés que tous les objets doivent avoir sont définies dans la méthode appelée .__init__()

  ATTRIBUTS DE CLASS ou ATTRIBUTS STATIC :
    les attributs de classe sont des attributs qui ont la même valeur pour toutes les instances de classe.
    Les attributs de classe sont définis directement sous la première ligne du nom de classe(en dehors de .__init__() ) 
    en attribuant une valeur à un nom de variable 
  Les attributs sont toujours publics et sont accessibles à l'aide de l'opérateur point (.). Exemple: Myclass.Myattribute

  ATTRIBUTS SPECIALS :
   SPECIAL ATTRIBUTS in Python  start and end with the double underscores.
   Ils sont créés de manière implicite lors de la création d’une instance. 
   Ils contiennent des informations sur l’instance, for example: __dict__, __doc__, 
  
 METHODES:
  Les méthodes sont des fonctions qui sont associées de manière explicite à une classe.
  Elles ont comme particularité un accès privilégié aux données(attributs) de la classe elle-même.
  A part le premier paramètre qui doit de préférence s’appeler self, la syntaxe de définition d’une méthode
  ressemble en tout point à celle d’une fonction


 La création d'une nouvelle classe crée un nouveau type d'objet, permettant de créer de nouvelles instances de ce type
'''

#INSTANCE
'''Une instance est un objet qui est construit à partir d'une classe et contient des données réelles

 une classe est comme un formulaire ou un questionnaire. Une instance est comme un formulaire rempli
 d'informations.

  Chaque instance de classe peut avoir des attributs qui lui sont attachés pour conserver son état.
  Les instances de classe peuvent également avoir des méthodes (définies par leur classe) pour modifier leur état.

  Lorsqu'une nouvelle instance de classe est créée, l'instance est automatiquement passée au selfparamètre 
  dans .__init__()   afin que de nouveaux attributs puissent être définis sur l'objet.

  Chaque attribut d’une instance de classe est inséré dans un dictionnaire appelé __dict__
'''

#METHODES
'''
 INSTANCE METHODS:
  Les méthodes régulières (instance) ont besoin d'une instance de classe et peuvent accéder à l'instance via self.
  Ils peuvent lire et modifier librement l'état d'un objet.

  MAGIC METHODS OR DUNDER:
    Magic methods in Python are the special methods that start and end with the double underscores.
    for example: __init__, __str__ ......


 CLASS METHODS :
  Les méthodes de classe, marquées du @classmethod décorateur, n'ont pas besoin d'une instance de classe.
  Ils ne peuvent pas accéder à l'instance (self) mais ils ont accès à la classe elle-même via cls.
  les méthodes de classe peuvent modifier l'état de classe qui s'applique à toutes les instances de la classe

 STATIC METHODS:
  Les méthodes statiques, marquées du @staticmethod décorateur, n'ont pas accès à cls ou self.
  Elles fonctionnent comme des fonctions normales mais appartiennent à l'espace de noms de la classe.
  Par conséquent, une méthode statique ne peut ni modifier l'état de l'objet ni l'état de la classe.
  Les méthodes statiques sont limitées dans les données auxquelles elles peuvent accéder - 
  et elles constituent principalement un moyen d'espacer les noms de vos méthodes

 
'''