import discord
from discord.ext import commands
import os
import requests
import json
import random
import dotenv
from dotenv import load_dotenv
from key import key




os.chdir("D:\\Users\\Eu\\Desktop\\(Audiovisual)\\Argo-Bot")


intents = discord.Intents.default()
intents.message_content = True
bot = client = commands.Bot(command_prefix = '-', case_insensitive = True, activity=discord.Game(name="Para ajuda use '-ajuda'"), status=discord.Status.online, intents=intents)
versao = ('0.0.1')
banner = ('https://imgur.com/H6pKvIH')


## Bancos de dado ##


cara_coroa = ["Cara", "Coroa"]
frases_do_dia = [
  "'O ignorante afirma, o sábio duvida, o sensato reflete.' — Aristóteles",
  "'Nossas dúvidas são traidoras e nos fazem perder o que, com frequência, poderíamos ganhar, por simples medo de arriscar.' — William Shakespeare",
  "'Querias ser livre. Para essa liberdade, só há um caminho: o desprezo das coisas que não dependem de nós.' — Epicteto",
  "'A dor é inevitável, já o sofrimento, completamente opcional.' — Pain",
  "'O mundo é impiedoso, e exatamente por isso, lindo.' — Hajime Isayama",
  "'Uma boa pessoa? Bem... eu não gosto desse termo. Pra mim, isso só significa uma boa pessoa para você. E eu não acho que exista alguém bom para todos.' — Armin Arlert",
  "'Se você ganhar, você vive. Se você perder, você morre. Se você não lutar, não pode vencer. Lute! Lute!' — Eren Jaeger",
  "'Não existe nada que te prive da liberdade além da ignorância.' — Hajime Isayama",
  "A única coisa que podemos fazer é acreditar que não vamos nos arrepender da escolha que fizemos.' — Hajime Isayama",
  "'Palavras bonitas não podem mudar o mundo.' — Lelouch Lamperouge",
  "'Se o Rei não se mover, seus súditos não irão segui-lo.' — Zero",
  "'Não importa o quanto se tente mudá-lo, o mundo continua o mesmo.' — Lelouch Lamperouge",
  "'Uma vida sem mudanças não se chama “vida”. Você apenas pode chama-lá de “experiência”.' — Lelouch Vi Britannia",
  "'O que você fará quando houver um mal que não pode ser derrotado por justiça? Você derrotará o mal com mal ou aceitará que sua justiça pereça diante do mal?' — Zero",
  "'Falsas lágrimas são capazes de machucar outras pessoas. Falsos sorrisos são capazes de machucar a sí mesmo.' — C.C.",
  "Todos procuram por esperança. Vencer significa atropelar isso. Inimigos e aliados são iguais. Porque estamos procurando por algo…' — Schneizel el Britannia",
  "'Isso mesmo. Destruição é necessária antes da reconstrução. Se meus sentimentos se tornarem um problema no processo, será melhor eliminá-los.' — Zero",
  "'Objetivos alcançados de modos errados são objetivos errados' — Kururugi Suzaku",
  "'A partir daquele dia eu estive mentindo pra mim mesmo… O fato de que eu estou vivo é uma mentira… Meu nome é uma mentira. Minha história é uma mentira. Cheia de mentiras… Estando farto de um mundo que não muda nunca, mas sou incapaz de desistir do desespero dessa mentira, de que ele vai mudar.' — Lelouch Vi Britannia",
  "'Mesmo sabendo que há várias coisas que não se pode esquecer e várias coisas tristes também, amanhã continuará vindo, não é?' — Shirley Fenette",
  "'Sentimentos são como rochas que são construídas no nosso coração. Seriam essas rochas os restos de ontem ou os fundamentos do amanhã?' — Lelouch Lamperouge",
  "'Não desista, não há vergonha em cair! A verdadeira vergonha é não se levantar novamente!' — Shintaro Midorima",
  "'Você pode morrer a qualquer momento, mas viver requer coragem.' — Kenshin Himura",
  "'É mais importante dominar as cartas que você tem nas mãos do que reclamar das cartas que seu oponente recebeu.' — Grimsley",
  "'Se você não gosta do seu destino, não o aceite. Em vez disso, tenha a coragem para transformá-lo naquilo que você quer que ele seja.' — Sem autor",
  "'O mundo não é perfeito. Mas ele está aqui para nós, fazendo o melhor que pode... e é isso que o faz tão lindo!' — Roy Mustang",
  "'O que quer que você perca, você encontrará novamente. Mas aquilo que jogar fora, você nunca terá de volta.' — Kenshin Himura",
  "'Mesmo que nós esqueçamos os rostos dos nossos amigos, jamais esqueceremos os laços que foram cravados nas nossas almas.' — Otonashi Yuzuru",
  "'Há momentos que você precisa desistir de alguma coisa para preservar a outra.' — Rize",
  "'Se você aceita tudo sem ao menos questionar, vai acabar perdendo a capacidade de pensar.' — Pandora",
  "'Está tudo bem. Nós nunca estaremos separados. Contanto que estejamos vivos, nos encontraremos sempre.' — Angel Sanctuary",
  "'Seres humanos morrem. Animais morrem. Plantas morrem. Até os ceifadores de almas morrem. É o arco do universo. Tudo o que ganha vida acaba deixando de existir.' — Baraggan Louisenbairn",
  "'Eu estou cansado de não fazer nada, mas eu sou muito preguiçoso pra fazer alguma coisa.' — Hikki",
  "'Esta é uma peça mágica que suprime meus poderes mágicos. Se eu fosse tirar isso, uma grande catástrofe certamente aconteceria neste mundo ... Ah, mentira. Eu só a uso mesmo para deixar o look mais estiloso. — Magumin",
  "'Se você desviar os olhos das coisas tristes, elas acontecerão novamente um dia. Se você continuar fugindo, continuará repetindo os mesmos erros. É por isso que você precisa encarar a verdade diretamente.' — Riki Naoe",
  "'O medo não é malvado. Ele te mostra qual é a sua franqueza. E quando você conhece a sua franqueza, então pode se tornar mais forte e mais gentil.' — Gildarts Clive",
  "'Se as pessoas acreditam em tudo que ouvem, então não há diferença entre a mentira e a verdade.' — Kuroshitsuji",
  "'O que é importante não é o que os outros pensam de você, mas como você age perante a isso.' — Alguém de Nanatsu",
  "'A fim de ganhar algo, deve sacrificar um outro de valor equivalente. Essa é a lei da Alquimia. — Edward Elric",
  "'Ensinamentos obtidos sem sofrimento são desprovidos de valor.' — Edward Elric",
  "You are a great person."
]
animes = [
  "https://i.pinimg.com/originals/0a/62/60/0a6260f36f2ecd219dba2f8652809699.jpg",
  "https://i.pinimg.com/564x/67/2c/78/672c785268609622791428bb836600ed.jpg",
  "https://i.pinimg.com/564x/04/e6/b5/04e6b56e15340f320dbffc0900829992.jpg",
  "https://i.pinimg.com/564x/33/4b/45/334b4544e4228a2a22a4ee36d4bd1a13.jpg",
  "https://static.zerochan.net/Pixiv.Id.10885088.full.3340719.jpg",
  "https://static.zerochan.net/Pixiv.Id.10885088.full.3340716.jpg",
  "https://static.zerochan.net/Tsukino.Usagi.full.3340727.png",
  "https://static.zerochan.net/Genshin.Impact.full.3340625.png",
  "https://static.zerochan.net/Genshin.Impact.full.3340493.png",
  "https://static.zerochan.net/Genshin.Impact.full.3340484.jpg",
  "https://static.zerochan.net/Genshin.Impact.full.3340470.jpg",
  "https://static.zerochan.net/Diluc.full.3340154.jpg",
  "https://static.zerochan.net/Lumine.(Genshin.Impact).full.3340082.jpg",
  "https://static.zerochan.net/Lio.Fotia.full.3339324.jpg",
  "https://static.zerochan.net/Archer.Inferno.full.3339308.png",
  "https://static.zerochan.net/Kochou.Shinobu.full.3340647.png",
  "https://static.zerochan.net/BerryVerrine.full.3340617.png",
  "https://static.zerochan.net/Nakano.Miku.full.2684109.jpg",
  "https://static.zerochan.net/Nakano.Nino.full.2330082.jpg",
  "https://static.zerochan.net/Nakano.Itsuki.full.2845210.jpg",
  "https://static.zerochan.net/Nakano.Miku.full.2845208.jpg",
  "https://static.zerochan.net/Go-Toubun.no.Hanayome.full.2913323.jpg",
  "https://static.zerochan.net/DRAGON.BALL.full.289989.jpg",
  "https://static.zerochan.net/Vegeta.full.224396.jpg",
  "https://static.zerochan.net/DRAGON.BALL.Z.full.199087.jpg",
  "https://static.zerochan.net/Pixiv.Id.33638616.full.3339396.jpg",
  "https://static.zerochan.net/%27O%27ne.full.3338354.jpg",
  "https://static.zerochan.net/Amamiya.Erena.full.3336259.jpg",
  "https://static.zerochan.net/Finana.Ryugu.full.3334984.jpg",
  "https://static.zerochan.net/Pixiv.Id.10885088.full.3334514.jpg",
  "https://static.zerochan.net/Ninomae.Ina%27nis.full.3336248.jpg",
  "https://static.zerochan.net/Pixiv.Id.46612726.full.3336096.jpg",
  "https://static.zerochan.net/Ayanami.%28Azur.Lane%29.full.3333555.png",
  "https://static.zerochan.net/Gawr.Gura.full.3332632.jpg",
  "https://static.zerochan.net/%27O%27ne.full.3332625.jpg",
  "https://static.zerochan.net/Hu.Tao.full.3332551.jpg",
  "https://static.zerochan.net/Tenma.Tsukasa.full.3331962.jpg",
  "https://static.zerochan.net/CangQiong.full.3331957.jpg",
  "https://static.zerochan.net/Amane.Kanata.full.3331320.png",
  "https://static.zerochan.net/Mikasa.Ackerman.full.3338411.jpg",
  "https://static.zerochan.net/Levi.Ackerman.full.3336901.jpg",
  "https://static.zerochan.net/Lara.Tybur.full.3325056.jpg",
  "https://static.zerochan.net/Eren.Jaeger.full.3317723.jpg",
  "https://static.zerochan.net/Kagerou.Project.full.3311937.jpg",
  "https://static.zerochan.net/Tateyama.Ayano.full.3285607.jpg",
  "https://static.zerochan.net/Pieck.Finger.full.3209196.jpg",
  "https://static.zerochan.net/Satoru.Gojou.full.3160839.jpg",
  "https://static.zerochan.net/Satoru.Gojou.full.3133792.jpg",
  "https://static.zerochan.net/Satoru.Gojou.full.3137448.png",
  "https://static.zerochan.net/Saber.%28Fate.stay.night%29.full.1823456.jpg",
  "https://static.zerochan.net/Gilgamesh.full.1166027.jpg",
  "https://static.zerochan.net/Saber.%28Fate.stay.night%29.full.1044734.jpg",
  "https://static.zerochan.net/Gilgamesh.full.929250.jpg",
  "https://static.zerochan.net/Fate.zero.full.1023558.jpg",
  "https://static.zerochan.net/Yu-Gi-Oh%21.GX.full.82476.jpg",
  "https://static.zerochan.net/Haou.full.1497867.jpg",
  "https://static.zerochan.net/Yu-Gi-Oh%21.full.2051350.jpg",
  "https://static.zerochan.net/Inazuma.Eleven.full.530657.jpg",
  "https://static.zerochan.net/Matatagi.Hayato.full.2989054.jpg",
  "https://static.zerochan.net/Nosaka.Yuuma.full.2989050.jpg",
  "https://static.zerochan.net/Antarcticite.full.1948760.jpg",
  "https://static.zerochan.net/Cinnabar.%28Houseki.no.Kuni%29.full.1701708.jpg",
  "https://static.zerochan.net/Phosphophyllite.%28Houseki.no.Kuni%29.full.1915816.jpg",
  "https://static.zerochan.net/Diamond.%28Houseki.no.Kuni%29.full.1840162.jpg",
  "https://static.zerochan.net/Inazuma.Eleven.Orion.no.Kokuin.full.2659198.jpg",
  "https://static.zerochan.net/Kiyama.Hiroto.full.2517619.png",
  "https://static.zerochan.net/Fubuki.Shirou.full.2502388.png",
  "https://static.zerochan.net/Nagumo.Haruya.full.2497494.jpg",
  "https://static.zerochan.net/Nosaka.Yuuma.full.2464107.png",
  "https://static.zerochan.net/Nosaka.Yuuma.full.2081026.jpg",
  "https://static.zerochan.net/Juudai.Yuuki.full.1423750.jpg",
  "https://static.zerochan.net/Juudai.Yuuki.full.1818461.jpg",
  "https://static.zerochan.net/Johan.Andersen.full.1729680.jpg",
  "https://static.zerochan.net/Oze.Maki.full.3019193.png",
  "https://static.zerochan.net/Kusakabe.Shinra.full.2667872.png",
  "https://static.zerochan.net/Uta.%28Tokyo.Ghoul%29.full.1765071.jpg",
  "https://static.zerochan.net/Tokyo.Ghoul.full.1762476.jpg",
  "https://static.zerochan.net/Suzuya.Juuzou.full.1786526.jpg",
  "https://static.zerochan.net/Tokyo.Ghoul.full.1816935.jpg",
  "https://static.zerochan.net/Kaneki.Ken.full.1826987.jpg",
  "https://static.zerochan.net/Suzuya.Juuzou.full.1870230.jpg",
  "https://static.zerochan.net/Kamishiro.Rize.full.1972713.jpg",
  "https://static.zerochan.net/Kaneki.Ken.full.1825170.jpg",
  "https://static.zerochan.net/Surtr.%28Arknights%29.full.3340948.jpg",
  "https://static.zerochan.net/Alucard.%28Hellsing%29.full.876120.jpg",
  "https://static.zerochan.net/HELLSING.full.770333.jpg",
  "https://static.zerochan.net/Nagatoro.Hayase.full.3331901.jpg",
  "https://static.zerochan.net/Nagatoro.Hayase.full.3272781.jpg",
  "https://static.zerochan.net/Nagatoro.Hayase.full.3193185.jpg",
  "https://static.zerochan.net/Nagatoro.Hayase.full.3326021.jpg",
  "https://static.zerochan.net/Ryougi.Shiki.full.1519146.jpg",
  "https://static.zerochan.net/Ryougi.Shiki.full.1975320.jpg",
  "https://static.zerochan.net/Ryougi.Shiki.full.1071922.jpg",
  "https://static.zerochan.net/Ginga.Bishounen.full.362850.jpg",
  "https://static.zerochan.net/Star.Driver.full.335454.jpg",
  "https://static.zerochan.net/Star.Driver.full.1089787.jpg",
  "https://static.zerochan.net/Kirahoshi.Ciel.full.3341145.png",
  "https://static.zerochan.net/Dimitri.Alexandre.Blaiddyd.full.3325236.jpg",
  "https://static.zerochan.net/Dimitri.Alexandre.Blaiddyd.full.3282411.jpg",
  "https://static.zerochan.net/Navi.%28Persona.5%29.full.2443211.png",
  "https://static.zerochan.net/Panther.%28Persona.5%29.full.2443209.png",
  "https://static.zerochan.net/Amamiya.Ren.%28Persona.5%29.full.2443206.png",
  "https://static.zerochan.net/Queen.%28Persona.5%29.full.2443213.png",
  "https://static.zerochan.net/Noir.%28Persona.5%29.full.2443212.png",
  "https://static.zerochan.net/Fox.%28Persona.5%29.full.2443210.png",
  "https://static.zerochan.net/Skull.%28Persona.5%29.full.2443207.png",
  "https://static.zerochan.net/Shin.Megami.Tensei%3A.PERSONA.5.full.2203533.png",
  "https://static.zerochan.net/Kamado.Nezuko.full.3340990.jpg",
  "https://static.zerochan.net/Akechi.Goro.full.2154341.png",
  "https://static.zerochan.net/Akechi.Goro.full.2239838.jpg",
  "https://static.zerochan.net/Akechi.Goro.full.2975837.jpg",
  "https://static.zerochan.net/Rengoku.Kyoujurou.full.3331144.jpg",
  "https://static.zerochan.net/Agatsuma.Zenitsu.full.3325913.jpg",
  "https://static.zerochan.net/Tomioka.Giyuu.full.3292750.jpg",
  "https://static.zerochan.net/Kokushibou.full.3305568.jpg",
  "https://static.zerochan.net/Genshin.Impact.full.3341879.jpg",
  "https://static.zerochan.net/Ayanami.Rei.full.3341902.jpg",
  "https://static.zerochan.net/Genshin.Impact.full.3341899.png",
  "https://static.zerochan.net/Kaine.full.3341891.png",
  "https://static.zerochan.net/Yubiteru.full.3341887.png",
  "https://static.zerochan.net/Pok%C3%A9mon.Sun...Moon.full.3341884.jpg",
  "https://static.zerochan.net/Pixiv.Id.44869033.full.3341872.png",
  "https://static.zerochan.net/Pixiv.Id.5797264.full.3341873.jpg",
  "https://static.zerochan.net/Mimikyu.full.3341871.jpg",
  "https://static.zerochan.net/Mash.Kyrielight.full.3341866.jpg",
  "https://static.zerochan.net/Mejiro.McQueen.full.3341859.jpg",
  "https://static.zerochan.net/Pixiv.Id.10520636.full.3341855.jpg",
  "https://static.zerochan.net/Zelda.%28Breath.of.the.Wild%29.full.3341858.jpg",
  "https://static.zerochan.net/Genshin.Impact.full.3341852.jpg",
  "https://static.zerochan.net/Genshin.Impact.full.3341849.jpg",
  "https://static.zerochan.net/Genshin.Impact.full.3341850.png",
  "https://static.zerochan.net/Aisaka.Taiga.full.465401.jpg",
  "https://static.zerochan.net/Aisaka.Taiga.full.542182.jpg",
  "https://static.zerochan.net/Aisaka.Taiga.full.118651.jpg",
  "https://static.zerochan.net/Aisaka.Taiga.full.669785.jpg",
  "https://static.zerochan.net/Aisaka.Taiga.full.1642947.jpg",
  "https://static.zerochan.net/Hikigaya.Hachiman.full.1662714.jpg",
  "https://static.zerochan.net/Hikigaya.Hachiman.full.2334848.jpg",
  "https://static.zerochan.net/Yahari.Ore.no.Seishun.Love.Come.wa.Machigatteiru.full.1667015.jpg",
  "https://static.zerochan.net/Totsuka.Saika.full.1522820.jpg",
  "https://static.zerochan.net/Yukinoshita.Yukino.full.2227212.jpg",
  "https://static.zerochan.net/Yukinoshita.Yukino.full.1539740.jpg",
  "https://static.zerochan.net/Yuigahama.Yui.full.1940440.jpg",
  "https://static.zerochan.net/Yukinoshita.Yukino.full.2886031.png",
  "https://static.zerochan.net/Youkoso.Jitsuryoku.Shijou.Shugi.no.Kyoushitsu.e.full.2191735.jpg",
  "https://static.zerochan.net/Ayanokouji.Kiyotaka.full.2174934.jpg",
  "https://static.zerochan.net/Youkoso.Jitsuryoku.Shijou.Shugi.no.Kyoushitsu.e.full.2176616.jpg",
  "https://static.zerochan.net/Sakura.Airi.full.2262415.jpg",
  "https://static.zerochan.net/Nanase.Tsubasa.full.2826467.jpg",
  "https://static.zerochan.net/Kugisaki.Nobara.full.3343296.jpg",
  "https://static.zerochan.net/Red.Saber.full.3343295.jpg",
  "https://static.zerochan.net/Lumine.%28Genshin.Impact%29.full.3343294.jpg",
  "https://static.zerochan.net/Red.Saber.full.2311649.jpg",
  "https://static.zerochan.net/Komeiji.Koishi.full.3343290.png",
  "https://static.zerochan.net/Komeiji.Koishi.full.3341185.png",
  "https://static.zerochan.net/Asagami.Fujino.full.3343288.jpg",
  "https://static.zerochan.net/Red.Saber.full.2163541.jpg",
  "https://static.zerochan.net/Red.Saber.full.2111387.jpg",
  "https://static.zerochan.net/Joan.of.Arc.%28Fate.Apocrypha%29.full.2068645.jpg",
  "https://static.zerochan.net/Joan.of.Arc.%28Fate.Apocrypha%29.full.1691099.jpg",
  "https://static.zerochan.net/Joan.of.Arc.%28Fate.Apocrypha%29.full.1952910.jpg",
  "https://static.zerochan.net/Joan.of.Arc.%28Fate.Apocrypha%29.full.2084232.jpg",
  "https://static.zerochan.net/Black.Rider.full.1966090.jpg",
  "https://static.zerochan.net/Black.Rider.full.2361607.png",
  "https://static.zerochan.net/Violet.Evergarden.%28Character%29.full.2256158.jpg",
  "https://static.zerochan.net/Dazai.Osamu.full.2342288.jpg",
  "https://static.zerochan.net/Zero.Two.%28Darling.in.the.FranXX%29.full.2251611.png",
  "https://static.zerochan.net/Yakusoku.no.Neverland.full.2313838.jpg",
  "https://static.zerochan.net/Tanya.Degurechaff.full.2208555.jpg",
  "https://static.zerochan.net/Suna.no.Wakusei.full.2333243.jpg",
  "https://static.zerochan.net/Edward.Elric.full.559982.jpg",
  "https://static.zerochan.net/Hand.in.Hand.%28Magical.Mirai%29.full.1933448.jpg",
  "https://static.zerochan.net/Hatsune.Miku.full.2000673.jpg",
  "https://static.zerochan.net/Hatsune.Miku.full.2020149.jpg",
  "https://static.zerochan.net/Suna.no.Wakusei.full.2122444.png",
  "https://static.zerochan.net/Suna.no.Wakusei.full.2122204.jpg",
  "https://static.zerochan.net/Greed.Greeling.full.624698.jpg",
  "https://static.zerochan.net/Fullmetal.Alchemist.full.2588256.png",
  "https://static.zerochan.net/Fullmetal.Alchemist.Brotherhood.full.1735079.jpg",
  "https://static.zerochan.net/Greed.Greeling.full.624112.jpg",
  "https://static.zerochan.net/Fullmetal.Alchemist.full.222499.jpg",
  "https://static.zerochan.net/Roy.Mustang.full.1357254.jpg",
  "https://static.zerochan.net/Roy.Mustang.full.2008161.jpg",
  "https://static.zerochan.net/Roy.Mustang.full.575161.jpg",
  "https://static.zerochan.net/Roy.Mustang.full.732260.jpg",
  "https://static.zerochan.net/Lancer.%28Fate.Grand.Order%29.full.2398178.jpg",
  "https://static.zerochan.net/Darling.in.the.FranXX.full.2344307.png",
  "https://static.zerochan.net/Marnie.full.2232079.png",
  "https://static.zerochan.net/Dabi.full.2308726.png",
  "https://static.zerochan.net/Yuigahama.Yui.full.2364633.png",
  "https://static.zerochan.net/Norman.%28Yakusoku.no.Neverland%29.full.2491492.jpg",
  "https://static.zerochan.net/Ray.%28Yakusoku.no.Neverland%29.full.2491493.jpg",
  "https://static.zerochan.net/Fate.Grand.Order.full.2281692.jpg",
  "https://static.zerochan.net/YoRHa.Type.A.No.2.full.2216457.png",
  "https://static.zerochan.net/Dabi.full.2381562.png",
  "https://static.zerochan.net/Dororo.%28Manga%29.full.2494653.jpg",
  "https://static.zerochan.net/Black.Rider.full.2383413.png",
  "https://static.zerochan.net/Black.Rider.full.2111839.jpg",
  "https://static.zerochan.net/Black.Rider.full.2405817.jpg",
  "https://static.zerochan.net/Lapis.Lazuli.%28Houseki.no.Kuni%29.full.2252491.png",
  "https://static.zerochan.net/Kaneki.Ken.full.2228165.jpg",
  "https://static.zerochan.net/Attack.on.Titan.full.2283499.jpg",
  "https://static.zerochan.net/Phosphophyllite.%28Houseki.no.Kuni%29.full.2303276.jpg",
  "https://static.zerochan.net/Violet.Evergarden.%28Character%29.full.2251726.png",
  "https://static.zerochan.net/Satoru.Gojou.full.3196168.jpg",
  "https://static.zerochan.net/Uta.%28Tokyo.Ghoul%29.full.2208326.jpg",
  "https://static.zerochan.net/CODE.GEASS%3A.Hangyaku.no.Lelouch.full.786955.jpg",
  "https://static.zerochan.net/CODE.GEASS%3A.Hangyaku.no.Lelouch.full.160326.jpg",
  "https://static.zerochan.net/CODE.GEASS%3A.Hangyaku.no.Lelouch.full.1162225.jpg",
  "https://static.zerochan.net/CODE.GEASS%3A.Hangyaku.no.Lelouch.full.1602525.jpg",
  "https://static.zerochan.net/Hata.no.Kokoro.full.1526830.jpg",
  "https://static.zerochan.net/Hata.no.Kokoro.full.1849622.jpg",
  "https://static.zerochan.net/Hata.no.Kokoro.full.1560576.jpg",
  "https://static.zerochan.net/Hata.no.Kokoro.full.2062452.jpg",
  "https://static.zerochan.net/Hata.no.Kokoro.full.1513782.jpg",
  "https://static.zerochan.net/CODE.GEASS%3A.Hangyaku.no.Lelouch.R2.full.1635787.jpg",
  "https://static.zerochan.net/CODE.GEASS%3A.Hangyaku.no.Lelouch.R2.full.2305703.jpg",
  "https://static.zerochan.net/CODE.GEASS%3A.Hangyaku.no.Lelouch.full.2512063.png",
  "https://static.zerochan.net/Rolo.Lamperouge.full.271663.jpg",
  "https://static.zerochan.net/Akemi.Homura.full.3343233.jpg",
  "https://static.zerochan.net/Rem.%28Re%3AZero%29.full.3333854.jpg",
  "https://static.zerochan.net/Rem.%28Re%3AZero%29.full.3326027.jpg",
  "https://static.zerochan.net/Re%3AZero.Kara.Hajimeru.Isekai.Seikatsu.-.Itsuwari.no.Ou-sen.Kouho.full.3317136.png",
  "https://static.zerochan.net/Rem.%28Re%3AZero%29.full.3315399.jpg",
  "https://static.zerochan.net/Rem.%28Re%3AZero%29.full.3309818.jpg"
]
suguestão = [
  "Ijiranaide, Nagatoro-san\nhttps://myanimelist.net/anime/42361/Ijiranaide_Nagatoro-san",
  "Fumetsu no Anata e\nhttps://myanimelist.net/anime/41025/Fumetsu_no_Anata_e",
  "Tokyo Revengers\nhttps://myanimelist.net/anime/42249/Tokyo_Revengers",
  "Holo no Graffiti\nhttps://myanimelist.net/anime/44042/Holo_no_Graffiti",
  "Vivy: Fluorite Eye's Song\nhttps://myanimelist.net/anime/46095/Vivy__Fluorite_Eyes_Song",
  "Violet Evergarden\nhttps://myanimelist.net/anime/33352/Violet_Evergarden",
  "Shigatsu wa Kimi no Uso\nhttps://myanimelist.net/anime/23273/Shigatsu_wa_Kimi_no_Uso",
  "Koe no Katachi\nhttps://myanimelist.net/anime/28851/Koe_no_Katachi",
  "Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai.\nhttps://myanimelist.net/anime/9989/Ano_Hi_Mita_Hana_no_Namae_wo_Bokutachi_wa_Mada_Shiranai",
  "Kimi no Na wa.\nhttps://myanimelist.net/anime/32281/Kimi_no_Na_wa",
  "Charlotte\nhttps://myanimelist.net/anime/28999/Charlotte",
  "Boku dake ga Inai Machi\nhttps://myanimelist.net/anime/31043/Boku_dake_ga_Inai_Machi",
  "Code Geass: Hangyaku no Lelouch\nhttps://myanimelist.net/anime/1575/Code_Geass__Hangyaku_no_Lelouch",
  "Steins;Gate\nhttps://myanimelist.net/anime/9253/Steins_Gate",
  "Re:Zero kara Hajimeru Isekai Seikatsu\nhttps://myanimelist.net/anime/31240/Re_Zero_kara_Hajimeru_Isekai_Seikatsu",
  "Sword Art Online\nhttps://myanimelist.net/anime/11757/Sword_Art_Online",
  "Kono Subarashii Sekai ni Shukufuku wo!\nhttps://myanimelist.net/anime/30831/Kono_Subarashii_Sekai_ni_Shukufuku_wo",
  "No Game No Life\nhttps://myanimelist.net/anime/19815/No_Game_No_Life",
  "Kimi no Iru Machi\nhttps://myanimelist.net/anime/17741/Kimi_no_Iru_Machi",
  "True Tears\nhttps://myanimelist.net/anime/2129/True_Tears",
  "White Album\nhttps://myanimelist.net/anime/4720/White_Album",
  "School Days\nhttps://myanimelist.net/anime/2476/School_Days",
  "Monster\nhttps://myanimelist.net/anime/19/Monster",
  "Made in Abyss\nhttps://myanimelist.net/anime/34599/Made_in_Abyss",
  "Vinland Saga\nhttps://myanimelist.net/anime/37521/Vinland_Saga",
  "Elfen Lied\nhttps://myanimelist.net/anime/226/Elfen_Lied",
  "Vampire Knight\nhttps://myanimelist.net/anime/3457/Vampire_Knight",
  "Rosario to Vampire\nhttps://myanimelist.net/anime/2993/Rosario_to_Vampire",
  "Toradora!\nhttps://myanimelist.net/anime/4224/Toradora",
  "Chuunibyou demo Koi ga Shitai!\nhttps://myanimelist.net/anime/14741/Chuunibyou_demo_Koi_ga_Shitai",
  "Yahari Ore no Seishun Love Comedy wa Machigatteiru.\nhttps://myanimelist.net/anime/14813/Yahari_Ore_no_Seishun_Love_Comedy_wa_Machigatteiru",
  "Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e\nhttps://myanimelist.net/anime/35507/Youkoso_Jitsuryoku_Shijou_Shugi_no_Kyoushitsu_e_TV",
  "Hyouka\nhttps://myanimelist.net/anime/12189/Hyouka",
  "3-gatsu no Lion\nhttps://myanimelist.net/anime/31646/3-gatsu_no_Lion",
  "Howl's Moving Castle\nhttps://myanimelist.net/anime/431/Howl_no_Ugoku_Shiro",
  "Sen to Chihiro no Kamikakushi\nhttps://myanimelist.net/anime/199/Sen_to_Chihiro_no_Kamikakushi",
  "Mononoke Hime\nhttps://myanimelist.net/anime/164/Mononoke_Hime",
  "Tengen Toppa Gurren Lagann\nhttps://myanimelist.net/anime/2001/Tengen_Toppa_Gurren_Lagann",
  "Cowbow Bebop\nhttps://myanimelist.net/anime/1/Cowboy_Bebop",
  "Mushishi Zoku Shou\nhttps://myanimelist.net/anime/21939/Mushishi_Zoku_Shou",
  "Kimi no Suizou wo Tabetai\nhttps://myanimelist.net/anime/36098/Kimi_no_Suizou_wo_Tabetai",
  "One Punch Man\nhttps://myanimelist.net/anime/30276/One_Punch_Man",
  "Uchuu Kyoudai\nhttps://myanimelist.net/anime/12431/Uchuu_Kyoudai",
  "Perfect Blue\n https://myanimelist.net/anime/437/Perfect_Blue",
  "Banana Fish\n https://myanimelist.net/anime/36649/Banana_Fish",
]
traps = [
  "https://static.zerochan.net/Saber.%28Astolfo%29.full.3011262.png",
  "https://static.zerochan.net/Saber.%28Astolfo%29.full.2784350.png",
  "https://static.zerochan.net/Saber.%28Astolfo%29.full.2814588.png",
  "https://static.zerochan.net/Saber.%28Astolfo%29.full.3006281.png",
  "https://static.zerochan.net/Felix.Argyle.full.2018176.jpg",
  "https://static.zerochan.net/Felix.Argyle.full.2012123.jpg",
  "https://static.zerochan.net/Kinoshita.Hideyoshi.full.986490.jpg",
  "https://static.zerochan.net/Kinoshita.Hideyoshi.full.161684.jpg",
  "https://static.zerochan.net/Kinoshita.Hideyoshi.full.416806.jpg",
  "https://static.zerochan.net/Amane.Nishiki.full.1246052.jpg",
  "https://static.zerochan.net/Amane.Nishiki.full.1426197.jpg",
  "https://static.zerochan.net/Amane.Nishiki.full.1399837.jpg",
  "https://static.zerochan.net/Cross-Over.full.965276.jpg",
  "https://static.zerochan.net/Fisheye.full.3183737.jpg",
  "https://static.zerochan.net/Fisheye.full.3153944.jpg",
  "https://static.zerochan.net/Fisheye.full.3169836.jpg",
  "https://static.zerochan.net/Hacka.Doll.No..3.full.1956604.jpg",
  "https://static.zerochan.net/Hacka.Doll.No..3.full.1958301.jpg",
  "https://static.zerochan.net/Arikawa.Hime.full.1796751.jpg",
  "https://static.zerochan.net/Arikawa.Hime.full.2119363.jpg",
  "https://static.zerochan.net/Arikawa.Hime.full.2626797.jpg",
  "https://static.zerochan.net/Arikawa.Hime.full.2119364.jpg",
  "https://static.zerochan.net/Arikawa.Hime.full.2255298.png",
  "https://static.zerochan.net/Arikawa.Hime.full.2213820.png",
  "https://static.zerochan.net/Yuuki.Kei.full.537233.jpg",
  "https://static.zerochan.net/Moyashimon.full.513110.jpg",
  "https://static.zerochan.net/Ansatsu.Kyoushitsu.full.1924891.jpg",
  "https://static.zerochan.net/Shiota.Nagisa.full.1929898.jpg"
]
bichos = [
  "Cão de Guarda"
]
nomesh = [
  "Naru",
  "Oye",
  "Igarashi",
  "Asai",
  "Matsushita",
  "Yashiro",
  "Oki",
  "Murata",
  "Oogami",
  "Uchibayase",
  "Sakiyama",
  "Akibara",
  "Miyamoto",
  "Ouji",
  "Okumura",
  "Wakatanabe",
  "Miyasato",
  "Takamori",
  "Takamoto",
  "Mizutani",
]
sobrenomeh = [
  "Kanbe",
  "Gyokusho",
  "Susumo",
  "Kojiro",
  "Norihide",
  "Sasekien",
  "Matsudarai",
  "Ryoko",
  "Masanori",
  "Kazuhiro",
  "Danjuro",
  "Mamoru",
  "Seishiro",
  "Tomoeio",
  "Kenji",
  "Muneyaki",
  "Takamasa",
  "Kazuhiko",
  "Mitsunari",
  "Yasuhito",
]
menos25 = [
  "Estudante",
  "Entrgador",
  "Estudante de Intercâmbio",
  "Attendente",
  "Garçom",
  "Vendedor",
  "Estudante de Artes",
  "Atleta",
  "Capitão do Time de Futebol",
  "Presidente do Conselho Estudantil",
  "Estudante Transferido"
]
mais26 = [
  'Médico',
  'Day Trader',
  'Advogado',
  'Professor',
  "Engenheiro Civil",
  "Policial",
  "Detetive",
  "Construtor",
  "Assistente de Construção",
  "Programador"
]
sangue = [
  'A',
  'B',
  'O',
  'AB'
]
sanguemm = [
  '+',
  '-'
]
personalidades = [
  'Lógico',
  'Estratégico',
  'Independete',
  'Reservado',
  'Adaptável',
  'Criativo',
  'Líder',
  'Sociável',
  'Comandante',
  'Confiante',
  'Explosivo',
  'Cooperativo',
  'Aventureiro',
  'Observador'
]
menos25m = [
  'Cavaleiro em Treinamento',
  'Arqueiro em Treinamento',
  'Escravo',
  'Aprendiz de Feiriceiro',
  'Aprendiz de Curandeiro',
  'Estudante na academia de artes marciais'
]
mais26m = [
  'Cavaleiro Real',
  'Arqueiro',
  'Espadachim',
  'Mago/Bruxa',
  'Curandeira(o)'
]
mahaa = [
  'Eu kimetsu no seu rayba, locão de juju na cara\nSe o Sol não te queimar\nOniMinha katana te rasga',
  'Para de brigar net, hater é tudo otário\nVem brigar com meu Mike Tyson que dá soco no teu rabo',
  'Ela é da gangue do Valhalla, Valhalla, Valhalla\nVai, rala a tcheca na peça, vai, rala a tcheca na caixa',
  'Andam dizendo que o sukuna é o demônio\nAham mas eu que sou o demônio socando',
  'Misato me mamou em cima do robô\nDesliza no LCL, vem jogando esse popô',
  'De dia eu sou o Bruce Wayne\nAmo quando as notas vem\nFaço o corre direitinho\nPra bancar minhas neném',
]
japa = [
'https://javhd.pics/media/japanese/yua-mikami/64/hd-yua-mikami-11.jpg',
'https://javhd.pics/media/japanese/yua-mikami/64/hd-yua-mikami-1.jpg',
'https://javhd.pics/media/japanese/yua-mikami/64/hd-yua-mikami-2.jpg',
'https://javhd.pics/media/japanese/yua-mikami/24/hd-yua-mikami-1.jpg',
'https://javhd.pics/media/japanese/yua-mikami/24/hd-yua-mikami-2.jpg',
'https://javhd.pics/media/japanese/yua-mikami/24/hd-yua-mikami-3.jpg',
'https://javhd.pics/media/japanese/yua-mikami/24/hd-yua-mikami-4.jpg',
'https://javhd.pics/media/japanese/yua-mikami/54/hd-yua-mikami-2.jpg',
'https://javhd.pics/media/japanese/yua-mikami/54/hd-yua-mikami-3.jpg',
'https://javhd.pics/media/japanese/yua-mikami/60/hd-yua-mikami-7.jpg',
'https://javhd.pics/media/japanese/yua-mikami/60/hd-yua-mikami-10.jpg',
'https://javhd.pics/media/japanese/yua-mikami/30/hd-yua-mikami-1.jpg',
]

