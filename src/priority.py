"""Fictional Meridian ticket priority normalisation. Intentional starter defect."""


def normalise_priority(value):
    return value if value in ("P0", "P1", "P2", "P3") else "P3"
