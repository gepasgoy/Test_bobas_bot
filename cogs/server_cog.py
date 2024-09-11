from disnake.ext import commands
import socket


class serv(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # Создаем сокет
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Указываем IP-адрес и порт для прослушивания (в данном случае 8080)
        host = '0.0.0.0'  # Это значит, что сервер будет прослушивать все сетевые интерфейсы
        port = 8080

        # Связываем сокет с адресом и портом
        server_socket.bind((host, port))

        # Запускаем прослушивание
        server_socket.listen(5)
        print(f"Сервер запущен и прослушивает порт {port}...")

        while True:
    # Ожидаем подключения
            client_socket, address = server_socket.accept()
            print(f"Подключение от {address}")

    # Получаем данные от клиента
            data = client_socket.recv(1024).decode()
            print(f"Данные от клиента: {data}")

    # Отправляем ответ клиенту
            response = "HTTP/1.1 200 OK\n\nПривет, клиент!"
            client_socket.send(response.encode())

    # Закрываем соединение с клиентом
            client_socket.close()


def setup(bot):
    bot.add_cog(serv(bot))
