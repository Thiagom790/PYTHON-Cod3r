#! python
bloco_attr = ('bloco_accesskey', 'bloco_id')
ul_attr = ('ul_id', 'ul_style')


def filtrar_atrs(informado, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"' for k, v in informado.items()
                    if k in suportados)


def tag_bloco(conteudo, *args, classe="success", inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(
        conteudo) else conteudo(*args, **novos_atrs)
    atributos = filtrar_atrs(novos_atrs, bloco_attr)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atrs):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul {filtrar_atrs(novos_atrs, ul_attr)}>{lista}</ul>'


if __name__ == '__main__':
    # print(tag_bloco('bloco'))
    # print(tag_bloco('inline e classe', classe='info', inline=True))
    # print(tag_bloco('inline', inline=True))
    # print(tag_bloco('falhou', classe="erro"))
    # print(tag_bloco(inline=True, conteudo="inline"))
    # print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe="ifo"))
    # print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info',
    #                 inline=True))
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='Info',
          bloco_accesskey='m', bloco_id='conteudo', ul_id="lista",
          ul_style="color:red"))
