init -3 python:
######################################################
##      Tradução Para o Inglês                      ##
######################################################
    if lang == "en":
######## Nome do Jogo
        config.name = 'I Am Lost'
######## Navegação
        nav_newgame = 'New Game'
        nav_history = 'Dialogues'
        nav_save = 'Save'
        nav_continue = 'Continue'
        nav_menu = 'Menu'
        nav_option = 'Options'
        nav_about = 'About'
        nav_help = 'Help'
        nav_quit = 'Exit'
        nav_skip = 'Skip'
######## Geral
        lang_Yes = 'Yes'
        lang_No = 'No'
        lang_version = 'Version'
        lang_back = 'Back'
######## Confirmações
        confirm_quit = 'Are you sure you want to leave the game?'
        confirm_menu = "Are you sure you want to return to the main menu?\nYou will lose any progress that hasn't been saved."
        confirm_overwrite = 'Are you sure you want to overwrite this saved game?'
        confirm_loadSave = "Loading this game will make you lose any progress that hasn't been saved.\n Are you sure you want to do this?"
        confirm_deleteSave = 'Are you sure you want to delete the saved game?'######## Salvar/Carregar
##### Salvar/Carregar
        sl_emptySlot = 'Empty Slot.'
        sl_page = 'Page'
######## Configurações
        config_display = 'Exhibition'
        config_window = 'Window'
        config_fullscreen = 'Full Screen'
        config_lang = 'Game Language'
        config_br = 'Portuguese'
        config_en = 'English'
        config_es = 'Spanish'
        config_textSpeed = 'Subtitle Speed'
        config_default = 'Standard'
        config_fast = 'Fast'
        config_textSize = 'Subtitle Size'
        config_small = 'Small'
        config_medium = 'Medium'
        config_big = 'Big'   
        config_sound = 'Sound Volume'
        config_music = 'Music Volume'
        config_mute = 'Mute'
        config_rebot = "* Necessário reiniciar o jogo."
######################################################
##      Tradução do Iventário                       ##
######################################################
######## Menu
        inv_name = 'Inventário'
        inv_status = 'Estado'
        inv_item = 'Itens'
        inv_obj = 'Objetivos'
######## Itens
        item_SemItem_name = "Sem Itens"
        item_SemItem_desc = "Você não pode carregar itens no momento."
        item_mochila_name = "Mochila"
        item_mochila_desc = "Uma mochila de viagens. É possível carregar itens nela."
######## Objetivos
        obj_c = "{color=#54FF9F}[Completado]{/color} "
        obj_n = "{color=#FF6347}[Não Completado]{/color}"
        obj_semObj_title = "Sem Objetivos"
        obj_semObj_desc = "Você ainda Não Possui Objetivos."
        obj_ComerAlgo_title = "Comer alguma coisa"
        obj_ComerAlgo_desc = "Achar algo na ilha que mate a sua fome."
        obj_SairDaIlha_title = "Sair da Ilha"
        obj_SairDaIlha_desc = "Achar algum meio de sair da ilha."
######## Estado
        sts_fome_name = "{color=#FF6347}Fome{/color}"
        sts_fome_desc = "Você está com fome no momento."
        sts_fome2_name = "{b}Fome{b}"
        sts_fome2_desc = "Você está com muita fome no momento."
        sts_fome3_name = "{b}Fome{/b}"
        sts_fome3_desc = "{color=#EEAD0E} Você está morrendo de fome!{/color} ."
        sts_semFome_name = "Satisfeito"
        sts_semFome_desc = "Atualmente você está Satisfeito."
        sts_calcado_name = "Você está calçado"
        sts_calcado_desc = "Atualmente você está calçando um tênis que protege seus pés."
        sts_descalco_name = "Você está descalço"
        sts_descalco_desc = "Atualmente você está descalço. Melhor olhar onde pisa."
        sts_ciumesJoao_name = "Você sente ciúmes de João"
        sts_ciumesJoao_desc = "Você demostrou sentir ciúmes da conversa de Beatriz e João no avião."
