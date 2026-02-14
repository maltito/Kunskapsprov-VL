file_path = "hello_world.txt"
expected_text = "Hello World!"

def test_that_file_data_is_correct():
    with open (file_path, "r") as file:
        content = file.read()
    
    assert content == expected_text
