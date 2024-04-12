import discord
from main import versao



ajuda = discord.Embed(
    title = 'Parece que você precisa de ajuda, certo? Então vá em frente!',
    description = 'Aqui você encontra uma lista com diversos comandos. Caso o comando que você esteja atrás não esteja aqui, entre em contato com o perfil do rodapé.\n Por enquanto o bot ainda conta com comandos bem simples, mas já são o suficiente para fazer algumas coisas interessantes.',
    color = 2602879
  )

ajuda.set_author(name= f'Ajuda foi chamada!', icon_url= 'https://www.tibiawiki.com.br/images/d/d7/Golden_Newspaper.gif')

ajuda.set_thumbnail(url = 'https://www.tibiawiki.com.br/images/d/d7/Golden_Newspaper.gif')

ajuda.set_image(url= 'https://64.media.tumblr.com/554afaca94ce64ce2f1943e373dee212/69093404c1702635-ad/s640x960/5a1c90b56d1e1386234f548c2920c6b4eca80f62.jpg')

ajuda.set_footer(text= f'Em caso de instabilidade, fale com horue_. Atualmente na versão {versao}')

ajuda.add_field(name= 'Jogar um dado', value= 'Para rolar qualquer dado, simplesemente digite o meu prefíxo "-" e o número do dado. Lembrando que eu posso fazer operações matemáticas junto com o resultado.', inline=False)
ajuda.add_field(name= 'Informações sobre atualizações', value= 'Pra você saber o que eu tenho de novo é só usar o "-log".', inline=False)
ajuda.add_field(name= 'Versão atual', value= 'Para saber a versão em que eu me encontro atualmente use o comando "-version".', inline=False)
ajuda.add_field(name= 'Sugerir uma modificação', value= 'Para sugerir uma modificação use o comando "-sugestão".', inline=False)


  