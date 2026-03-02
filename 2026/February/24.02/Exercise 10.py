import webbrowser

url = "https://youtu.be/gpc5c5PMQiw?si=ARFrbEZIEU5mYAYS"

try:
  abriu = webbrowser.open(url)

  if abriu:
    print("o navegador foi aberto com sucesso!")
  else:
    print("o navegador não conseguiu abrir a URL.")

except Exception as erro:
    print("ocorreu um erro ao tentar abrir a página.")
    print("detalhes do erro:", erro)


    