import pytest


@pytest.mark.django_db
def test_normalize_nationality(migrator):
    old_state = migrator.apply_initial_migration(("app", "0002_insert_data"))
    old_nationality = old_state.apps.get_model("app", "Nationality")
    assert old_nationality.objects.count() == 2142

    num_of_unique_countries: int = (
        old_nationality
        .objects
        .order_by("country")
        .distinct("country")
        .count()
    )

    new_state = migrator.apply_tested_migration(("app", "0003_normalize_nationality"))
    nationality = new_state.apps.get_model("app", "Nationality")
    assert nationality.objects.count() == num_of_unique_countries + 2142
    assert nationality.objects.filter(deleted_at__isnull=True).count() == 1502

    migrator.reset()

