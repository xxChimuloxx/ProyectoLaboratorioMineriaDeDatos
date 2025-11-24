# README — Proyecto Telco Churn Pipeline (MLOps)
## Proyecto Laboratorio Mineria de Datos
### Nombre del Proyecto: Telco Churn 
### Tipo: Pipeline Reproducible con MLOps, DVC y GitHub Actions

## Introduccion
Este repositorio contiene el desarrollo completo de un pipeline reproducible de Machine Learning orientado a la predicción de churn (baja de clientes) para la empresa ficticia TelcoVision. El proyecto replica el flujo de trabajo de un equipo real de datos, aplicando buenas prácticas de MLOps, versionado de datos y modelos, experimentación con trazabilidad, CI/CD y documentación profesional.

El objetivo principal fue construir un sistema capaz de predecir si un cliente abandonará el servicio (churn = 1) o permanecerá activo (churn = 0), utilizando datos demográficos, de uso y de facturación.

## 🗂️ Estructura del Repositorio

``` python
Proyecto/
├── data/
│   
├── raw/                  # Dataset original (versionado por DVC)
│   
└── processed/            # Dataset limpio generado por el pipeline
├── models/                   # Modelos entrenados (bajo control DVC)
├── reports/
│   └── roc_curve.png         # Curva ROC del modelo final
├── src/
│   ├── data_prep.py          # Script de limpieza y preparación de datos
│   ├── train.py              # Entrenamiento del modelo (Logistic Regression)
│   └── evaluate.py           # Evaluación extendida + curva ROC
├── .github/workflows/
│   └── ci.yaml               # Workflow de CI/CD con GitHub Actions
├── params.yaml               # Hiperparámetros del modelo
├── dvc.yaml                  # Definición del pipeline completo
├── dvc.lock                  # Registro determinístico de versiones
├── metrics.json              # Métricas base del modelo
├── metrics_extended.json     # Métricas extendidas
└── README.md                 # (este archivo)
``` 

## 🗂️ Dataset

Archivo original: 
> data/raw/telco_churn.xlsx

Características principales:

- 10.000 registros
- Variables demográficas
- Servicios contratados
- Métodos de pago
- Cargos mensuales y acumulados
- Variable objetivo: 
> churn

El dataset está versionado con DVC y almacenado en DagsHub.

## ⚙️ Pipeline Reproducible (DVC)

El pipeline se compone de 3 stages:

> data_prep

- Limpieza de datos:
- elimina duplicados
- corrige valores faltantes
- genera data/processed/telco_clean.csv

> train

- Entrenamiento del modelo:
- modelo base: Logistic Regression
- hiperparámetros controlados por params.yaml
- guarda modelo en models/model.pkl
- genera métricas en metrics.json

> evaluate

- Evaluación adicional del modelo:
- métricas extendidas (precision, recall, f1, roc_auc)
- curva ROC en reports/roc_curve.png
- archivo metrics_extended.json

Ejecución completa del pipeline:
``` python
dvc repro
``` 

Reproducible en cualquier máquina con:
``` python
dvc pull
dvc repro
``` 

## 🔍 Experimentos (DVC Experiments)

Se realizaron múltiples experimentos variando hiperparámetros con:
``` python
dvc exp run --set-param train.C=0.5
dvc exp run --set-param train.C=2.0 --set-param train.max_iter=300
``` 

Comparación de experimentos:
``` python
dvc exp show
``` 

Se seleccionó como modelo final el experimento con:

- C = 0.5
- F1 superior al baseline
- Mejor estabilidad en validación

Aplicación del mejor experimento:
``` python
dvc exp apply <ID>
``` 

## 🔁 Integración Continua (CI/CD)

Se implementó un workflow en GitHub Actions:
> .github/workflows/ci.yaml

El CI ejecuta:

1. nstalación de dependencias
2. Configuración de DVC remote
3. dvc pull
4. dvc repro
5. Publicación de métricas

Los secretos usados:

