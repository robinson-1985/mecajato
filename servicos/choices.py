from django.db.models import TextChoices


class ChoicesCategoriaManutencao(TextChoices):
    ALINHAMENTO = 'A', 'Alinhamento'
    ARRUMAR_O_MOTOR = 'AM', 'Arrumar o motor'
    BALANCEAMENTO = 'B', 'Balanceamento'
    TROCAR_PAINEL_DE_COMBUSTIVEL = 'TPC', 'Troca de painel de combustível'
    TROCAR_VALVULA_MOTOR = 'TVM', 'Trocar válvula do motor'
    TROCAR_OLEO = 'TO', 'Troca de óleo'
    TROCAR_PNEU = 'TP', 'Troca de pneu'
    TROCAR_FAROL = 'TF', 'Troca de farol'
    TROCAR_LANTERNA = 'TL', 'Troca de lanterna'
    TROCAR_PASTILHAS_DO_FREIO = 'TPF', 'Troca de pastilhas do freio'
    TROCAR_FILTRO_DE_AR = 'TFA', 'Troca de filtro de ar'
    TROCAR_FILTRO_DE_COMBUSTIVEL = 'TFC', 'Troca de filtro de combustível'
    TROCAR_LAMPADAS_INTERNAS = 'TLI', 'Troca de lâmpadas internas'
    