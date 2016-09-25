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
######## Geral
        lang_Yes = 'Yes'
        lang_No = 'No'
        lang_version ='Version'
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
        obj_c = "{color=#458B00}[Completado]{/color} "
        obj_n = "[Não Completado]"
        obj_semObj_title = "Sem Objetivos"
        obj_semObj_desc = "Você ainda Não Possui Objetivos."
        obj_ComerAlgo_title = "Comer alguma coisa"
        obj_ComerAlgo_desc = "Achar algo na praia que mate a sua fome."
######## Estado
        sts_fome_name = "Fome"
        sts_fome_desc = "Você está com fome no momento."
        sts_fome2_name = "{b}Fome{b}"
        sts_fome2_desc = "Você está com muita fome no momento."
        sts_fome3_name = "{b}Fome{/b}"
        sts_fome3_desc = "{color=#EEAD0E} Você está morrendo de fome!{/color} ."
        sts_semFome_name = "Satisfeito"
        sts_semFome_desc = "Atualmente você está Satisfeito."
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
##      Tradução da História                        ##
######################################################
        game_you = 'You'
        game_unknow = 'Weird'
        game_joao = 'João'
        game_bia = 'Beatriz'
        game_alex = 'Alex Silva'
        chapter_1 = "{size=100}Capitulo 1{/size}{p} Sozinho"
