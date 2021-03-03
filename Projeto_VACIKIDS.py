print("-"*130)
print(f'{"ficha catalográfica": ^110}'.upper())
print("-"*130)
print(f'{"objetivo": ^110}'.upper())
print(""" 1)Conscientizar as crianças, pais e adolescentes sobre a importância da vacinação infantil""")
print(""" 2)Mostrar a importância da vacina como medida profilática na prevenção de doenças""")
print(""" 3)Aumentar o índice de vacinação nas crianças""")
print("-"*130)
print("""De acordo com o programa de pesquisa Intramural da Fundação Oswaldo Cruz (Fiocruz) publicado
em junho de 2020 no Internacional Journal of Infectious Diseases, houve redução de 13,6% nas doses de vacina
aplicada a crianças no ano de 2019""")  
print(" "*130)
print(f'{"para ler a pesquisa, clique em um dos links abaixo": ^110}'.upper())
print("-"*130)
print("""1)https://cidacs.bahia.fiocruz.br/2020/08/05/aplicacao-de-vacinas-em-criancas-vem-reduzindo-no-brasil-diz-estudo/""") 
print(" "*130)
print("""2)https://www.sciencedirect.com/science/article/pii/S1201971220305270""")  
print(" "*130)
print("""3)https://www.sciencedirect.com/science/article/pii/S1201971220305270""")  
print("-"*130)
print("-"*130)
print(f'{"vacikids: o joguinho que é a sua cara": ^110}'.upper())
print("-"*130)
print("""APRESENTADOR DO JOGO: Olá, crianças! Sou o Zé Dorinho, irmão do Zé Gotinha. Tudo bem com vocês?
Com o joguinho VACIKIDS,iremos em busca do reino encantado das crianças. Nesse reino encontraremos hobbits,
duendes, elfos domésticos e fadas que nos ajudarão a chegar no castelo fantástico. Para isso, encontraremos
diversos cenários e muitos desafios com perguntas que testam o nosso conhecimento sobre vacinação infantil. 
Vamos brincar?""")

print("-"*120)
print(""" Selecione uma das opções :
[1] Ler roteiro do jogo
[2] Escolher personagem """)

jogador = int(input("Digite a opção desejada:   "))
minhoca = "Mililo"
borboleta = "Lila"
leao = "Lico"
flor = "Alira"
sapo = "Sapolé"

if jogador == 1:
    print("""     Um personagem está numa terra encantada recheada de seres mágicos que o ajudarão a chegar ao CASTELO 
    FANTÁSTICO DAS CRIANÇAS. Para chegar ao castelo, o personagem deve completar um mapa através das perguntas que 
    acerta em cada cenário do jogo: jardim, floresta,deserto e montanha. A cada acerto, uma parte do mapa é revelado
    e uma chave é dada pelo guardião do local. Essa chave pode ser de bronze, prata, ouro ou diamante e abre um
    portal para que nosso personagem avance no jogo. 
    Se errar a pergunta, o personagem é recebido por monstros imaginários. Nesse caso, a Cuca, o Gasparzinho, o
    Curupira e o Rei de Copas tentarão, a todo custo, enviá-lo a um dos quatro castelos proibidos: Castelo das Fake
    News, Castelo da Teoria da Conspiração,Castelo Antivacina e Castelo da Doença. Nosso dever é ajudar o personagem
    a chegar ao Castelo Fantástico das crianças em total segurança, pois os monstrinhos imaginários querem infectá-lo 
    e prendê-lo no castelo proibido para sempre. Vamos brincar? """)
print("-"*130)
personagem_do_jogo = int(input("Escolha seu personagem:\n[1] Mililo [2] Lila [3]Sapolé [4] Lico [5] Alira \nDigite o código = "))
print("-"*130)
print(" "*130)
personagem = ""
if (personagem_do_jogo == 1):
    personagem = "Mililo"
    print(f"Olá, meu nome é {personagem}. Obrigado por me escolher, fiquei muito feliz. Juntos chegaremos\n"
    "ao castelo mais fantástico do mundo e encontraremos nossos amigos em segurança e vacinados.")
elif (personagem_do_jogo == 2):
    personagem = "Lila"
    print(f"Olá, meu nome é {personagem}. Sou uma borboleta super simpática e estou muito feliz de ser a escolhida para te ajudar\n"
    "a chegar ao castelo. Espero que tenhamos uma trajetória cheia de aventuras e com muito aprendizado. Vamos começar?:p")
elif (personagem_do_jogo == 3):
    personagem = "Sapolé"
    print(f"Olá, criançada! Me chamo {personagem}, o sapo mais travesso do reino encantado. Adoro comer insetos\n"
    "e espero encontrar muitos deles em nosso reino, pois preciso estar forte para te ajudar a chegar ao\n"
    "castelo. Vamos começar?;)")
