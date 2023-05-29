def solution(image):
    # Obtém as dimensões da imagem
    rows = len(image)
    cols = len(image[0])
    
    # Inicializa a matriz de resultado com zeros
    blurred_image = [[0] * (cols - 2) for _ in range(rows - 2)]
    
    # Itera sobre os pixels internos da imagem
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Calcula a média dos valores dos pixels na janela 3x3
            average = (
                image[i - 1][j - 1] + image[i - 1][j] + image[i - 1][j + 1] +
                image[i][j - 1] + image[i][j] + image[i][j + 1] +
                image[i + 1][j - 1] + image[i + 1][j] + image[i + 1][j + 1]
            ) // 9
            
            # Atribui o valor médio ao pixel correspondente na imagem resultante
            blurred_image[i - 1][j - 1] = average
    
    return blurred_image