######## Cena Avião
airplane_1 = "You are on a commercial flight coming home from a trip with two of your friends.{w=1} You got the window seat on the right row, and your friends are seating next to you, on your left.:{w=1} João is right beside you and Beatriz is right beside him, taking the aisle seat."
        airplane_2 = "Looking out of the window you can see how far from the ground the airplane is.{w=1} At that moment you were crossing the ocean, very close to the clouds falling apart to the touch of the airplane's wing, and also next to a flock of birds migrating{w=1}.An astonishing scene, for sure."
        airplane_3 = "Now you turn to your left and see both of your friends chatting, they seem pretty happy.{w=1}You do not intrude their conversation, Beatriz laughs really hard and João keeps glancing at you, with a concerned expression on his face.{w=1} After a while, he finally asks you:"
        airplane_4 = "Dude, are you okay?"
        airplane_5 = "At this point Beatriz stops laughing and both of them wait for your reply:"
        airplane_notify1 = "{b}{color=#33b77a} João{/color}{/b} is worried about you"
        airplane_5c1 = "Say that you are fine."
        airplane_5c2 = "Complain because you felt left out of the conversation."
        airplane_ID1_1_vc1 = "Yeah, I'm good, thanks for asking. It's just that there's something that's bothering me..."
        airplane_ID1_1_j1 = "Oh man, what's up? Can I help?{w=1} You know you can count on me, right?"
        airplane_ID1_1_n = "You definitely feel troubled, it may be because the girl you are in love with has been chatting a little too intimately with your best friend.{w=1} You also have another feeling... a very strange type of feeling.{w=1} You feel like something unexpected is about to go down, it almost feels like some sort of... Intuition, maybe?.{w=1}  You think that's too weird (even for you), and so you are afraid of telling that to your friends, since they may not understand you and say you are crazy"
        airplane_ID1_1_c1 = "Talk about João's conversation with Beatriz"
        airplane_ID1_1_c2 = "Talk about the feeling you have"
        airplane_ID1_1_c3 = "Don't tell anything"
        airplane_ID2_1_vc1 = "It's nothing... I don't want to interrupt you guys... "
        airplane_ID2_1_j1 = "Sooo... are you jelly again, man?"
        airplane_ID2_1_b1 = "Hey, what are you talking about?"
        airplane_notify1 = "{b}{color=#33b77a} João{/color}{/b} has noticed your jealousy"
        airplane_ID2_1_j2 = "Nothing, it's not about you, - he winks at her - don't worry."
        airplane_ID2_1_b2 = "I don't like the tone of this conversation..."
        airplane_ID2_1_vc2 = "You know what? I'm gonna take a nap, wake me up when we get home"
        airplane_ID2_1_b3 = "Well, you've been acting so weird that we might not even notice if you're asleep or awake (Laughter)."
        airplane_ID2_1_vc3 = "Haha, you're so funny..."
        airplane_ID2_1_j3 = "Sleep tight dude!"
        airplane_ID2_1 = "Você então encosta cabeça na poltrona e vira a cabeça para a janela do avião, aquela paisagem vai te relaxando e rapidamente você cai no sono."
        airplane_ID2_2_vc1 = "I don't know exacly. I just feel like something really bad was about to happen..."
        airplane_ID2_2_j1 = "What do you mean man? We are on a plane! Eu como um ex militar te garanto que é o meio de transporte mais seguro que existe!{w=1} Acho que isso é mania de detetive."
        airplane_ID2_2_b1 = "Cara, deixa de paranóia. Relaxa ai..."
        airplane_ID2_2 = "Ele e Beatriz começam a rir."
        airplane_ID2_2_vc2 = "Qual o motivo da graça?"
        airplane_ID2_2_b2 = "Nada... Só tenta relaxar um pouco.{w=1} Não vai acontecer nada. É só... {w=1}- ela segura o riso -{w=1}{b} medo.{/b} "
        airplane_ID2_2_vc3 = "Acho que é o melhor que eu faço... me acorde na hora de desembarcar."
        airplane_ID2_2_b3 = "Ok, não se procupe!"
        airplane_ID2_3_vc1 = "Não é nada, é besteira minha."
        airplane_ID2_3_b1 = "Como sempre né?"
        airplane_ID2_3_vc2 = "Não perde uma eim..."
        airplane_ID2_3_j1 = "Tudo bem cara, se você diz que não é nada."
        airplane_ID2_3_b2 = "Tenta relaxar um pouco ai, você parece mais estranho que o normal."
        airplane_ID2_3_vc3 = "Agora falou algo de útil! Vou dormir, me acordem na hora do desembarque!"
        airplane_ID1_2_vc1 = "Ah, agora vocês perceberam que eu estou aqui né!"
        airplane_ID1_2_j1 = "Que isso cara, calma. Só estavamos..."
        airplane_ID1_2_vc2 = "Não precisa falar mais nada, se eu soubesse que iria ficar sobrando..."
        airplane_ID1_2_b1 = "Calma aew cara! O que você tem? Você não é assim... está acontecendo alguma coisa?"
        airplane_ID1_2 = "Você começa a ficar com calafrios, a suar frio e suas mãos tremem por alguns segundos,{w=1} mas logo depois esses sintomas passam.{w=1} Algo misteriosamente começa a preocupar você, uma sensação ruim toma conta de você. Algo que nunca aconteceu antes.{w=1} Parece coisa de louco, e, talvez seus amigos ririam disso."
        airplane_ID1_2_c1 = "Não contar nada e admitir o ciúmes."
        airplane_ID1_2_c2 = "Contar sobre o que você sentiu."
        airplane_ID1_2_c3 = "Dizer que não é da conta deles."
        airplane_ID3_1_vc1 = "Não é nada de mais cara! Apenas fiquei com um pouco de ciúmes, admito."
        airplane_ID3_1_j1 = "Não precisa se desculpar cara, acho que tenho um pouco de culpa nisso também."
        airplane_ID3_1_b1 = "Concordo com João, a culpa é dele mesmo!"
        airplane_ID3_1_j2 = "Cala boca Bia, você não entra em nada."
        airplane_notify_3 = "Todos se lembrarão disso."
        airplane_ID3_1 = "Naquele momento todos começam a rir, como se estivessem ainda nas férias."
        airplane_ID3_1_j3 = "Fazemos uma bela equipe, espero que nunca nos separamos!"
        airplane_ID3_1_b2 = "Vocês são minha familia, o que dizer de João? Mal conheço e já considero pakas!"
        airplane_ID3_1_j4 = "Graças a nosso amigo em comum pudemos nos conhecer!"
        airplane_ID3_1_b3 = "Tem razão, ele é um gênio!"
        airplane_ID3_1_vc2 = "Obrigado, obrigado...{p=1}Estou um pouco cansado, vou dormir um pouco... {w=1}Só não me deixem no avião dormindo eim!"
        airplane_ID3_1_j5 = "Pode deixar!"
        airplane_ID3_3_vc1 = "Não é da conta de vocês."
        airplane_ID3_3_j1 = "Ui, nossa, que grosseiro. Vai me morder agora ou depois?"
        airplane_ID3_3_b1 = "Deixa ele se acalmar João. Melhor não provocar o bebê bravo!"
        airplane_notify_4 = "Eles se lembrarão disso."
        airplane_ID3_3 = "No momento os dois riem."
        airplane_ID3_3_vc2 = "Melhor eu dormir, já que não tão nem aí mesmo..."
        airplane_ID3_3_b2 = "Ei, não fica assim!"
        airplane_ID3_3_j2 = "O que nós fizemos?"
        airplane_ID3_3_vc3 = "Nada, esqueçam..."
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
        dream1_15 = "{cps=10} Os círculos vão se aproximando de você{/cps}{cps=5}...{/cps}{p=1}{cps=20} Mas ao tocarem na luz que sai da passagem eles somem do nada, junto com a neblina e toda aquela cena de terror.{/cps}"
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
        airplane_wakeup_1 = "Você então acorda, abrindo lentamente os olhos você vê a janela com vista para o oceano e uma ilha. Um pouco tonto, seus sentidos vão voltando aos poucos, e, como em um reflexo você olha para seus dois braços em busca de algum ferimento - não há nada, nem um arranhão -."
        airplane_wakeup_2 = "Você respira aliviado, sem entender nada e já parcialmente recuperado você comenta, virando a cabeça para a sua esquerda:"
        airplane_wakeup_vc1 = "Gente, vocês não vão acreditar..."
        airplane_wakeup_3 = "Seus amigos estão com máscaras de ar no rosto e os cintos apertados.{p=1}{color=#f00}Uma aeromoça é arremessada de uma ponta a outra do avião.{/color}{p=1}Com seus sentidos recuperados você sente o avião tremer muito e consegue ouvir as pessoas gritarem apavorizadas."
        airplane_wakeup_4 = "Há um buraco enorme do casco do avião. {p=1}Há pessoas que são arrastadas para aquele buraco e entram em queda livre no céu. As malas dos compartimentos voam sobre o interior do avião.{p=1}Você está sem seus cintos e começa a sentir {b}dificuldades para respirar.{/b}"
        airplane_wakeup_c1 = "Apertar os Cintos"
        airplane_wakeup_c1_1 = "Você tenta puxar os cintos de segurança da poltrona do avião, mas parece está emperrado em alguma coisa, o avião começa a se inclinar para frente e você é jogado para a poltrona da frente com muita força."
        airplane_wakeup_c2 = "Colocar mascara de oxigênio"
        airplane_wakeup_c2_1 = "Você pega a máscara de oxigênio bem a sua frente e coloca sobre seu rosto. Você vai respirando o oxigênio lentamente, quando o avião se inclina para frente e você é arremessado em direção a potrona da frente."
        airplane_wakeup_5 = "Você vai levantando e apoia as suas costas na poltrona, ficando de frente para seus amigos, eles viram a cena e choram muito, tentam gritar mas os gritos são abafados pelas mascaras sobre seus rostos."
        airplane_wakeup_6 = " João estica a mão dele, parece que ele quer que você a segure. O avião balança muito."
        airplane_wakeup_c3 = "Segurar a mão dele"
        airplane_wakeup_7 = "Como essa pode ser a sua única opção, você estica seu braço em direção a João.{p=1}O avião se inclina ainda mais e você só tem o braço dele para se segurar.{p=1}Olhando para cima você vê as malas caindo em sua direção e uma delas acerta a sua cabeça."
        airplane_wakeup_8 = "Você então larga a mão de João e se bate em várias poltronas até ser sugado pelo buraco em uma velocidade absurda. Você entra em queda livre. Dá para ver o avião caindo e as chamas saindo das duas asas. "
        airplane_wakeup_9 = " Logo você começa a girar várias vezes no ar e sente pancadas no seu corpo todo - são as correntes de ar que colidem com seu corpo em velocidades altíssimas. Você sente dores insuportáveis e perde a consciência."
        airplane_wakeup_10 = "Você está desacordado"
        airplane_wakeup_11 = "Você vai recuperando o seus sentidos aos poucos..."
