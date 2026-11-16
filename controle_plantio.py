# Controle de Plantio - AgroGestão

def cadastrar_plantio(cultura, area, data_plantio):
    """Registra informações básicas de um novo plantio."""
    plantio = {
        "cultura": cultura,
        "area_hectares": area,
        "data_plantio": data_plantio
    }

    return plantio


# Exemplo de utilização
novo_plantio = cadastrar_plantio("Milho", 5, "15/11/2026")

print("Plantio cadastrado com sucesso!")
print(novo_plantio)