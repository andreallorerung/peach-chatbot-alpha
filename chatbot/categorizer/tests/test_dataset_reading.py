import categorize.dataset_reading

def test_read_twice():
    '''
    assert read data structure is deterministic (i.e., it does not shuffle the
    data read)
    '''
    one = categorize.dataset_reading.read_data("categorize/data/sample_data.csv", format="csv")
    two = categorize.dataset_reading.read_data("categorize/data/sample_data.csv", format="csv")

    assert one == two
