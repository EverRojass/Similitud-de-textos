from nltk import ngrams
from nltk.tokenize import word_tokenize
import string

def comparar_ngramas(texto1, texto2, n):
    # Tokenización de los textos, quitando signos de puntuacion.
    tokens_texto1 = word_tokenize(texto1.translate(str.maketrans({key: None for key in string.punctuation})))
    tokens_texto2 = word_tokenize(texto2.translate(str.maketrans({key: None for key in string.punctuation})))
    
    # Convertir los tokens a minúsculas
    tokens_texto1 = [token.lower() for token in tokens_texto1]
    tokens_texto2 = [token.lower() for token in tokens_texto2]

    # Generación de n-gramas para ambos textos
    ngramas1 = set(ngrams(tokens_texto1, n))
    ngramas2 = set(ngrams(tokens_texto2, n))
    
    # Cálculo de la intersección de n-gramas
    interseccion = ngramas1.intersection(ngramas2)
    
    # Cálculo de la similitud basada en la cantidad de n-gramas compartidos
    similitud = len(interseccion) / max(len(ngramas1), len(ngramas2))
    
    print ("Similitud: ",similitud)
    print("Segmentos iguales: ", interseccion)

#REPORTES DE LECTURA MIOS.
#William Wilson
libro1 ="Introducción Libro relato el narrador pide que por el momento se le llame William Wilson y este empieza a dar una entrada de lo que sería un discurso que se acerca a la aproximación de que va contar una historia de su vida y dice que es la crónica de un hombre que ha vivido atado o sujeto a sus decisiones y actos que lo ha llevado a vivir ansiedad para la gente que lo rodea y perjuicios para él. Que ha sido gobernado por el mismo y sin escuchar las acciones que sus padres para contener sus malos actos o tendencias y que a su temprana edad se convirtió en el amo de todas sus acciones.Desarrollo Empieza a contar donde había vivido en un pueblo en Inglaterra en un lugar lleno a árboles era como un lugar de ensueño. Había una iglesia que hacía sonar sus campanas cada hora y dice que recordar su niñez es el mayor placer que puede tener actualmente pues le hacen recordar la presencia de sus primeros avisos de su destino más adelante en su vida. Vivía en una casa antigua de ladrillos de que estaba en una parte alta, tenía las ventanas con vidrios rotos, pero parecía una cárcel solo salían tres veces por semana, una los sábados y otras dos los domingos cuando tenían que ir al culto. Resulta que el director de la escuela era también el pastor, era un hombre serano, reverente y benigno. La casa tenía un muro de forma irregular, el piso estaba construido de pequeña gravilla. Por lo tanto, era un lugar muy extraño. Dentro de la casa había varias aulas de clases parecían abandonadas porque todo era viejo, con sus sillas para las personas y las pizarras muy desgastadas como si nadie las hubiera utilizado desde hace mucho tiempo. Entonces este personaje paso ahí sus hasta sus quince años de edad. Cuenta que tuvo una vida no tan monótona que aún recuerda esos momentos de diversión y todo lo que había vivido en su niñez, esos recuerdos aun los guarda en su memoria. Pero de joven el entusiasmo de su naturaleza lo destaco y gano jerarquía entre sus demás compañeros de la casa donde vivía. Pero resulta que había otro joven con quien compartía nombre y apellido y era su competencia era igual de listos que él. Era el joven que se oponía a que el fuera el mejor de aquel grupo. Este otro chico llamado Wilson era una persona que siempre se oponía al personaje principal del libro y que trataba de minimizarlo con insultos, intentaba dejarlo mal frente a los demás como si fuese un enemigo, pero resulta que Wilson el narrador también sentía la inseguridad de que ese personaje fuese mejor que él.  A pesar que el narrador odiara tanto al otro Wilson había una brecha línea de respeto hacia con los dos, es decir existía esa brecha de buenas relaciones, pero como cada uno mantenía su orgullo de ser el mejor del grupo. Y aun así era compañeros inseparables. Resulta que las represalias y ataques del otro Wilson le parecían odiosas y de testante había algo que lo hacían molestar más que todo, esto era que llevara el mismo nombre que él, y se sentía muy incómodo ya que tenía que convivir con él en todas las actividades. Wilson trataba de imitar todo del protagonista del libro, desde su vestimenta, su voz, su estatura y hasta casi su rostro, y todos sus condiscípulos que habitaban en esa misma escuela y habitación estaban convencidos de que estas dos personas tenían algún tipo de parentesco. Llego el punto en que Wilson termino con la paciencia del protagonista que este empezó a tomarle odio y se separaron de su amistad. Desde entonces sintieron más odio entre uno y otro que el narrador recuerda como la última vez que hablaron por última vez. La casa donde vivían ya estaba vieja y contenía varias subdivisiones y en las más pequeñas era donde vivía Wilson. Una noche el protagonista intento hacerle una broma a su homólogo y compañero de escuela el otro Wilson, mientras el otro dormía, este se acercó con su lámpara para llegar a su dormitorio y mientras dormía intento ejecutar su hazaña, pero al momento de verlo ahí acostado se dio cuenta que no era el, es decir si era el, pero parecía otra persona con otros rasgos, entonces este se asustó tanto que abandonó inmediatamente el lugar. Después de un tiempo el Wilson protagonista se fue a otra escuela en Eton Inglaterra en ese pequeño segmento de tiempo basto para que se olvidara, aunque sea un poco de su mal paso por la escuela en la que había estado. Una vez se juntó con los estudiantes más extravagantes de aquella escuela y armo una fiesta para celebrar toda la noche cuando de repente le avisaron que alguien preguntaba y reclamaba por el afuera del lugar donde estaban. Era un joven que se le acercó y le dijo al ido su nombre y en ese momento su embriaguez desapareció casi en total. Le hizo venir varios recuerdos a su mente, era una voz muy conocida la que le había susurrado en voz baja y sobre todo el carácter de aquella persona que le hablo en ese momento repentino porque después de un momento había desaparecido. Pasado un tiempo el William Wilson original se salió del colegio de Eton y se fue a Oxford ya que sus padres podían pagarle todo tipo de lujo y extravagantes delirios. Una vez mientras estudiaba en la universidad de Oxford llego un joven muy rico a a la misma escuela, William se había dado cuenta que el hombre nuevo era demasiado adinerado con mucho poder, por lo tanto, quería proponerle un juego de apuestas y embriagarlo para ganarle todo o amenos un poco de dinero pues ya sabía que el dinero le sobraba, así que preparo todo tal cual le salió porque lo hizo endeudarse demasiado. Pero justo cuando William se preparaba para retirarse con todo el dinero que habían ganado en el juego llego a lugar un hombre que le conto a todos los presentes en la mesa de juego que William había hecho trampa porque había falseado las cartas y que las tenía escondidos en los bolsillos de su chaqueta, esa noche William fue expuesto y quedo como antagonista que lo corrieron de la universidad de Oxford y fue echado del aquel lugar. Resulta que el hombre que siempre lo vigilaba lo seguido a todos lados en donde fue, y que era el mismo de la escuela de infancia su mayor enemigo y también en Eton, Oxford y lo siguió a varios a lados donde después fue. En una fiesta en Roma con el duque napolitano William quiso pasar la noche con la esposa del duque y empezó a perseguirla cuando se aproximaba hacia ella, un brazo lo tomo por el hombro, entonces este quiso terminar con la vida de una vez por todas con el hombre que siempre lo había atormentado. Cuando volteo a verlo era un hombre con el mismo rostro que el mismo disfraz, tuvieron un gran combate los dos y le atravesó su espada y el hombre moribundo era Wilson el mismo de la escuela de su infancia pero el hombre le dijo que se había asesinado el mismo, porque siempre había sido el mismo su mismo tormento."
wiliamwilson ="Introducción En la parte introductoria del relato el narrador pide que por el momento se le llame William Wilson y este empieza a dar una entrada de lo que sería un discurso que se acerca a la aproximación de que va contar una historia de su vida y dice que es la crónica de un hombre que ha vivido atado o sujeto a sus decisiones y actos que lo ha llevado a vivir ansiedad para la gente que lo rodea y perjuicios para él. Que ha sido gobernado por el mismo y sin escuchar las acciones que sus padres para contener sus malos actos o tendencias y que a su temprana edad se convirtió en el amo de todas sus acciones.Desarrollo Empieza a contar donde había vivido en un pueblo en Inglaterra en un lugar lleno a árboles era como un lugar de ensueño. Había una iglesia que hacía sonar sus campanas cada hora y dice que recordar su niñez es el mayor placer que puede tener actualmente pues le hacen recordar la presencia de sus primeros avisos de su destino más adelante en su vida. Vivía en una casa antigua de ladrillos de que estaba en una parte alta, tenía las ventanas con vidrios rotos, pero parecía una cárcel solo salían tres veces por semana, una los sábados y otras dos los domingos cuando tenían que ir al culto. Resulta que el director de la escuela era también el pastor, era un hombre serano, reverente y benigno. La casa tenía un muro de forma irregular, el piso estaba construido de pequeña gravilla. Por lo tanto, era un lugar muy extraño. Dentro de la casa había varias aulas de clases parecían abandonadas porque todo era viejo, con sus sillas para las personas y las pizarras muy desgastadas como si nadie las hubiera utilizado desde hace mucho tiempo. Entonces este personaje paso ahí sus hasta sus quince años de edad. Cuenta que tuvo una vida no tan monótona que aún recuerda esos momentos de diversión y todo lo que había vivido en su niñez, esos recuerdos aun los guarda en su memoria. Pero de joven el entusiasmo de su naturaleza lo destaco y gano jerarquía entre sus demás compañeros de la casa donde vivía. Pero resulta que había otro joven con quien compartía nombre y apellido y era su competencia era igual de listos que él. Era el joven que se oponía a que el fuera el mejor de aquel grupo. Este otro chico llamado Wilson era una persona que siempre se oponía al personaje principal del libro y que trataba de minimizarlo con insultos, intentaba dejarlo mal frente a los demás como si fuese un enemigo, pero resulta que Wilson el narrador también sentía la inseguridad de que ese personaje fuese mejor que él.  A pesar que el narrador odiara tanto al otro Wilson había una brecha línea de respeto hacia con los dos, es decir existía esa brecha de buenas relaciones, pero como cada uno mantenía su orgullo de ser el mejor del grupo. Y aun así era compañeros inseparables. Resulta que las represalias y ataques del otro Wilson le parecían odiosas y de testante había algo que lo hacían molestar más que todo, esto era que llevara el mismo nombre que él, y se sentía muy incómodo ya que tenía que convivir con él en todas las actividades. Wilson trataba de imitar todo del protagonista del libro, desde su vestimenta, su voz, su estatura y hasta casi su rostro, y todos sus condiscípulos que habitaban en esa misma escuela y habitación estaban convencidos de que estas dos personas tenían algún tipo de parentesco. Llego el punto en que Wilson termino con la paciencia del protagonista que este empezó a tomarle odio y se separaron de su amistad. Desde entonces sintieron más odio entre uno y otro que el narrador recuerda como la última vez que hablaron por última vez. La casa donde vivían ya estaba vieja y contenía varias subdivisiones y en las más pequeñas era donde vivía Wilson. Una noche el protagonista intento hacerle una broma a su homólogo y compañero de escuela el otro Wilson, mientras el otro dormía, este se acercó con su lámpara para llegar a su dormitorio y mientras dormía intento ejecutar su hazaña, pero al momento de verlo ahí acostado se dio cuenta que no era el, es decir si era el, pero parecía otra persona con otros rasgos, entonces este se asustó tanto que abandonó inmediatamente el lugar. Después de un tiempo el Wilson protagonista se fue a otra escuela en Eton Inglaterra en ese pequeño segmento de tiempo basto para que se olvidara, aunque sea un poco de su mal paso por la escuela en la que había estado. Una vez se juntó con los estudiantes más extravagantes de aquella escuela y armo una fiesta para celebrar toda la noche cuando de repente le avisaron que alguien preguntaba y reclamaba por el afuera del lugar donde estaban. Era un joven que se le acercó y le dijo al ido su nombre y en ese momento su embriaguez desapareció casi en total. Le hizo venir varios recuerdos a su mente, era una voz muy conocida la que le había susurrado en voz baja y sobre todo el carácter de aquella persona que le hablo en ese momento repentino porque después de un momento había desaparecido. Pasado un tiempo el William Wilson original se salió del colegio de Eton y se fue a Oxford ya que sus padres podían pagarle todo tipo de lujo y extravagantes delirios. Una vez mientras estudiaba en la universidad de Oxford llego un joven muy rico a a la misma escuela, William se había dado cuenta que el hombre nuevo era demasiado adinerado con mucho poder, por lo tanto, quería proponerle un juego de apuestas y embriagarlo para ganarle todo o amenos un poco de dinero pues ya sabía que el dinero le sobraba, así que preparo todo tal cual le salió porque lo hizo endeudarse demasiado. Pero justo cuando William se preparaba para retirarse con todo el dinero que habían ganado en el juego llego a lugar un hombre que le conto a todos los presentes en la mesa de juego que William había hecho trampa porque había falseado las cartas y que las tenía escondidos en los bolsillos de su chaqueta, esa noche William fue expuesto y quedo como antagonista que lo corrieron de la universidad de Oxford y fue echado del aquel lugar. Resulta que el hombre que siempre lo vigilaba lo seguido a todos lados en donde fue, y que era el mismo de la escuela de infancia su mayor enemigo y también en Eton, Oxford y lo siguió a varios a lados donde después fue. En una fiesta en Roma con el duque napolitano William quiso pasar la noche con la esposa del duque y empezó a perseguirla cuando se aproximaba hacia ella, un brazo lo tomo por el hombro, entonces este quiso terminar con la vida de una vez por todas con el hombre que siempre lo había atormentado. Cuando volteo a verlo era un hombre con el mismo rostro que el mismo disfraz, tuvieron un gran combate los dos y le atravesó su espada y el hombre moribundo era Wilson el mismo de la escuela de su infancia pero el hombre le dijo que se había asesinado el mismo, porque siempre había sido el mismo su mismo tormento."