#Gifs#

beijo = [
  'https://media.giphy.com/media/FqBTvSNjNzeZG/giphy.gif',
  'https://media.giphy.com/media/N3IuFaIanEs6I/giphy.gif',
  'https://media.giphy.com/media/jR22gdcPiOLaE/giphy.gif',
  'https://media.giphy.com/media/87vvTexnItOkE/giphy.gif',
  'https://media.giphy.com/media/12VXIxKaIEarL2/giphy.gif',
  'https://media.giphy.com/media/G3va31oEEnIkM/giphy.gif',
  'https://media.giphy.com/media/zkppEMFvRX5FC/giphy.gif',
  'https://media.giphy.com/media/kU586ictpGb0Q/giphy.gif',
  'https://media.giphy.com/media/bm2O3nXTcKJeU/giphy.gif',
  'https://media.giphy.com/media/nyGFcsP0kAobm/giphy.gif',
  'https://media.giphy.com/media/QGc8RgRvMonFm/giphy.gif',
  'https://c.tenor.com/3wE3JNW0fswAAAAC/anime-kiss-love.gif',
  'https://c.tenor.com/e6cYiAPPCq4AAAAC/anime-kissing.gif',
  'https://c.tenor.com/bkF2kFvXR50AAAAC/yes-love.gif',
  'https://c.tenor.com/hjhEoMvMTOIAAAAC/girls-anime.gif',
]
abraço = [
  'https://media.giphy.com/media/WynnqxhdFEPYY/giphy.gif',
  'https://media.giphy.com/media/du8yT5dStTeMg/giphy.gif',
  'https://media.giphy.com/media/3ZnBrkqoaI2hq/giphy.gif',
  'https://media.giphy.com/media/ZQN9jsRWp1M76/giphy.gif',
  'https://media.giphy.com/media/aD1fI3UUWC4/giphy.gif',
  'https://media.giphy.com/media/QFPoctlgZ5s0E/giphy.gif',
  'https://media.giphy.com/media/svXXBgduBsJ1u/giphy.gif',
  'https://media.giphy.com/media/3bqtLDeiDtwhq/giphy.gif',
  'https://media.giphy.com/media/wSY4wcrHnB0CA/giphy.gif',
  'https://media.giphy.com/media/5eyhBKLvYhafu/giphy.gif',
  'https://media.giphy.com/media/lrr9rHuoJOE0w/giphy.gif',
  'https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif',
  'https://media.giphy.com/media/wnsgren9NtITS/giphy.gif',
  'https://media.giphy.com/media/kvKFM3UWg2P04/giphy.gif',
  'https://media.giphy.com/media/yziFo5qYAOgY8/giphy.gif',
  'https://c.tenor.com/Ct4bdr2ZGeAAAAAC/teria-wang-kishuku-gakkou-no-juliet.gif',
  'https://c.tenor.com/xgVPw2QK5n8AAAAC/sakura-quest-anime.gif',
  'https://c.tenor.com/X5nBTYuoKpoAAAAC/anime-cheeks.gif',
  'https://c.tenor.com/9e1aE_xBLCsAAAAC/anime-hug.gif',
  'https://c.tenor.com/X5nBTYuoKpoAAAAC/anime-cheeks.gif',
  'https://c.tenor.com/sBFE3GeNpJ4AAAAC/tackle-hug-couple.gif',
  'https://c.tenor.com/ixaDEFhZJSsAAAAS/anime-choke.gif',
  'https://c.tenor.com/zirc8LTWVUkAAAAC/hug-anime.gif',
  'https://c.tenor.com/GJ6oX6r0mZsAAAAC/chuunibyou-anime.gif',
]
nani = [
  'https://static.hentai-gif-anime.com/upload/20160529/16/32051/1.gif',
  'https://static.hentai-gif-anime.com/upload/20160504/9/18093/detail.gif',
  'https://static.hentai-gif-anime.com/upload/20160529/16/32049/1.gif',
  'https://static.hentai-gif-anime.com/upload/20160529/16/32054/1.gif',
  'https://wetgif.com/wp-content/uploads/gif-hentai-incest-11-22.gif',
  'https://wetgif.com/wp-content/uploads/gif-hentai-incest-36.gif',
  'https://wetgif.com/wp-content/uploads/hentai-23.gif',
  'https://wetgif.com/wp-content/uploads/porno-anime-68.gif',
  'https://wetgif.com/wp-content/uploads/gif-hentai-incest-40.gif',
  'https://wetgif.com/wp-content/uploads/gif-hentai-incest-36.gif',
]




