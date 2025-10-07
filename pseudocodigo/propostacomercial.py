nome_cliente = input("Digite o nome do Cliente: ")
valor_proposta = float(input("Digite o Valor da Proposta: "))
reposta_vip = input("Seu Cliente é VIP? S/N: ")
canal_envio = input("Ecolha o canal de envio(Email ou WhatsApp): ")

if reposta_vip.lower() == "s":
    desconto = valor_proposta * 0.10
    valor_final = valor_proposta - desconto
else:
    valor_final = valor_proposta
    
mensagem = f"Olá, {nome_cliente}! Segue sua proposta comercial no valor de R$ {valor_final:.2f}."


if reposta_vip.lower() == "s":
    mensagem += "(Desconto VIP de 10% aplicado!)"
    
if canal_envio.lower() == "email":
        print("\nEnviando proposta para o email do cliente...")
        
        print("Proposta enviada com sucesso via email! ")
elif canal_envio.lower() == "WhatsApp":
    print("\nEnviamos proposta para o WhatsApp do cliente...")
    
    print("Proposta enviada com sucesso via WhatsApp!")
else:
    print("\n Canal inválido. Proposta não enviada.")
    
print("\nConfirmação de envio")
print(f"Cliente: {nome_cliente}")
print(f"Valor final da proposta: R$ {valor_final:.2f}")
print("Mensagem enviada: ")
print(mensagem)