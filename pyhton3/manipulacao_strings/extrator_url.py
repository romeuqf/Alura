import re
class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self,url):
        if type(url) == str:
            return url.strip()
        else: return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("URL VAZIA!")
        else:
            padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
            match_url = padrao_url.match(self.url)

            if not match_url:
                raise ValueError("URL NÃO VÁLIDA!")


    def get_url_base(self):
        interrogacao = self.url.find("?")
        url_base = self.url[:interrogacao]
        return url_base

    def get_url_parametros(self):
        interrogacao = self.url.find("?")
        url_parametros = self.url[interrogacao+1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&")
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]

        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url




teste = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
teste2 = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
print(teste)
print("O tamanho da URL: ", len(teste))
valor_quantidade = teste.get_valor_parametro("quantidade")
print(valor_quantidade)

print(id(teste))
print(id(teste2))
print(teste == teste2)
a = 1
b = a
print(id(a))
print(id(b))
print(a == b)