## Básicos ##


@client.event
async def on_ready():
  print('Entramos como {0.user}' . format(client))

@client.event
async def on_member_join(member):
  channel = discord.util.get(member.guild.channel, name='welcome')
  await channel.send(f'Bem vindo, {member.mention}! Lembre-se de tratar todos bem e de se divertir.')

@client.event
async def on_member_join(member):
  role = discord.utils.get(member.server.roles, name = '╚ Soldado')
  await client.add_roles(member, role)

## Informações ##


@client.command()
async def log(ctx):
  await ctx.send('Agora estou imparável!\nAntes de ir pras novidades, vamos as coisas que foram consertadas"\nAgora quando uma operação, usando os dados, daria um número negativo, ele vira 1! Até porque é impossível um dado negativo.\nForam adicionadas MUITAS novas imagens ao comando "anime", além disso também da pra ativar ele usando o "-wa".\nOutra coisa muito importante é que o "-avatar" foi muito implementado"! Agora quando tiver algo faltando ou algo de errado eu vou te avisar.\nAgora a única novidade dessa versão é que eu posso sugerir animes agora! Isso mesmo. Usando o comando "-sugerir" vou te sugerir um anime, acompanhado da página dele no MAL.\nPor fim, existem duas funções que estão sendo desenvolvidas. Por serem meio complexas, é capaz que ainda demore um pouco até eu ser capaz de fazê-las.\nEntão é isso, até a próxima versão!')


