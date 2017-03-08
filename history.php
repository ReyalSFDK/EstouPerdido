<?php
$Jname = '<font color="#3c9"><b>'.$_COOKIE["Jname"].'</b></font>';
$Bname = '<font color="#c39"><b>'.$_COOKIE["Bname"].'</b></font>';
$Player = '<font color="#39c"><b>You</b></font>';
$CPname = '<b><font color="#b7b77a">Alex Silva</font></b>';
$Weird = '<b><font color="#7a33b7">Stranger</font></b>';

$continue = "Continue";
$yes = "Yes";
$no = "No";

$airplane_1_p1 = "Você está dentro de um avião comercial voltando de uma viagem de férias com seus dois amigos. Você está sentado na fileira da direita, na poltrona bem do lado da janela e seus dois amigos estão sentados à sua esquerda: $Jname bem do seu lado e $Bnam3 na última poltrona.";
$airplane_1_p2 = "Olhando pela janela do avião dá para ver o tanto que o avião está longe do chão. No momento ele sobrevoa o oceano, bem perto das nuvens, que desmancham ao tocar na asa, e próximo a pássaros que voam em bando. Uma cena de encher os olhos.";
$airplane_1_p3 = "Você olha para o outro lado e vê seus dois amigos conversando, eles parecem muitos felizes. Você não participa da conversa, $Bname ri bastante e $Jname fica olhando várias vezes para você, com uma cara de preocupado. Em uma dessas olhadas ele para e te pergunta:";
$airplane_1_j1 = "Cara, você está se sentindo bem?";
$airplane_notify_1 = " $Jname se preocupa com você!";
$airplane_1_p4 = "Nesse momento $Bname para de rir e os dois te olham atentamente esperando a sua resposta:";
///Escolhas
$airplane_1_c1 = "Dizer que está bem.";
$airplane_1_c2 = "Reclamar por deixar de fora da conversa.";

///Dizer que esta bem (airplane_1_c1)
$airplane_1_1_vc1 = "Estou bem sim, obrigado por perguntar. Só estou incomodado com uma coisa aqui...";
$airplane_1_1_j1 = "Ah cara, o que que te incomoda? Posso ajudar? Você sabe que pode contar comigo à qualquer hora né?";
$airplane_1_1_p1 = "Você está mesmo incomodado, talvez seja aquela cena da menina que você é apaixonado conversando tão intimamente com o seu melhor amigo. Você também sente uma outra sensação, uma do tipo bem estranha. Você sente que algo inesperado vai acontecer ali, uma intuição. Até você acha estranho aquilo e sente receio de falar, pois acha que vão te chamar de maluco...";
///Escolhas
$airplane_1_1_c1 = "Falar da conversa dele com $Bname";
$airplane_1_1_c2 = "Falar do pressentimento que você tem";
$airplane_1_1_c3 = "Não contar nada";

/// Reclamar por deixar(airplane_1_c2)
$airplane_1_2_vc1 = "Ah, agora vocês perceberam que eu estou aqui né!";
$airplane_1_2_j1 =  "Que isso cara, calma. Só estavamos...";
$airplane_1_2_vc2 =  "Não precisa falar mais nada! Se eu soubesse que iria ficar sobrando...";
$airplane_1_2_b1 = "Calma aew cara! O que você tem? Você não é assim... está acontecendo alguma coisa?";
$airplane_1_2_p1 = "Você começa a ficar com calafrios, a suar frio e suas mãos tremem por alguns segundos, mas logo depois esses sintomas passam. Algo misteriosamente começa a preocupar você, uma sensação ruim toma conta de você. Algo que nunca aconteceu antes. Parece coisa de louco, e, talvez seus amigos ririam disso.";
///Escolhas
$airplane_1_2_c1 = "Não contar nada e admitir o ciúmes.";
$airplane_1_2_c2 = "Contar sobre o que você sentiu.";
$airplane_1_2_c3 = "Dizer que não é da conta deles.";