- DAGSHUB_USER
- DAGSHUB_TOKEN

CI corre en:

- ada push a main
- cada Pull Request

Un PR válido muestra:

- ✔️ Checks en verde
- ✔️ Pipeline ejecutado
- ✔️ Métricas impresas

Esto asegura que cualquier cambio rompe o valida el pipeline automáticamente.

## Iteración Colaborativa (Etapa 6)

En esta seccion se replicó el flujo de trabajo de un equipo profesional:

- ramas feat-*
- Pull Requests
- validación automática con CI
- merge del mejor experimento

Se generaron capturas de evidencia mostrando:

- PR creado
- CI ejecutándose y aprobado
- cambios integrados en main

Toda la historia está disponible en el historial del repositorio.

## Evaluación Extendida (Etapa 7)

Se implementó evaluate.py, que genera:

- precisión
- recall
- f1-score
- roc_auc
- curva ROC

La curva ROC final está almacenada en reports/roc_curve.png.

## Despliegue del Modelo (Diseño Conceptual)
Aunque no se exigió un servicio real, se documentó cómo desplegarlo:

✔️ Opción A — API con FastAPI

- Un servidor FastAPI podría:
- cargar models/model.pkl
- recibir datos de cliente en JSON
- aplicar preprocesamiento
- retornar probabilidad de churn

Endpoint sugerido:
``` python
POST /predict
``` 

✔️ Opción B — Dashboard en Streamlit

Ideal para usuarios de negocio:

- sliders para edad, tipo de contrato, cargo mensual, etc.
- predicción en tiempo real
- explicación del resultado

✔️ Beneficios del enfoque MLOps:

- reproducibilidad garantizada (DVC + GitHub Actions)
- trazabilidad de datos y modelos
- integración segura mediante versión de artefactos

🎥 Video de Presentación (pendiente para entrega final)

El video de 10–15 minutos debe mostrar:

- caso de uso
- pipeline completo
- ejecución real (git clone, dvc pull, dvc repro)
- experimentos
- CI en PR
- conclusiones

El enlace será incluido en este README cuando esté listo.

## 👤 Autores

- xxxx
- xxxx
- xxxx

Proyecto académico — ISTEA
MLOps / Data Mining Laboratory
2025

## Instrucciones para reproducir el proyecto

Clonar repo:
``` python
git clone https://github.com/xxChimuloxx/ProyectoLaboratorioMineriaDeDatos
``` 

Entrar al directorio:
``` python
cd ProyectoLaboratorioMineriaDeDatos
``` 

Instalar dependencias:
``` python
pip install -r requirements.txt
``` 

Obtener los datos:
``` python
dvc pull
``` 

Reproducir pipeline:
``` python
dvc repro
```

## 📦 Estado del Proyecto

- ✅ Setup inicial (Completo)
- ✅ Limpieza + features (Completo)
- ✅ Entrenamiento (Completo)
- ✅ Experimentos (Completo)
- ✅ CI/CD (Completo)
- ✅ Iteración colaborativa (Completo)
- ✅ Evaluación extendida (bonus) (Completo)


#
# ADICIONALES

## Comparación Exhaustiva de los Experimentos

La fase de experimentación se desarrolló utilizando **DVC Experiments**, lo que permitió registrar sistemáticamente cada combinación de hiperparámetros, sus métricas resultantes y los artefactos asociados (modelo, métricas y versions del lock file). Este enfoque garantiza trazabilidad total: cada experimento puede ser recreado, comparado, revertido o aplicado al workspace en cualquier momento.

El modelo inicial consistió en una **Logistic Regression** con parámetros por defecto. A partir de esta base, se ejecutaron múltiples experimentos con variaciones específicas en los parámetros de regularización y número máximo de iteraciones.

