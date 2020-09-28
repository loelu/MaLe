## Antworten
### Was bedeuten die Kurven?
Die Kurven zeigen die cross validierten training und test scores im Verhältnis zu der Anzahl Trainingsdaten.
### Welchen Einfluss hat die Grösse des Trainingssets?
In unserem Fall mit n=20 ändern sich die Kurven kaum, egal wie gross das Traininsset ist. Die Scores betragen immer ca. 0.78.
### Wie verändern sie sich?
Mit einem kleineren n-Wert (n=5) steigt der trainings score auf >0.8, der test score sinkt jedoch auf ~0.75.
Bei einem grösserer Wert (n=30) verändern sich die scores kaum.
Ein Cross-Validation-Parameter von 2 (default ist 5), führt dazu, dass der Unsicherheitsbereich bei der Anzahl Trainingsdaten grösser wird. Jedoch nur bis ~3000 Trainingssets, danach stabilisieren sich die scores erneut bei ~0.78. 
### Welche Ihrer Eigenschaften können Sie erklären?
Der kleine n-Wert führt zu einem overfitting, was den höheren Trainingsscore und den tieferen Testscore erklärt. 
Die Trainingskurve liegt höher als die Testkurve, da das Modell auf den Trainingsdaten trainiert ist und diese somit besser hervorsagen kann. Mit der Erhöhung der Anzahl Testdaten sollten sich die Kurven jedoch nähern, da mit mehr Trainingsdaten bessere Voraussagen getroffen werden können.
### Was passiert bei wenn N=1 (Anzahl nearest neighbours)?  
Der training score ist immer 1, der test score jedoch unter 0.7. Der training score von 1 ist typisch für 1-nearest-neighbor, da damit nur genau auf die Trainingsdaten geschaut wird. Es liegt somit ein overfitting vor, was den tiefen test Wert erklärt.
### Liegt ein Overfitting vor?
Da die Trainingskurve und die Testkurve sehr nah beieinander liegen, sollte kein Overfitting vorliegen. Die Kurven sagen aus, dass das Modell auch mit Unbekannten Daten eine gleich gute Voraussage machen kann.
