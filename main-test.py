from main import Add, Subtract

def test_Add():
    assert Add(2, 3) == 5
    assert Add(5, 5) == 10
    print("Add Function works correctly")
    
def test_Subtract():
    assert Subtract(5, 2) == 3
    print("Subtract Function works correctly")
    
if __name__ == "__main__":
    test_Add()
    test_Subtract()