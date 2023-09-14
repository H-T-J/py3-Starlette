from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

import uvicorn


async def homepage(request):
    return JSONResponse({"Hello": "World"})


async def about(requests):
    return JSONResponse({"message": "rorange"})


async def contact(requests):
    return JSONResponse({"Work Email": "eiwdjwbcjhjwnkxnqw"})

app = Starlette(
    debug=True,
    routes=[
        Route("/", homepage),
        Route("/about", about),
        Route("/contact", contact)
    ]
)

uvicorn.run(app, port=8080)