elif (personagem_do_jogo == 4):
    personagem = "Lico"
    print(f"Olá, crianças! Me chamo {personagem} e sou o leão mais simpático do reino encantado. Adoro\n"
    "carne e sempre me preocupo com a saúde para ser um leão forte e saudável. Por isso tomo\n"
    "todas as vacinas. Quero ver você acertando todas as perguntas, hein? Vamos começar? :o")
elif (personagem_do_jogo == 5):
    personagem = "Alira"
    print(f"Olá, me chamo {personagem} e estou super entusiasmada com a nossa aventura. Sou uma flor super delicada\n"
    "e muito corajosa. Juntos iremos descobrir todos os segredos do reino até preencher o nosso cartão\n"
    "de vacina para chegar ao castelo, pois como diz a mamãe: criança inteligente é criança vacinada:)")
else:
    print("Você não escolheu nenhum jogador. Volte e escolha")

print("-"*130)
print(""" 
    [1] Escolher outro personagem
    [2] Iniciar jogo com esse personagem """)
print("-"*130)
escolha = int(input("Digite a opção desejada:   "))
if escolha == 1:
    personagem_do_jogo = int(input("Escolha seu personagem novamente:\n[1] Mililo [2] Lila [3]Sapolé [4] Lico [5] Alira \nDigite o código = "))
    if personagem_do_jogo == 1:
        personagem = "Mililo"
        print(" "*130)
        print(f"Olá, meu nome é {personagem}. Obrigado por me escolher, fiquei muito feliz. Juntos chegaremos\n"
    "ao castelo mais fantástico do mundo e encontraremos nossos amigos em segurança e vacinados.")
    elif personagem_do_jogo == 2:
        personagem = "Lila"
        print(" "*130)
        print(f"Olá, meu nome é {personagem}. Sou uma borboleta super simpática e estou muito feliz de ser a escolhida para te ajudar\n"
    "a chegar ao castelo. Espero que tenhamos uma trajetória cheia de aventuras e com muito aprendizado. Vamos começar?:p")
    elif personagem_do_jogo == 3:
        personagem = "Sapolé"
        print(" "*130)
        print(f"Olá, criançada! Me chamo {personagem}, o sapo mais travesso do reino encantado. Adoro comer insetos\n"
    "e espero encontrar muitos deles em nosso reino, pois preciso estar forte para te ajudar a chegar ao\n"
    "castelo. Vamos começar?;)")
    elif personagem_do_jogo == 4:
        personagem = "Lico"
        print(" "*130)
        print(f"Olá, crianças! Me chamo {personagem} e sou o leão mais simpático do reino encantado. Adoro\n"
    "carne e sempre me preocupo com a saúde para ser um leão forte e saudável. Por isso tomo\n"
    "todas as vacinas. Quero ver você acertando todas as perguntas, hein? Vamos começar? :o")
    elif personagem_do_jogo == 5:
        personagem = "Alira"
        print(f"Olá, me chamo {personagem} e estou super entusiasmada com a nossa aventura. Sou uma flor super delicada\n"
    "e muito corajosa. Juntos iremos descobrir todos os segredos do reino até preencher o nosso cartão\n"
    "de vacina para chegar ao castelo, pois como diz a mamãe: criança inteligente é criança vacinada:)")
    else:
        print("")
elif escolha == 2:
    print(f'{"Avance no jogo": ^110}'.title())
else:
    print("Opção errada. Volte e tente novamente")
