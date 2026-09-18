def test_count(read_data):
    source, target = read_data
    print(source)
    print(target)
    assert len(source) ==len(target)


# def test_dummy(request): #request is a fixture which will hold meta data of your test
#     print("test name", request.node.name)
#     print("test file name", request.node.fspath)
#     print("test folder name", request.node.fspath.dirname)