/// Falar da conversa (airplane_1_1_c1)
$airplane_1_1_1_vc1 = "Nada cara... Só não queria atrapalhar a conversinha de vocês dois ai...";
$airplane_1_1_1_j1 = "Xiii, lá vem ele de ciuminhos de novo...";
$airplane_1_1_1_b1 = "Ei! Mas que conversa é essa?";
$airplane_notify_2 = "$Bname notou seus ciúmes.";
$airplane_1_1_1_j2 = "Não, não é nada sobre você, - ele olha para você e pisca um olho - não se preocupe.";
$airplane_1_1_1_b2 ="Não gosto desse tom da conversa de vocês...";
$airplane_1_1_1_vc2 = "Quer saber? Vou dormir que eu ganho mais, me acordem na hora de desembarcar.";
$airplane_1_1_1_b3 = "Do jeito que você <i>tá</i> estranho, te deixo aí pra te mandarem de volta hahaha (Risos).";
$airplane_1_1_1_vc3 = "Haha, engraçada...";
$airplane_1_1_1_j3 = "Dorme bem cara!";
$airplane_1_1_1_p1 = "Você então encosta cabeça na poltrona e vira a cabeça para a janela do avião, aquela paisagem vai te relaxando e rapidamente você cai no sono.";
    
//Falar do presentimento (airplane_1_1_c2)(airplane_1_2_c2)
$airplane_1_1_2_vc1 = "Não sei bem o que é. Eu sinto como se alguma coisa de ruim estivesse para acontecer...";
$airplane_1_1_2_j1 = "Como assim cara? Estamos em um avião! Eu como um ex militar te garanto que é o meio de transporte mais seguro que existe! Acho que isso é mania de detetive.";
$airplane_1_1_2_b1 = "Cara, deixa de paranóia. Relaxa ai...";
$airplane_1_1_2_p1 = "Seus amigos começam a rir.";
$airplane_1_1_2_vc2 = "Qual o motivo da graça?";
$airplane_1_1_2_b2 = "Nada... Só tenta relaxar um pouco. Não vai acontecer nada. É só... - ela segura o riso -<em> medo.</em> ";
$airplane_1_1_2_vc3 = "Acho que é o melhor que eu faço... me acorde na hora de desembarcar.";
$airplane_1_1_2_b3 = "Ok, não se procupe!";
$airplane_1_1_2_p2 = "Você então encosta cabeça na poltrona e vira a cabeça para a janela do avião, aquela paisagem vai te relaxando e rapidamente você cai no sono.";

// Nao contar nada (airplane_1_1_c3)
$airplane_1_1_3_vc1 = "Não é nada, é besteira minha.";
$airplane_1_1_3_b1 = "Como sempre né?";
$airplane_1_1_3_vc2 = "Não perde uma eim...";
$airplane_1_1_3_j1 = "Tudo bem cara, se você diz que não é nada.";
$airplane_1_1_3_b2 = "Tenta relaxar um pouco ai, você parece mais estranho que o normal.";
$airplane_1_1_3_vc3 = "Agora falou algo de útil! Vou dormir, me acordem na hora do desembarque!";
$airplane_1_1_3_p1 = "Você então encosta cabeça na poltrona e vira a cabeça para a janela do avião, aquela paisagem vai te relaxando e rapidamente você cai no sono.";


// Adimitit os ciumes
$airplane_1_2_1_vc1 = "Não é nada de mais cara! Apenas fiquei com um pouco de ciúmes, admito.";
$airplane_1_2_1_j1 = "Não precisa se desculpar cara, acho que tenho um pouco de culpa nisso também.";
$airplane_1_2_1_b1 = "Concordo com $Jname, a culpa é dele mesmo!";
$airplane_1_2_1_j2 = "Cala boca $Bname, você não entra em nada.";
$airplane_notify_3 = "Todos se lembrarão disso.";
$airplane_1_2_1_p1 = "Naquele momento todos começam a rir, como se estivessem ainda nas férias.";
$airplane_1_2_1_j3 = "Fazemos uma bela equipe, espero que nunca nos separamos!";
$airplane_1_2_1_b2 = "Vocês são minha familia, o que dizer de $Jname? Mal conheço e já considero pakas!";
$airplane_1_2_1_j4 = "Graças a nosso amigo em comum pudemos nos conhecer!";
$airplane_1_2_1_b3 = "Tem razão, ele é um gênio!";
$airplane_1_2_1_vc2 = "Obrigado, obrigado... Estou um pouco cansado, vou dormir um pouco... Só não me deixem no avião dormindo eim!";
$airplane_1_2_1_j5 = "Pode deixar!";
$airplane_1_2_1_p2 =  "Você então encosta cabeça na poltrona e vira a cabeça para a janela do avião, aquela paisagem vai te relaxando e rapidamente você cai no sono.";

