from abc import ABC, abstractmethod

class pagamento(ABC):
  @abstractmethod
  def pay(self, amount):
    pass

class cartaocred(pagamento):
  def pay(self, amount):
    print(f"pagando R$ {amount} com cartão de crédito.")

class Pix(pagamento):
  def pay(self, amount):
    print(f"pagando R$ {amount} via PIX")

class boleto(pagamento):
  def pay(self, amount):
    print(f"pagando R$ {amount} com o boleto")

def process_payment(processor: pagamento, amount):
  processor.pay(amount)

# Exemplo:
pix = Pix()  
card = cartaocred()
boleto = boleto()

process_payment(pix, 100)
process_payment(card, 250)
process_payment(boleto, 300)
