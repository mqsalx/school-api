# 🛡️Throttling - School API

## 📜 Introdução

- O Throttle foi usado neste projeto para limitar a taxa de requisições que um cliente pode fazer a uma API dentro de um período de tempo definido. Isso é útil para proteger a API contra abuso ou uso excessivo, tanto por usuários anônimos quanto autenticados.

## 📝 Neste projeto, como exemplo, implementamos duas classes de Throttle personalizadas:

- `RegistrationAnonRateThrottle`: Limita o número de registros diários para usuários anônimos.

- `RegistrationUserRateThrottle`: Limita o número de registros diários para usuários autenticados.

## ⚒️ Como Funciona o Throttling?

- O Throttling é configurado para garantir que um número específico de requisições possa ser feito dentro de um intervalo de tempo determinado. Se um usuário exceder esse limite, uma resposta com o código de status 429 Too Many Requests será retornada.

### 🔬 Exemplo de Configuração

- Abaixo estão os exemplos das duas classes de throttle configuradas:

1. - **RegistrationAnonRateThrottle**

   Esta classe herda de `AnonRateThrottle` e define uma taxa de 5 requisições por dia para usuários anônimos.

   ```python
   from rest_framework.throttling import AnonRateThrottle

   class RegistrationAnonRateThrottle(AnonRateThrottle):
       rate = "5/day"
   ```

   **Explicação**:

   - **Classe Base**: `AnonRateThrottle` é usada para usuários que não estão autenticados.
   - **Rate**: Neste valor configurado como "5/day", o que significa que um usuário anônimo pode fazer até 5 requisições em um período de 24 horas.

2. - **RegistrationUserRateThrottle**

   Esta classe herda de `UserRateThrottle` e define uma taxa de 30 requisições por dia para usuários autenticados.

   ```python
   from rest_framework.throttling import UserRateThrottle

   class RegistrationUserRateThrottle(UserRateThrottle):
     rate = "30/day"
   ```

   **Explicação**:

   - **Classe Base**: `UserRateThrottle` é usada para usuários autenticados.
   - **Rate**: A taxa é configurada como "30/day", o que significa que um usuário autenticado pode fazer até 30 requisições em um período de 24 horas.

## 👨🏽‍🏫 Como Usar

- Para aplicar essas regras de throttling, você precisa adicioná-las à view ou ao conjunto de views no seu Django REST Framework:

  ```python

  from rest_framework.views import APIView
  from .throttles import RegistrationAnonRateThrottle, RegistrationUserRateThrottle

  class UserView(APIView):
  throttle_classes = [RegistrationAnonRateThrottle, RegistrationUserRateThrottle]

  def post(self, request, *args, **kwargs):
      # lógica de registro aqui
      return Response({"message": "User registered successfully!"})
  ```

- Passos:

1. - Crie as classes de throttle no arquivo **throttles.py**.
2. - Adicione a configuração de throttle na view que deseja limitar o número de requisições, usando o parâmetro throttle_classes.
3. - Defina a lógica da view (neste caso, a lógica de registro de usuário).

## 🌐 Configurações Globais (Opcional)

- Se preferir, você pode configurar essas classes de `throttle` globalmente, no arquivo de configurações settings.py, para que elas sejam aplicadas a todas as views:

    ```python
    REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
            "anon": "50/day",
            "user": "20/day"
        },
    }
    ```

## ✅ Conclusão
- O uso de throttling é essencial para proteger a API contra abuso de requisições excessivas.
Ao configurar corretamente, você garante que tanto usuários anônimos quanto autenticados sigam os limites estabelecidos, mantendo a saúde e a segurança do seu sistema.
