
# SnapBot
SnapBot es una aplicación de Python que captura una foto con la webcam del ordenador victima y la envía a través de Telegram.

## Características principales

- Envío a través de Telegram: Los resultados recopilados se envían 
directamente a través de Telegram a un destinatario específico o a un grupo.

- Seguridad y personalización: Puedes personalizar la configuración de Telegram para adaptarla a tus 
necesidades de seguridad. Asegúrate de configurar el archivo config.py con tus credenciales de Telegram.

## Uso
- Configura tus credenciales de Telegram en el archivo config.py. Debes proporcionar
   tu TOKEN de bot de Telegram y el CHAT_ID del destinatario o grupo al que deseas enviar la información.

    ```python  
    def get_telegram_config():   
        return {  
            'TOKEN': 'YOUR_TOKEN',  
            'CHAT_ID': 'YOUR_ID'  
        }  
    ```
       
# Responsabilidad y Uso Ético
El autor de este software no asume ninguna responsabilidad por el uso indebido del 
software o cualquier daño que pueda resultar del uso de este software. El usuario es el único 
responsable de su uso y debe utilizarlo de manera ética y legal.

El autor de este software no será responsable de ninguna pérdida, daño o consecuencia que resulte del uso de este software.
Por favor, utilice este software con responsabilidad y de acuerdo con las leyes y regulaciones aplicables en su jurisdicción.

