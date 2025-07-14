from collections.abc import Sequence
from typing import Any, Tuple, cast

from sqlalchemy import Column, delete, select, update
from sqlalchemy.engine.row import Row
from sqlalchemy.orm import Session

from models.dish_ingredient import DishIngredients
from models.dish_taste import DishTaste
from models.dishes import Dishes
from models.ingredients import Ingredients
from models.taste import Taste


class DishesOnlyService:
    @staticmethod
    def get_dish_by_id(session: Session, dish_id: int) -> Dishes | None:
        stmt = select(Dishes).where(Dishes.id == dish_id)
        result = session.execute(stmt).scalar_one_or_none()
        return result

    @staticmethod
    def get_dish_by_dish_name(session: Session, dish_name: str) -> Dishes | None:
        stmt = select(Dishes).where(Dishes.dish_name == dish_name)
        result = session.execute(stmt).scalar_one_or_none()
        return result

    @staticmethod
    def get_dish_by_series(session: Session, series: str) -> Sequence[Dishes]:
        stmt = select(Dishes).where(Dishes.series == series)
        result = session.execute(stmt).scalars().all()
        return result

    @staticmethod
    def get_all_dishes(session: Session) -> Sequence[Dishes]:
        stmt = select(Dishes)
        result = session.execute(stmt).scalars().all()
        return result

    @staticmethod
    def create_dish(session: Session, dish: Dishes):
        session.add(dish)
        session.commit()

    @staticmethod
    def update_dish(session: Session, dish: Dishes):
        stmt = (
            update(Dishes)
            .where(Dishes.dish_name == dish.dish_name)
            .values(
                series=dish.series,
                score=dish.score,
                free_choose=dish.free_choose,
            )
        )
        session.execute(stmt)
        session.commit()

    @staticmethod
    def delete_dish(session: Session, dish: Dishes):
        stmt = delete(Dishes).where(Dishes.dish_name == dish.dish_name)
        session.execute(stmt)
        session.commit()


class DishIngredientsService:
    @staticmethod
    def get_dish_ingredients_by_dish_name(session: Session, dish_name: str) -> Sequence[Ingredients]:
        stmt = (
            select(Ingredients)
            .join(
                DishIngredients,
                DishIngredients.ingredient_id == Ingredients.id,
            )
            .join(
                Dishes,
                DishIngredients.dish_id == Dishes.id,
            )
            .where(Dishes.dish_name == dish_name)
        )
        result = session.execute(stmt).scalars().all()
        return result

    @staticmethod
    def get_only_dish_ingredients_by_dish_id(dish: Dishes) -> Sequence[DishIngredients]:
        pass

    @staticmethod
    def get_only_dish_ingredients_by_ingredient_id(dish: Dishes) -> Sequence[DishIngredients]:
        pass


class DishTasteService:
    pass


if __name__ == "__main__":
    from db.mysql_conn import context_mysql_session

    # with context_mysql_session() as session:
    #     # insert
    #     test_dish = Dishes(
    #         dish_name="测试菜品",
    #         series="测试系列",
    #         score=2.5,
    #         free_choose=False,
    #     )
    #     DishesOnlyService.create_dish(session=session, dish=test_dish)
    #     # update
    #     test_dish_modified = Dishes(
    #         dish_name="测试菜品",
    #         series="测试系列",
    #         score=3.5,
    #         free_choose=False,
    #     )
    #     DishesOnlyService.update_dish(session=session, dish=test_dish_modified)
    #     # delete
    #     DishesOnlyService.delete_dish(session=session, dish=test_dish)
    #     # select
    #     a = DishesOnlyService.get_all_dishes(session=session)
    #     b = DishesOnlyService.get_dish_by_id(session=session, dish_id=1)
    #     c = DishesOnlyService.get_dish_by_dish_name(session=session, dish_name=str(test_dish.dish_name))
    #     c = DishesOnlyService.get_dish_by_dish_name(session=session, dish_name="辣糊糊")
    #     d = DishesOnlyService.get_dish_by_series(session=session, series="宁夏菜")

    with context_mysql_session() as session:
        a = DishIngredientsService.get_dish_ingredients_by_dish_name(
            session=session,
            dish_name="咖喱胡萝卜牛肉",
        )

    print("done")
