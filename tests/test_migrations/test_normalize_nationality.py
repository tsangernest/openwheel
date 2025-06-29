import pytest


@pytest.mark.django_db
def test_normalize_nationality(migrator):
    old_nationality_state = migrator.apply_initial_migration("0002_insert_data")

    with pytest.raises(expected_exception=LookupError):
        old_nationality_state.apps.get_model("app", "Nationality")

    new_state = migrator.apply_test_migration("0003_insert_data")
    Nationality = new_state.apps.get_model("app", "Nationality")
    assert Nationality.objects.count() == 1502





    breakpoint()
    migrator.reset()

