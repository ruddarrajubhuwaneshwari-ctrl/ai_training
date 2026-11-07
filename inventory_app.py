from fastapi import FastAPI, HTTPException, status

app = FastAPI()

inventory = {
    1 : {
        "make" : "KTM",
        "model" : "Duke 390",
        "year" : 2025
    },
    2 : {
        "make" : "Yamaha",
        "model" : "R15",
        "year" : 2024
    }
}


@app.get("/about")
def about():
    return {"about": "This is an inventory management application."}

@app.get("/")
def root():
    return {"intro": "Hello! How are you today?"}

#http:120.0.0.1.8000/get-vehicle/1
@app.get("/get-vehicle/{vehicle_id}")
def get_vehicle(vehicle_id: int):
    if vehicle_id not in inventory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vehicle with ID {vehicle_id} not found."
        )
    return inventory[vehicle_id]

    