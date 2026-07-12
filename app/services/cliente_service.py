from ..models import Cliente

def cadastrar_cliente(cliente):
    Cliente.objects.create(nome=cliente.nome, email=cliente.email, endereco=cliente.endereco, 
        cpf=cliente.cpf, data_nascimento=cliente.data_nascimento, profissao=cliente.profissao)

def listar_clientes():
    return Cliente.objects.all()

def buscar_cliente_id(id):
    return Cliente.objects.get(id=id)

def editar_cliente(cliente, novo):
    cliente.nome = novo.nome
    cliente.email = novo.email
    cliente.endereco = novo.endereco
    cliente.cpf = novo.cpf
    cliente.data_nascimento = novo.data_nascimento
    cliente.profissao = novo.profissao
    cliente.save(force_update=True)

def remover_cliente(cliente):
    cliente.delete()
    