// Dizer q nao e da conta deles (airplane_1_2_c3 )
$airplane_1_2_2_vc1 = "Não é da conta de vocês.";
$airplane_1_2_2_j1 = "Ui, nossa, que grosseiro. Vai me morder agora ou depois?";
$airplane_1_2_2_b1 = "Deixa ele se acalmar $Jname. Melhor não provocar o bebê bravo!";
$airplane_notify_4 = "Eles se lembrarão disso.";
$airplane_1_2_2_p1 = "No momento os dois riem.";
$airplane_1_2_2_vc2 = "Melhor eu dormir, já que não tão nem aí mesmo...";
$airplane_1_2_2_b2 = "Ei, não fica assim!";
$airplane_1_2_2_j2 = "O que nós fizemos?";
$airplane_1_2_2_vc3 = "Nada, esqueçam...";
$airplane_1_2_2_p2 =  "Você então encosta cabeça na poltrona e vira a cabeça para a janela do avião, aquela paisagem vai te relaxando e rapidamente você cai no sono.";

//Sonho 
$sleep = "Dormir";
$dream1_1 = "Você está um lugar bastante escuro, não dá para enxergar nada em qualquer direção que você olhe.";
$dream1_2 = "Você até tenta andar em busca de alguma saída mas é como se não houvesse fim naquele lugar.";
$dream1_3 = "Você tomba em algo que impede a sua passagem, você começa a esticar a sua mão com o fim de descobrir o que te fez parar <b> - parece ser uma parede -.</b>";
$dream1_4 = "Ainda está muito escuro, mas de repente, a parede começa a surgir um pequeno feixe de luz vermelha na altura dos seus ombros. ";
$dream1_5 = "A luz vai ficando cada vez mais forte e vai se tornando um desenho. Depois de alguns segundos o desenho se completa. <b>É um tubarão.</b>";
$dream1_6 = " Você então sente aquele desenho te chamar, vozes ecoam na sua mente, e como em uma ação involuntária, você estica a mão lentamente até tocar o desenho. ";
$dream1_7 = "Logo outra luz aparece cortando bem no meio daquela parede na vertical, do chão até lá no alto, e vai se intensificando, a parede parece abrir para os lados, como se houvesse uma passagem secreta. ";
$dream1_8 = 'Ela se abre aos poucos e entre a brecha dá para ver uma floresta linda, arvores altas e tons de verde hipnotizantes <font color="#0f0">- um verdadeiro paraíso -.</font>';
$dream1_9 = '<font color="#bd1010">Você começa a escutar um barulho atrás de você.</font>';
$dream1_10 = "Olhando para trás não dá para ver o que é, é muito escuro ainda e a luz que vem da passagem só é capaz de iluminar um pedaço daquele lugar.";
$dream1_11 = "Você se vira para trás e O barulho vai ficando mais alto.";
$dream1_12 = 'De repente... <font color="#bd1010"><b>Três olhos cheios de sangue aparecem flutuando na sua frente!</b> </font> Um rosnado ecoa no local, uma neblina densa aparece de repente no ambiente. Um cenário que deixaria qualquer um com medo.';
$dream1_13 = "Os olhos vão se aproximando de você... Mas ao tocarem na luz que sai da passagem eles somem do nada, junto com a neblina e toda aquela cena de terror.";
$dream1_14 = '<font color="#bd1010"><b>Você ouve gritos agora</b></font>';
$dream1_15 = "Você começa a tossir por causa de uma fumaça, ela vem da passagem que se abriu.";
$dream1_16 = 'Virando para ela você vê um cenário de destruição. Aquela paisagem que ali estava antes agora está queimando em chamas e virando cinzas, um verdadeiro <font color="#bd1010">inferno.</font>';
$dream1_17 = " Máquinas gigantes vão abrindo caminho entre as arvores queimadas, todas elas tem uma marca em vermelho, estão longe mas dá para ver que nitidamente é um desenho de um <b>tubarão.</b>";
$dream1_18 = " Elas estão sendo escoltadas por homens: Eles estão vestindo uma armadura hidráulica e equipados com lança-chamas - parecem retirados de um Vídeo Game -.";
$dream1_19 = "Parecem ter algumas pessoas lutando contra eles, mas são facilmente massacradas. ";
$dream1_20 = "Alguns tentam fugir queimando em chamas, uma cena pertubadora.";
$dream1_21 = 'Você até consegue sentir a dor das pessoas, seu corpo começa a <b>surgir <font color="#bd1010">queimaduras</font> sua pele começa a cair e a dor é agonizante</b>.';
$dream1_22 = " Você cai no chão se debatendo com aquela dor alucinante e desmaia.";
$dream1_c1 = "Acordar";

