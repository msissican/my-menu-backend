from db.mysql_conn import context_mysql_session
from models.dishes import Dishes
from services.dishes_join_services import DishesOnlyService, DishIngredientsService


def test_dishes_only_service_create_update_delete():
    with context_mysql_session() as session:
        # insert
        test_dish = Dishes(
            dish_name="测试菜品",
            series="测试系列",
            score=2.5,
            free_choose=False,
        )
        DishesOnlyService.create_dish(session=session, dish=test_dish)
        # update
        test_dish_modified = Dishes(
            dish_name="测试菜品",
            series="测试系列",
            score=3.5,
            free_choose=False,
        )
        DishesOnlyService.update_dish(session=session, dish=test_dish_modified)
        # delete
        DishesOnlyService.delete_dish(session=session, dish=test_dish)


def test_dishes_only_service_select():
    with context_mysql_session() as session:
        test_dish = Dishes(
            dish_name="测试菜品",
            series="测试系列",
            score=2.5,
            free_choose=False,
        )
        # select
        a = DishesOnlyService.get_all_dishes(session=session)
        assert len(a) > 1

        b = DishesOnlyService.get_dish_by_id(session=session, dish_id=1)
        if b is not None:
            assert str(b.dish_name) == "西红柿炒鸡蛋"
        else:
            assert False

        c = DishesOnlyService.get_dish_by_dish_name(session=session, dish_name=str(test_dish.dish_name))
        assert c is None

        d = DishesOnlyService.get_dish_by_dish_name(session=session, dish_name="辣糊糊")
        if d is not None:
            assert int(str(d.id)) == 3
            assert str(d.dish_name) == "辣糊糊"
            assert str(d.series) == "宁夏菜"
        else:
            assert False

        e = DishesOnlyService.get_dish_by_series(session=session, series="宁夏菜")
        assert len(e) >= 1