@client.command(aliases=['bom dia', 'boa tarde', 'boa noite'])
async def olá(ctx):
  await ctx.send(f'Sempre é hora de dar um bom dia. Então, bom dia, {ctx.author.mention}!')

@client.command()
async def frase(ctx):
  await ctx.send(random.choice(frases_do_dia))


@client.command()
async def servidor(ctx):
  await ctx.send(f'Sinta-se livre para entrar no meu servidor oficial, {ctx.author.mention}!\nAqui está o link: https://discord.gg/t2HBP7q37s')

@client.command()
async def l(ctx):
  await ctx.send("I lived, Bithces.")


## Economia ##


@client.command()
async def carteira(ctx, user: discord.Member):
  await open_account(user)
  user = ctx.author
  users = await get_bank_data()

  carteira_quantidade = users[str(user.id)]["carteira"]
  banco_quantidade = users[str(user.id)]["banco"]

  wallet = discord.Embed(
    title = f'Dinheiro de {ctx.author.name}',
    description = 'Aqui estão suas informações bancárias:',
    color = 2602879
  )

  wallet.add_field(name = "Carteira:", value = carteira_quantidade)
  wallet.add_field(name = "Banco:", value = banco_quantidade)



  await ctx.send(embed = wallet)


@client.command()
async def pedir(ctx):
  await open_account(ctx.author)

  users = await get_bank_data()

  user = ctx.author

  earnings = random.randrange(100, 500)

  await ctx.send(f"Você achou {earnings} no chão!")

  users[str(user.id)]["carteira"] += earnings

  with open("mainbank.json","w") as f:
    json.dump(users,f)