######## Cena Praia
        beach_1 = "Você está deitado de olhos fechados e sente á água batendo em seu rosto.{p=1}Você vai abrindo os olhos lentamente e enxerga o mar a sua frente.{p=1}Seu rosto está sujo de areia, você apoia as duas mãos no chão e dá um impulso para levantar, e logo começa a limpar o rosto com as mãos."
        beach_2 = "Olhando ao redor parece ser uma praia, o cheiro do mar é predominante junto com o som das ondas se quebrando. "
        beach_3 = "{w=1}Perto da praia há uma {b}floresta bem densa.{/b}{p=1}No encontro da floresta com a praia há coqueiros altos e bananeiras com cachos cheios. {w=1}Já na beira do mar há algumas malas abertas no chão. Sua barriga ronca de {color=#f00}fome{/color}, parece que você não come {b}à dias.{/b}"
        beach_notify_1 = ["Função Desbloqueada: Inventário!","Agora você pode acompanhar seu Estado! Você verá um novo alerta quando as informações forem atualizadas."]
        beach_4 = "Suas roupas estão rasgadas, mas não há qualquer tipo de ferimento.{p=1}Também não há qualquer sinal de vida no seu campo de visão - nem sinal de morte -.O único sinal que faz você lembrar do que aconteceu no avião são aquelas malas ali na areia, nada além disso."
        beach_vc1 = "Cara, estou um pouco tonto... Minha cabeça dói, e {b}estou com fome...{/b} E ainda teve aquele acidente, como ainda estou vivo? E o mais importante, como vou sair daqui?"     
        beach_notify_2 = ["Função Desbloqueada no Inventário!","Agora você pode acompanhar seus Objetivos! {p}Você tem um novo Objetivo!{p}Você verá um novo alerta quando as informações forem atualizadas."]

        beach_ID1_vc1 = "O que devo fazer agora?"
        beach_ID1_c1 = "Olhar Coqueiros"
        beach_ID1_c2 = "Olhar Bananeiras"
        beach_ID1_c3 = "Olhar Destroços na Areia"
        beach_ID1_c4 = "Vasculhar Ilha"
        beach_ID1_c1_1 = "Você chega perto de um dos coqueiros da praia, esse está carregado de cocos, mas é muito alto."
        beach_ID1_c1_vc1 = "Parece que vou ter que ficar na vontade, os coqueiros são muito altos para eu subir, não conseguiria com a fome que estou."
        beach_ID1_c2_1 = "Você vai chegando perto de uma das inúmeras bananeiras da praia, esta está com o cacho cheio e uma cor atraente. Você pega algumas e come."
        beach_ID1_c2_vc1 = "Hum, que delícia essas bananas, estou satisfeito por agora. Melhor eu seguir meu caminho e arranjar um jeito de sair daqui."
        beach_notify_4 = ["Atualização de Inventário","O {b} Estado{/b} foi atualizado!"]
        beach_ID1_c3_1 = "Você vai chegando perto do mar e observa uma mala aberta e toda revirada no chão da areia. As roupas e alguns pertences estão um pouco longe da mala. Você pega o lacre da mala e vê que ele foi cortado com algum objeto afiado. Não há mais nada de útil aqui."
        beach_ID1_c4_1 = "Você sai caminhando pela costa da praia em busca de algum mantimento ou até mesmo uma saída daquele lugar. Já são vários Quilômetros percorridos e você não encontrou nada o que possa te ajudar."
