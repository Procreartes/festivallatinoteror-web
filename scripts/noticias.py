"""Noticias de la web. La más reciente, primero.

Para añadir una noticia: copia un bloque, cambia los datos y ejecuta
python3 scripts/generar.py. 'imagen' es la ruta sin el sufijo -800.webp.
"""

NOTICIAS = [
    {
        "slug": "mas-de-5000-personas-30-aniversario",
        "fecha": "2026-07-27",
        "titulo": "Más de 5.000 personas celebraron en Teror el 30.º aniversario de su Festival Latino",
        "resumen": "La edición más ambiciosa de sus tres décadas: una semana de talleres, la jornada «Gran Canaria Joven» y una gala internacional con Tony y Mimy Succar y Tromboranga.",
        "imagen": "img/carteles/banner-30",
        "imagen_alt": "Cartel del 30.º Festival Latino Villa de Teror",
        "anchos": [800, 1600],
        "cuerpo": """
<p class="entradilla">El 30.º Festival Latino Villa de Teror reunió a más de 5.000 personas en la Plaza de Sintes, en la edición más ambiciosa de sus tres décadas de historia.</p>
<p>Organizado por el Ayuntamiento de Teror, el festival creció durante toda una semana, con talleres de baile latino cada tarde, hasta culminar el sábado 25 de julio en una gala internacional encabezada por los peruanos Tony y Mimy Succar, primeros artistas de su país en ganar un Grammy.</p>
<p>Treinta años después de su nacimiento, el festival volvió a confirmarse como una de las grandes citas del verano en Gran Canaria y como parte de la identidad cultural de la Villa Mariana. La edición del aniversario combinó el talento local con figuras internacionales de primer nivel.</p>
<h2>Toda la semana: talleres de salsa en la Alameda</h2>
<p>El festival arrancó el lunes 20 de julio con sus tradicionales clases de bailes latinos, que cada tarde llenaron la Alameda de Pío XII. Los hermanos Ancor y Ayose Domínguez, de la academia Paso a Paso Las Palmas, enseñaron de forma gratuita a bailar salsa, bachata y otros ritmos latinos hasta el jueves 23, de 20:30 a 22:30 h, como antesala del fin de semana grande.</p>
<h2>Viernes 24: la «Edición Gran Canaria Joven»</h2>
<p>Desde las 11:00 h, la Plaza de Sintes se convirtió en un gran espacio de música, cultura y baile, con talleres participativos, exposiciones como la muestra sobre la Historia de la Salsa, proyecciones, pasacalles y los conciertos de Dos de Azúcar, Havana 500, Yet Garbey, Idel El Mulatito y DJ Ruymán Melián. Esta jornada, dirigida especialmente al público joven, contó con el apoyo de la Consejería de Educación y Juventud del Cabildo de Gran Canaria.</p>
<h2>Sábado 25: el gran día</h2>
<p>A partir de las 19:00 h, las academias de baile de Gran Canaria, con Paso a Paso Las Palmas, y la orquesta La Golosina calentaron la plaza antes de los grandes conciertos: Tony y Mimy Succar, llegados desde Miami junto a Kenyi Succar, y la orquesta Tromboranga, referente europeo de la salsa dura. La noche se cerró con la sesión de DJ Yotu. La gala internacional contó con el patrocinio del Gobierno de Canarias, a través de la marca «Islas Canarias» (Promotur Turismo Canarias, S.A.).</p>
<p>El acceso a todas las actividades del festival, desde las clases de baile hasta los conciertos, fue gratuito.</p>
""",
    },
    {
        "slug": "tony-y-mimy-succar-grandes-protagonistas",
        "fecha": "2026-07-20",
        "titulo": "Tony y Mimy Succar, grandes protagonistas del 30.º Festival Latino Villa de Teror",
        "resumen": "La Plaza de Sintes acoge el sábado 25 de julio, desde las 19:00 horas, el plato fuerte de la trigésima edición, con Tony y Mimy Succar y Tromboranga.",
        "imagen": "img/carteles/cartel-30",
        "imagen_alt": "Cartel del 30.º Festival Latino Villa de Teror con Tony y Mimy Succar",
        "anchos": [500, 1000],
        "cuerpo": """
<p class="entradilla">La Plaza de Sintes acogerá el próximo sábado 25 de julio, a partir de las 19:00 horas, el plato fuerte de la trigésima edición del Festival Latino Villa de Teror, una cita ya consolidada en el calendario cultural de Canarias que volverá a llenar el municipio de música, baile y ritmos latinos.</p>
<p>El espectáculo contará como grandes protagonistas con Tony y Mimy Succar, acompañados por Kenyi Succar. Ganadores de dos premios Grammy, Tony y Mimy ofrecerán en Teror una actuación cargada de energía, emoción y fusión latina, en la que compartirán su talento y su complicidad familiar sobre el escenario.</p>
<p>La programación se completa con la participación de Tromboranga, una de las formaciones más reconocidas de la salsa actual, caracterizada por su sonido potente, el protagonismo de los trombones y una propuesta pensada para disfrutar y bailar.</p>
<p>La jornada comenzará desde las 19:00 horas con actividades para todos los públicos y la participación de Paso a Paso Las Palmas, La Golosina, academias de baile de Gran Canaria y sesiones de DJ, convirtiendo la Plaza de Sintes en un gran punto de encuentro para los amantes de la música y la cultura latina.</p>
<p>El 30.º Festival Latino Villa de Teror está organizado por el Ayuntamiento de Teror y cuenta con la colaboración del Gobierno de Canarias, Islas Canarias Latitud de Vida y Turismo de las Islas Canarias.</p>
<p>La entrada será gratuita hasta completar aforo.</p>
<div class="ficha">
<h2>Datos del evento</h2>
<ul>
<li>Fecha: sábado 25 de julio de 2026.</li>
<li>Hora: desde las 19:00 horas.</li>
<li>Lugar: Plaza de Sintes, Teror.</li>
<li>Artistas principales: Tony y Mimy Succar, con Kenyi Succar, y Tromboranga.</li>
<li>Entrada gratuita.</li>
</ul>
</div>
""",
    },
    {
        "slug": "tony-y-mimy-succar-25-de-julio",
        "fecha": "2026-04-14",
        "titulo": "Tony y Mimy Succar estarán el 25 de julio en el 30.º Festival Latino Villa de Teror",
        "resumen": "Teror celebrará la edición más especial del Festival Latino con Tony y Mimy Succar, junto a Kenyi Succar y Jean Rodríguez, Tromboranga y La Golosina.",
        "imagen": "img/carteles/anuncio-30",
        "imagen_alt": "Anuncio del cartel del 30.º Festival Latino Villa de Teror",
        "anchos": [800],
        "cuerpo": """
<p class="entradilla">Teror celebrará la edición más especial del Festival Latino con un cartel internacional de primer nivel que vibrará con la actuación de Tony y Mimy Succar, junto a Kenyi Succar y Jean Rodríguez; Tromboranga y La Golosina.</p>
<p>El Festival Latino Villa de Teror 2026 celebra su 30.ª edición el 25 de julio, consolidándose como una de las citas musicales más destacadas del verano en Canarias, con una propuesta que reunirá a grandes referentes de la música latina en un entorno único.</p>
<p>El festival contará con la actuación estelar de Tony y Mimy Succar, junto a Kenyi Succar y Jean Rodríguez, que desde Miami traen un espectáculo que fusiona tradición y modernidad con una puesta en escena espectacular. Desde Gran Canaria, el público podrá vibrar además con la fuerza salsera de La Golosina; y desde Barcelona llegará la salsa brava de Tromboranga.</p>
<p>La Plaza de Sintes acogerá el sábado 25 de julio una noche llena de ritmo, sabor y energía con entrada libre, invitando a disfrutar de un evento que ya forma parte de la identidad cultural del municipio.</p>
<p>Esta edición especial, que conmemora tres décadas de trayectoria, refuerza la apuesta del Ayuntamiento de Teror por la música latina como vehículo de encuentro cultural y festivo de gran calidad para todos los públicos, que reúne a artistas de proyección nacional e internacional.</p>
<p>El Festival Latino Villa de Teror vuelve así a convertirse en punto de encuentro para amantes de la salsa y los ritmos latinos, consolidando su carácter festivo y su proyección dentro del calendario cultural de Canarias.</p>
""",
    },
    {
        "slug": "29-edicion-jose-alberto-el-canario",
        "fecha": "2025-07-03",
        "titulo": "La 29.ª edición contará con José Alberto «El Canario», Estrellas de Buena Vista y Más, Pinto Picasso y La Golosina",
        "resumen": "El XXIX Festival Latino Villa de Teror llega el 25 de julio con un cartel de lujo: el dominicano José Alberto «El Canario», Pinto Picasso, Estrellas de Buena Vista y Más y La Golosina.",
        "imagen": "img/carteles/cartel-29",
        "imagen_alt": "Cartel de la 29.ª edición del Festival Latino Villa de Teror",
        "anchos": [400, 800],
        "cuerpo": """
<p class="entradilla">El XXIX Festival Latino Villa de Teror llega el próximo 25 de julio con un cartel de lujo y la presencia del dominicano José Alberto «El Canario», todo un referente de la música latina. También estará en esta cita con la música caribeña y los sonidos tropicales el puertorriqueño Pinto Picasso; desde Cuba llegará Estrellas de Buena Vista y Más; y el grupo grancanario La Golosina completará una noche festiva de ritmo y sabor latino.</p>
<p>El Festival Latino Villa de Teror, organizado desde la Concejalía de Festejos del Ayuntamiento de Teror, se consolida un año más como uno de los encuentros más esperados del verano en Gran Canaria, ofreciendo una experiencia única para todos los públicos, con entrada libre y un ambiente muy festivo y familiar.</p>
<h2>Animación y conciertos gratuitos</h2>
<p>La Plaza de Sintes acogerá un año más este veterano festival, que comenzará el 25 de julio a las <strong>19:00 horas</strong> con animación de la Academia Paso a Paso Las Palmas y las academias de baile de Gran Canaria, además del concierto que ofrecerá <strong>La Golosina</strong> a partir de las 19:30 horas.</p>
<p>A las <strong>21:00 horas</strong>, el escenario se llenará de son y sabor cubano con el espectáculo de <strong>Estrellas de Buena Vista y Más</strong>, herederos del mítico legado musical del Buena Vista Social Club.</p>
<p>A las <strong>23:00 horas</strong> llegará la energía urbana y colorida de la bachata de <strong>Pinto Picasso</strong>, una de las voces emergentes más destacadas del panorama latino, procedente de Puerto Rico.</p>
<p>A las <strong>24:00 horas</strong>, el broche lo pondrá uno de los grandes referentes de la salsa, <strong>José Alberto «El Canario»</strong>, de República Dominicana, que desplegará todo su carisma y potencia vocal para deleite de los amantes del género.</p>
<p>El festival cerrará con la sesión SBK de <strong>DJ Nau</strong>, con grandes éxitos de la salsa, la bachata y la kizomba.</p>
<h2>Clases gratuitas de bailes latinos, del 21 al 24 de julio</h2>
<p>Antes del festival, Teror se prepara con cuatro días de clases de bailes latinos en la Alameda de Pío XII, del 21 al 24 de julio, de 20:00 a 22:00 horas, impartidas de manera gratuita por Ancor y Ayose Domínguez, de la Academia Paso a Paso Las Palmas, y sesión SBK.</p>
<h3>José Alberto «El Canario»</h3>
<p>Con más de cuatro décadas sobre los escenarios, José Alberto «El Canario» no es solo una voz legendaria de la salsa: es un símbolo de elegancia, sabor y evolución dentro del género. Nacido en Santo Domingo (República Dominicana) en 1958, emigró desde joven a Puerto Rico y luego a Nueva York, donde se formó artísticamente en la época dorada de la salsa. Su apodo nació de una habilidad única: improvisar silbando con la misma fluidez con la que otros tocan una flauta. Ese silbido se volvió su sello personal.</p>
<p>En los años 70 se unió como cantante principal a la mítica Típica 73, una de las orquestas pioneras en fusionar salsa con jazz y timba. Su gran explosión llegó en los 80, cuando fundó su propia agrupación y apostó por un estilo más romántico sin perder la esencia del son caribeño. Con éxitos como <em>Sueño contigo</em>, <em>Discúlpeme señora</em> o <em>Bailemos otra vez</em>, fue uno de los impulsores de la salsa romántica.</p>
<p>Ha llevado su música por América Latina, Europa, Asia y África, y ha compartido escenario con leyendas como Celia Cruz, Tito Puente, Rubén Blades, Oscar D'León y Johnny Pacheco. Su trayectoria ha sido reconocida con discos de oro y platino y con el Latin Grammy en 2013, 2015 y 2018. Su voz, su silbido inconfundible y su presencia escénica lo mantienen como uno de los referentes indiscutibles del género.</p>
<h3>Estrellas de Buena Vista y Más</h3>
<p>Estrellas de Buena Vista y Más nació en 2021 bajo la dirección musical de Pancho Amat, reconocido como el mejor «tresero» del mundo, con la misión de preservar el patrimonio del Buena Vista Social Club. Formado por miembros originales y nuevas generaciones de músicos, el grupo transmite las raíces más profundas de la música de la isla respetando sus tradiciones e integrando influencias contemporáneas. Su propuesta revive la época dorada de la música cubana y la proyecta hacia el futuro en escenarios de todo el mundo.</p>
<h3>Pinto Picasso</h3>
<p>Cantante, compositor y productor puertorriqueño, ha colaborado con artistas del género urbano como Plan B, Tito «El Bambino», Ñengo Flow, J Alvarez, Tempo, Franco El Gorila, Trebol Clan y Daddy Yankee. Representó a Puerto Rico en el certamen a capela «The Sing-Off» de NBC y en 2015 fue el telonero de la gira europea de Daddy Yankee. Ha realizado cuatro giras como artista principal en Europa y dos en Latinoamérica, con citas como el All Music Fest de Lima ante 45.000 espectadores.</p>
<p>En los últimos años ha centrado su producción en la bachata, con fusiones de R&amp;B y ritmos urbanos. Su álbum más reciente, «CASAGEMAS», salió en 2025 y refleja esa evolución.</p>
<h3>La Golosina</h3>
<p>La Golosina es la orquesta de salsa con sello canario que pondrá el sabor local al festival. Con más de dos décadas de trayectoria, esta formación de Gran Canaria se ha ganado el cariño del público a base de ritmo, profesionalidad y un repertorio que combina clásicos de la salsa con composiciones propias.</p>
<p>«Para nosotros es un orgullo participar en un evento tan emblemático como el Festival Latino de Teror, compartiendo cartel con grandes figuras internacionales y llevando nuestra música a casa llena», destacan desde la agrupación, que será la encargada de abrir la velada del 25 de julio.</p>
""",
    },
    {
        "slug": "teror-calienta-motores-2025",
        "fecha": "2025-06-30",
        "titulo": "Teror calienta motores para el Festival Latino 2025: ritmo, baile y sabor en la Plaza de Sintes",
        "resumen": "El Ayuntamiento de Teror anuncia una nueva edición del Festival Latino Villa de Teror, el viernes 25 de julio en la Plaza de Sintes, con clases gratuitas de baile la semana previa.",
        "imagen": "img/fotos/plaza-2025",
        "imagen_alt": "Festival Latino Villa de Teror 2025",
        "anchos": [800, 1600],
        "cuerpo": """
<p class="entradilla">El Ayuntamiento de Teror, a través de la Concejalía de Festejos, anuncia una nueva edición del emblemático Festival Latino Villa de Teror, que se celebrará el próximo viernes 25 de julio en la Plaza de Sintes.</p>
<p>El evento, que arrancará a las 19:00 horas, volverá a llenar el corazón del municipio con los ritmos más calientes del Caribe y América Latina, convirtiéndose en una cita ineludible del verano en Gran Canaria.</p>
<p>Como antesala al gran espectáculo, del 21 al 24 de julio se ofrecerán clases gratuitas de salsa, bachata y kizomba en la Alameda de Pío XII, de 20:00 a 22:00 horas, para que nadie se quede sin moverse al compás del festival.</p>
<p>Con entrada libre y ambiente festivo, el Festival Latino Villa de Teror promete una noche inolvidable para bailar, disfrutar y vivir la cultura latina en uno de los enclaves más icónicos de la isla.</p>
""",
    },
]