$airplane_2_p1 = "Você então acorda, abrindo lentamente os olhos você vê a janela com vista para o oceano e uma ilha. Um pouco tonto, seus sentidos vão voltando aos poucos, e, como em um reflexo você olha para seus dois braços em busca de algum ferimento - não há nada, nem um arranhão -.";
$airplane_2_p2 = "Você respira aliviado, sem entender nada e já parcialmente recuperado você comenta, virando a cabeça para a sua esquerda:";
$airplane_2_vc1 = "Gente, vocês não vão acreditar...";
$airplane_2_p3 = 'Seus amigos estão com máscaras de ar no rosto e os cintos apertados. <font color="#bd1010">Uma aeromoça é arremessada de uma ponta a outra do avião.</font> Com seus sentidos recuperados você sente o avião tremer muito e consegue ouvir as pessoas gritarem apavoradas.';
$airplane_2_p4 = "Há um buraco enorme do casco do avião. Há pessoas que são arrastadas para aquele buraco e entram em queda livre no céu. As malas dos compartimentos voam sobre o interior do avião. Você está sem seus cintos e começa a sentir <b>dificuldades para respirar.</b>";
$airplane_2_c1 = "Apertar os Cintos";
$airplane_2_c2 = "Colocar mascara de oxigênio";

$airplane_2_1_p1 = "Você tenta puxar os cintos de segurança da poltrona do avião, mas parece está emperrado em alguma coisa, o avião começa a se inclinar para frente e você é jogado para a poltrona da frente com muita força.";

$airplane_2_2_p1 = "Você pega a máscara de oxigênio bem a sua frente e coloca sobre seu rosto. Você vai respirando o oxigênio lentamente, quando o avião se inclina para frente e você é arremessado em direção a potrona da frente.";

$airplane_3_p1 = "Você vai levantando e apoia as suas costas na poltrona, ficando de frente para seus amigos, eles viram a cena e choram muito, tentam gritar mas os gritos são abafados pelas mascaras sobre seus rostos.";
$airplane_3_p2 = "$Jname estica a mão dele, parece que ele quer que você a segure. O avião balança muito.";
$airplane_3_c1 = "Segurar a mão dele";
        
$airplane_4_p1 = "Como essa pode ser a sua única opção, você estica seu braço em direção a $Jname. O avião se inclina ainda mais e você só tem o braço dele para se segurar. Olhando para cima você vê as malas caindo em sua direção e uma delas acerta a sua cabeça.";
$airplane_4_p2 = "Você então larga a mão de $Jname, e se bate em várias poltronas até ser sugado pelo buraco em uma velocidade absurda. Você entra em queda livre. Dá para ver o avião caindo e as chamas saindo das duas asas.";
$airplane_4_p3 = "Logo você começa a girar várias vezes no ar e sente pancadas no seu corpo todo - são as correntes de ar que colidem com seu corpo em velocidades altíssimas. Você sente dores insuportáveis e perde a consciência.";

$airplane_5_p1 = "Você está desacordado.";
$airplane_5_p2 = "Você vai recuperando o seus sentidos aos poucos...";

