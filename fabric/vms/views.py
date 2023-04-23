from django.shortcuts import render
from django.http import HttpResponse
import asyncio


async def tcp_view(request):
    host = 'localhost'
    port = 8888
    client_socket = await asyncio.open_connection(host, port)
