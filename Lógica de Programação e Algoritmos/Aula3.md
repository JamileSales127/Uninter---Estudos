# ✨ Aula3 - Condicionais Aninhadas e Múltipla Escolha (`elif`) 📝💡

## 📌 Resumo

Nesta aula, aprendemos sobre **condicionais aninhadas** e **condicionais de múltipla escolha (`elif`)**, fundamentais para a tomada de decisões em programação! 🎯

---

## 🎀 Condicionais Aninhadas 🎀

As **condicionais aninhadas** são como uma **decisão dentro de outra decisão**. Primeiro, avaliamos uma condição e, se for verdadeira, verificamos outra dentro dela. Isso permite criar lógicas mais detalhadas e personalizadas.  

📌 **Exemplo: Escolhendo um lanche! 🍔🍟**  

```python
fome = input("Você está com fome? (sim/não): ").lower()

if fome == "sim":
    comida = input("Prefere hambúrguer ou pizza? ").lower()
    if comida == "hambúrguer":
        print("Ótima escolha! Um hambúrguer bem suculento chegando! 🍔")
    elif comida == "pizza":
        print("Pizza é sempre uma boa ideia! 🍕")
    else:
        print("Hmm... não temos essa opção no cardápio! 😅")
else:
    print("Tudo bem! Se mudar de ideia, é só pedir! 😉")

```
## 💡 Condicionais de Múltipla Escolha (`elif`) 💡  

O `elif` é ideal quando temos **várias opções possíveis**, mas **apenas uma pode ser escolhida**. Assim, evitamos escrever vários `if` separados e deixamos o código mais organizado.  

📌 **Exemplo: Escolhendo uma bebida! ☕🥤**  

```python
bebida = input("Escolha sua bebida (café, chá ou suco): ").lower()

if bebida == "café":
    print("Cafézinho pronto! ☕ Energia garantida!")
elif bebida == "chá":
    print("Chá quentinho para relaxar! 🍵")
elif bebida == "suco":
    print("Um suco natural super refrescante! 🥤")
else:
    print("Ops! Não temos essa opção no menu. 😅")