$beach_1_p1 = "Você está deitado de olhos fechados e sente á água batendo em seu rosto. Você vai abrindo os olhos lentamente e enxerga o mar a sua frente. Seu rosto está sujo de areia, você apoia as duas mãos no chão e dá um impulso para levantar, e logo começa a limpar o rosto com as mãos.";
$beach_1_p2 = "Olhando ao redor parece ser uma praia, o cheiro do mar é predominante junto com o som das ondas se quebrando. ";
$beach_1_p3 = 'Perto da praia há uma <b>floresta bem densa.</b> No encontro da floresta com a praia há coqueiros altos e bananeiras com cachos cheios. Já na beira do mar há algumas malas abertas no chão. Sua barriga ronca de <font color="#f00"> fome</font>, parece que você não come <b>à dias.</b>';
$beach_notify_1 = array("Função Desbloqueada: Inventário!","Agora você pode acompanhar seu <b>Estado!</b> Você verá um novo alerta quando as informações forem atualizadas.");
$beach_1_p4 = "Suas roupas estão rasgadas, mas não há qualquer tipo de ferimento. Também não há qualquer sinal de vida no seu campo de visão - nem sinal de morte -. O único sinal que faz você lembrar do que aconteceu no avião são aquelas malas ali na areia, nada além disso.";
$beach_1_vc1 = "Cara, estou um pouco tonto... Minha cabeça dói, e <b>estou com fome...</b> E ainda teve aquele acidente, como ainda estou vivo? E o mais importante, como vou sair daqui?";
$beach_notify_2 = array("Função Desbloqueada no Inventário!","Agora você pode acompanhar seus <b>Objetivos!</b> Você verá um novo alerta quando as informações forem atualizadas.<small>* Você tem um novo Objetivo!</small>");

$beach_1_vc2 = "O que devo fazer agora?";
/// Escolhas
$beach_1_c1 = "Olhar Coqueiros";
$beach_1_c2 = "Olhar Bananeiras";
$beach_1_c3 = "Olhar Destroços na Areia";
$beach_1_c4 = "Vasculhar Ilha";

/// Coqueiros
$beach_1_1_p1 = "Você chega perto de um dos coqueiros da praia, esse está carregado de cocos, mas é muito alto.";
$beach_1_1_vc1 = "Parece que vou ter que ficar na vontade, os coqueiros são muito altos para eu subir, não conseguiria com a fome que estou.";

///Bananeiras
$beach_1_2_p1 = "Você vai chegando perto de uma das inúmeras bananeiras da praia, esta está com o cacho cheio e uma cor atraente. Você pega algumas e come.";
$beach_1_2_vc1 = "Hum, que delícia essas bananas, estou satisfeito por agora. Melhor eu seguir meu caminho e arranjar um jeito de sair daqui.";
$beach_notify_3 = array("Atualização de Inventário","O <b> Estado</b> e <b>Objetivos</b> foram atualizados!");

/// Malas
$beach_1_3_p1 = "Você vai chegando perto do mar e observa uma mala aberta e toda revirada no chão da areia. As roupas e alguns pertences estão um pouco longe da mala. Você pega o lacre da mala e vê que ele foi cortado com algum objeto afiado. Não há mais nada de útil aqui.";

//// Vasculhar Ilha
$beach_2_p1 = "Você sai caminhando pela costa da praia em busca de algum mantimento ou até mesmo uma saída daquele lugar. Já são vários Quilômetros percorridos e você não encontrou nada o que possa te ajudar.";
$beach_2_vc1 = "Não consigo achar nada nessa ilha... Meus amigos? Será que estão vivos? Como que eu consegui sobreviver aquela queda? Tantas perguntas... Tenho que achar um meio <b>de sair dessa ilha rápido!</b>";
$beach_notify_4 = array("Atualização de Inventário","O <b> Objetivo</b> foi atualizado!<small>* Você tem um novo Objetivo!</small>");
$beach_2_p2 = "Você então sai andando pela costa da ilha. Um lugar que parece ser tranquilo. Mas não há quaisquer sinal de vida, nem mesmo aves. Você ja está andando a muito tempo e a paisagem sempre parece a mesma.";

$beach_3_p1 = "A areia da praia começa a entrar em seu tênis causando um desconforto nos seus pés.";
$beach_3_p2 = "<b>Você deseja retirar seus sapatos?</b>";


