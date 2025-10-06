# ---------------------------------------------------------------
# Aplicación: Calculadora de IMC (Índice de Masa Corporal)
# Objetivo: Crear una interfaz gráfica con PyQt5 que permita
# calcular el IMC ingresando peso y altura del usuario.
# ---------------------------------------------------------------

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QComboBox
import sys

class VentanaIMC(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de IMC")
        self.setGeometry(200, 200, 300, 300)
        
        # --- Widgets básicos ---
        self.lbl_genero = QLabel("Género:")
        self.cmb_genero = QComboBox()
        self.cmb_genero.addItems(["Masculino", "Femenino"])
        
        self.lbl_peso = QLabel("Peso (kg):")
        self.txt_peso = QLineEdit()
        self.txt_peso.setPlaceholderText("Ejemplo: 70")
        
        self.lbl_altura = QLabel("Altura (m):")
        self.txt_altura = QLineEdit()
        self.txt_altura.setPlaceholderText("Ejemplo: 1.75")
        
        self.btn_calcular = QPushButton("Calcular IMC")
        self.btn_calcular.clicked.connect(self.calcular_imc)
        
        self.lbl_resultado = QLabel("Resultado:")
        self.txt_resultado = QTextEdit()
        self.txt_resultado.setReadOnly(True)
        
        # --- Diseño (Layouts) ---
        layout = QVBoxLayout()
        
        # Fila de género
        fila_genero = QHBoxLayout()
        fila_genero.addWidget(self.lbl_genero)
        fila_genero.addWidget(self.cmb_genero)
        layout.addLayout(fila_genero)
        
        # Fila de peso
        fila_peso = QHBoxLayout()
        fila_peso.addWidget(self.lbl_peso)
        fila_peso.addWidget(self.txt_peso)
        layout.addLayout(fila_peso)
        
        # Fila de altura
        fila_altura = QHBoxLayout()
        fila_altura.addWidget(self.lbl_altura)
        fila_altura.addWidget(self.txt_altura)
        layout.addLayout(fila_altura)
        
        # Botón de cálculo
        layout.addWidget(self.btn_calcular)
        
        # Resultado
        layout.addWidget(self.lbl_resultado)
        layout.addWidget(self.txt_resultado)
        
        self.setLayout(layout)

    # --- Función que calcula el IMC ---
    def calcular_imc(self):
        try:
            peso = float(self.txt_peso.text())
            altura = float(self.txt_altura.text())
            imc = peso / (altura ** 2)

            # Clasificación según OMS
            if imc < 18.5:
                estado = "Bajo peso"
            elif 18.5 <= imc < 25:
                estado = "Peso normal"
            elif 25 <= imc < 30:
                estado = "Sobrepeso"
            else:
                estado = "Obesidad"

            # Mostrar resultado
            self.txt_resultado.setText(f"Tu IMC es: {imc:.2f}\nClasificación: {estado}")

        except ValueError:
            self.txt_resultado.setText("Por favor ingresa valores válidos para peso y altura.")

# --- Ejecución del programa ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaIMC()
    ventana.show()
    sys.exit(app.exec_())
