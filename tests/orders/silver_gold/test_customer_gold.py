def test_count(read_data):
    source, target = read_data
    print(source)
    print(target)
    assert len(source) ==len(target)