$beach_3_1_p1 = "Você retirou os sapatos.";

$beach_3_2_p1 = "Você continua calçado.";

$beach_3_p3 = "Continuando andando pela areia da praia você ouve alguns gritos de dor vindo de trás de algumas pedras a alguns metros à sua frente.";
$beach_3_p4 = "<b>Você deseja ir até lá?</b>";

$beach_4_p1 = "Á medida que você vai se aproximando os gritos vão diminuindo aos poucos. Atrás das pedras você encontra um homem deitado no chão, com um ferro atravessado em sua barriga. Seu sangue está escorrendo pelo chão e dá para ver que alguns de seus órgãos saem pelo buraco na sua barriga. O homem é um senhor já de idade, cabelos e barba grisalhos e com uniforme que parece ser da empresa do avião. Há um crachá no uniforme escrito $CPname - Copiloto.";
$beach_4_p2 = "O homem está muito pálido e parece fraco demais tentar alguma coisa, ele tenta dizer alguma coisa. Mas suas palavras engasgam junto com o sangue na sua boca.";
$beach_4_vc1 = "Você está bem senhor... $CPname?";
$beach_4_p3 = "Uma pergunta automática e a qual já é retórica. Talvez ele saiba de algo que aconteceu no avião, afinal é o copiloto. Talvez saiba quem fez isso com ele, pois não há qualquer fragmento do avião por perto, até mesmo onde podem estar os outros tripulantes.{w=1} De qualquer forma, ele está sofrendo muito e não parece aguentar muito tempo.";

$beach_4_c1 = "Perguntar o que aconteceu no avião";
$beach_4_1_vc1 = "Senhor Alex, o que aconteceu no avião?";
$beach_4_1_cp1 = "A culpa... foi o piloto! <i>- O homem tosse fortemente e fala pausadamente, alternado entre as palavras e os gritos de dor -</i> Ele era meu amigo há muito tempo, mas naquela viagem... Ele não... era o... mesmo!<i> - O senhor começa a ficar inquieto, se remexendo no chão e consequentemente rasgando seu abdômen ainda mais -</i> Eu Tentei... Juro que... Tentei...";
$beach_4_1_vc2 = "Ele desviou a rota? Por quê? $CPname?";
$beach_4_1_p1 = "Logo o homem para de respirar, suas últimas palavras ficam gravadas na memória...";

$beach_4_c2 = "Perguntar o que aconteceu com ele";
$beach_4_2_vc1 = "Senhor $CPname, o que aconteceu com o senhor?";
$beach_4_2_cp1 = "Foram eles! Eles conseguiram me achar! <i>- O senhor começa a ficar inquieto, se remexendo no chão e consequentemente rasgando seu abdômen ainda mais -</i> Depois de <b>tantos anos... tantas tentativas...</b>";
$beach_4_2_vc2 = "Eles? Quem senhor $CPname?";
$beach_4_2_cp2 = "Fuja... filho! <i>- O homem tosse fortemente e fala pausadamente, alternado entre as palavras e os gritos de dor -</i>Fuja antes que... O próximo... Seja... Você!...";
$beach_4_2_vc3 = "Eles quem? E porquê? $CPname?";
$beach_4_2_p1 = "Logo o homem para de respirar, suas últimas palavras ficam gravadas na memória...";

$beach_4_c3 = "Perguntar onde estão os outros tripulantes";
$beach_4_3_vc1 = "Senhor $CPname, onde estão os outros? Você os viu?";
$beach_4_3_cp1 = "Eles os levaram! A maioria!<i> - O senhor começa a ficar inquieto, se remexendo no chão e consequentemente rasgando seu abdômen ainda mais. -</i> Eu estava com um grupo de tripulantes... Foi uma emboscada... Alguns fugiram... Outros foram levados... E eu... Aqui...";
$beach_4_3_vc2 = "$Jname e $Bname estavam com o senhor? Eles conseguiram fugir? Senhor $CPname? <b>Senhor $CPname!?!</b>";
$beach_4_3_p1 = "Logo o homem para de respirar, suas últimas palavras ficam gravadas na memória...";

