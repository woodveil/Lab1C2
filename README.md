# 🧮 Calculadora de IMC (Índice de Masa Corporal)

## 📘 Descripción
Esta aplicación gráfica permite calcular el **Índice de Masa Corporal (IMC)** a partir del peso y la altura del usuario.  
El programa fue desarrollado en **Python** utilizando la biblioteca **PyQt5**.

---

## 🎯 Objetivo
Aplicar los conocimientos de interfaces gráficas con PyQt5 para crear un programa funcional que ayude al usuario a conocer su estado de peso corporal según los valores de IMC.

---

## 💡 Planteamiento del problema
Muchas personas desconocen si su peso se encuentra dentro de un rango saludable.  
Esta aplicación ofrece una solución práctica que permite calcular el IMC ingresando los datos básicos y mostrando una clasificación según la Organización Mundial de la Salud (OMS).

---

## ⚙️ Tecnologías utilizadas
- Lenguaje: **Python 3**
- Librería gráfica: **PyQt5**

---

## 🧱 Widgets utilizados
| Widget | Descripción |
|--------|--------------|
| QLabel | Muestra textos fijos o etiquetas. |
| QLineEdit | Permite ingresar peso y altura. |
| QPushButton | Ejecuta el cálculo del IMC. |
| QTextEdit | Muestra el resultado y clasificación. |
| QComboBox | Selecciona el género del usuario. |

---

## 🧠 Funcionamiento
1. El usuario selecciona su **género**.  
2. Ingresa su **peso (kg)** y **altura (m)**.  
3. Presiona el botón **“Calcular IMC”**.  
4. El sistema muestra el **resultado numérico** y su **clasificación** (bajo peso, normal, sobrepeso u obesidad).

---

## ▶️ Ejecución
Para ejecutar la aplicación, abre una terminal y escribe:

```bash
python calculadora_imc.py