async def open_account(user):
 
  users = await get_bank_data()

  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["carteira"] = 0
    users[str(user.id)]["banco"] = 0

  with open("mainbank.json","w") as f:
    json.dump(users,f)
  return True


async def get_bank_data():
  with open("mainbank.json","r") as f:
    users = json.load(f)

  return users



## Rolls ##


@client.command(aliases=['r', 'dado', 'dice'])
async def roll(ctx, numero=20, conta='', ficha=''):
  rolagem = random.randint(1,int(numero))
  if conta == '':
        total = (int(rolagem))
  elif conta == '+':
         total = (int(rolagem) + int(ficha))
  elif conta == '-':
         total = (int(rolagem) - int(ficha))
  elif conta == 'x':
         total = (int(rolagem) * int(ficha))
  elif conta == '/':
         total = (int(rolagem) / int(ficha))
  if ficha == '':
          ficha = ''
  if total < 1:
          total = '1'
  if rolagem == 20:
          rolagem = '**20**'
  if rolagem == 1:
          rolagem = '**1**'
  await ctx.send(f'{ctx.author.mention} 🎇 \n**Resultado**: D{numero} ({rolagem}) {conta} {ficha}\n**Total**: {total}')


@client.command()
async def moeda(ctx):
  await ctx.send('E o resultado é...')
  await ctx.send('...')
  await ctx.send(random.choice(cara_coroa))