#Diario de un loco
diariodeunloco="Este libro es un relato de una persona que escribe un diario, pero no es un diario normal, más bien  lo escribe una persona que tiene problemas mentales y que tiene alucinaciones por eso el título del libro. No lleva un orden en las fechas o así está escrito el libro.El personaje se llama Aksanti Ivanovich es un noble de Rusia. Empieza a relatar en la fecha 3 de octubre pero no especifica año y dice que realmente no tiene nada, trabaja en una empresa y su oficio es sacarle puntas a los lápices, que a menudo es humillado y regañado por su jefe inmediato, Aksanti dice que su jefe le tiene envidia porque él trabaja en la oficina del director general y que por eso siempre lo quiere humillar cuando llega tarde o hace algo mal.Ese día saliendo de su trabajo, estaba la lluvia y vio el carro de su jefe en un sitio, pero era su hija la que iba en ese carro, en ese instante se acercó disimuladamente y oyó voces hasta que se da cuenta que son unas perritas las que hablan, y que estas perritas se comunican entre sí, ya que una perrita que se llama Fideli es de la hija de su director y la otra Medji es de una familia que  vive por la zona. Pero a este personaje le interesa la hija del director quiere saber de ella, por medio de su perrita llamada Fideli.Se da cuenta que las perritas hablan y que a menudo se mandan cartas, así que decide seguir a Medji, la perrita a quién le llegan las cartas de Fideli, para saber dónde vive y poder venir en otra ocasión.Llega el día 4 de octubre y en este relato cuenta se tuvo un encuentro con la hija del director que era joven y bella. La chica le pregunto por su papa, y este le contesto que no, aunque en su mente pensaba muchas cosas en ese instante queriéndole decir pero que su voz no le permitía. Llegando a su casa empezó a escribir un poema.Llega el día 6 de noviembre, en este día el jefe de personal lo llama a su oficina y lo regaña diciéndole porque se ha dado cuenta que anda detrás del director y le dice que él es un cero y otras palabras ofensivas.  Aksanti no le dice nada se queda callado pero en su mente piensa todas las cosas que le hubiese querido contestar. El día 8 de noviembre, cuenta que estuvo en el teatro y que se divirtió mucho.El día 11 de noviembre estuvo en el despacho del director y saco punta a veinticuatro plumas, a Aksanti le da curiosidad en interés que es lo que piensa el director ya que siempre esta callado. Aunque  intenta platicar con el no puede más que solo unas cuantas palabras acerca de tiempo. Se acuerda de la conversación de las dos perritas y se acuerda de las cartas y decide ir a buscar el nido de la perrita para encontrar las cartas y averiguar todo sobre la  familia del director, dijo que los perros son mucho más inteligentes que las personas y que incluso pueden hablar pero son bastante tercos.El día 12 de noviembre cuando llega a  buscar a la perrita Fideli quien recibe las cartas de Medji, el olor de repollo sale de todas las casas, entro a la casa de Fideli a robar las cartas y se fue a su casa.El 13 de noviembre empieza a leer las cartas, en esas cartas Medji le cuenta muchas cosas a Fideli, cosas de lo que pasa en la casa del director, se admira de la buen escritura de los perros. En las cartas cuenta cosas que se viven en esa casa día a día, sobre como actúa el papa que es el director de donde trabaja, y también la perrita cuenta cosas de su señorita Sofía, la hija del director. También  Aksanti se da cuenta que la perrita habla de él y lo describe una persona desagradable.También se cuenta que el director quiere casar a su hija con general o coronel lo cual lo hace ponerse triste pero también enojarse porque por no ser un general o alguien de la cámara no podría obtener su mano y no los consideran importante. Después rompe las cartas.Llega el día 3 de noviembre según la fecha del personaje,  Aksanti se entera que si habrá boda de Sofía con el general.El día 5 de diciembre lee un periódico donde anunciaba que España se había quedado sin rey, se decía que lo iba ocupar una mujer, pero Aksanti se decía que eso era imposible, que era necesarios que el lugar lo ocupara un hombre para que fuera el rey.El día 8 de diciembre cuando se iba a ir a su trabajo, se acuerda de que España no tiene rey y no puede aceptar que existe una reina decía que había muchos asuntos políticos que le iban a traer problemas a España y así se la paso todo el día pensando en eso.Llega el año 2000, 3 de abril según la fecha de diario del personaje, entre sus alucinaciones Aksanti dice que él es el rey de España y lo han nombrado a él. Se lo dice a Marva con quien vive, se pone feliz que ya no va trabajar de lo que hace tan odioso y que ya no lo humillaran.El 86 de marzo entre el día y la noche vinieron a buscarlo de su trabajo porque hace tres semanas que ya no iba, y se va a las oficinas pero él iba pensando que era el rey de España y que todos deberían admirarlo y venerarlo, pero aún no lo sabían. Después de esto empezó a imaginarse muchas cosas que solo el pensaba pero no decía. Un día sin fecha. Fue disimuladamente a Nevsky, quería un traje de rey ya que no tenía. Así que consiguió tela y se lo hizo el mismo.El día 1º no especifica mes ni año. Estaba esperando que llegaran los diputados de España para que se reunieran con él. Entonces fue a la oficina de correos para que le informaran acerca de ellos, donde le dijeron que no sabían nada de eso.Madrid, 30 de febrero, Aksanti se encuentra en España se dice ser e rey, dice que se presentaron donde él estaba los diputados españoles y se fue con ellos en una carroza pero realmente se lo habían llevado preso, lo que era la realidad. El imagina ser el rey pero no era así. Cuenta que vio personas con la cabeza rapada pensaba que eran dominicos pero en realidad eran presos.Aksanti estaba imaginando cosas en su cabeza que ya no eran reales. Imaginaba a los policías como diputados de su corte pero estos lo golpeaban y eso no lo entendía. Después lo encierran.El día  34 de febrero de 343, cuando por fin se da cuenta de la realidad que vive, se lamenta que nadie lo escucha ni le hace caso, que no está viviendo en la realidad, pensaba que era el rey de España pero no lo trataban como tal, lloraba de tanto martirio y miraba a lejos de norte imaginando estar en casa con su madre."
#La rebelion de la granja
larebelion="Era una granja del señor Jones, donde vivían muchos animales, caballos, gallinas, cerdos, vacas, un burro, entre otros animales. Una noche cuando Jones ya se iba a dormir, se le olvido cerrar las trampillas de la granja. Así que solo tomo un poco más de cerveza y se fue a acostar. Cuando se apagó la luz todos los animales salieron a reunirse en un lugar porque el comandante quien era un cerdo de doce años ya veterano deseaba contar a todos los sueños que había tenido la noche anterior, y así empezaron a llegar todos los animales cada uno, además que les gustaba escuchar las palabras del cerdo que era muy respetado. Cuando todos estaban acomodados para escucharlo comenzó a hablar y reflexionar sobre la vida que ellos llevan como animales, para recordarles que todo su trabajo no es valorado porque una vez llegan a viejos los matan y eso no es felicidad. Les dijo que los humanos son sus enemigos, si nos deshacemos de los humanos, entonces seremos felices porque ellos son lo que daña el mundo. Son los únicos seres que disfrutan de nuestro trabajo sin hacer nada. Todas estas palabras les dijeron el cerdo conocido como el comandante, además les dijo que debían hacer una rebelión, no tenía una fecha fija pero que en algún momento lo iban a lograr, debían contar esto a todas sus generaciones, aunque ellos murieran sus futuras generaciones lograrían hacer el objetivo y seguir luchando por su libertad. Después el cerdo les conto el sueño que había tenido, cantando una canción que hablaba acerca de la esperanza de la libertad. Tres noches más tarde el cerdo murió. Aprendieron la canción y enseñaron a todos los animales las ideas que les había dado el cerdo, había tres cerdos más que lideraban a los demás animales porque eran los más inteligentes. Por lo tanto, hacían sus reuniones secretas y estaban dispuestos a hacer su rebelión. Una vez que ya se habían cansado de pasar hambre después de tres días de no comer una de las vacas rompió e granero y todos los animales entraron a comer. El dueño de la granja y sus peones empezaron a golpear a los animales, entonces estos se defendieron y pegaron a los humanos que los cuidaban al ver su raro comportamiento, los peones y el dueño de la granja salieron huyendo por rumbos desconocidos. Los animales habían quedado libres y felices ahora, la granja les pertenecía y podían hacer lo que ellos querían. Pero redactaron sus mandamientos que debían seguir. Así trabajaron bien organizados por bastante tiempo, crearon reglas, siguieron sus mandamientos y trabajaban en equipo. Todos los animales habían entendido sus deberes a excepción de unos como la gata y algunos otros que no les gustaba trabajar mucho. Empezaron a aprender a leer y a escribir, los cerdos eran los más inteligentes porque dirigían a toda la granja y siempre aprendían por lo tanto estudiaban libros de ingeniería entre otros. Tiempo después corrían los rumores de lo que había sucedido en la granja, las palomas llevaban los mensajes a las granjas vecinas, y todo el lugar rumoraba y tenía miedo de estos sucesos incluso lo humanos. Jones el granjero estaba molesto y con intenciones de recuperar sus propiedades. Regreso con un grupo de hombres y con armas para luchar contra los animales. Pero los cerdos ya tenían un plan preparado ante un ataque y lo llevaron a cabo, pelaron y en la guerra murió una cabra, además hubo héroes de aquella batalla que ganaron por la retirada de los granjeros, que huyeron de miedo. Surgieron problemas, porque salió la idea de que se debían construir un molino de viento, pero había división en las decisiones que tenía que hacer ya que un cerdito llamado bola de nieve proponía hacerlo, pero el otro decía que no había necesidad. Al final de tantos problemas y discusiones bola de nieve fue expulsado de la granja por ser considerado un farsante. Al final de todo se empezó el proyecto que llevaría dos años. Todo ese año trabajaron como esclavos, se levantaban más temprano porque tenían un objetivo claro, no les daba mucho tiempo de sembrar y cosechar, pero les daba satisfacción que su molino de viento ya estaba a casi la mitad de su construcción. El líder de lo animales decidió hacer negocios con los productos que producían, vendía en el mercado del lugar, pero lo hacía a través de un hombre llamado wyner. Al principio lo demás animales se opinión ya que las leyes que habían dictado después de correr a Jones de la granja decía que no había que tener contacto con los humanos nunca más. Pero después de todo se resolvió, lo harían con cuidado y mejoraría su forma de vida. Algunos animales fueron ejecutados por los perros por órdenes de Napoleón el líder, debido a que habían cometido actos de traición a la granja, todos los animales estaban consternados y tristes porque no era lo que deseaban cuando el viejo comandante le había llamado a la rebelión. Tuvieron otra batalla con los humanos que los habían venido a atacar, ganaron la guerra, pero ello con explosivos habían destruido el molino de viento ya que algunos granjeros rumoraban y envidiaban a la granja. Así pasaba el tiempo, el líder el cerdo napoleón tomaba decisiones sin consultar a los animales y que en ocasiones violaban los mandamientos escritos que debían seguir. Los cerdos eran más beneficiados porque llevaban una vida más cómoda, eran órdenes del líder. La organización se había vuelto una dictadura donde el líder daba las órdenes y modificaba las leyes a su favor. El caballo había enfermado, ya era muy viejo, a pesar de su edad seguía trabajando, creía que napoleón siempre tenía la razón y se esforzaba demasiado. Por eso surgió el rumor de que napoleón lo llevaría al hospital de animales a curarlo, pero cuando vino una camioneta a recogerlo, algunos animales notaron que se lo llevaban al matadero e intentaron avisarle para que saliera de ahí. No se pudo, así que el caballo de fue. Tiempo después se supo que murió.  Al fin el líder y gobernante de la granja animal había roto todas la reglas y normas a su favor. Lo cerdos eran los únicos con privilegios, los demás animales trabajaban como esclavos, pasaban hambre y frio. Una el cerdo tuvo una fiesta privada con los demás granjeros dentro de la casa donde no podía entrar otro animal. Los cerdos habían aprendido a comportarse como humanos, se vestían como ellos, fumaban y tomaban cerveza. Napoleón se habían convertido en un régimen que gobernaba y se aprovechaba de todos los animales de la granja, en la fiesta los animales supieron que el espíritu de hermandad y guerra ya no estaba. Todo se perdió. La granja se convirtió en una república gobernada por cerdos con más privilegios que los demás animales. "


