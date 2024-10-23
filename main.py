import random
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS to allow requests from anywhere
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class GambleResult(BaseModel):
    amount_bet: float
    win_percentage: float
    won: bool
    amount_won: float

@app.get("/gamble", response_model=GambleResult)
async def gamble(amount_bet: float, win_percentage: float):
    won = random.random() < win_percentage / 100
    amount_won = amount_bet * 100 / win_percentage if won else 0
    
    return GambleResult(
        amount_bet=amount_bet,
        win_percentage=win_percentage,
        won=won,
        amount_won=amount_won
    )   