# ejercicio-14-segunda-parte-laums25
ejercicio-14-segunda-parte-laums25 created by GitHub Classroom


\Primera pregunta: Con lambda=1, se obtiene una ecuación de tipo oscilador armónico.

\Segunda pregunta: Los tipos de solución que se obtienen son senos y cosenos.

\Tercera pregunta: Euler.cpp

\Cuarta pregunta: La función de yn(0), es decir la de la posición a partir de la cual se obtiene la velocidad siempre aumenta en función del tiempo, en este caso aproximadamente 0.01 en cada paso (correspondiente con el delta utilizado). (14.png)

\Quinta pregunta: Utilizando el código propuesto en clase, vemos que hay dos métodos para calcular el Runge-Kutta, donde la diferencia principal es que uno recibe valores por referencia, mientras que el otro utiliza vectores. Por otro lado, si comparamos el método de Euler con el de Runge-Kutta, vemos que en el primero las gráficas de yn(0) vs t y yn(1) vs t tienen una forma de oscilador armónico donde varía la amplitud (en relación a si se tienen un k muy grande o más pequeño), y en la gráfica de yn(0) vs yn(1) se obtienen varias elipses (por la variación de la amplitud). No obstante, por medio del método de Runge-Kutta se plotean las mismas gráficas, y se observan amplitudes iguales y una sola elipse (en la gráfica de yn(0) vs t y yn(1) vs t).  (Runge.cpp, Runge.py)

\Sexta pregunta: Al momento de graficar yn(0) vs yn(1) espero ver una gráfica ciclíca, ya que los datos para yn(1) se repiten para un determinado rango de t. Por consiguiente, cuando realizamos está gráfica obtenemos una especie de espiras elípticas, por el tipo de soluciones (senos y cosenos)

\Séptima pregunta: Rungefri.cpp Rungfri.png

\Octava pregunta: Cuando el valor de lambda es mayor a 1 la función tiende a ser lineal. (Runge2.cpp Runge2.png)