$beach_4_c4 = "Acabar com o sofrimento dele de vez";
$beach_4_4_vc1 = "Ninguém deve sofrer tanto assim...";
$beach_4_4_p1 = "Você vai andando até as rochas e olha elas por alguns segundos, se abaixa, pega uma e fala:";
$beach_4_4_vc2 = "Deve servir...";
$beach_4_4_p2 = "Você então se aproxima do homem e levanta a rocha sobre sua cabeça. O senhor olha para cima em sua direção e sorrir. Você então arremessa a rocha sobre a cabeça do homem. O som da rocha quebrando a cabeça do homem é estrindente, você quase sente o crânio dele se partindo. O impacto faz espalhar sangue e pedaços do cérebro para todos os lados. O que restou da sua cabeça foi atolada na areia. ";

$beach_4_c5 = "Confotá-lo nos momentos finais da vida dele";
$beach_4_5_vc1 = "Calma senhor, vai ficar tudo bem, o senhor vai ficar bem...";
$beach_4_5_cp1 = "Obrigado meu jovem... Depois de tanto lutar, vou morrer aqui, que irônia... Minha hora chegou... Obrigado por não me.. Deixar... ";
$beach_4_5_p1 = "Logo o senhor para de respirar, uma lágrima sai do rosto do homem, que morreu em paz.";

$beach_4_c6 = "Ir Embora";
$beach_4_6_vc1 = "Não, eu não aguento ver mais isso...";
$beach_4_6_p1 = "Você então se afasta rápidamente daquele local.";

$beach_5_vc1 = " Nossa... O que foi isso? Um homem com a barriga aberta na costa praia? Como?";
$beach_5_p1 = "Você então tenta analisar o que pode ter acontecido.";
$beach_5_vc2 = "O ferro parece bem preso na areia, como se alguem <i>tivesse</i> fincado ele lá. Será que ele caiu em cima do ferro?";
  
$beach_5_c1_vc1 = "Não não, acho impossível. O ferro é muito longo pra alguem tropeçar e caír em cima dele, ou mesmo ser <b> empurrado</b>...";
        
$beach_5_c2_vc1 = "Acho que seria impossivél mesmo de alguem cair. O ferro é muito longo e não há sangue na parte superior dele.";
        
$beach_notify_5 = array("Habilidade Ativada: Raciocínio","Cada escolha correta melhora sua habilidade. Pense com cuidado em cada escolha para obter vantagens no futuro.");
$beach_5_vc3 = "É parece que ele não caiu em cima daquele ferro... O que pode ter acontecido? Será que alguem fincou o ferro na barriga daquele senhor?";

$beach_5_c3 = "Parece que sim";
$beach_5_c3_vc1 = "Com certeza, o modo que ele está bem preso e a falta de sangue na parte de cima do ferro só apontam para esse caminho! Mas quem pode ter feito isso?";

$beach_5_c4 = "Acho pouco provavél";
$beach_5_c4_vc1 = "Pode ser que sim, pode ser que não... Não dá para saber ao certo.";

$beach_5_vc4 = "Essa ilha está começando a me deixar com calafrios! Melhor eu continuar com a minha busca!  É bom eu ter cuidado, não sei o que pode vim pela frente.";
        

$beach_6_p1 = "Você dá à volta pelas rochas o mais distante possível e continua seu caminho.";
$beach_6_vc1 = "Não sei se era uma boa ideia ir até lá, sabe-se lá o que me esperava...";

$beach_7_p1 = "Nesse momento você é surpreendido por gritos que vêm atrás de você. Ao virar você se dá de frente com uma pessoa, ela grita desesperadamente, sua aparência não é das melhores e seu rosto transmite medo. É um rapaz magro com roupas rasgadas e com alguns ferimentos.";
$beach_7_npc1 = "Você! Você não é deles né? Ou é? Não faça nada comigo... <b>Socorro!</b>";
$beach_7_p2 = "O tom de voz do rapaz é de desespero e medo.";
$beach_7_npc2 = "Eu lembro de você! Você não faz parte <b>deles</b>, ou faz? ";

