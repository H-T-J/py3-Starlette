from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

import uvicorn


async def homepage(request):
    return JSONResponse({"Hello": "World"})


async def about(requests):
    return JSONResponse({"message": "rorange"})

app = Starlette(
    debug=True,
    routes=[
        Route("/", homepage),
        Route("/about", about)
    ]
)

uvicorn.run(app, port=8080)
