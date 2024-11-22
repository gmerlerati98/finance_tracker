from pydantic import BaseModel
from datetime import date

#Section is to build the Pydantic models definitions in order to validate the data
class ExpenseBase(BaseModel):
    description: str
    amount: float
    category: str
    date: date

class ExpenseCreate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int


    class Config:
        orm_mode = True

class IncomeBase(BaseModel):
    description: str
    amount: float
    date: date

class IncomeCreate(IncomeBase):
    pass

class Income(IncomeBase):
    id: int


    class Config:
        orm_mode = True

