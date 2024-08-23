banner = ('https://imgur.com/H6pKvIH')

good_pass = [
  'consegue efetuar um passe incrível para um companheiro de time!'
]
partidaaa = [
  'O time oponente rouba a bola!',
  'A bola saí! Vantagem do time inimigo.',
  'Um companheiro de time avança mas perde a bola!',
  'A equipe inimiga chega muito perto de marcar um gol mas joga para fora! É tiro de meta!',
  'E é goooool! A equipe inimiga marca um gol incrível!',
  "Goooool! E é gol pra equipe!",
  'Passe feito com sucesso.',
  'Passe oponente feito com sucesso.',
  'Cruzamento para área.',
  'Nas mãos do goleiro!'
]

banners = [
  "https://imgur.com/H6pKvIH"
]


good_pass = [
  'consegue efetuar um passe incrível para um companheiro de time!'
]

## Inazuma Eleven RPG ##

@client.command()
async def passe(ctx, user: discord.Member):
  passebom = random.choice(good_pass)
  await ctx.send(f'{ctx.author.mention} {passebom} {user.mention}')

@client.command()
async def partida(ctx):
  partidaa = random.choice(partidaaa)
  await ctx.send(f'{partidaa}')

## SAO ##

@client.command()
async def eventos(ctx):
  await ctx.send(f'O evento atual é: {banner}')

##General Stuff##
  
@client.event
async def on_member_join(member):
  role = discord.utils.get(member.server.roles, name = '╚ Soldado')
  await client.add_roles(member, role)


## Batalha ##

@client.command()
async def farm(ctx):
  await ctx.send(f'Um {random.choice(bichos)} apareceu! O que deseja fazer?\nAtacar\nDefender\nFugir')
  msg = await client.wait_for('escolha')
  attempt = int(msg.content)
  if attempt == 'Atacar':
    await ctx.send('Você causou X de dano!')
        

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

@client.event
async def on_member_join(member):
  channel = discord.util.get(member.guild.channel, name='welcome')
  await channel.send(f'Bem vindo, {member.mention}! Lembre-se de tratar todos bem e de se divertir.')