######################################################
##      Tradução das Conquistas                     ##
######################################################
        cnqst_unloked = "Conquista Desbloqueada!"
        cnqst_1vez_title = "Estou Perdido"
        cnqst_1vez_text = 'Acordar em um lugar {i}"desconhecido"{/i}'
        cnqst_1vez_info = "Jogue o Estou perdido pela primeira vez. "
        cnqst_Alex1_title = "Quebrando Crânios!"
        cnqst_Alex1_text = "Mostrar sangue frio como assassino."
        cnqst_Alex1_info = "Matar Alex com uma pedra."
        cnqst_Alex2_title = "Descanse em Paz"
        cnqst_Alex2_text = "Mostrar compaixão com Alex."
        cnqst_Alex2_info = "Acompanhar Alex em seus momentos finais."
        cnqst_doido_title = "Ficando Doido?!"
        cnqst_doido_text = "Falando sozinho na praia"
        cnqst_doido_info = "Raciocinar sobre uma cena pela 1ª vez"

######################################################
##      Tradução dos Créditos                       ##
######################################################
        creditos_1 = "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"
        creditos_2 = "\n Tradução para o Inglês por {color=#F00}{b}Pandora Pimentel{/b}{/color}\n Email: {a=mailto:pandorahari@hotmail.com}pandorahari@hotmail.com{/a}"
######################################################
##      Tradução da História                        ##
######################################################
        game_you = 'Você'
        game_unknow = 'Estranho'
        game_joao = 'João'
        game_bia = 'Beatriz'
        game_alex = 'Alex Silva'
        chapter_1 = "{size=100}Capitulo 1{/size}{p} Sozinho"
        choice_j_name = "Digite o nome do seu melhor amigo:"
        choice_b_name = "Digite o nome da sua melhor amiga:"
        confirm_choices = ["Obrigado, o nome do seu melhor amigo é "
                        , " e o da sua melhor amiga é "
                        ," {p=1}{b} Bom Jogo!{/b} "]
