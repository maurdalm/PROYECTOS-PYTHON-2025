import matplotlib.pyplot as plt
import numpy as np

# --- Configuración Estilística ---
plt.style.use('seaborn-v0_8-darkgrid')
# Colores personalizados para un toque "espectacular"
COLORES_BARRA = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF6']
COLOR_FONDO_TORTA = '#F0F8FF' # AliceBlue para la torta
COLOR_FONDO_PIE = '#FFFACD' # LemonChiffon para el pie

def crear_datos_aleatorios():
    """Genera datos aleatorios consistentes para las 3 opciones."""
    # Nombres de categorías para todas las gráficas
    categorias = ['Tecnología', 'Salud', 'Educación', 'Finanzas',
'Alimentos']
    # Valores aleatorios enteros para las categorías
    valores = np.random.randint(20, 100, size=len(categorias))
    
    return categorias, valores

def opcion_grafico_barras(categorias, valores):
    """Muestra un gráfico de barras con estilo."""
    plt.figure(figsize=(10, 6))
    
    # Crear el gráfico de barras
    barras = plt.bar(
        categorias, 
        valores, 
        color=COLORES_BARRA, 
        edgecolor='black', 
        linewidth=1.2,
        alpha=0.8
    )
    
    # Agregar valores encima de cada barra
    for barra in barras:
        yval = barra.get_height()
        plt.text(
            barra.get_x() + barra.get_width()/2.0, 
            yval + 2, 
            int(yval), 
            ha='center', 
            va='bottom', 
            fontsize=10, 
            fontweight='bold'
        )
        
    # Mejorar el título y etiquetas
    plt.title(
        '📊 Distribución de Ventas por Categoría (Gráfico de Barras)', 
        fontsize=16, 
        fontweight='bold', 
        color='#4B0082' # Indigo
    )
    plt.xlabel('Categorías', fontsize=12)
    plt.ylabel('Volumen de Ventas', fontsize=12)
    
    # Rotar las etiquetas para mejor visualización
    plt.xticks(rotation=15, ha='right', fontsize=10) 
    plt.ylim(0, max(valores) + 15) # Ajustar el límite y para espacio del texto
    
    plt.tight_layout()
    plt.show()

def opcion_grafico_torta(categorias, valores):
    """Muestra un gráfico de torta (pie) con estilo."""
    plt.figure(figsize=(8, 8), facecolor=COLOR_FONDO_TORTA)
    
    # Calcular el sector a "explotar" (destacar)
    explodes = [0.1 if valor == max(valores) else 0 for valor in valores]
    
    # Crear el gráfico de torta
    plt.pie(
        valores, 
        labels=categorias, 
        autopct='%1.1f%%', # Formato de porcentaje (un decimal)
        startangle=90, 
        colors=plt.cm.coolwarm(np.linspace(0.1, 0.9, len(categorias))), #olores del mapa coolwarm
        explode=explodes, # Aplicar el "explode"
        shadow=True, # Sombra para un efecto 3D
        wedgeprops={'edgecolor': 'black', 'linewidth': 1} # Borde de los sectores
    )
    
    # Título y Leyenda
    plt.title(
        '🎂 Cuota de Mercado por Categoría (Gráfico de Torta)', 
        fontsize=16, 
        fontweight='bold', 
        color='#8B0000' # DarkRed
    )
    plt.legend(
        categorias, 
        title="Categorías", 
        loc="best", 
        bbox_to_anchor=(1, 0, 0.5, 1)
    )
    
    plt.tight_layout()
    plt.show()

def opcion_grafico_pie_porcentajes(categorias, valores):
    """Muestra un gráfico de pie con porcentajes personalizados."""
    plt.figure(figsize=(10, 6), facecolor=COLOR_FONDO_PIE)

    # Convertir valores a porcentajes
    total = sum(valores)
    porcentajes = (valores / total) * 100
    
    # Crear etiquetas con porcentaje y valor
    etiquetas_personalizadas = [
        f'{cat}\n({p:.1f}%) - {val} unidades' 
        for cat, p, val in zip(categorias, porcentajes, valores)
    ]
    
    # Crear el gráfico de pie (donut chart) 
    colores_pie = plt.cm.viridis(np.linspace(0, 1, len(categorias))) 
    
    wedges, texts = plt.pie(
        valores,  
        startangle=90, 
        colors=colores_pie,
        wedgeprops=dict(width=0.4, edgecolor='w') # Crea el agujero (donut)
    )

    # Agregar texto descriptivo en el centro
    centro_circulo = plt.Circle((0,0), 0.3, fc='white', edgecolor='black',
linewidth=1)
    plt.gca().add_artist(centro_circulo)
    plt.text(
        0, 
        0, 
        f'Total: {total}', 
        ha='center', 
        va='center', 
        fontsize=14, 
        fontweight='bold', 
        color='black'
    )
    
    # Leyenda detallada
    plt.legend(
        wedges, 
        etiquetas_personalizadas, 
        title="Detalles", 
        loc="center left", 
        bbox_to_anchor=(1, 0, 0.5, 1),
        fontsize=9
    )

    plt.title(
        '🍩 Análisis de Contribución (Gráfico de Donut con Detalles)', 
        fontsize=16, 
        fontweight='bold', 
        color='#006400' # DarkGreen
    )
    plt.tight_layout()
    plt.show()

def main_menu():
    """Función principal que ejecuta el menú interactivo."""
    
    # Generar los datos UNA SOLA VEZ al inicio
    categorias, valores = crear_datos_aleatorios()
    
    while True:
        print("\n" + "="*50)
        print("✨ MENÚ INTERACTIVO DE VISUALIZACIÓN DE DATOS ✨")
        print("="*50)
        print("1. 📈 Gráfico de Barras Espectacular")
        print("2. 🎂 Gráfico de Torta (Pastel) Dinámico")
        print("3. 🍩 Gráfico de Pie (Donut) con Porcentajes Detallados")
        print("4. 🚪 Salir")
        print("-" * 50)
        
        opcion = input("➡️ Seleccione una opción (1-4): ")
        
        if opcion == '1':
            print("Cargando Gráfico de Barras...") 
            opcion_grafico_barras(categorias, valores) 
        elif opcion == '2':
            print("Cargando Gráfico de Torta...")
            opcion_grafico_torta(categorias, valores) 
        elif opcion == '3':
            print("Cargando Gráfico de Pie (Donut)...")
            opcion_grafico_pie_porcentajes(categorias, valores)
        elif opcion == '4':
            print("\n👋 ¡Gracias por usar el visualizador! ¡Adiós!")
            break
        else:
            print("\n❌ Opción no válida. Por favor, ingrese un número del 1al 4.")

if __name__ == "__main__":
    # Asegúrate de tener Matplotlib y NumPy instalados:
    # pip install matplotlib numpy
    
    main_menu() 