# Projeto de Geração de Recibos em PDF

Este é um projeto de exemplo para criar recibos em PDF usando o framework Django. O projeto permite que você preencha um formulário com detalhes do recibo e, em seguida, gere um recibo em PDF que pode ser baixado. Projeto criado para fins didáticos de estudos da ferramenta.

## Configuração do Ambiente

1. Clone este repositório:

   ```bash
   git clone https://github.com/marcelohdsantos/receiptGenerator.git
   cd seu-repositorio
   ```

2. Instale as dependências do projeto:
   ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use 'venv\Scripts\activate'
   ```

3. Execute as migrações do banco de dados:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
5. Acesso o aplicativo no seu navegador em `http://localhost:8000`.
   
Uso do Aplicativo
Acesse a página de criação de recibo em http://localhost:8000/receipt/criar_recibo/.

Preencha o formulário com os detalhes do recibo, como nome do destinatário, valor, referente, etc.

Clique em "Enviar" para gerar o recibo em PDF.

O recibo em PDF será baixado automaticamente para o seu dispositivo.

Personalização
Você pode personalizar este projeto de acordo com as necessidades do seu aplicativo. Você pode adicionar campos adicionais ao modelo Receipt ou ajustar a aparência do PDF gerado com base nas suas preferências.

Licença
Este projeto é licenciado sob a licença MIT - consulte o arquivo LICENSE para obter detalhes.

Criado por Marcelo Henrique dos Santos
e-mail: marcelodossantos732@yahoo.com.br