### Contexto estadístico del problema
El dataset de churn presenta características típicas del dominio:
- Ligero desbalance entre clases (la cantidad de clientes que se dan de baja es menor que los que permanecen activos).
- Variables categóricas de alta cardinalidad (región, tipo de contrato, método de pago).
- Efectos no lineales que una regresión logística simple puede no capturar completamente.
En este tipo de contextos, la métrica F1 suele ser más informativa que la accuracy, ya que penaliza más los falsos negativos (clientes que abandonan y no se predicen como tal).

---

### **🔹 Baseline**
Modelo inicial sin cambios de hiperparámetros:
- **Accuracy:** 0.6855  
- **F1-score:** 0.5158  
- Sin advertencias relevantes.

Este baseline sirve como punto de referencia para evaluar si vale la pena aumentar (o disminuir) la fuerza de regularización.

---

### **🔹 Experimento 1 — Regularización más fuerte (`C = 0.5`)**

- **Accuracy:** 0.6885  
- **F1-score:** 0.5197  
- Sin warnings de convergencia.

**Interpretación:**  
Reducir el valor de C en una regresión logística implica **aumentar la penalización L2**, promoviendo coeficientes más pequeños y un modelo menos sensible al ruido.  
Este experimento produjo una mejora simultánea en accuracy y F1-score, indicando:
- mejor capacidad de generalización,  
- menor sobreajuste,  
- mayor sensibilidad a la clase minoritaria.  

Esto es especialmente significativo en churn: detectar correctamente al cliente que se va es más importante que predecir correctamente al cliente que se queda.

---

### **🔹 Experimento 2 — Regularización más débil (`C = 2.0`) y mayor `max_iter`**

- **Accuracy:** 0.6845  
- **F1-score:** 0.5135  
- **Advertencias de convergencia**, incluso con 300 iteraciones.

**Interpretación:**  
Un valor alto de C reduce la regularización y permite que el modelo sea más flexible. Sin embargo:
- No mejoró los resultados,
- Mostró mayor sensibilidad al ruido,
- Exigió más iteraciones sin resolver el problema de convergencia.

Esto indica que el modelo estaba intentando ajustar patrones que no aportaban al desempeño real, típico síntoma de **sobreajuste**.

---

### **Comparativa Final**

| Experimento | C | max_iter | Accuracy | F1-score | Estabilidad |
|------------|---|----------|----------|----------|-------------|
| Baseline   | 1.0 | 200 | 0.6855 | 0.5158 | Estable |
| Exp. 1     | 0.5 | 200 | **0.6885** | **0.5197** | Muy estable |
| Exp. 2     | 2.0 | 300 | 0.6845 | 0.5135 | Con warnings |

**Conclusión general:**  
➡️ El experimento con `C = 0.5` ofrece el **mejor equilibrio entre estabilidad, generalización y métricas críticas para el dominio de churn**.

---

## Justificación en detalle del Modelo Final Elegido

El modelo final seleccionado corresponde al experimento con **regularización moderada (`C = 0.5`)**, debido a una combinación de factores técnicos y prácticos relevantes para su futuro despliegue.

### **1. Superioridad en métricas prioritarias**
Aunque la mejora absoluta puede parecer pequeña, en problemas de churn —donde la clase positiva es minoritaria y estratégica— incluso incrementos leves en F1-score reflejan un mejor desempeño real en la identificación de clientes que se darán de baja.

### **2. Estabilidad matemática del modelo**
El modelo:
- no presentó warnings de convergencia,
- no requirió aumentos innecesarios de iteraciones,
- mantuvo coherencia entre accuracy y F1.

Esto lo vuelve más confiable como *artefacto productivo*.

### **3. Robustez frente al ruido**
En modelos lineales como la regressión logística:
- la regularización controla la magnitud de los coeficientes,
- coeficientes más pequeños implican un modelo más estable,
- estabilidad implica mayor resiliencia ante cambios sutiles en la distribución del dataset.

En entornos reales (como TelcoVision), la distribución de datos cambia mes a mes. Un modelo con C=0.5 responde mejor a estos cambios.

### **4. Adecuación al uso en un pipeline productivo**
El modelo final:
- es liviano y rápido de ejecutar,
- tiene baja complejidad,
- se versiona de forma simple,
- es reproducible con DVC en cualquier entorno.

