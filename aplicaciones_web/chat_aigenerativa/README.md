# Ollama y Web.py

Este ejemplo muestra la creación de una aplicación web que sirve de interfaz para ollama, para poder enviar **prompts** y mostrar en un **textarea** los **response** que genere el módelo de lenguaje largo instalado.

## 1. Instalar ollama

**Ollama** es un servicio que permite gestionar modelos de lenguaje largo (llm) publicos, cómo: gemmini, llama, deepseek, etc. entre otros, proporcionando una **API REST** para poder interactuar con los modelos de forma local.

Cómo primer paso hay que descargar e instalar **ollama** desde el sitio web [https://ollama.com/download](https://ollama.com/download)

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## 2. Ejecutar el servidor ollama

Una vez descargado e instalado **ollama** hay que verificar si funciona, una forma rapida es mediante el comando

```bash
ollama list
```

Este comando muestra los modelos descargados localmente, en caso de que el servidor este apagado mostrará el siguiente mensaje:

```bash
Error: ollama server not responding - could not connect to ollama server, run 'ollama serve' to start it
```

Para inicializar el servidor se utiliza el siguiente comando:

```bash
ollama serve
```

Una vez que se inicializa el servidor se muestra una configuración similiar a la siguiente:

```bash
time=2025-06-09T18:07:26.707Z level=INFO source=routes.go:1234 msg="server config" env="map[CUDA_VISIBLE_DEVICES: GPU_DEVICE_ORDINAL: HIP_VISIBLE_DEVICES: HSA_OVERRIDE_GFX_VERSION: HTTPS_PROXY: HTTP_PROXY: NO_PROXY: OLLAMA_CONTEXT_LENGTH:4096 OLLAMA_DEBUG:INFO OLLAMA_FLASH_ATTENTION:false OLLAMA_GPU_OVERHEAD:0 OLLAMA_HOST:http://127.0.0.1:11434 OLLAMA_INTEL_GPU:false OLLAMA_KEEP_ALIVE:5m0s OLLAMA_KV_CACHE_TYPE: OLLAMA_LLM_LIBRARY: OLLAMA_LOAD_TIMEOUT:5m0s OLLAMA_MAX_LOADED_MODELS:0 OLLAMA_MAX_QUEUE:512 OLLAMA_MODELS:/home/codespace/.ollama/models OLLAMA_MULTIUSER_CACHE:false OLLAMA_NEW_ENGINE:false OLLAMA_NOHISTORY:false OLLAMA_NOPRUNE:false OLLAMA_NUM_PARALLEL:0 OLLAMA_ORIGINS:[http://localhost https://localhost http://localhost:* https://localhost:* http://127.0.0.1 https://127.0.0.1 http://127.0.0.1:* https://127.0.0.1:* http://0.0.0.0 https://0.0.0.0 http://0.0.0.0:* https://0.0.0.0:* app://* file://* tauri://* vscode-webview://* vscode-file://*] OLLAMA_SCHED_SPREAD:false ROCR_VISIBLE_DEVICES: http_proxy: https_proxy: no_proxy:]"
time=2025-06-09T18:07:26.708Z level=INFO source=images.go:479 msg="total blobs: 0"
time=2025-06-09T18:07:26.708Z level=INFO source=images.go:486 msg="total unused blobs removed: 0"
time=2025-06-09T18:07:26.708Z level=INFO source=routes.go:1287 msg="Listening on 127.0.0.1:11434 (version 0.9.0)"
time=2025-06-09T18:07:26.709Z level=INFO source=gpu.go:217 msg="looking for compatible GPUs"
time=2025-06-09T18:07:26.761Z level=INFO source=gpu.go:377 msg="no compatible GPUs were discovered"
time=2025-06-09T18:07:26.762Z level=INFO source=types.go:130 msg="inference compute" id=0 library=cpu variant="" compute="" driver=0.0 name="" total="7.8 GiB" available="4.8 GiB"
```

## 3. Descargar modelos

En la pagina de **ollama** [https://ollama.com/search](https://ollama.com/search) hay un listado de modelos listos para descargarse, éste proceso se realiza seleccionado el modelo deseado con el comando **pull** de la siguiente forma:

```bash
ollama pull gemma3:1b
```

con este comando se descarga y configurará el modelo indicado, mostrando una salida como la siguiente:

```bash
pulling manifest 
pulling 7cd4618c1faf: 100% ▕█████████████████████████████████████████████▏ 815 MB                         
pulling e0a42594d802: 100% ▕█████████████████████████████████████████████▏  358 B                         
pulling dd084c7d92a3: 100% ▕█████████████████████████████████████████████▏ 8.4 KB                         
pulling 3116c5225075: 100% ▕█████████████████████████████████████████████▏   77 B                         
pulling 120007c81bf8: 100% ▕█████████████████████████████████████████████▏  492 B                         
verifying sha256 digest 
writing manifest 
success 
```

## 4. Verfificar el modelo descargado

Para verificar que modélos se tienen disponibles localmente se utiliza el siguiente comando que lista los modélos disponible.

```bash
ollama list
```

Tal cómo se muestra en la salida siguiente se listan los modélos disponibles de forma local.

```bash
NAME         ID              SIZE      MODIFIED      
gemma3:1b    8648f39daa8f    815 MB    9 minutes ago    
```

## 5. Interactuar con el modélo

Para interactuar con cualquiera de los modelos desacargados se utiliza el siguiente comando, indicando el nombre del módelo con el que se va a interactuar.

```bash
ollama run gemma3:1b
```

El comando anterior carga en memoria RAM el módelo seleccionado y abre un shell para escribir propmts y mostrar las respuestas.

```bash
>>> Send a message (/? for help)
```

**NOTA**: Para salir de la sesión de chat se utiliza **Ctrl + D**.

## 6. Acceder a la API de Ollama

Cómo se menciono anteriormente **ollama** hablita una **API REST** lo que permite interactura con los modelos desde una terminal utilizando **curl** o alguna aplicación que tenga acceso al protocolo **HTTP** y acceso a **API REST**. En el respositorio de **Github** [https://github.com/ollama/ollama](https://github.com/ollama/ollama) hay un ejemplo de uso con **curl**.


```bash
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3:1b",
  "prompt":"Hola"
}'
```

Al pegar y ejecutar el comando anterior se obtiene la siguiente salida, en la que cada **token** es mostrado de forma independiente.

```bash
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:42.349114703Z","response":"¡","done":false}
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:42.435659806Z","response":"Hola","done":false}
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:42.506482005Z","response":"!","done":false}
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:42.576331361Z","response":" ¿","done":false}
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:42.653336521Z","response":"Cómo","done":false}
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:42.72234535Z","response":" estás","done":false}
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:42.791074426Z","response":" hoy","done":false}
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:42.859469379Z","response":"?","done":false}
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:42.928237548Z","response":" 😊","done":false}
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:43.001343286Z","response":" ","done":false}
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:43.069392645Z","response":"\n\n","done":false}
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:43.138465732Z","response":"How","done":false}
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:43.218786556Z","response":" can","done":false}
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:43.297677103Z","response":" I","done":false}
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:43.385089523Z","response":" help","done":false}
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:43.452368325Z","response":" you","done":false}
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:43.524038876Z","response":"?","done":false}
{"model":"gemma3:1b","created_at":"2025-06-09T18:46:43.607778506Z","response":"","done":true,"done_reason":"stop","context":[105,2364,107,21529,106,107,105,4368,107,238631,21529,236888,7196,33266,64135,16229,236881,103453,236743,108,3910,740,564,1601,611,236881],"total_duration":1389921742,"load_duration":58955125,"prompt_eval_count":10,"prompt_eval_duration":70869455,"eval_count":18,"eval_duration":1259443687}
```

Para tener más opciones en los solicitudes **requests** se puede consultar la documentación sobre **API** de ollama en la siguiente liga:  [https://github.com/ollama/ollama/blob/main/docs/api.md](https://github.com/ollama/ollama/blob/main/docs/api.md)


En el siguiente ejemplo se agrego el parámetro **stream** con un valor de **false** esto hará que se concatenen los **tokens** en una sola salida.

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3:1b",
  "prompt":"Hola",
  "stream":false
}'
```

```bash
{"model":"gemma3:1b","created_at":"2025-06-09T18:45:11.296045554Z","response":"¡Hola! ¿En qué puedo ayudarte hoy? 😊 \n\n(Hello! How can I help you today?)","done":true,"done_reason":"stop","context":[105,2364,107,21529,106,107,105,4368,107,238631,21529,236888,7196,2730,15300,55606,182805,16229,236881,103453,236743,108,236769,9259,236888,2088,740,564,1601,611,3124,17103],"total_duration":4617691178,"load_duration":2512236183,"prompt_eval_count":10,"prompt_eval_duration":428473481,"eval_count":24,"eval_duration":1676016247}
```
