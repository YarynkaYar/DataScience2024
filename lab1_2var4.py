import numpy as np

# функція для створення матриці обертання
def rotation_matrix(theta):
    # Перетворюємо градуси в радіани
    theta = np.radians(theta)
    # Створюємо матрицю обертання за допомогою формул обертання
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

# Функція для створення матриці масштабування
def scaling_matrix(sx, sy):
    # Створюємо матрицю масштабування заданими коофіцієнтами
    return np.array([[sx, 0], [0, sy]])

# Функція для створення вектора переміщення
def translation_matrix(tx, ty):
    # Створюємо вектор переміщення заданими коофіцієнтами
    return np.array([tx, ty])

# Головна функція для виконання послідовності трансформацій
def modelMatrix(inMatrix, sequence):
    # Створюємо словник функцій для кожної трансформації
    operations = {'R': rotation_matrix, 'S': scaling_matrix, 'T': translation_matrix}

# Визначаємо вихідний вектор
    vector = np.array(inMatrix['V'])

# Застосовуємо трансформації в заданому порядку
    for operation in sequence:
        # Використовуємо матричне множення для застосування трансформації до вектора
        vector = np.dot(operations[operation](*inMatrix[operation]), vector)


    return vector
# Тестовий блок
inMatrix = {'R':(33,),'T':(1.0,2.0),'S':(3.0,1.2),'V':(2,3)}
result = modelMatrix(inMatrix, 'SRT')
print(f"Після застосування трансформацій {inMatrix} в порядку 'SRT', вектор перетворюється в {result}")

inMatrix = {'R':(16,),'T':(1.0,2.0),'S':(1.0,1.2),'V':(2,3)}
result = modelMatrix(inMatrix, 'TRS')
print(f"Після застосування трансформацій {inMatrix} в порядку 'TRS', вектор перетворюється в {result}")