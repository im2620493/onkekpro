from django.http import HttpResponse
from django.views import View


class Main(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse(
            """
            <!DOCTYPE html>
                <html lang="en">
                <head>
                    <style>
                        div.content {
                          margin-top: 100px;
                          height: 150px;
                          align-items: center;
                        }
                    </style>
                    <title>Onkekpro</title>
                </head>
                
                <body>
                    <div class="content">
                        <h1 align="center">onkekpro</h1>
                        <p align="center">открываем бизнес, будем делать бабки ;)</p>
                        <br>
                        <h3 align="center">
                            <a style="color: #000; outline: none; text-decoration: none;" href="https://github.com/im2620493/onkekpro">join</a>
                        </h3>
                    </div>
                </body>
                </html>
            """
        )