Esto lo convierte en un candidato ideal para despliegue en servicios REST, dashboards o pipelines batch.

---

## 🚀 Reflexión Extendida sobre el Despliegue en Producción

El despliegue de un modelo de Machine Learning no consiste únicamente en poner en funcionamiento un archivo `model.pkl`. Implica trasladar todo el pipeline —desde la preparación de datos hasta el scoring final— a un entorno capaz de operar con altos niveles de estabilidad, trazabilidad, seguridad y escalabilidad. En organizaciones como TelcoVision, este proceso debe alinearse con prácticas de MLOps, garantizando que el modelo no solo funcione hoy, sino que continúe funcionando de manera confiable a medida que cambian los datos, el negocio y la infraestructura.

A continuación se presenta una reflexión detallada sobre cómo podría desplegarse este modelo de predicción de churn en un entorno productivo real, incluyendo alternativas, estrategias y desafíos operativos.

---

### 1. Principios fundamentales para el despliegue

Antes de elegir la arquitectura final, es imprescindible tener presentes los siguientes principios:

- **Reproducibilidad:** La misma versión del modelo debe producir los mismos resultados en cualquier entorno.
- **Versionado absoluto:** Datos, código, modelos y métricas deben contar con versiones explícitas (DVC ya lo resuelve).
- **Escalabilidad:** El servicio debe responder tanto a consultas individuales como a miles de predicciones en procesos batch.
- **Trazabilidad:** Cada predicción debe ser auditable: qué modelo la generó, con qué parámetros y en qué momento.
- **Mantenibilidad:** El equipo debe poder actualizar el modelo sin interrumpir servicios críticos.
- **Monitoreo activo:** La degradación del modelo debe detectarse tempranamente para evitar impactos en el negocio.

El pipeline actual ya cumple varios de estos principios gracias a DVC y GitHub Actions, lo que facilita considerablemente el camino hacia producción.

---

### 2. Arquitectura de Servicio: API REST con FastAPI

La alternativa más flexible y utilizada en la industria para exponer modelos de ML es el uso de un servicio REST.

#### **Cómo funcionaría:**

1. **El servidor carga `models/model.pkl` al iniciar**  
   Esto evita recargar el modelo en cada solicitud, optimizando latencia.

2. **Un endpoint `/predict`** recibe datos de un cliente en formato JSON:

```json
{
  "age": 43,
  "gender": "Male",
  "region": "West",
  "contract_type": "Month-to-Month",
  "tenure_months": 12,
  "monthly_charges": 72.5,
  "total_charges": 850.0,
  "internet_service": "Fiber optic",
  "phone_service": "Yes",
  "multiple_lines": "Yes",
  "payment_method": "Electronic check"
}
```

El servicio:

- aplica el mismo preprocesamiento que se utilizó en entrenamiento (one-hot encoding),
- genera la probabilidad de churn,
- devuelve una respuesta como:

```json
{
  "probabilidad_churn": 0.72,
  "prediccion": 1
}
```

Ventajas:
- Integración inmediata con CRM, sistemas internos o aplicaciones web.
- Respuestas en tiempo real.
- Fácil balanceo de carga y escalado horizontal.
- Despliegue sencillo en Docker, Kubernetes o servicios cloud.

### 3. Dashboard de Análisis para Usuarios de Negocio (Streamlit)
Además del servicio REST, un dashboard visual aporta un valor decisivo para áreas como:

- Marketing,
- Fidelización,
- Data Analytics,
- Atención al cliente.

**¿Qué permitiría un dashboard?**
- Cargar datos de un cliente y obtener su score.
- Manipular variables y observar cambios en el riesgo de churn.
- Mostrar métricas como curva ROC, matriz de confusión o distribución de scores.
- Integrar explicabilidad del modelo con SHAP o LIME, permitiendo conocer qué variables influyen más en la predicción.

