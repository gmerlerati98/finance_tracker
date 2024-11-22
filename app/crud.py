# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def create_expense(db: Session, expense: schemas.ExpenseCreate):
    db_expense = models.Expense(
        description=expense.description,
        amount=expense.amount,
        category=expense.category,
        date=expense.date
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def create_income(db: Session, income: schemas.IncomeCreate):
    db_income = models.Income(
        description=income.description,
        amount=income.amount,
        date=income.date
    )
    db.add(db_income)
    db.commit()
    db.refresh(db_income)
    return db_income

def get_expenses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Expense).offset(skip).limit(limit).all()

def get_incomes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Income).offset(skip).limit(limit).all()