print(" "*130)
print(f'{"Passeando no Jardim": ^110}'.upper())
print("-"*130)
def jardim (personagem):
    print(f"""      {personagem} inicia a trajetória rumo ao castelo fantástico: lugar enigmático recheado de crianças
    saudáveis e vacinadas. Ele está no jardim, onde terá que encontrar o primeiro pedaço do mapa que o conduzirá ao 
    portal da floresta. Para isso, precisa localizar Alice, uma fada bem sapeca que possui a chave de bronze que abre 
    o portal. Para ter acesso a chave, {personagem} precisa convencer a fada a liberar o primeiro pedaço do mapa que 
    conduz ao castelo, mas ela só fará isso se acertarmos a pergunta de vacinação infantil. A Cuca, monstrinho do jardim,
    pode aparecer a qualquer momento. Seu objetivo é espalhar notícias falsas sobre vacinação e levá-lo ao Castelo proibido 
    das Fake News, te prendendo para sempre. Por isso, acerte os testes e avance no jogo, ou erre as perguntas e fique preso 
    no castelo da Cuca """)
    
    print(f'{"Pergunta 1": ^110}'.upper())
    print("-"*130)
    print(""" Por que a vacinação em dia é tão importante na vida de uma criança? """) 

    print(f"""Escolha a alternativa correta:
    [A] A vacina é importante porque ajuda o {personagem} a entrar no castelo proibido das Fake News.
    Nesse castelo, ele não  vai ficar preso e poderá ajudar a Cuca em sua missão de destruir o castelo 
    fantástico das crianças.
    [B] A vacina é importante para impedir que a Cuca malvada prenda o {personagem} no Castelo das Fake 
    News. Com a vacina,o {personagem} fica mais forte, mais saudável e a Cuca malvada não pode prendê-lo
    [C] A vacina é importante como forma de   """)
    usuario = input("Digite o código = ")
    print("-"*130)
    if usuario == "B":
        print(f"Parabéns,{personagem}!Pegue a chave de bronze que abre o portal do jardim e siga para a floresta.\n O primeiro pedaço do mapa irá te ajudar a chegar ao castelo fantástico das crianças! Boa sorte ")
    elif usuario == "A":
        print("Você errou, provavelmente por acreditar em Fake News. Agora a Cuca te levará ao Castelo proibido das\n Fake News e você ficará preso para sempre")
    elif usuario == "C":
        print("Poxa, amigo. Você errou e o Zé Dorinho, apresentador do jogo, ficou muito triste. Você caiu nas mãos\n da Cuca e será enviado ao castelo proibido :(")
    else:
        print("FIM")

jardim(personagem)


print("-"*130)
print(f'{"Correndo do Gasparzinho": ^110}'.upper())
print(" "*130)

def floresta (personagem):
    print(f"""Após sair do jardim,{personagem} entra na floresta em busca do segundo
pedaço do mapa que o conduzirá ao deserto. Para encontrar o mapa, precisa localizar Morpheu, um
hobbit de 90 centímetros de altura que é o guardião da floresta, pois só ele tem acesso ao mapa e a
chave de prata que abre o segundo portal. O grande problema é que o Gasparzinho,
monstrinho da floresta, irá tentar despistar nosso personagem através de teorias conspiratórias.
Seu objetivo é levar todos os animais da floresta para o castelo proibido da conspiração: lugar
sombrio com bichinhos alienados que não acreditam na importância da vacina. Diante disso, acerte o
teste e avance no jogo, ou erre a pergunta e se torne alienado dentro do castelo do Gasparzinho: """)
    print(" "*130)
    print(f'{"Pergunta 2": ^110}'.lower())
    print("-"*130)
    print(""" Como a vacina reage no organismo? """)
    usuario = str(input("""Escolha a alternativa correta:
    [A] A vacina estimula o corpo a se defender contra vírus e bactérias que provocam doenças
    [B] A vacina só traz prejuízos para a saúde, pois toda vacina contém vírus que transformam 
    nosso personagem em um monstrinho
    [C] A vacina é uma forma de escravizar todos os animais da nossa floresta  """))
    print("-")
    if usuario == "A":
        print("Parabéns! Pegue a chave de prata que abre o portal da floresta e o segundo\n pedaço do mapa que te conduzirá ao castelo fantástico das crianças. Boa sorte,amigo. Vai precisar!")
    elif usuario == "B":
        print("Você errou! Agora, o Gasparzinho irá te levar para o Castelo da Teoria da Conspiração e você\n ficará alienado para sempre.")
    elif usuario == "C":
        print(" Poxa, você errou! O Zé Dorinho, apresentador do jogo, ficou muito triste, pois o Gasparzinho\n te levará ao Castelo da Conspiração e você ficará alienado para sempre")
    else:
        print("FIM")

