import pandas as pd
import matplotlib.pyplot as plt
import os

print("=" * 50)
print("INICIANDO ANALISIS DE VENTAS")
print("=" * 50)

# Cargar datos
df = pd.read_csv('datos/ventas.csv')
print(f"✓ Datos cargados: {df.shape[0]} registros")

# Preparar datos
df['sales_date'] = pd.to_datetime(df['sales_date'])
df['mes'] = df['sales_date'].dt.to_period('M')

# Calcular indicadores
ventas_totales = df['sales_amount'].sum()
producto_ventas = df.groupby('product')['sales_amount'].sum()
producto_mas_vendido = producto_ventas.idxmax()
ventas_por_mes = df.groupby('mes')['sales_amount'].sum()

print(f"\n📊 INDICADORES:")
print(f"   Ventas totales: ${ventas_totales:,.2f}")
print(f"   Producto mas vendido: {producto_mas_vendido}")

print(f"\n📅 Ventas por mes:")
for mes, venta in ventas_por_mes.items():
    print(f"   {mes}: ${venta:,.2f}")

# Generar grafico
plt.figure(figsize=(10, 6))
ventas_por_mes.plot(kind='bar', color='skyblue', edgecolor='navy')
plt.title('Evolucion de Ventas por Mes', fontsize=14, fontweight='bold')
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Monto Vendido (USD)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Guardar grafico
os.makedirs('resultados', exist_ok=True)
plt.savefig('resultados/ventas_por_mes.png', dpi=150)
plt.show()

# Guardar resumen
with open('resultados/resumen_ventas.txt', 'w') as out:
    out.write("RESUMEN DE ANALISIS DE VENTAS\n")
    out.write("=" * 40 + "\n")
    out.write(f"Ventas totales: ${ventas_totales:,.2f}\n")
    out.write(f"Producto mas vendido: {producto_mas_vendido}\n\n")
    out.write("Ventas por mes:\n")
    for mes, venta in ventas_por_mes.items():
        out.write(f"  {mes}: ${venta:,.2f}\n")

print("\n🎉 ANALISIS COMPLETADO CON EXITO")

# Fin del script