######## Cena Avião
        aviao_1 = ["Você está dentro de um avião comercial voltando de uma viagem de férias com seus dois amigos.{w=1} Você está sentado na fileira da direita, na poltrona bem do lado da janela e seus dois amigos estão sentados à sua esquerda:{w=1} "
            ," bem do seu lado e "
            ," na última poltrona."]
        aviao_2 = "Olhando pela janela do avião dá para ver o tanto que o avião está longe do chão.{w=1} No momento ele sobrevoa o oceano, bem perto das nuvens, que desmancham ao tocar na asa, e próximo a pássaros que voam em bando{w=1}. Uma cena de encher os olhos."
        aviao_3 = ["Você olha para o outro lado e vê seus dois amigos conversando, eles parecem muitos felizes.{w=1} Você não participa da conversa, "
            ," ri bastante e "
            ," fica olhando várias vezes para você, com uma cara de preocupado.{w=1} Em uma dessas olhadas ele para e te pergunta:"]
        aviao_4 = "Cara, você está se sentindo bem?"
        aviao_notify_1 = "{b} {color=#33b77a} [jname]{/color}{/b} se preocupa com você!"
        aviao_5 = ["Nesse momento "
            ," para de rir e os dois te olham atentamente esperando a sua resposta:"]
        aviao_5c1 = "Dizer que está bem."
        aviao_5c2 = "Reclamar por deixar de fora da conversa."

        aviao_ID1_1_vc1 = "Estou bem sim, obrigado por perguntar. Só estou incomodado com uma coisa aqui..."
        aviao_ID1_1_j1 = "Ah cara, o que que te incomoda? Posso ajudar?{w=1} Você sabe que pode contar comigo à qualquer hora né?"
        aviao_ID1_1_n1 = "Você está mesmo incomodado, talvez seja aquela cena da menina que você é apaixonado conversando tão intimamente com o seu melhor amigo.{w=1} Você também sente uma outra sensação, uma do tipo bem estranha.{w=1} Você sente que algo inesperado vai acontecer ali, uma intuição.{w=1} Até você acha estranho aquilo e sente receio de falar, pois acha que vão te chamar de maluco..."
        aviao_ID1_1_c1 = "Falar da conversa dele com "
        aviao_ID1_1_c2 = "Falar do pressentimento que você tem"
        aviao_ID1_1_c3 = "Não contar nada"

        aviao_ID1_2_vc1 = "Ah, agora vocês perceberam que eu estou aqui né!"
        aviao_ID1_2_j1 = "Que isso cara, calma. Só estavamos..."
        aviao_ID1_2_vc2 = "Não precisa falar mais nada!{w=1} Se eu soubesse que iria ficar sobrando..."
        aviao_ID1_2_b1 = "Calma aew cara! O que você tem? Você não é assim... está acontecendo alguma coisa?"
        aviao_ID1_2_n1 = "Você começa a ficar com calafrios, a suar frio e suas mãos tremem por alguns segundos,{w=1} mas logo depois esses sintomas passam.{w=1} Algo misteriosamente começa a preocupar você, uma sensação ruim toma conta de você. Algo que nunca aconteceu antes.{w=1} Parece coisa de louco, e, talvez seus amigos ririam disso."
        aviao_ID1_2_c1 = "Não contar nada e admitir o ciúmes."
        aviao_ID1_2_c2 = "Contar sobre o que você sentiu."
        aviao_ID1_2_c3 = "Dizer que não é da conta deles."

        aviao_ID2_1_vc1 = "Nada cara... Só não queria atrapalhar a conversinha de vocês dois ai..."
        aviao_ID2_1_j1 = "Xiii, lá vem ele de ciuminhos de novo..."
        aviao_ID2_1_b1 = "Ei! Mas que conversa é essa?"
        aviao_notify_2 = "{b}{color=#33b77a} [jname]{/color}{/b} notou seus ciúmes"
        aviao_ID2_1_j2 = "Não, não é nada sobre você, - ele olha para você e pisca um olho - não se preocupe."
        aviao_ID2_1_b2 = "Não gosto desse tom da conversa de vocês..."
        aviao_ID2_1_vc2 = "Quer saber? Vou dormir que eu ganho mais, me acordem na hora de desembarcar."
        aviao_ID2_1_b3 = "Do jeito que você {i}tá{/i} estranho, te deixo aí pra te mandarem de volta hahaha (Risos)."
        aviao_ID2_1_vc3 = "Haha, engraçada..."
        aviao_ID2_1_j3 = "Dorme bem cara!"
        aviao_ID2_1 = "Você então encosta cabeça na poltrona e vira a cabeça para a janela do avião, aquela paisagem vai te relaxando e rapidamente você cai no sono."

       
        aviao_ID2_2_vc1 = "Não sei bem o que é. Eu sinto como se alguma coisa de ruim estivesse para acontecer..."
        aviao_ID2_2_j1 = "Como assim cara? Estamos em um avião! Eu como um ex militar te garanto que é o meio de transporte mais seguro que existe!{w=1} Acho que isso é mania de detetive."
        aviao_ID2_2_b1 = "Cara, deixa de paranóia. Relaxa ai..."
        aviao_ID2_2 = [" e "," começam a rir."]
        aviao_ID2_2_vc2 = "Qual o motivo da graça?"
        aviao_ID2_2_b2 = "Nada... Só tenta relaxar um pouco.{w=1} Não vai acontecer nada. É só... {w=1}- ela segura o riso -{w=1}{b} medo.{/b} "
        aviao_ID2_2_vc3 = "Acho que é o melhor que eu faço... me acorde na hora de desembarcar."
        aviao_ID2_2_b3 = "Ok, não se procupe!"

        aviao_ID2_3_vc1 = "Não é nada, é besteira minha."
        aviao_ID2_3_b1 = "Como sempre né?"
        aviao_ID2_3_vc2 = "Não perde uma eim..."
        aviao_ID2_3_j1 = "Tudo bem cara, se você diz que não é nada."
        aviao_ID2_3_b2 = "Tenta relaxar um pouco ai, você parece mais estranho que o normal."
        aviao_ID2_3_vc3 = "Agora falou algo de útil!{w=1} Vou dormir, me acordem na hora do desembarque!"

        aviao_ID3_1_vc1 = "Não é nada de mais cara! Apenas fiquei com um pouco de ciúmes, admito."
        aviao_ID3_1_j1 = "Não precisa se desculpar cara, acho que tenho um pouco de culpa nisso também."
        aviao_ID3_1_b1 = ["Concordo com ",", a culpa é dele mesmo!"]
        aviao_ID3_1_j2 = ["Cala boca ",", você não entra em nada."]
        aviao_notify_3 = "Todos se lembrarão disso."
        aviao_ID3_1 = "Naquele momento todos começam a rir, como se estivessem ainda nas férias."
        aviao_ID3_1_j3 = "Fazemos uma bela equipe, espero que nunca nos separamos!"
        aviao_ID3_1_b2 = ["Vocês são minha familia, o que dizer de ","? Mal conheço e já considero pakas!"]
        aviao_ID3_1_j4 = "Graças a nosso amigo em comum pudemos nos conhecer!"
        aviao_ID3_1_b3 = "Tem razão, ele é um gênio!"
        aviao_ID3_1_vc2 = "Obrigado, obrigado...{p=1}Estou um pouco cansado, vou dormir um pouco... {w=1}Só não me deixem no avião dormindo eim!"
        aviao_ID3_1_j5 = "Pode deixar!"

        aviao_ID3_3_vc1 = "Não é da conta de vocês."
        aviao_ID3_3_j1 = "Ui, nossa, que grosseiro. Vai me morder agora ou depois?"
        aviao_ID3_3_b1 = ["Deixa ele se acalmar ",". Melhor não provocar o bebê bravo!"]
        aviao_notify_4 = "Eles se lembrarão disso."
        aviao_ID3_3 = "No momento os dois riem."
        aviao_ID3_3_vc2 = "Melhor eu dormir, já que não tão nem aí mesmo..."
        aviao_ID3_3_b2 = "Ei, não fica assim!"
        aviao_ID3_3_j2 = "O que nós fizemos?"
        aviao_ID3_3_vc3 = "Nada, esqueçam..."
