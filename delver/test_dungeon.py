import dungeon

def test_dungeon_exists():
    columns = 3
    rows = 4
    sut = dungeon.Dungeon(columns, rows)
    assert sut.columns == columns, f"dungeon should have {columns} columns, but has {sut.columns}"
    assert sut.rows == rows, f"dungeon should have {rows} rows, but has {sut.rows}"
    for row in range(rows):
        for column in range(columns):
            assert sut.get_room(column, row) is not None