@client.command(aliases=['dilmas pernetas', 'dinossauros pelados', 'duas peles'])
async def dp(ctx):
  dproll = random.randint(100,500)
  await ctx.send(f'{ctx.author.mention} 🎇 \n**Como resultado desse duelo, você ganhou**: {dproll}')


@client.command()
async def per(ctx):
  idade = random.randint(14,60)
  jobb = random.choice(menos25) if idade <= 25 else random.choice(mais26)
  tipos = random.choice(sangue) + random.choice(sanguemm)
  persona= random.choice(personalidades)
  await ctx.send(f'`Nome:{random.choice(nomesh)} {random.choice(sobrenomeh)}\nIdade: {idade}\nTipo Sanguíneo: {tipos}\nOcupação: {jobb}\nPersonalidade: {persona}`')


@client.command(aliases=['personagem medieval'])
async def permedi(ctx):
  idade = random.randint(20,60)
  jobb = random.choice(menos25m) if idade <= 25 else random.choice(mais26m)
  tipos = random.choice(sangue) + random.choice(sanguemm)
  persona= random.choice(personalidades)
  await ctx.send(f'`Nome:{random.choice(nomesh)} {random.choice(sobrenomeh)}\nIdade: {idade}\nTipo Sanguíneo: {tipos}\nOcupação: {jobb}\nPersonalidade: {persona}`')