######## Cena Sono 1
        dream1_1 = "{font=fontes/Old Dreams.otf}{color=39c}{size=40}Você está um lugar bastante escuro, não dá para enxergar nada em qualquer direção que você olhe.{/font}"
        dream1_2 = "Você até tenta andar em busca de alguma saída mas é como se não houvesse fim naquele lugar."
        dream1_3 = "Você tomba em algo que impede a sua passagem, você começa a esticar a sua mão com o fim de descobrir o que te fez parar"   
        dream1_4 = "{b} - parece ser uma parede -.{/b} "
        dream1_5 = "Ainda está muito escuro, mas de repente, a parede começa a surgir um pequeno feixe de luz vermelha na altura dos seus ombros. "
        dream1_6 = "A luz vai ficando cada vez mais forte e vai se tornando um desenho. Depois de alguns segundos o desenho se completa. {w=1}{b}É um tubarão.{/b}"
        dream1_7 = ""
        dream1_8 = " Você então sente aquele desenho te chamar, vozes ecoam na sua mente, e como em uma ação involuntária, você estica a mão lentamente até tocar o desenho. "
        dream1_9 = "Logo outra luz aparece cortando bem no meio daquela parede na vertical, do chão até lá no alto, e vai se intensificando, a parede parece abrir para os lados, como se houvesse uma passagem secreta. "
        dream1_10 = " Ela se abre aos poucos e entre a brecha dá para ver uma floresta linda, arvores altas e tons de verde hipnotizantes {w=1}{color=#0f0}- um verdadeiro paraíso -.{/color}"
        dream1_11 = "{font=fontes/Old Dreams.otf}{color=f33}{size=40}Você começa a escutar um barulho atrás de você. {/color}{/font}"
        dream1_12 = " Olhando para trás não dá para ver o que é, é muito escuro ainda e a luz que vem da passagem só é capaz de iluminar um pedaço daquele lugar."
        dream1_13 = " Você se vira para trás e O barulho vai ficando mais alto."
        dream1_14 = "{cps=10} De repente{/cps}{cps=5}...{/cps}{p=1}{color=f00}{b} Três olhos cheios de sangue aparecem flutuando na sua frente!{/b} {/color} {p=1} Um rosnado ecoa no local, uma neblina densa aparece de repente no ambiente. Um cenário que deixaria qualquer um com medo. "
        dream1_15 = "{cps=10} Os olhos vão se aproximando de você{/cps}{cps=5}...{/cps}{p=1}{cps=20} Mas ao tocarem na luz que sai da passagem eles somem do nada, junto com a neblina e toda aquela cena de terror.{/cps}"
        dream1_16 = "{font=fontes/Old Dreams.otf}{color=f00}{size=40}Você ouve gritos agora{/color}{/font}"
        dream1_17 = " Você começa a tossir por causa de uma fumaça, ela vem da passagem que se abriu."
        dream1_18 = " Virando para ela você vê um cenário de destruição. Aquela paisagem que ali estava antes agora está queimando em chamas e virando cinzas, um verdadeiro {color=#f00}inferno.{/color}"
        dream1_19 = " Máquinas gigantes vão abrindo caminho entre as arvores queimadas, todas elas tem uma marca em vermelho, estão longe mas dá para ver que nitidamente é um desenho de um {b}tubarão.{/b}"
        dream1_20 = " Elas estão sendo escoltadas por homens:{p=1} Eles estão vestindo uma armadura hidráulica e equipados com lança-chamas - parecem retirados de um Vídeo Game -."
        dream1_21 = "Parecem ter algumas pessoas lutando contra eles, mas são facilmente massacradas. "
        dream1_22 = "Alguns tentam fugir queimando em chamas, uma cena pertubadora."
        dream1_23 = " Você até consegue sentir a dor das pessoas"
        dream1_24 = ", seu corpo começa a surgir {color=#f00}queimaduras{/color}, {b}sua pele começa a cair e a dor é agonizante{/b}."
        dream1_25 = " Você cai no chão se debatendo com aquela dor alucinante e {cps=5}desmaia."
        dream1_26 = "Acordar"

        aviao_ID4_1 = "Você então acorda, abrindo lentamente os olhos você vê a janela com vista para o oceano e uma ilha. Um pouco tonto, seus sentidos vão voltando aos poucos, e, como em um reflexo você olha para seus dois braços em busca de algum ferimento - não há nada, nem um arranhão -."
        aviao_ID4_2 = "Você respira aliviado, sem entender nada e já parcialmente recuperado você comenta, virando a cabeça para a sua esquerda:"
        aviao_ID4_vc1 = "Gente, vocês não vão acreditar..."
        aviao_ID4_3 = "Seus amigos estão com máscaras de ar no rosto e os cintos apertados.{p=1}{color=#f00}Uma aeromoça é arremessada de uma ponta a outra do avião.{/color}{p=1}Com seus sentidos recuperados você sente o avião tremer muito e consegue ouvir as pessoas gritarem apavorizadas."
        aviao_ID4_4 = "Há um buraco enorme do casco do avião. {p=1}Há pessoas que são arrastadas para aquele buraco e entram em queda livre no céu. As malas dos compartimentos voam sobre o interior do avião.{p=1}Você está sem seus cintos e começa a sentir {b}dificuldades para respirar.{/b}"
        aviao_ID4_c1 = "Apertar os Cintos"
        aviao_ID4_c1_1 = "Você tenta puxar os cintos de segurança da poltrona do avião, mas parece está emperrado em alguma coisa, o avião começa a se inclinar para frente e você é jogado para a poltrona da frente com muita força."
        aviao_ID4_c2 = "Colocar mascara de oxigênio"
        aviao_ID4_c2_1 = "Você pega a máscara de oxigênio bem a sua frente e coloca sobre seu rosto. Você vai respirando o oxigênio lentamente, quando o avião se inclina para frente e você é arremessado em direção a potrona da frente."
        aviao_ID4_5 = "Você vai levantando e apoia as suas costas na poltrona, ficando de frente para seus amigos, eles viram a cena e choram muito, tentam gritar mas os gritos são abafados pelas mascaras sobre seus rostos."
        aviao_ID4_6 = " estica a mão dele, parece que ele quer que você a segure. O avião balança muito."
        aviao_ID4_c3 = "Segurar a mão dele"
        aviao_ID4_7 = ["Como essa pode ser a sua única opção, você estica seu braço em direção a ",".{p=1}O avião se inclina ainda mais e você só tem o braço dele para se segurar.{p=1}Olhando para cima você vê as malas caindo em sua direção e uma delas acerta a sua cabeça."]
        aviao_ID4_8 =[ "Você então larga a mão de "," e se bate em várias poltronas até ser sugado pelo buraco em uma velocidade absurda. Você entra em queda livre. Dá para ver o avião caindo e as chamas saindo das duas asas. "]
        aviao_ID4_9 = " Logo você começa a girar várias vezes no ar e sente pancadas no seu corpo todo - são as correntes de ar que colidem com seu corpo em velocidades altíssimas. Você sente dores insuportáveis e perde a consciência."
        aviao_ID4_10 = "{font=fontes/Old Dreams.otf}{size=+30}Você está desacordado{/size}{/font} "
        aviao_ID4_11 = "{font=fontes/Old Dreams.otf}{size=+30}Você vai recuperando o seus sentidos aos poucos...{/size}{/font} "

