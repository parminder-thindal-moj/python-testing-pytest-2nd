def test_val_not_in_str():
    assert "monado" not in "This is the power of the"
    

def test_val_not_in_list():
    assert "monado" not in ["buster",
                            "speed",
                            "shield",
                            #"monado",
                            "eater",
                            "enchant"
                            "purge",
                            "armour"]