@client.command()
async def maha(ctx):
  await ctx.send(random.choice(mahaa))

@client.command()
async def hug(ctx, user: discord.Member):
  abraçoe = discord.Embed(
    title = f'Olha que fofinhos!',
    description = f'{ctx.author.mention} abraçou {user.mention}',
    color = 2602879
  )

  abraçoe.set_image(url=(random.choice(abraço)))
  
  await ctx.send(f'**{ctx.author.mention} e {user.mention}**')
  await ctx.send(embed = abraçoe)


@client.command()
async def kiss(ctx, user: discord.Member):
  beijoe = discord.Embed(
    title = f'Que isso meu patrão!',
    description = f'{ctx.author.mention} beijou {user.mention}',
    color = 2602879
  )

  beijoe.set_image(url=(random.choice(beijo)))
  
  await ctx.send(f'**{ctx.author.mention} e {user.mention}**')
  await ctx.send(embed = beijoe)


@client.command()
async def eat(ctx, user: discord.Member):
  nanie = discord.Embed(
    title = f'Pode isso, Arnaldo?!',
    description = f'{ctx.author.mention} está fazendo coisas com {user.mention}',
    color = 2602879
  )

  nanie.set_image(url=(random.choice(nani)))
  
  await ctx.send(f'**{ctx.author.mention} e {user.mention}**')
  await ctx.send(embed = nanie)


