# AlphaFold
AlphaFold es un programa de inteligencia artificial desarrollado por DeepMind que predice las estructuras de las proteínas con precisión comparable a los métodos experimentales. Utiliza un enfoque basado en aprendizaje profundo para modelar la forma en que las cadenas de aminoácidos se pliegan en estructuras tridimensionales complejas, proporcionando insights fundamentales para la biología y potencialmente acelerando la investigación biomédica y farmacéutica.

## Ejecución en la nube

AlphaFold no se ejecuta localmente debido a sus altos requisitos de hardware, que incluyen al menos 32 GB de RAM (o 16 GB), un procesador multicore moderno de Intel/AMD, una GPU potente de nVidia como la A100 con suficiente RAM para el plegamiento de proteínas más largas, y 3 TB de espacio en disco, idealmente en un SSD para acelerar la búsqueda de alineaciones múltiples de secuencias (o 1 TB con bases de datos reducidas). Estos [requisitos](https://github.com/google-deepmind/alphafold/issues/384) hacen que sea más viable y económico usar AlphaFold a través de plataformas en la nube que ya cuentan con la infraestructura necesaria. Puedes encontrar algunos ejemplos de ejecución/rendimiento [Aquí](https://www.rbvi.ucsf.edu/chimerax/data/alphafold-jan2022/afspeed.html).

# Hojas de Colab
Utilizaremos los scripts proporcionados por la comunidad y la capacidad de procesamiento de Google para ejecutar AlphaFold con nuestras propias secuencias de aminoácidos, con el fin de predecir el modelo en 3D. El repositorio en GitHub, [ColabFold](https://github.com/sokrypton/ColabFold), es fundamentalmente una colección de cuadernos de Google Colab diseñados para operar AlphaFold en diversos entornos de computación. Estos entornos se adaptan a las necesidades computacionales específicas de cada herramienta utilizada, lo que es crucial dado que los requerimientos de capacidad de procesamiento varían. Además, el artículo ["ColabFold: making protein folding accessible to all"](https://www.nature.com/articles/s41592-022-01488-1) ofrece una explicación detallada de estos cuadernos, incluyendo pruebas de rendimiento y análisis detallados para cada código. Este método facilita el acceso a la predicción de estructuras de proteínas sin la necesidad de contar con recursos computacionales avanzados, democratizando así la investigación en el plegamiento de proteínas.

### Links 

#### [Hojas de ColabFold](https://github.com/sokrypton/ColabFold)
#### [](https://biomedbiotec.encb.ipn.mx/bioinformatica/tablas/aminoacidos.html)

# Secuencias de aminoácidos (25 de abril)
En la clase del 25 de abril, se emplearán las siguientes secuencias de aminoácidos para estudiar cómo las modificaciones en ciertos aminoácidos impactan en la estructura tridimensional y cómo esto se relaciona con sus propiedades químicas:

ANSTVATDEHHHRWNTMILTNERKGPWFIATTR
ANSTVATDEHHHRWNTMILTNERKTTSNQNTTR

Esto proporcionará una comprensión práctica sobre la importancia de la secuencia en la conformación y función de las proteínas.

# Información del curso
Este curso es impartido en el COLEGIO DE MATEMÁTICAS BOURBAKI, con los profesores Carlos Alfonso y Álvaro de Obeso. También se contó con la ayuda de Ángel Pedrés, en colaboración con BioPlaster para la elaboración de scripts y ejecución del modelo.