######## Cena Praia
        praia_1 = "Você está deitado de olhos fechados e sente á água batendo em seu rosto.{w=1} Você vai abrindo os olhos lentamente e enxerga o mar a sua frente.{w=1} Seu rosto está sujo de areia, você apoia as duas mãos no chão e dá um impulso para levantar, e logo começa a limpar o rosto com as mãos."
        praia_2 = "Olhando ao redor parece ser uma praia, o cheiro do mar é predominante junto com o som das ondas se quebrando. "
        praia_3 = "Perto da praia há uma {b}floresta bem densa.{/b}{w=1} No encontro da floresta com a praia há coqueiros altos e bananeiras com cachos cheios. {w=1}Já na beira do mar há algumas malas abertas no chão. Sua barriga ronca de {color=#f00}fome{/color}, parece que você não come {b}à dias.{/b}"
        praia_notify_1 = ["Função Desbloqueada: Inventário!","Agora você pode acompanhar seu {b}Estado!{/b} Você verá um novo alerta quando as informações forem atualizadas."]
        praia_4 = "Suas roupas estão rasgadas, mas não há qualquer tipo de ferimento.{w=1} Também não há qualquer sinal de vida no seu campo de visão - nem sinal de morte -.{w=1} O único sinal que faz você lembrar do que aconteceu no avião são aquelas malas ali na areia, nada além disso."
        praia_vc1 = "Cara, estou um pouco tonto... Minha cabeça dói, e {b}estou com fome...{/b} E ainda teve aquele acidente, como ainda estou vivo? E o mais importante, como vou sair daqui?"     
        praia_notify_2 = ["Função Desbloqueada no Inventário!","Agora você pode acompanhar seus {b}Objetivos!{/b} Você verá um novo alerta quando as informações forem atualizadas.{p}{b}* Você tem um novo Objetivo!{/b}"]

        praia_ID1_vc1 = "O que devo fazer agora?"
        praia_ID1_c1 = "Olhar Coqueiros"
        praia_ID1_c2 = "Olhar Bananeiras"
        praia_ID1_c3 = "Olhar Destroços na Areia"
        praia_ID1_c4 = "Vasculhar Ilha"
        praia_ID1_c1_1 = "Você chega perto de um dos coqueiros da praia, esse está carregado de cocos, mas é muito alto."
        praia_ID1_c1_vc1 = "Parece que vou ter que ficar na vontade, os coqueiros são muito altos para eu subir, não conseguiria com a fome que estou."
        praia_ID1_c2_1 = "Você vai chegando perto de uma das inúmeras bananeiras da praia, esta está com o cacho cheio e uma cor atraente. Você pega algumas e come."
        praia_ID1_c2_vc1 = "Hum, que delícia essas bananas, estou satisfeito por agora. Melhor eu seguir meu caminho e arranjar um jeito de sair daqui."
        praia_notify_4 = ["Atualização de Inventário","O {b} Estado{/b} e {b}Objetivos foram atualizados!"]
        praia_ID1_c3_1 = "Você vai chegando perto do mar e observa uma mala aberta e toda revirada no chão da areia. As roupas e alguns pertences estão um pouco longe da mala. Você pega o lacre da mala e vê que ele foi cortado com algum objeto afiado. Não há mais nada de útil aqui."
        praia_ID1_c4_1 = "Você sai caminhando pela costa da praia em busca de algum mantimento ou até mesmo uma saída daquele lugar. Já são vários Quilômetros percorridos e você não encontrou nada o que possa te ajudar."
        praia_notify_5 = ["Atualização de Inventário","O {b} Objetivo{/b} foi atualizado!"]
        praia_notify_6 = ["Atualização de Inventário","O {b} Estado{/b} foi atualizado!"]
        praia_ID1_vc2 = "Não consigo achar nada nessa ilha... Meus amigos?{w=1} Será que estão vivos?{w=1} Como que eu consegui sobreviver aquela queda?{w=1} Tantas perguntas... {w=1}Tenho que achar um meio {b}de sair dessa ilha rápido!{/b}"

        praia_ID2_n1 = "Você então sai andando pela costa da ilha.{w=1} Um lugar que parece ser tranquilo.{w=1} Mas não há quaisquer sinal de vida, nem mesmo aves.{w=1} Você ja está andando a muito tempo e a paisagem sempre parece a mesma."
        praia_ID2_n2 = "A areia da praia começa a entrar em seu tênis causando um desconforto nos seus pés."
        praia_ID2_n3 = "{b} Você deseja retirar seus sapatos?{/b}"
        praia_ID2_c1 = "Sim"
        praia_ID2_c2 = "Não"
        praia_ID2_c1_n1 = "Você retirou os sapatos."
        praia_ID2_c2_n1 = "Você continua calçado."
        praia_ID2_n4 = "Continuando andando pela areia da praia você ouve alguns gritos de dor vindo de trás de algumas pedras a alguns metros à sua frente."
        praia_ID2_n5 = "{b}Você deseja ir até lá?{/b}"
        praia_ID2_c3 = "Sim"
        praia_ID2_c4 = "Não"
        praia_ID2_c4_1 = "Você dá à volta pelas rochas o mais distante possível e continua seu caminho."
        praia_ID2_n6 = "Á medida que você vai se aproximando os gritos vão diminuindo aos poucos.{w=1} Atrás das pedras você encontra um homem deitado no chão, com um ferro atravessado em sua barriga.{w=1} Seu sangue está escorrendo pelo chão e dá para ver que alguns de seus órgãos saem pelo buraco na sua barriga.{w=1} O homem é um senhor já de idade, cabelos e barba grisalhos e com uniforme que parece ser da empresa do avião. Há um crachá no uniforme escrito {b}{color=#b7b77a}Alex Silva - Copiloto{/color}{/b}"
        praia_ID2_n7 = "O homem está muito pálido e parece fraco demais tentar alguma coisa, ele tenta dizer alguma coisa.{w=1} Mas suas palavras engasgam junto com o sangue na sua boca."
        praia_ID2_vc1 = "Você está bem senhor... Alex?"
        praia_ID2_n8 = "Uma pergunta automática e a qual já é retórica.{w=1} Talvez ele saiba de algo que aconteceu no avião, afinal é o copiloto.{w=1} Talvez saiba quem fez isso com ele, pois não há qualquer fragmento do avião por perto, até mesmo onde podem estar os outros tripulantes.{w=1} De qualquer forma, ele está sofrendo muito e não parece aguentar muito tempo."

        praia_ID2_c5 = "Perguntar o que aconteceu no avião"
        praia_ID2_c5_vc1 = "Senhor Alex, o que aconteceu no avião?"
        praia_ID2_c5_a1 = "A culpa... foi o piloto! {w=1}{i}- O homem tosse fortemente e fala pausadamente, alternado entre as palavras e os gritos de dor -{/i}{w=1}{cps=15} Ele era meu amigo há muito tempo, mas naquela viagem... Ele não... era o... mesmo!{/cps}{w=1}{i} - O senhor começa a ficar inquieto, se remexendo no chão e consequentemente rasgando seu abdômen ainda mais -{/i}{w=1}{cps=15} Eu Tentei... Juro que... Tentei...{/cps}"
        praia_ID2_c5_vc2 = "Ele desviou a rota?{w=1} Por quê?{w=1} Alex?"
        praia_ID2_c5_n1 = "Logo o homem para de respirar, suas últimas palavras ficam gravadas na memória..."

        praia_ID2_c6 = "Perguntar o que aconteceu com ele"
        praia_ID2_c6_vc1 = "Senhor Alex, o que aconteceu com o senhor?"
        praia_ID2_c6_a1 = "Foram eles!{w=1} Eles conseguiram me achar! {w=1}{i}- O senhor começa a ficar inquieto, se remexendo no chão e consequentemente rasgando seu abdômen ainda mais -{/i}{w=1} Depois de {b}tantos anos... tantas vezes...{/b}"
        praia_ID2_c6_vc2 = "Eles? {w=1}Quem senhor Alex?"
        praia_ID2_c6_a2 = "Fuja... filho! {w=1}{i}- O homem tosse fortemente e fala pausadamente, alternado entre as palavras e os gritos de dor -{/i}.{w=1} {cps=20}Fuja antes que{cps=15}... o próximo{cps=10}... seja... você!...{/cps}{/cps}{/cps}"
        praia_ID2_c6_vc3 = "Eles quem?{w=1} E porquê?{w=1} Alex?"
        praia_ID2_c6_n1 = "Logo o homem para de respirar, suas últimas palavras ficam gravadas na memória..."

        praia_ID2_c7 = "Perguntar onde estão os outros tripulantes"
        praia_ID2_c7_vc1 = "Senhor Alex, onde estão os outros? Você os viu?"
        praia_ID2_c7_a1 = "Eles os levaram!{w=1} A maioria!{w=1}{i} - O senhor começa a ficar inquieto, se remexendo no chão e consequentemente rasgando seu abdômen ainda mais -{/i}{w=1} Eu estava com um grupo de tripulantes... {cps=20}foi uma emboscada... {cps=15}alguns fugiram... outros foram levados{cps=10}... e eu... aqui...{/cps}{/cps}{/cps}"
        praia_ID2_c7_vc2 = [" e ", " estavam com você?{w=1} Será que estão bem?{w=1} Senhor Alex? {w=1}{b}Senhor Alex?!{/b}"]
        praia_ID2_c7_n1 = "Logo o homem para de respirar, suas últimas palavras ficam gravadas na memória..."

        praia_ID2_c8 = "Acabar com o sofrimento dele de vez"
        praia_ID2_c8_vc1 = "Ninguém deve sofrer tanto assim..."
        praia_ID2_c8_n1 = "Você vai andando até as rochas e olha elas por alguns segundos, se abaixa, pega uma e fala:"
        praia_ID2_c8_vc2 = "Deve servir..."
        praia_ID2_c8_n2 = "Você então se aproxima do homem e levanta a rocha sobre sua cabeça.{w=1} O senhor olha para cima em sua direção e sorrir.{w=1} Você então arremessa a rocha sobre a cabeça do homem, o impacto faz espalhar sangue e pedaços do celebro para todos os lados.{w=1} O que restou da sua cabeça foi atolada na areia. "

        praia_ID2_c9 = "Confotá-lo nos momentos finais da vida dele"
        praia_ID2_c9_vc1 = "Calma senhor, vai ficar tudo bem, o senhor vai ficar bem..."
        praia_ID2_c9_a1 = "Obrigado meu jovem...{w=1}{cps=20} Mas minha hora chegou...{w=0.5}{cps=15} Obrigado por não me...{w=0.5} {cps=10}Deixar...{/cps}{/cps}{/cps} "
        praia_ID2_c9_n1 = "Logo o senhor para de respirar, uma lágrima sai do rosto do homem, que morreu em paz."

        praia_ID2_c10 = "Ir Embora"
        praia_ID2_c10_vc1 = "Não, eu não aguento ver mais isso..."
        praia_ID2_c10_n1 = "Você então se afasta rápidamente daquele local."
