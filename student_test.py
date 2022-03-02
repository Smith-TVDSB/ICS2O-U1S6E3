import pytest
import student 



def test_default():
    input_values=['3.14159268','3']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert '3.142' ==  str(output[2]),"Output the number only"
    
def test_more_decimals():
    input_values=['3.14159268','4']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert '3.1416' ==  str(output[2]), "Output the number only"
    

def test_tau_two():
    input_values=['6.283185','2']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert '6.28' ==  str(output[2]), "Output the number only"
    
def test_tau_whole():
    input_values=['6.283185','0']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert '6' ==  str(output[2]) or '6.0' ==  str(output[2]), "Output the number only"
    
def test_nines():
    input_values=['9.9999','2']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert '10' ==  str(output[2]) or '10.0' ==  str(output[2]) or '10.00' == str(output[2]), "Output the number only"
    
def test_nine_off():
    input_values=['9.991','2']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert '9.99' == str(output[2]) or '9.99' == str(output[2]), "Output the number only"
