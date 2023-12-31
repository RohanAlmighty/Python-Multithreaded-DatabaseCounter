from database import engine, SessionLocal
import models

models.Base.metadata.create_all(bind=engine)


def create_reset_counter(counter_id: int = 1) -> None:
    with SessionLocal() as db:
        counter_model = (
            db.query(models.Counter).filter(models.Counter.id == counter_id).first()
        )

        if counter_model is None:
            counter_model = models.Counter()

        counter_model.counter_val = 0

        db.add(counter_model)
        db.commit()


def increment_counter(counter_id: int = 1) -> None:
    with SessionLocal() as db:
        counter_model = (
            db.query(models.Counter).filter(models.Counter.id == counter_id).first()
        )

        counter_model.counter_val = counter_model.counter_val + 1

        db.add(counter_model)
        db.commit()


def view_counter(counter_id: int = 1) -> int:
    with SessionLocal() as db:
        counter_model = (
            db.query(models.Counter).filter(models.Counter.id == counter_id).first()
        )

        return counter_model.counter_val


if __name__ == "__main__":
    create_reset_counter()
    for _ in range(100):
        increment_counter()
    print(view_counter())