@client.command()
async def jav(ctx):
  japae = discord.Embed(
    title = f'As coisas estão ficando quentes por aqui!',
    description = f'{ctx.author.mention} eu não acredito que você está vendo esse tipo de coisa!',
    color = 2602879
  )

  japae.set_image(url=(random.choice(japa)))
  
  await ctx.send(f'**{ctx.author.mention}**')
  await ctx.send(embed = japae)





## Utilidades ##

@client.command(aliases=['versão', 'versao', 'ver'])
async def version(ctx):
  await ctx.send(f'Atualmente me encontro na versão {versao}.')

@client.command(aliases=['foto', 'perfil', 'imagem', 'profile'])
async def avatar(ctx, member: discord.Member):
  show_avatar = discord.Embed(
    title = f'Aqui está a foto dele, senhor {ctx.author}',
    color = 2602879
  )
  show_avatar.set_image(url='{}'.format(member.avatar_url))
  await ctx.send(f'{ctx.author.mention}', embed=show_avatar)


@client.command()
async def sugestão(ctx):
  await ctx.send(f'{ctx.author.mention}, você pode enviar uma sugestão de comando por este link: https://bit.ly/3uwBLfb')


## Memes ##



   

@client.command(aliases=['sessão?'])
async def sessão(ctx):
  await ctx.send('Eu ouvi sessão?')


@client.command(aliases=['rec', 'sug', 'sugerir'])
async def recomendar(ctx):
  await ctx.send(f'**{ctx.author.mention}, minha recomendação pra você é**: {random.choice(suguestão)}')


@client.command(aliases=['waifu', 'wa', 'garota', 'girl'])
async def anime(ctx):
  await ctx.send('**Via**: https://www.zerochan.net')
  await ctx.send(random.choice(animes))


@client.command()
async def trap(ctx):
  await ctx.send(random.choice(traps))



@client.command()
async def pobre(ctx):
  await ctx.send ('https://imgur.com/S8uJQVm')


@client.command()
async def multi(ctx):
  await ctx.send('esse jogo e multi, voces nao tem idea da mídia do ps4 eles pagam pelo jogo que voces jogam sao mais caros e mais evoluídos assim e diferente e voce nunca ira entender pois sao infieis ao console')


## Música ##

@client.command()
async def joi(ctx):
  canal = ctx.author.voice.voice_channel
  await client.join_voice_channel(canal)


@client.command()
async def join(ctx):
    if not ctx.message.author.voice_channel:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()


## SAO ##

@client.command()
async def eventos(ctx):
  await ctx.send(f'O evento atual é: {banner}')





## Batalha ##

@client.command()
async def farm(ctx):
  await ctx.send(f'Um {random.choice(bichos)} apareceu! O que deseja fazer?\nAtacar\nDefender\nFugir')
  msg = await client.wait_for('escolha')
  attempt = int(msg.content)
  if attempt == 'Atacar':
    await ctx.send('Você causou X de dano!')
        




## Embeds ##


@client.command()
async def ajuda(ctx):
  ajuda = discord.Embed(
    title = 'Parece que você precisa de ajuda, certo? Então vá em frente!',
    description = 'Aqui você encontra uma lista com diversos comandos. Caso o comando que você esteja atrás não esteja aqui, entre em contato com o perfil do rodapé.\n Por enquanto o bot ainda conta com comandos bem simples, mas já são o suficiente para fazer algumas coisas interessantes.',
    color = 2602879
  )

  ajuda.set_author(name= f'{ctx.author} chamou por ajuda!', icon_url= 'https://www.tibiawiki.com.br/images/d/d7/Golden_Newspaper.gif')

  ajuda.set_thumbnail(url = 'https://www.tibiawiki.com.br/images/d/d7/Golden_Newspaper.gif')

  ajuda.set_image(url= 'https://64.media.tumblr.com/554afaca94ce64ce2f1943e373dee212/69093404c1702635-ad/s640x960/5a1c90b56d1e1386234f548c2920c6b4eca80f62.jpg')

  ajuda.set_footer(text= f'Em caso de instabilidade, fale com 𝑯 𝑰 𝑹 𝑶#5692. Atualmente na versão {versao}')

  ajuda.add_field(name= 'Jogar um dado', value= 'Para rolar qualquer dado, simplesemente digite o meu prefíxo "-" e o número do dado. Lembrando que eu posso fazer operações matemáticas junto com o resultado.', inline=False)
  ajuda.add_field(name= 'Informações sobre atualizações', value= 'Pra você saber o que eu tenho de novo é só usar o "-log".', inline=False)
  ajuda.add_field(name= 'Versão atual', value= 'Para saber a versão em que eu me encontro atualmente use o comando "-version".', inline=False)
  ajuda.add_field(name= 'Sugerir uma modificação', value= 'Para sugerir uma modificação use o comando "-sugestão".', inline=False)


  

  await ctx.send(embed = ajuda)


## Erros ##

@avatar.error
async def avatar_handler(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send(f'Alô? Esqueceu de marcar de quem você quer a foto, {ctx.author.mention}!')


@anime.error
async def avatar_handler(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send(f'Tá na Disney, meu querido? Esse comando não existe!')


client.run(key)