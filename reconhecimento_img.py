import cv2

# Função para identificar se uma forma é círculo ou quadrado
def identificar_forma(contorno):
    # Aproxima o contorno para calcular o número de vértices
    perimetro = cv2.arcLength(contorno, True)
    approx = cv2.approxPolyDP(contorno, 0.04 * perimetro, True)
    
    # Se tem 4 vértices, é um quadrado (ou retângulo)
    if len(approx) == 4:
        return "Quadrado"
    # Se tem mais de 4 vértices (muitos), assume-se um círculo
    elif len(approx) > 4:
        return "Círculo"
    else:
        return "Outra forma"

# Carrega a imagem
imagem = cv2.imread('formas.png')

# Converte para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplica limiar para binarizar a imagem
_, imagem_bin = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

# Detecta contornos
contornos, _ = cv2.findContours(imagem_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Itera sobre cada contorno para identificar a forma
for contorno in contornos:
    forma = identificar_forma(contorno)
    
    # Desenha os contornos e exibe a forma detectada
    cv2.drawContours(imagem, [contorno], 0, (0, 255, 0), 3)
    
    # Posição do texto
    x, y = contorno[0][0]
    cv2.putText(imagem, forma, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Exibe a imagem com as formas identificadas
cv2.imshow('Formas Identificadas', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
