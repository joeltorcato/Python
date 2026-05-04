from transformers import pipeline

analisador = pipeline("sentiment-analysis")

frases = [
    "eu amo este produto!",
    "este filme é terrível.",
    "o serviço foi excelente.",
    "não gostei do atendimento.",
    "a comida estava deliciosa."
]

for frase in frases:
  resultado = analisador(frase)[0]
  print(f"frase: '{frase}' - sentimento: {resultado['label']} (confiança: {resultado['score']:.2f})")
  print()