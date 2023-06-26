from pydantic import BaseModel


class CreateIncome(BaseModel):
    employer_id: int
    all_income: float
    month_income: float


class GetIncome(CreateIncome):
    id_: int