#REPORTES DE OTROS ALUMNOS
#LA ULTIMA PREGUNTA
librolapregunta1="Esta historia comienza con computadoras que han surgido y que están a escala universal llamadas Multivac, esta historia se centra en la vida hacia el futuro en el año 2061 donde nos dice y nos menciona que la humanidad se bañó en luz y que todas las personas se hacen la misma pregunta durante mucho tiempo. Se busca respuesta a la última pregunta hecha por los personajes, ¿cómo puede disminuirse masivamente la cantidad neta de entropía del universo? A lo largo del libro durante diferentes periodos de tiempo se plantea la pregunta de cómo revertir el desgaste que lleva al colapso del universo. La entropía planteada en el libro sería nuestro universo desgastándose con el paso del tiempo lo cual lo lleva al desequilibrio hasta que finalmente llega a colapsar con la extinción de la humanidad. Pero a pesar de que el universo continuaba desgastándose se tomaron algunas medidas que mantuviera en tanto se podía el equilibrio de la vida. Se almacenó, modifico y utilizó la energía del sol en todo el planeta. Por mucho tiempo Multivac ayudo a las personas a diseñar naves que permitieran ir y llegar a otros planetas como Marte, Venus incluso a la Luna ya que para ello encontraron una planta hacia la Luna que hiciera que fusionara los rayos de la luz solar de una manera invisible, pero con el paso del tiempo los recursos se fueron agotando y ya no alcanzaban para los viajes largos que realizaban. El propósito era evitar el colapso del planeta, pero además que la energía del sol no se agotara. Para evitar el colapso del planeta se generó una propia fuente de recursos que no fueran el carbono pero que se alimentara del sol, sin embargo, el sol también se agotaría y colapsaría como todo en el mundo, para ello buscaban respuestas en las máquinas de Multivac, pero esta solo decía: “DATOS INSUFICIENTES PARA UNA RESPUESTA ESCLARECEDORA.” Al tener su propia fuente de energía con el paso del tiempo fue suficiente para que los humanos se expandieran a otras galaxias en el universo alcanzando la inmortalidad. Con lo anterior descrito los cuerpos y las mentes cambiaron fusionándose en una sola mente, donde finalmente se fusiono en el propio Multivac. Alexander Adell, Bertram Lupov y los asistentes de Multivac tenían claro el objetivo: Buscar una fuente alterna de energía en la cual todos trabajaron en conjunto con Multivac para hacerlo realidad. La computadora analógica que existía (AC) demostró y pensó en todo el desastre que había sucedido durante su largo tiempo de vida que la inventaron por lo que después de todo el caos la computadora analógica dijo ¡HAGASE LA LUZ! Y la luz se hizo."
librolapregunta2="La obra la última pregunta es del género ciencia-ficción con una visión futurista con respecto a la Inteligencia Artificial. La historia comienza en el año 2061 entre dos hombres comenzando con una apuesta, la cual era hacer una pregunta, sin saber que sería la última. Los dos hombres en conjunto con otros asistentes trabajaban con Multivac que era una computadora tan compleja de usar y entender que solo podían hacer poco con ella. Se podían hacer preguntas y esta respondía de acuerdo a toda la información recopilada después de tanto tiempo, así como el poco mantenimiento que se podía hacer ya que esta se autoajustaba y corregía. Realmente lo que los asistentes podían hacer no era increíble ya que esto lo podía hacer cualquiera en esa era. Ya que los recursos de la Tierra ya se habían consumido en gran medida, se necesitaba otra fuente que proveyera energía, así que comenzaron a diseñar estrategias que reemplazaran materiales como el carbono. Una de las soluciones fue crear naves para viajar a otros planetas y explorar los recursos de estos; sin embargo, no se tuvo éxito ya que las naves no resistieron. Pero Multivac logró resolver el problema; se crearon sistemas alrededor de la órbita que recibiera y transformara la energía del sol para utilizarla. Los asistentes ya las dos personas sobresalientes se alegraron por encontrar una solución y se dieron la propia recompensa de tomar un descanso hablando sobre el gran logro. Uno de ellos dijo que estaba realmente contento porque habían encontrado energía infinita, pero ¿realmente lo habían hecho?  Ante esta afirmación la otra persona reaccionó argumentando que todo se acaba, todo tiene un ciclo y eso significaba que quizá algunos miles de millones de años aprovecharían el sol, sin embargo, este también se agotaría y se acabaría. Pasando a otra era donde una familia tenía que mudarse a otro planeta una de las pequeñas de esta familia preguntó porque tenían que mudarse de su lugar de origen a lo que el padre respondió que debido a que los recursos se habían agotado y debían buscar un lugar donde que les permitiera seguir viviendo por lo que la pequeña comenzó a llorar, su madre la consoló diciendo que seguramente la máquina (sucesora de Multivac) podría dar una respuesta para solucionar el problema. Sin embargo, el resultado no fue diferente a lo que el padre mencionó. Miles de años más tarde donde las personas vivían en galaxias diferentes y se comunicaban a través de herramientas mucho más avanzadas, dos niños se preguntaban por los nombres de sus galaxias y el nombre de la galaxia original donde se originó la vida, sin embargo, no lo sabían así que preguntaron a la máquina y esta resolvió su duda, también preguntaron si algún día podrían resolver el problema de la energía para no acabarse la energía del sol, pero esta seguía sin resolver el enigma. Cuando el humano acabó casi con toda la existencia y quedaba solo un rayo de luz volvió a preguntar si sabía como resolver el problema de la energía sin embargo seguí sin poder responder objetivamente. La vida terminó y entonces Multivac analizó todo aquello que aprendió, que más podría pasar, así que inició una nueva era de la vida."

#PRUEBAS 1 EXAMEN ORDINARIO 
texto1="Hola mundo!"
texto2="Hola mundos!"

#PRUEBAS 2 EXAMEN ORDINARIO 
texto3="Matemáticas Aplicadas II"
texto4="Inteligencia Artificial"

similitud = comparar_ngramas(texto3,texto4,1)  