Beneficio estratégico:
- Los usuarios sin conocimientos técnicos pueden interactuar con el modelo y comprenderlo.

### 4. Integración en Pipelines Batch (Airflow, Control-M, Databricks)
En muchas empresas el scoring de churn se realiza de forma masiva, ejecutando predicciones para miles de clientes en horarios específicos del día o la noche.

**¿Cómo funcionaría?**
1. Airflow o Control-M dispara un job diario.
2. El job ejecuta un script que:
    - carga el dataset diario de clientes,
    - realiza el preprocesamiento,
    -   aplica el modelo versionado,
    - genera un archivo de resultados (CSV, Parquet, API interna).
3. El job guarda el resultado en el Data Lake o lo envía al CRM.
El modelo actual es ideal para esto porque:
    - es ligero,
    - se carga rápido,
    - no requiere GPU,
    - funciona bien con procesamiento vectorizado.

### 5. Monitoreo del Modelo en Producción (ML Monitoring)
Todo modelo se degrada con el tiempo debido a:

- cambios en el comportamiento de clientes,
- nuevos patrones de consumo,
- promociones o cambios en tarifas,
- estacionalidad,
- nuevos métodos de pago,
- cambios en el perfil demográfico.

Por eso el monitoreo es esencial.

Métricas recomendadas:

- Data drift: comparar la distribución de features actuales vs originales.
- Model drift: comparar predicciones con nuevos valores reales.
- F1-score en producción: si hay etiquetas diferidas (por ejemplo, se sabe al mes siguiente quién churneo).
- Volumen y patrones de predicciones: detectar anomalías.

Herramientas recomendadas:

- Evidently AI
- Prometheus + Grafana
- MLflow Monitoring
- Servicios cloud como Vertex AI Model Monitoring

### 6. Estrategia de Reentrenamiento
Con DVC y GitHub Actions ya configurados, el reentrenamiento puede automatizarse:

1. Un job (manual o programado) actualiza el dataset en data/raw/.
2. Se ejecuta dvc repro.
3. GitHub Actions reconstruye el pipeline.
4. DVC genera una nueva versión del modelo.
5. El equipo evalúa las métricas extendidas.
6. Si el modelo es mejor, se promueve a “versión en producción”.

Esta estrategia se llama Continuous Training (CT) y es parte madura de MLOps.

### 7. Versionado y Rollbacks
Gracias a DVC:

- cada dataset tiene un hash,
- cada modelo tiene un hash,
- cada experimento tiene un ID único.

Esto hace que el rollback sea inmediato:

```php
dvc checkout <versión-anterior>
```

O incluso desde interfaz web en DagsHub.

Este nivel de trazabilidad es esencial en telecomunicaciones, donde una mala predicción puede implicar pérdidas económicas o campañas erróneas.

### 8. Infraestructura de Despliegue Recomendada

Dependiendo de los recursos de TelcoVision, se pueden considerar:

> Opción A – Contenedores (Docker + Kubernetes)

- ideal para microservicios,
- escalado automático,
- aislamiento limpio.

> Opción B – Serverless (AWS Lambda / Google Cloud Run)

- óptimo si el volumen de predicciones no es constante.
- paga solo por ejecución.

> Opción C – On-premise / Virtualizado

- si existen restricciones regulatorias,
- integra con Airflow, Control-M o ETL internos.

#
# Conclusión

El modelo entrenado, junto con el pipeline reproducible creado con DVC y ejecutado mediante CI/CD en GitHub Actions, está completamente preparado para entrar en un proceso de despliegue productivo. El uso de técnicas modernas de MLOps asegura que:

- las predicciones sean confiables,
- el modelo sea trazable,
- los datos estén versionados,
- las actualizaciones sean seguras,
- y el rollback sea posible en segundos.

En síntesis, el trabajo realizado en este proyecto no solo resuelve la predicción de churn, sino que sienta las bases técnicas para un flujo de MLOps maduro, replicable y escalable en un entorno real de telecomunicaciones.