floresta(personagem)
print(" "*130)
print(f'{"O sol de quase um deserto": ^110}'.upper())
print("-"*130)
print("-"*130)
def deserto ():
    print("""Chegando ao deserto, nosso personagem precisa encontrar o guardião do cenário. Seu nome é Linnus,
um elfo doméstico flutuante em forma de caveira que não precisa de água para sobreviver. Linnus possui uma
pele escamada no interior do seu esqueleto que suporta altas temperaturas. Seu habitat natural é o deserto
e sua função é protegê-lo do Curupira: monstrinho do jogo. Diz a lenda que o Curupira era um elfo doméstico,
mas por recusar a vacinação infantil, acabou se transformando num monstrinho horripilante de pés invertidos.
Agora, revoltado, quer enviar todos os bichinhos para o Castelo proibido Antivacina: local onde todos os 
bichinhos sofrem mutação e se transformam em Curupiras. Para evitar que isso aconteça, nosso personagem precisa 
da ajuda do elfo doméstico,pois apenas ele tem o terceiro pedaço do mapa que nos guiará ao Castelo Fantástico das 
Crianças e a chave de ouro que abre o portal para o último cenário. Para ter acesso a chave e ao mapa, nosso
personagem só tem uma escolha: acertar a pergunta. Essa é sua chance, essa é sua escolha. Acerte o teste e avance 
no jogo, ou erre a pergunta e seja transformado em Curupira no Castelo Anvacina """)
    print("-"*130)
    print(f'{"Pergunta 3": ^110}'.upper())
    print("-"*130)
    print(""" Sobre a vacina em gotinha, marque a alternativa FALSA """) 

    print("""Escolha a alternativa FALSA:
    [A] A vacina em gotinha é feita pelo Zé Dorinho, imão do Zé Gotinha. Ele irá aplicar a dose da vacina
    e proteger a criança contra as doenças do castelo antivacina.
    [B] A vacina em gotinha foi inventada pelo Castelo Antivacina para proteger as crianças do Castelo Fantástico.
    No Castelo Antivacina, todas as crianças estão vacinadas com a ajuda do guiardião do castelo: o Curupira.
    [C] Diz a lenda que o Curupira era um elfo doméstico, mas por não tomar a vacina em gotinha, sofreu mutações
    e virou um monstrinho de pés invertidos que assusta as crianças """) 
    usuario = input("Digite o código = ")
    print("-"*130)
    if usuario == "A":
        print(f"Você errou,{personagem}! Agora, o Curupira irá te levar para o Castelo Antivacina.\n Lá você será será trsnformado em Curupira.")
    elif usuario == "B":
        print(f"Parabéns, {personagem}. Você acertou! Pegue a chave de prata que abre o portal da montanha e o terceiro\n pedaço do mapa que te conduzirá ao castelo fantástico das crianças. Logo chegará ao seu destino!")
    elif usuario == "C":
        print(" Poxa, você errou! Por não ter tomado a vacina, o Curupira te levará ao Castelo proibido Antina\n  e você nunca mais poderá encontrar seus amigos no Cstelo Fantástico das Crianças")
    else:
        print("FIM")
deserto()

print("-"*130)
print(f'{"Subindo pelas montanhas": ^110}'.upper())
print("-"*130)
def montanha():
    print("""Enfim, chegamos a montanha. Nosso objetivo agora é encontrar o duende alado que possui asas de gavião
e penas de papagaio. Super falante, é fácil encontrá-lo, pois ele sempre repete tudo o que escuta. Guardião da
montanha, esconde o último pedaço do mapa que nos guiará ao Castelo Fantástico, além de guardar em suas penas a
chave de diamante que abre o portal do Castelo mais querido do nosso reino. O Rei de Copas, monstrinho da montanha,
quer enviá-lo ao Castelo proibido da doença. O nosso personagem está atento, confiante e sabe da importância da 
vacinação infantil. Responda a pergunta, encontre o duende alado e tenha acesso a chave de diamante para entrar no 
reino encantado, ou seja infectado pelo Rei de Copas no Castelo proibido da Doença""")
    print("-"*130)
    print(f'{"Pergunta 4": ^110}'.upper())
    print("-"*130)
    print(""" O que são vacinas? 
    [A] São substâncias químicas utilizadas pelo rei de Copas para deixar nosso personagem doente, impedindo-o de
    chegar ao reino encantado
    [B] Vacina é uma substância que ajuda na prevenção de doenças causadas por bactérias e vírus, deixando o 
    personagem mais forte, mais saudável e próximo do reino encantado das crianças no Castelo fantástico
    [C] Diz a lenda que o Curupira era um elfo doméstico, mas por não tomar a vacina em gotinha, sofreu mutações
    e virou um monstrinho de pés invertidos que assusta as crianças """)     
    usuario = input("Digite o código = ")
    print("-"*130)
    if usuario == "A":
        print(f"Poxa, {personagem}! Você ficará preso no Castelo da Doença e será infectado por vírus enviados pelo Rei de Copas, monstrinho do jogo")
    elif usuario == "B":
        print(f"Você acertoou! Parabéns,{personagem}. Aqui está a chave de diamante que abre o portal da montanha e o último pedaço do\n mapa que te conduzirá ao castelo mais fántástico do nosso reino. Seja feliz:)")
    elif usuario == "C":
        print(f"Você errou,{personagem}. Agora será enviado ao Castelo da Doença e infectado pelos vírus do Rei de Copas :(")
    else:
        print("Não há essa alternativa. escolha novamente")
montanha()
print(" "*110)
print("-")
print("ENFIM, CHEGAMOS AO CASTELO".center(110))


