import utils
from fastapi import APIRouter
from fastapi.responses import StreamingResponse, JSONResponse

router = APIRouter()

@router.get("/taxcalc")
async def tax_calculation(amount : float):
    amount_to_pay = round(amount + (amount / 11.500002875000717))
    amount_loss = round(amount / 12.5)
    return JSONResponse(
        {
            "amountInserted": f"{amount}",
            "amountToPay": f"{amount_to_pay}",
            "taxAmount": "8",
            "amountLossByTax": f"{amount_loss}"
        },
        status_code=200
    )