$beach_7_c1 = "Calma, O que aconteceu?";
$beach_7_c1_vc1 = "Respira um pouco, calma. Me conta, o que aconteceu?";
$beach_7_c1_npc1 = " Eu... Estava no avião... Acho que lembro de você, é... Lembro! Você estava com seus amigos! Você não lembra de mim? Meu deus, eles ficaram lá! Eles os pegaram.... <b>ELES OS PEGARAM!</b> É O FIM! FUJA, FUJA PARA LONGE... <b>MAS NÃO ENTRE NESSA MALDITA FLORESTA!</b>";
       
$beach_7_c2 = "Deles? Deles quêm?";
$beach_7_c2_vc1 = "Eles? De quem que você está falando?";
$beach_7_c2_npc1 = "Eles cara! Os homens robôs! Você viajava com seus amigos né? Você não se lembra de mim? MEU DEUS, SEUS AMIGOS! FICARAM LÁ DENTRO DA FLORESTA! CORRA MEU AMIGO, FUJA PARA AS MONTANHAS!";

$beach_7_p3 = "O estranho então sai correndo e continua gritando como um louco.";
 
$beach_8_p1 = "Que cara louco, acho que me lembro dele no check-in no aeroporto, ele parece transtornado. $Jname e $Bname! Será que eles estão mesmo na floresta? Do jeito que esse homem saiu de lá não me parece uma boa ideia entrar... Mas meus amigos...";

$beach_8_c1 = "Quem é $Bname?";
$beach_8_1_vc1 = "Ah, $Bname Correia Sampaio, 20 anos. Jeito de menina em um corpo de mulher, estranha e ao mesmo tempo encantadora. Um mistério que eu dedicaria minha vida a tentar resolve-lo. Tão sensível e ao mesmo tempo tão forte, uma verdadeira obra prima da natureza. Tão cheia de vida, oh $Bname! Tantos momentos tristes em sua vida e agora mais esse episódio te assusta, talvez desse eu possa salva-la e ela poderá enxergar quem sou eu de verdade, e não apenas um <b>amigo...</b>";

$beach_8_c2 = "O que $Bname é para você?";
$beach_8_2_vc1 = "Primeiro seu pai desaparece, e logo em seguida a sua mãe. Como uma pessoa pode ser tão forte assim? - Talvez seja isso que me encante nela. - Ela preencheu o vazio dentro de mim quando o $Jname se foi. O que seria de mim sem ela? Um pobre coitado que sempre perde as pessoas a sua volta? Não! Não posso deixar com que isso aconteça denovo! Não com a $Bname! Eu devo isso a ela.";
        
$beach_8_c3 = "Quem é $Jname?";
$beach_8_3_vc1 = "... Um irmão para a vida toda. Sempre esteve do meu lado e nunca me deixou só, mesmo com seus problemas familiares. Um cara companheiro e protetor, sempre me ajudou nos tempos ruim, nos tempos bons, nos tempos de bagunça... não posso abandoná-lo logo agora... Meu irmão... ";
        
$beach_8_c4 = "O que $Jname é para você?";
$beach_8_4_vc1 = "Quando eu perdi minha mãe ele estava lá. Quando eu sofria na escola ele estava lá. Quando eu não tinha mais ninguém, ele me acolheu. Não devo abandoná-lo nesse momento, não é o que ele faria por mim. Ele nunca me abandonou... Ele é a unica familia que eu tenho...";
        
$beach_9_p1 = "Depois de lembrar sobre seus amigos, você sente um enorme impulso de entrar na floresta em busca deles.";
$beach_9_vc1 = "Eles dois, são tipo, minha família. São tudo o que tenho e não posso abandoná-los nesse momento. Eu não vou suportar nem permitir que nada nem ninguém nos afaste um do outro!  Mas tambem não sei se eles estão vivos... É um risco enorme...";
$beach_9_p2 = "O sol vai desaparecendo no horizonte aos poucos, o pôr-do-sol na praia é uma coisa tão maravilhosa que não há palavras para descrever, aquela mistura de cores e o reflexo no mar é uma combinação divina e, por um momento, você consegue esquecer de toda aquela tragédia, e isso te deixa mais calmo.";
$beach_9_vc2 = "Tenho que tomar uma decisão e rápido!";



?>





/

