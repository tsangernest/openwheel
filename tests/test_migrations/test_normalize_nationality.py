import pytest


@pytest.mark.django_db
def test_normalize_nationality(migrator):
    old_state = migrator.apply_initial_migration(("app", "0002_insert_data"))
    old_nationality = old_state.apps.get_model("app", "Nationality")
    assert old_nationality.objects.count() == 2142

    new_state = migrator.apply_test_migration(("app", "0003_insert_data"))
    nationality = new_state.apps.get_model("app", "Nationality")
    assert nationality.objects.count() == 1502





    breakpoint()
    migrator.reset()

