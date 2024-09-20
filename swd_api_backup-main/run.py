# from src.routers.products.utils import get_all_product

# print("a")
# result = get_all_product()
# print(result)

import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)